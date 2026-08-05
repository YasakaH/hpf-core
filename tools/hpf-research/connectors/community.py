"""Community Evidence Connector — v1: Devvit CLI (Reddit).

Gathers structured community signal from Reddit via the Devvit CLI. The
connector only emits *structured payloads*; it never interprets them. HPF
labels everything it produces as `community_signal` — observation, not truth.

Payload schema (written to --out as JSON):

    {
      "source": "reddit",
      "subreddit": "webscraping",
      "thread": "title or permalink",
      "score": 412,
      "comments": [
        {"text": "...", "score": 81, "author": "...", "url": "..."}
      ]
    }

Devvit CLI is optional at runtime: the connector is a thin wrapper. When the
binary is missing it reports so honestly and suggests installing it
(`npm i -g devvit`); the payload schema above can also be produced by any
other community source (HN, Stack Overflow, GitHub Discussions) — the
planner picks the connector, HPF only consumes the schema.
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

PAYLOAD_SCHEMA = ("source", "subreddit", "thread", "score", "comments")


def devvit_available() -> bool:
    return shutil.which("devvit") is not None


def run_devvit(subreddit: str, query: str, limit: int, out_path: Path) -> int:
    """Invoke the Devvit CLI and write the normalized payload.

    Expected CLI contract (v1):
        devvit hpf search --subreddit <sub> --query <q> --limit <n> --json

    When the binary is absent, fail loudly rather than fabricate data.
    """
    if not devvit_available():
        print("! Devvit CLI not found (community connector v1 is a thin wrapper).")
        print("  Install with:  npm i -g devvit")
        print("  Or supply a payload file: --payload community.json")
        return 4
    cmd = [
        "devvit", "hpf", "search",
        "--subreddit", subreddit,
        "--query", query,
        "--limit", str(limit),
        "--json",
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except (subprocess.TimeoutExpired, OSError) as e:
        print(f"! devvit invocation failed: {e}")
        return 5
    if proc.returncode != 0:
        print(f"! devvit exited {proc.returncode}: {proc.stderr.strip()[:500]}")
        return 6
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        print("! devvit output was not JSON; refusing to guess.")
        return 7
    return write_payload(payload, out_path)


def validate_payload(payload: dict) -> list:
    """Return a list of schema problems (empty = valid)."""
    problems = []
    for field in PAYLOAD_SCHEMA:
        if field not in payload:
            problems.append(f"missing field: {field}")
    if not isinstance(payload.get("comments"), list):
        problems.append("comments must be a list")
    return problems


def write_payload(payload: dict, out_path: Path) -> int:
    problems = validate_payload(payload)
    if problems:
        print("! invalid community payload:")
        for p in problems:
            print(f"  - {p}")
        return 8
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Community payload written: {out_path}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="HPF Community Evidence Connector (v1: Devvit CLI)")
    ap.add_argument("--subreddit", default="")
    ap.add_argument("--query", default="")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--out", default="community-payload.json")
    ap.add_argument("--payload", default="", help="validate/normalize an existing payload file")
    args = ap.parse_args()

    if args.payload:
        payload = json.loads(Path(args.payload).read_text(encoding="utf-8"))
        sys.exit(write_payload(payload, Path(args.out)))

    if not args.subreddit or not args.query:
        print("! need --subreddit and --query (or --payload file.json)")
        sys.exit(2)

    sys.exit(run_devvit(args.subreddit, args.query, args.limit, Path(args.out)))


if __name__ == "__main__":
    main()
