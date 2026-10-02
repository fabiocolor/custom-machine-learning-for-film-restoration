#!/usr/bin/env python3
"""Record accepted CWC work and collect bounded copies by ID, never by host path."""
from __future__ import annotations

import argparse
import hashlib
import fnmatch
import json
import os
import re
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

from research_storage import ROOT, artifact_path, identifier, policy, require_payload_path, results_root

DEFAULT_MAX_BYTES = 256 * 1024 * 1024


def remember_reference(name: str, role: str, sha256: str, *, job_id: str = "", artifact_id: str = "",
                       shared_storage_id: str = "", relative_path: str = "", size_bytes: int | None = None,
                       repo: Path = ROOT) -> dict:
    """Persist sources and intermediate dependencies without any device mount path."""
    name = identifier(name)
    if not role or not re.fullmatch("[0-9a-f]{64}", sha256.lower()):
        raise ValueError("Reference requires a role and canonical SHA-256")
    if (job_id or artifact_id) and not shared_storage_id and not relative_path:
        reference = {"type": "cwc_artifact", "job_id": identifier(job_id), "artifact_id": identifier(artifact_id)}
    elif shared_storage_id and relative_path and not (job_id or artifact_id):
        from pathlib import PurePosixPath
        if "\\" in relative_path or re.match(r"^[A-Za-z]:", relative_path):
            raise ValueError("Source reference needs a POSIX service-relative path, not a Windows path")
        path = PurePosixPath(relative_path)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("Source reference must be relative to canonical shared storage")
        reference = {"type": "shared_storage", "shared_storage_id": shared_storage_id, "relative_path": path.as_posix()}
    else:
        raise ValueError("Supply exactly one complete CWC artifact or canonical shared-storage reference")
    if size_bytes is not None and size_bytes < 0:
        raise ValueError("Negative source size")
    value = {"schema": "research_input_reference_v1", "role": role, "sha256": sha256.lower(), "reference": reference}
    if size_bytes is not None:
        value["size_bytes"] = size_bytes
    target = repo / "experiment_records/references" / (name + ".json")
    if target.exists() and json.loads(target.read_text()) != value:
        raise ValueError("Preserve earlier source reference; record a changed dependency under a new name")
    atomic_json(target, value)
    return value


def atomic_json(path: Path, value: dict) -> None:
    text = json.dumps(value, indent=2, sort_keys=True) + "\n"
    if len(text.encode()) > 1024 * 1024:
        raise ValueError("Custody record exceeds compact-record limit; shard the manifest instead of storing payloads")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        temporary.write_text(text)
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def job_record(job_id: str, repo: Path = ROOT) -> Path:
    return repo / "experiment_records/cwc_jobs" / (identifier(job_id) + ".json")


def remember_job(job_id: str, experiment_id: str = "", repo: Path = ROOT, max_bytes: int = DEFAULT_MAX_BYTES,
                 keep_in_cwc: list[str] | None = None) -> dict:
    path = job_record(job_id, repo)
    record = json.loads(path.read_text()) if path.exists() else {
        "schema": "research_cwc_custody_v1", "project": policy(repo)["project"],
        "job_id": job_id, "experiment_id": experiment_id, "state": "accepted",
        "artifacts": {}, "download_max_bytes": max_bytes,
    }
    if experiment_id and record.get("experiment_id") not in {"", experiment_id}:
        raise ValueError("Accepted job already belongs to another experiment")
    if experiment_id:
        record["experiment_id"] = experiment_id
    if keep_in_cwc is not None:
        record["keep_in_cwc"] = keep_in_cwc
    atomic_json(path, record)
    return record


def settings(repo: Path = ROOT) -> tuple[str, str]:
    values = {}
    for path in [repo.parent / ".env.local", repo / ".env.local"]:
        if path.is_file():
            for line in path.read_text().splitlines():
                if "=" in line and not line.lstrip().startswith("#"):
                    key, _, value = line.partition("=")
                    if path == repo.parent / ".env.local" and key.strip() != "CWC_BASE_URL":
                        continue  # Shared service configuration is not a project credential.
                    values[key.strip()] = value.strip().strip("\"'")
    values.update({k: os.environ[k] for k in ["CWC_BASE_URL", "CWC_API_KEY"] if k in os.environ})
    if not values.get("CWC_BASE_URL") or not values.get("CWC_API_KEY"):
        raise ValueError("Configure CWC_BASE_URL and project CWC_API_KEY")
    return values["CWC_BASE_URL"].rstrip("/"), values["CWC_API_KEY"]


