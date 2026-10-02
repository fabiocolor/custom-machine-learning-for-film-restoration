#!/usr/bin/env python3
"""Install checkout hooks; never regenerate historical payload exceptions."""
from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
common = Path(subprocess.check_output(["git", "-C", str(root), "rev-parse", "--git-common-dir"], text=True).strip())
if not common.is_absolute():
    common = (root / common).resolve()
installed = common / "research-storage-hooks"
current = subprocess.run(["git", "-C", str(root), "config", "--get", "core.hooksPath"], capture_output=True, text=True).stdout.strip()
if current and current not in {".research/hooks", str(installed)}:
    raise SystemExit("Existing hooksPath needs explicit integration; not overwriting it")
installed.mkdir(exist_ok=True)
for name in ["pre-commit", "pre-push"]:
    (root / ".research/hooks" / name).chmod(0o755)
    shutil.copy2(root / ".research/hooks" / name, installed / name)
subprocess.run(["git", "-C", str(root), "config", "core.hooksPath", str(installed)], check=True)
print("Research storage hooks installed. Configure RESEARCH_RESULTS_ROOT for this device.")
