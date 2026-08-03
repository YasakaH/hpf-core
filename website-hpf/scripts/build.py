"""Build script for the HPF Research Workbench site.

Regenerates the data layer for website-hpf/ from the research corpus:

    1. Produce the export contract (export.py)
    2. Gate on contract conformance (check_contract.py)
    3. Build the knowledge index (index.py)

The site itself is static: data/export.json and data/index.json are derived
projections of the corpus and are consumed by the workbench UI at runtime.

Usage (from repo root):
    python website-hpf/scripts/build.py
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE = REPO_ROOT / "tools" / "hpf-engine"
SITE = REPO_ROOT / "website-hpf"
DATA = SITE / "data"

EXPORT_OUT = DATA / "export.json"
INDEX_OUT = DATA / "index.json"


def run(script: str, *args: str, cwd: Path) -> None:
    cmd = [sys.executable, script, *args]
    print(f"> {' '.join(str(c) for c in cmd)}")
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.returncode != 0:
        print(proc.stderr, end="")
        sys.exit(f"FAILED: {script} exited {proc.returncode}")


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    run("export.py", "--out", str(EXPORT_OUT), cwd=ENGINE)
    run("check_contract.py", str(EXPORT_OUT), cwd=ENGINE)
    run("index.py", "--export", str(EXPORT_OUT), "--out", str(INDEX_OUT), cwd=ENGINE)
    print("Workbench data ready: data/export.json + data/index.json")


if __name__ == "__main__":
    main()