class Cwc:
    def __init__(self, repo: Path = ROOT, *, base_url: str | None = None, api_key: str | None = None):
        if base_url is not None and api_key is not None:
            self.base, self.key = base_url.rstrip("/"), api_key
        else:
            self.base, self.key = settings(repo)

    def open(self, route: str):
        if not route.startswith("/jobs/"):
            raise ValueError("Collector only reads CWC job and artifact APIs")
        request = urllib.request.Request(self.base + route, headers={"X-API-Key": self.key})
        # Do not forward the project credential if CWC redirects to a signed object URL.
        request.remove_header("X-API-Key")
        request.add_unredirected_header("X-API-Key", self.key)
        return urllib.request.urlopen(request, timeout=45)

    def json(self, route: str):
        with self.open(route) as response:
            return json.load(response)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def verified(path: Path, artifact: dict) -> bool:
    return (path.is_file() and path.stat().st_size == artifact["size_bytes"]
            and digest(path) == artifact["sha256"])


def metadata(artifact: dict) -> dict:
    aid = identifier(str(artifact["artifact_id"]))
    sha = str(artifact.get("sha256") or "").lower()
    size = artifact.get("size_bytes")
    if not re.fullmatch("[0-9a-f]{64}", sha) or not isinstance(size, int) or size < 0:
        raise ValueError("Artifact lacks canonical SHA-256 or size; collection is not verified")
    return {"artifact_id": aid, "filename": str(artifact["filename"]), "sha256": sha, "size_bytes": size}


def collect_job(job_id: str, *, client=None, repo: Path = ROOT, max_bytes: int | None = None) -> dict:
    record = remember_job(job_id, repo=repo)
    limit = max_bytes if max_bytes is not None else record.get("download_max_bytes", DEFAULT_MAX_BYTES)
    if limit < 0:
        raise ValueError("Download limit must be nonnegative")
    record["download_max_bytes"] = limit
    path = job_record(job_id, repo)
    try:
        results_root(repo)  # Fail before any download, with no local fallback.
        client = client or Cwc(repo)
        job = client.json(f"/jobs/{identifier(job_id)}")
        record["cwc_status"] = str(job.get("status") or "unknown")
        listing = client.json(f"/jobs/{job_id}/artifacts")
        items = listing.get("artifacts", []) if isinstance(listing, dict) else listing
        present = set()
        for item in items:
            artifact = metadata(item)
            aid = artifact["artifact_id"]
            present.add(aid)
            previous = record["artifacts"].get(aid)
            if previous and any(previous.get(k) != artifact[k] for k in ["sha256", "size_bytes", "filename"]):
                raise ValueError("Canonical artifact identity changed; preserve earlier evidence and report CWC incident")
            target = artifact_path(job_id, aid, artifact["filename"], repo)
            artifact["result_path"] = target.relative_to(results_root(repo)).as_posix()
            artifact["state"] = "expected"
            record["artifacts"][aid] = artifact
            atomic_json(path, record)  # Durable expectation BEFORE fetching any bytes.
            receipt = target.parent / "receipt.json"
            if any(fnmatch.fnmatch(target.name, pattern) for pattern in record.get("keep_in_cwc", [])):
                artifact["state"] = "canonical_only_policy"
                continue
            if verified(target, artifact):
                artifact["state"] = "verified_local"
                atomic_json(receipt, {**artifact, "schema": "research_artifact_copy_v1", "job_id": job_id})
                continue
            if artifact["size_bytes"] > limit:
                artifact["state"] = "canonical_only_size_limit"
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            partial = require_payload_path(target.with_name(target.name + "." + uuid.uuid4().hex + ".part"), repo)
            try:
                sha = hashlib.sha256()
                total = 0
                with client.open(f"/jobs/{job_id}/artifacts/{aid}") as response, partial.open("xb") as handle:
                    for block in iter(lambda: response.read(1024 * 1024), b""):
                        total += len(block)
                        if total > artifact["size_bytes"] or total > limit:
                            raise ValueError("Artifact exceeds canonical size or bounded download limit")
                        sha.update(block)
                        handle.write(block)
                    handle.flush()
                    os.fsync(handle.fileno())
                if total != artifact["size_bytes"] or sha.hexdigest() != artifact["sha256"]:
                    raise ValueError("Artifact SHA-256 or size mismatch; partial copy is not a result")
                partial.replace(target)
                artifact["state"] = "verified_local"
                atomic_json(receipt, {**artifact, "schema": "research_artifact_copy_v1", "job_id": job_id})
            except urllib.error.HTTPError as error:
                artifact["state"] = "unavailable_cwc" if error.code in {404, 410} else "collection_pending"
                artifact["http_status"] = error.code
            finally:
                partial.unlink(missing_ok=True)
            atomic_json(path, record)
        # Never discard known artifact IDs when a later listing is empty.
        for aid, artifact in record["artifacts"].items():
            if aid not in present:
                target = artifact_path(job_id, aid, artifact["filename"], repo)
                artifact["state"] = "verified_local" if verified(target, artifact) else "not_listed_cwc"
        states = {a["state"] for a in record["artifacts"].values()}
        if not states:
            record["state"] = "zero_artifacts" if record["cwc_status"] in {"failed", "cancelled", "canceled"} else "awaiting_artifacts"
        elif states == {"verified_local"}:
            record["state"] = "verified_local"
        else:
            record["state"] = "collection_pending"
        record.pop("error", None)
    except urllib.error.HTTPError as error:
        record["state"] = "job_not_found_cwc" if error.code in {404, 410} else "service_unavailable"
        record["http_status"] = error.code
    except urllib.error.URLError as error:
        record["state"] = "service_unavailable"
        record["error"] = type(error).__name__
    except (OSError, ValueError, KeyError) as error:
        record["state"] = "collection_pending"
        # Avoid storing URLs, credentials or API response bodies in portable records.
        record["error"] = type(error).__name__
    record["last_checked_at"] = time.time()
    atomic_json(path, record)
    return record


