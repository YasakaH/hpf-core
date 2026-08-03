"""Build script for the HPF Research Workbench site.

Assembles website-hpf/ from the committed release artifacts in exports/:

    1. Gate on contract conformance (check_contract.py against exports/latest.json)
    2. Verify the committed index parses
    3. Copy exports/latest.json -> data/export.json, latest.index.json -> data/index.json

The workbench serves a release, it never regenerates one. The export/index are
versioned, committed release artifacts; the corpus is the single source of
truth and generation happens only as an owner-driven release step.

Release flow (owner-driven):

    1. python tools/hpf-engine/export.py --out exports/YYYY-MM-DD.json
    2. python tools/hpf-engine/check_contract.py exports/YYYY-MM-DD.json
    3. python tools/hpf-engine/index.py --export exports/YYYY-MM-DD.json --out exports/YYYY-MM-DD.index.json
    4. copy the two files to exports/latest.json and exports/latest.index.json
    5. commit exports/ with the release
    6. python website-hpf/scripts/build.py
    7. dispatch the "Release HPF Workbench" workflow (deploys)

Usage (from repo root):
    python website-hpf/scripts/build.py
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE = REPO_ROOT / "tools" / "hpf-engine"
SITE = REPO_ROOT / "website-hpf"
DATA = SITE / "data"
EXPORTS = REPO_ROOT / "exports"

EXPORT_RELEASE = EXPORTS / "latest.json"
INDEX_RELEASE = EXPORTS / "latest.index.json"

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
    if not EXPORT_RELEASE.is_file() or not INDEX_RELEASE.is_file():
        sys.exit(f"FAILED: release artifacts missing in exports/ ({EXPORT_RELEASE.name}, {INDEX_RELEASE.name})")

    run("check_contract.py", str(EXPORT_RELEASE), cwd=ENGINE)

    with INDEX_RELEASE.open(encoding="utf-8") as fh:
        index = json.load(fh)
    objects = index.get("objects") or []
    if not objects:
        sys.exit("FAILED: committed index contains no objects")

    DATA.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(EXPORT_RELEASE, EXPORT_OUT)
    shutil.copyfile(INDEX_RELEASE, INDEX_OUT)
    print(
        f"Workbench data synced from {EXPORT_RELEASE.name} "
        f"({len(objects)} objects): data/export.json + data/index.json"
    )


if __name__ == "__main__":
    main()
