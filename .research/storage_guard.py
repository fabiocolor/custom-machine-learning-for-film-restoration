#!/usr/bin/env python3
"""Reject new result payloads in Git or in a checkout (including ignored files)."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 1024 * 1024
PAYLOAD_EXTENSIONS = set(".png .jpg .jpeg .gif .webp .tif .tiff .bmp .dpx .exr .mov .mp4 .mkv .avi .webm .wav .mp3 .flac .aiff .pt .pth .ckpt .safetensors .onnx .bin .npy .npz .pkl .pickle .zip .gz .bz2 .xz .7z .tar .sqlite .db .pdf .docx .pptx .xlsx".split())
PAYLOAD_DIRS = set("results runs outputs models checkpoints artifacts caches cache EXPERIMENT_RESULTS _media sampled_sequence".split())
DEPENDENCIES = set(".git .venv venv node_modules __pycache__ .tools .tooling-venv .venv-shotdetect .pytest_cache .mypy_cache .ruff_cache".split())


def git(*args: str, repo: Path = ROOT) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args])


def reason(path: str, size: int, sample: bytes = b"", mode: str = "100644") -> str | None:
    if mode == "120000":  # Compatibility links hold no result bytes.
        return None
    if mode == "160000":
        return "submodules require a separate storage review"
    parts = Path(path).parts
    if parts and parts[0] != "experiment_records" and any(p in PAYLOAD_DIRS for p in parts[:-1]):
        return "reserved payload directory"
    if Path(path).suffix.lower() in PAYLOAD_EXTENSIONS:
        return "media, model, array, archive or generated document payload"
    if size > LIMIT:
        return "file exceeds the 1 MiB compact-record limit"
    if b"\0" in sample:
        return "binary payload"
    try:
        # An incomplete final UTF-8 codepoint is harmless in this bounded probe.
        sample.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        if exc.reason != "unexpected end of data":
            return "non-text payload"
    return None


def tree_entries(ref: str, repo: Path = ROOT):
    for row in git("ls-tree", "-rlz", ref, repo=repo).split(b"\0"):
        if not row:
            continue
        meta, path = row.split(b"\t", 1)
        mode, kind, oid, size = meta.decode().split()
        yield path.decode(), mode, oid, int(size) if size != "-" else 0


def index_entries(repo: Path = ROOT):
    entries = []
    for row in git("ls-files", "--stage", "-z", repo=repo).split(b"\0"):
        if not row:
            continue
        meta, path = row.split(b"\t", 1)
        mode, oid, stage = meta.decode().split()
        if stage != "0":
            raise ValueError("Resolve the index conflict before committing")
        entries.append((path.decode(), mode, oid))
    oids = [oid for _, mode, oid in entries if mode != "160000"]
    sizes = subprocess.check_output(["git", "-C", str(repo), "cat-file", "--batch-check=%(objectname) %(objectsize)"], input=("\n".join(oids) + "\n").encode())
    sizes = {row.split()[0].decode(): int(row.split()[1]) for row in sizes.splitlines() if len(row.split()) == 2}
    for path, mode, oid in entries:
        yield path, mode, oid, sizes.get(oid, 0)


def check_git(entries, baseline: dict, repo: Path = ROOT) -> list[str]:
    errors = []
    process = subprocess.Popen(["git", "-C", str(repo), "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        for path, mode, oid, size in entries:
            if baseline.get(path) == oid:
                continue
            sample = b""
            if mode not in {"120000", "160000"} and size <= LIMIT:
                process.stdin.write((oid + "\n").encode())
                process.stdin.flush()
                header = process.stdout.readline().split()
                if len(header) != 3 or header[1] != b"blob":
                    raise ValueError("Cannot read indexed Git blob")
                sample = process.stdout.read(int(header[2]))[:8192]
                process.stdout.read(1)
            problem = reason(path, size, sample, mode)
            if problem:
                errors.append(f"{path}: {problem}")
    finally:
        process.stdin.close()
        process.stdout.close()
        process.wait()
    return errors


def local_files(repo: Path = ROOT):
    # Never follow compatibility links into the potentially huge shared result store.
    for folder, dirs, files in os.walk(repo, followlinks=False):
        dirs[:] = [d for d in dirs if d not in DEPENDENCIES and not (Path(folder) / d).is_symlink()]
        for name in files:
            path = Path(folder) / name
            if path.is_symlink() or name == ".git":
                continue
            stat = path.stat()
            yield path.relative_to(repo).as_posix(), path, stat


def local_baseline_path(repo: Path = ROOT) -> Path:
    value = Path(git("rev-parse", "--git-path", "research-storage-local-baseline.json", repo=repo).decode().strip())
    return value if value.is_absolute() else repo / value


def check_filesystem(repo: Path = ROOT) -> list[str]:
    path = local_baseline_path(repo)
    # Installation snapshots pre-existing local evidence without moving or deleting it.
    legacy = json.loads(path.read_text()) if path.is_file() else {}
    policy_path = repo / ".research/storage-policy.json"
    git_legacy = json.loads(policy_path.read_text()).get("legacy_git_blobs", {}) if policy_path.exists() else {}
    errors = []
    for relative, file, stat in local_files(repo):
        if legacy.get(relative) == [stat.st_size, stat.st_mtime_ns]:
            continue
        # Fresh clones have no device-local inventory. Preserve their immutable
        # tracked evidence using the same exact blob hashes as the Git guard.
        if relative in git_legacy:
            oid = git("hash-object", "--", str(file.resolve()), repo=repo).decode().strip()
            if oid == git_legacy[relative]:
                continue
        sample = b""
        if stat.st_size <= LIMIT:
            with file.open("rb") as handle:
                sample = handle.read(8192)
        problem = reason(relative, stat.st_size, sample)
        if problem:
            errors.append(f"{relative}: {problem}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staged", action="store_true")
    parser.add_argument("--tree", metavar="REF")
    parser.add_argument("--filesystem", action="store_true")
    args = parser.parse_args()
    if not (args.staged or args.tree or args.filesystem):
        parser.error("select --staged, --tree REF or --filesystem")
    policy = json.loads((ROOT / ".research/storage-policy.json").read_text())
    errors = []
    if args.staged:
        errors += check_git(index_entries(), policy["legacy_git_blobs"])
    if args.tree:
        errors += check_git(tree_entries(args.tree), policy["legacy_git_blobs"])
    if args.filesystem:
        errors += check_filesystem()
    if errors:
        print("Research storage boundary failed. Put payloads in the configured EXPERIMENT_RESULTS store; keep compact records in experiment_records/.")
        print("\n".join(errors[:40]))
        if len(errors) > 40:
            print(f"... {len(errors) - 40} further violations")
        return 1
    print("Research storage boundary passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