def locate(job_id: str, artifact_id: str, repo: Path = ROOT) -> Path:
    record = json.loads(job_record(job_id, repo).read_text())
    artifact = record["artifacts"][identifier(artifact_id)]
    target = artifact_path(job_id, artifact_id, artifact["filename"], repo)
    if not verified(target, artifact):
        raise FileNotFoundError("Expected shared-store artifact is absent or unverified; reconcile the recorded CWC IDs")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    reference = commands.add_parser("reference", help="Record portable source or intermediate custody")
    reference.add_argument("name")
    reference.add_argument("--role", required=True)
    reference.add_argument("--sha256", required=True)
    reference.add_argument("--size-bytes", type=int)
    reference.add_argument("--job-id", default="")
    reference.add_argument("--artifact-id", default="")
    reference.add_argument("--shared-storage-id", default="")
    reference.add_argument("--relative-path", default="")
    expect = commands.add_parser("expect", help="Record a job immediately after CWC accepts it")
    expect.add_argument("job_id")
    expect.add_argument("--experiment-id", default="")
    collect = commands.add_parser("collect", help="Reconcile and download once, without submitting compute")
    collect.add_argument("job_id")
    collect.add_argument("--max-bytes", type=int, default=None)
    find = commands.add_parser("locate", help="Verify a result on this device by job/artifact IDs")
    find.add_argument("job_id")
    find.add_argument("artifact_id")
    commands.add_parser("resume", help="Reconcile outstanding recorded jobs once (suitable for a timer)")
    args = parser.parse_args()
    if args.command == "reference":
        remember_reference(args.name, args.role, args.sha256, job_id=args.job_id, artifact_id=args.artifact_id,
                           shared_storage_id=args.shared_storage_id, relative_path=args.relative_path, size_bytes=args.size_bytes)
        print(json.dumps({"reference": args.name, "state": "recorded"}))
        return 0
    if args.command == "expect":
        remember_job(args.job_id, args.experiment_id)
        print(json.dumps({"job_id": args.job_id, "state": "accepted"}))
        return 0
    if args.command == "locate":
        print(locate(args.job_id, args.artifact_id))
        return 0
    if args.command == "collect":
        record = collect_job(args.job_id, max_bytes=args.max_bytes)
        print(json.dumps({"job_id": args.job_id, "state": record["state"]}))
        return 0 if record["state"] == "verified_local" else 2
    pending = []
    for path in sorted((ROOT / "experiment_records/cwc_jobs").glob("*.json")):
        record = json.loads(path.read_text())
        # Verify a synced completion on this device before trusting the previous device's record.
        if record["state"] == "verified_local":
            try:
                for aid in record["artifacts"]:
                    locate(record["job_id"], aid)
                continue
            except (OSError, ValueError, KeyError):
                pass
        record = collect_job(record["job_id"])
        if record["state"] != "verified_local":
            pending.append({"job_id": record["job_id"], "state": record["state"]})
    print(json.dumps({"pending": pending}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
