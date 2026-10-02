from __future__ import annotations

import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import research_artifacts as custody
import research_storage as storage

spec = importlib.util.spec_from_file_location("storage_guard", ROOT / ".research/storage_guard.py")
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class FakeCwc:
    def __init__(self, content=b"bounded review output"):
        self.content = content
        self.items = [{"artifact_id": "artifact_1", "filename": "review.mkv",
                       "size_bytes": len(content), "sha256": __import__("hashlib").sha256(content).hexdigest()}]
        self.downloads = 0
        self.error = None
        self.status = "completed"

    def json(self, route):
        if self.error:
            raise self.error
        return {"artifacts": self.items} if route.endswith("/artifacts") else {"status": self.status}

    def open(self, route):
        if self.error:
            raise self.error
        self.downloads += 1
        return io.BytesIO(self.content)


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.repo = self.base / "checkout"
        self.repo.mkdir()
        self.store = self.base / "device-A-store"
        self.store.mkdir()
        (self.repo / ".research").mkdir()
        (self.repo / ".research/storage-policy.json").write_text(json.dumps({"project": "Example Project", "legacy_git_blobs": {}}))
        (self.repo / ".research/storage.local.json").write_text(json.dumps({"results_root": str(self.store)}))
        self.env = patch.dict(os.environ, {}, clear=False)
        self.env.start()
        os.environ.pop("RESEARCH_RESULTS_ROOT", None)

    def tearDown(self):
        self.env.stop()
        self.temp.cleanup()

    def git(self, *args, check=True):
        return subprocess.run(["git", "-C", str(self.repo), *args], capture_output=True, text=True, check=check)

    def init_git(self):
        self.git("init", "-q")
        self.git("config", "user.email", "storage-test@example.invalid")
        self.git("config", "user.name", "Storage test")

    def test_no_repo_fallback(self):
        (self.repo / ".research/storage.local.json").unlink()
        with self.assertRaises(ValueError):
            storage.results_root(self.repo)

    def test_reject_store_in_repo(self):
        with patch.dict(os.environ, {"RESEARCH_RESULTS_ROOT": str(self.repo)}):
            with self.assertRaises(ValueError):
                storage.results_root(self.repo)

    def test_reject_other_git_checkout(self):
        (self.store / ".git").mkdir()
        with self.assertRaises(ValueError):
            storage.results_root(self.repo)

    def test_traversal_and_symlink_escape(self):
        for value in ["../escape", self.repo]:
            with self.assertRaises(ValueError):
                storage.payload_path(value, self.repo)
        (self.store / "Example Project").symlink_to(self.repo, target_is_directory=True)
        with self.assertRaises(ValueError):
            storage.payload_path("output.png", self.repo)

    def test_legacy_alias_requires_actual_external_destination(self):
        project = self.store / "Example Project"
        project.mkdir()
        (self.repo / "results").symlink_to(project, target_is_directory=True)
        self.assertEqual(storage.require_payload_path(self.repo / "results/output.png", self.repo), project / "output.png")
        with self.assertRaises(ValueError):
            storage.require_payload_path(self.repo / "unexpected/output.png", self.repo)

    def test_new_and_disguised_payloads_blocked(self):
        for path, data in [("results/report.json", b"{}"), ("unexpected.png", b"x"), ("notes.txt", b"a\0b"), ("huge.json", b"x" * (guard.LIMIT + 1))]:
            self.assertIsNotNone(guard.reason(path, len(data), data[:8192]), path)
        self.assertIsNone(guard.reason("experiment_records/receipt.json", 2, b"{}"))
        self.assertIsNone(guard.reason("scripts/experiment.py", 7, b"print()"))

    def test_index_blocks_force_added_ignored_media(self):
        self.init_git()
        (self.repo / ".gitignore").write_text("*.png\n")
        (self.repo / "output.png").write_bytes(b"new media")
        self.git("add", "-f", "output.png")
        self.assertTrue(guard.check_git(guard.index_entries(self.repo), {}, self.repo))

    def test_historical_blob_frozen(self):
        self.init_git()
        file = self.repo / "historic.png"
        file.write_bytes(b"old evidence")
        self.git("add", "historic.png")
        entries = list(guard.index_entries(self.repo))
        baseline = {entries[0][0]: entries[0][2]}
        self.assertEqual(guard.check_git(entries, baseline, self.repo), [])
        (self.repo / ".research/storage-policy.json").write_text(json.dumps({"project": "Example Project", "legacy_git_blobs": baseline}))
        self.assertEqual(guard.check_filesystem(self.repo), [])
        file.write_bytes(b"new result")
        self.git("add", "historic.png")
        self.assertTrue(guard.check_git(guard.index_entries(self.repo), baseline, self.repo))

    def test_commit_hook_actually_rejects_payload(self):
        self.init_git()
        shutil.copy(ROOT / ".research/storage_guard.py", self.repo / ".research/storage_guard.py")
        shutil.copytree(ROOT / ".research/hooks", self.repo / ".research/hooks")
        shutil.copy(ROOT / ".research/install.py", self.repo / ".research/install.py")
        for hook in (self.repo / ".research/hooks").iterdir():
            hook.chmod(0o644)  # Fresh checkouts can lose executable bits on some devices.
        subprocess.run([sys.executable, "-B", str(self.repo / ".research/install.py")], check=True, capture_output=True)
        (self.repo / "output.png").write_bytes(b"new media")
        self.git("add", "-f", "output.png")
        result = self.git("commit", "-m", "must fail", check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Research storage boundary failed", result.stdout + result.stderr)

    def test_ignored_local_payload_is_detected(self):
        self.init_git()
        (self.repo / ".gitignore").write_text("results/\n")
        (self.repo / "results").mkdir()
        (self.repo / "results/new.png").write_bytes(b"new media")
        self.assertTrue(any("results/new.png" in item for item in guard.check_filesystem(self.repo)))

    def test_expectation_survives_service_outage(self):
        custody.remember_job("job_1", "experiment_1", self.repo)
        client = FakeCwc()
        client.error = OSError("offline")
        record = custody.collect_job("job_1", client=client, repo=self.repo)
        self.assertEqual(record["job_id"], "job_1")
        self.assertEqual(record["experiment_id"], "experiment_1")
        self.assertEqual(record["state"], "collection_pending")
        client.error = None
        self.assertEqual(custody.collect_job("job_1", client=client, repo=self.repo)["state"], "verified_local")

    def test_late_artifact_after_empty_completed_job(self):
        client = FakeCwc()
        artifacts, client.items = client.items, []
        record = custody.collect_job("job_1", client=client, repo=self.repo)
        self.assertEqual(record["state"], "awaiting_artifacts")
        client.items = artifacts
        record = custody.collect_job("job_1", client=client, repo=self.repo)
        target = custody.locate("job_1", "artifact_1", self.repo)
        self.assertEqual(target.read_bytes(), client.content)
        self.assertEqual(record["artifacts"]["artifact_1"]["result_path"], "Example Project/artifacts/job_1/artifact_1/review.mkv")
        self.assertFalse(any(self.repo.rglob("*.mkv")))

    def test_collection_idempotent(self):
        client = FakeCwc()
        custody.collect_job("job_1", client=client, repo=self.repo)
        custody.collect_job("job_1", client=client, repo=self.repo)
        self.assertEqual(client.downloads, 1)

    def test_corrupt_download_not_published(self):
        client = FakeCwc()
        client.content = b"bad response"
        record = custody.collect_job("job_1", client=client, repo=self.repo)
        self.assertEqual(record["state"], "collection_pending")
        self.assertFalse(any(self.store.rglob("*.mkv")))
        self.assertFalse(any(self.store.rglob("*.part")))

    def test_shared_record_resolves_on_second_device(self):
        client = FakeCwc()
        custody.collect_job("job_1", client=client, repo=self.repo)
        store_b = self.base / "device-B-store"
        store_b.mkdir()
        with patch.dict(os.environ, {"RESEARCH_RESULTS_ROOT": str(store_b)}):
            with self.assertRaises(FileNotFoundError):
                custody.locate("job_1", "artifact_1", self.repo)
            shutil.copytree(self.store / "Example Project", store_b / "Example Project")
            self.assertEqual(custody.locate("job_1", "artifact_1", self.repo).read_bytes(), client.content)

    def test_empty_listing_preserves_known_ids(self):
        client = FakeCwc()
        custody.collect_job("job_1", client=client, repo=self.repo)
        client.items = []
        record = custody.collect_job("job_1", client=client, repo=self.repo)
        self.assertIn("artifact_1", record["artifacts"])
        self.assertEqual(record["state"], "verified_local")

    def test_bounded_copy_does_not_download_master(self):
        client = FakeCwc()
        record = custody.collect_job("job_1", client=client, repo=self.repo, max_bytes=1)
        self.assertEqual(client.downloads, 0)
        self.assertEqual(record["artifacts"]["artifact_1"]["state"], "canonical_only_size_limit")

    def test_terminal_zero_artifacts_not_completion(self):
        client = FakeCwc()
        client.status, client.items = "failed", []
        self.assertEqual(custody.collect_job("job_1", client=client, repo=self.repo)["state"], "zero_artifacts")

    def test_canonical_identity_change_does_not_overwrite(self):
        client = FakeCwc()
        custody.collect_job("job_1", client=client, repo=self.repo)
        target = custody.locate("job_1", "artifact_1", self.repo)
        client.items[0]["sha256"] = "a" * 64
        record = custody.collect_job("job_1", client=client, repo=self.repo)
        self.assertEqual(record["state"], "collection_pending")
        self.assertEqual(target.read_bytes(), client.content)

    def test_source_reference_rejects_device_mount_paths(self):
        for path in ["C:\\scans\\source.dpx", "/srv/scans/source.dpx", "../source.dpx", "\\\\server\\share\\source.dpx"]:
            with self.assertRaises(ValueError):
                custody.remember_reference("source_1", "original", "a" * 64, shared_storage_id="canonical-scans", relative_path=path, repo=self.repo)
        record = custody.remember_reference("source_1", "original", "a" * 64, shared_storage_id="canonical-scans", relative_path="reel/source.dpx", repo=self.repo)
        self.assertEqual(record["reference"]["relative_path"], "reel/source.dpx")
        with self.assertRaises(ValueError):
            custody.remember_reference("source_1", "original", "b" * 64, shared_storage_id="canonical-scans", relative_path="reel/source.dpx", repo=self.repo)

    def test_real_http_collector_reads_cwc_routes_only(self):
        import http.server
        import threading
        fake = FakeCwc()
        requests = []
        class Handler(http.server.BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass
            def do_GET(self):
                requests.append(self.path)
                if self.path.endswith("/artifact_1"):
                    body = fake.content
                else:
                    body = json.dumps(fake.json(self.path)).encode()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(body)
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            client = custody.Cwc(base_url=f"http://127.0.0.1:{server.server_port}", api_key="test-key")
            record = custody.collect_job("job_1", client=client, repo=self.repo)
            self.assertEqual(record["state"], "verified_local")
            self.assertEqual(requests, ["/jobs/job_1", "/jobs/job_1/artifacts", "/jobs/job_1/artifacts/artifact_1"])
            self.assertEqual(custody.locate("job_1", "artifact_1", self.repo).read_bytes(), fake.content)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
