#!/usr/bin/env python3
"""Install a device-local collection timer; run on one collector device per project."""
import hashlib
import platform
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
script = root / "scripts/research_artifacts.py"
name = "research-artifacts-" + hashlib.sha256(str(root).encode()).hexdigest()[:12]
if platform.system() == "Linux":
    directory = Path.home() / ".config/systemd/user"
    directory.mkdir(parents=True, exist_ok=True)
    def quote(value):
        return '"' + str(value).replace('\\', '\\\\').replace('"', '\\"').replace('%', '%%') + '"'
    (directory / (name + ".service")).write_text(
        "[Unit]\nDescription=Collect recorded research artifacts through CWC\n\n"
        "[Service]\nType=oneshot\nTimeoutStartSec=10min\n"
        f"ExecStart={quote(sys.executable)} -B {quote(script)} resume\n")
    (directory / (name + ".timer")).write_text(
        "[Unit]\nDescription=Resume outstanding research artifact collection\n\n"
        "[Timer]\nOnStartupSec=30s\nOnUnitInactiveSec=2min\nPersistent=true\n\n"
        "[Install]\nWantedBy=timers.target\n")
    subprocess.run(["systemd-analyze", "--user", "verify", str(directory / (name + ".service")), str(directory / (name + ".timer"))], check=True)
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "--user", "enable", "--now", name + ".timer"], check=True)
    subprocess.run(["systemctl", "--user", "start", name + ".service"], check=True)
elif platform.system() == "Windows":
    command = subprocess.list2cmdline([sys.executable, "-B", str(script), "resume"])
    subprocess.run(["schtasks", "/Create", "/SC", "MINUTE", "/MO", "2", "/TN", name, "/TR", command, "/F"], check=True)
else:
    raise SystemExit("Configure your device scheduler to run scripts/research_artifacts.py resume")
print(name)
