"""Promote a research session into the committed release area (exports/sessions).

Sessions are first-class release artifacts, exactly like the export contract:
immutable once released (refuses to overwrite), reproducible from the
orchestrator, assembled into the workbench at deploy time.

Usage:
    python tools/hpf-research/export_session.py <session-id> [--dir sessions]
"""
import argparse
import shutil
import sys
from pathlib import Path

from research import promote_session

EXPORTS = Path(__file__).resolve().parent.parent.parent / "exports"


def main():
    ap = argparse.ArgumentParser(description="HPF session release exporter")
    ap.add_argument("session_id")
    ap.add_argument("--dir", default=str(Path(__file__).resolve().parent / "sessions"))
    args = ap.parse_args()
    sys.exit(promote_session(args.session_id, Path(args.dir), EXPORTS))


if __name__ == "__main__":
    main()
