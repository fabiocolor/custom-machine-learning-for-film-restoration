"""Fail-closed paths for project-owned result copies; no worker routing."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def policy(repo: Path = ROOT) -> dict:
    return json.loads((repo / ".research/storage-policy.json").read_text())


def identifier(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,160}", value):
        raise ValueError("Invalid job, artifact or project identifier")
    return value


def results_root(repo: Path = ROOT) -> Path:
    config = repo / ".research/storage.local.json"
    configured = os.environ.get("RESEARCH_RESULTS_ROOT")
    if not configured and config.is_file():
        configured = json.loads(config.read_text()).get("results_root")
    if not configured:
        raise ValueError("Configure RESEARCH_RESULTS_ROOT or .research/storage.local.json; no repo-local fallback")
    path = Path(configured).expanduser()
    if not path.is_absolute():
        path = repo / path
    path = path.resolve()
    # Check all ancestors, including sibling or nested Git checkouts.
    if path == repo.resolve() or path.is_relative_to(repo.resolve()):
        raise ValueError("Result store must be outside the project checkout")
    if any((parent / ".git").exists() for parent in (path, *path.parents)):
        raise ValueError("Result store must be outside every Git checkout")
    if not path.is_dir():
        raise ValueError("Configured result store does not exist; do not create a fallback")
    return path


def payload_path(relative: str | Path, repo: Path = ROOT) -> Path:
    relative = Path(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Payload path must be relative with no parent traversal")
    root = results_root(repo)
    project = str(policy(repo)["project"])
    if not project or project in {".", ".."} or "/" in project or "\\" in project:
        raise ValueError("Invalid project directory")
    project_root = (root / project).resolve()
    target = (project_root / relative).resolve()
    if not project_root.is_relative_to(root) or not target.is_relative_to(project_root):
        raise ValueError("Result path escapes project store through a symlink")
    if any((parent / ".git").exists() for parent in (target, *target.parents)):
        raise ValueError("Result path enters a Git checkout")
    return target


def require_payload_path(path: Path | str, repo: Path = ROOT) -> Path:
    target = Path(path).resolve()
    base = payload_path(".", repo)
    if not target.is_relative_to(base):
        raise ValueError("Payload destination must be in this project's configured external result store")
    return payload_path(target.relative_to(base), repo)


def artifact_path(job_id: str, artifact_id: str, filename: str, repo: Path = ROOT) -> Path:
    # CWC names may include internal folders, but must never choose local directories.
    name = filename.replace("\\", "/").split("/")[-1]
    if not name or name in {".", "..", "receipt.json"} or "\0" in name:
        raise ValueError("Invalid artifact filename")
    return payload_path(Path("artifacts") / identifier(job_id) / identifier(artifact_id) / name, repo)
