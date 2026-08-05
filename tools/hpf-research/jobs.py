"""HPF Job Status Registry v0 — the shared work queue.

The Job Status Contract lets subsystems (research, publishing, marketing,
website) publish ONLY their current job state; HPF consumes those status
records and never depends on any subsystem's internals. This is the reverse
of the export contract: consumers never know HPF internals, HPF never knows
consumer internals.

Contract (schema `hpf-job-status-v0`, one file per job):

    {
      "schema": "hpf-job-status-v0",
      "job": "publish-42",
      "type": "publishing",          # research | publishing | marketing | website
      "owner": "publishing-engine",  # which subsystem wrote the record
      "status": "drafting",          # queued | running | drafting | review |
                                     # ready | done | blocked | cancelled
      "progress": "draft_complete",  # free-form, subsystem-chosen
      "research_session": "2026-08-05-0601-...",
      "started": "2026-08-05T14:20:00Z",
      "updated": "2026-08-05T15:01:00Z",
      "outputs": ["article.md"]
    }

Registry layout:

    exports/jobs/<job-id>.json      immutable-per-state record files
    exports/jobs/index.json         manifest of all job records

Usage:

    python jobs.py update <job-id> --type <t> --owner <o> --status <s> \
        [--progress ...] [--session <id>] [--outputs a.md,b.md]
    python jobs.py list
    python jobs.py check            # validate every record; exit 1 on problems

Only the `status` vocabulary is shared; `progress` and `outputs` are
free-form so subsystems stay loosely coupled.
"""

import argparse
import datetime
import json
import sys
from pathlib import Path

SCHEMA = "hpf-job-status-v0"
STATUSES = ("queued", "running", "drafting", "review", "ready", "done", "blocked", "cancelled")
TYPES = ("research", "publishing", "marketing", "website")
REQUIRED = ("schema", "job", "type", "owner", "status", "started", "updated")

ROOT = Path(__file__).resolve().parent.parent.parent
JOBS_DIR = ROOT / "exports" / "jobs"


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def problems_of(job: dict) -> list:
    p = []
    for field in REQUIRED:
        if not job.get(field):
            p.append(f"missing field: {field}")
    if job.get("schema") != SCHEMA:
        p.append(f"schema must be {SCHEMA}")
    if job.get("status") and job["status"] not in STATUSES:
        p.append(f"unknown status: {job['status']} (allowed: {', '.join(STATUSES)})")
    if job.get("type") and job["type"] not in TYPES:
        p.append(f"unknown type: {job['type']} (allowed: {', '.join(TYPES)})")
    if job.get("outputs") is not None and not isinstance(job.get("outputs"), list):
        p.append("outputs must be a list")
    return p


def write_index() -> int:
    entries = []
    for f in sorted(JOBS_DIR.glob("*.json")):
        if f.name == "index.json":
            continue
        try:
            job = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        entries.append(job)
    entries.sort(key=lambda j: j.get("updated") or "", reverse=True)
    (JOBS_DIR / "index.json").write_text(
        json.dumps({"schema": "hpf-jobs-manifest-v0", "jobs": entries}, indent=2),
        encoding="utf-8",
    )
    return len(entries)


def cmd_update(args) -> int:
    if args.status not in STATUSES:
        print(f"! unknown status: {args.status} (allowed: {', '.join(STATUSES)})")
        return 2
    if args.type not in TYPES:
        print(f"! unknown type: {args.type} (allowed: {', '.join(TYPES)})")
        return 2
    job_id = args.job
    path = JOBS_DIR / f"{job_id}.json"
    job = {}
    if path.exists():
        try:
            job = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print(f"! unreadable existing record {job_id}; refusing to overwrite")
            return 3
    started = job.get("started") or now_iso()
    job.update({
        "schema": SCHEMA,
        "job": job_id,
        "type": args.type,
        "owner": args.owner,
        "status": args.status,
        "started": started,
        "updated": now_iso(),
    })
    if args.progress is not None:
        job["progress"] = args.progress
    if args.session is not None:
        job["research_session"] = args.session
    if args.outputs is not None:
        job["outputs"] = [o.strip() for o in args.outputs.split(",") if o.strip()]
    problems = problems_of(job)
    if problems:
        print("! invalid job record:")
        for p in problems:
            print(f"  - {p}")
        return 4
    JOBS_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(job, indent=2), encoding="utf-8")
    n = write_index()
    print(f"Job {job_id}: {job['status']} (updated {job['updated']}) — {n} jobs in registry")
    return 0


def cmd_list(args) -> int:
    idx_path = JOBS_DIR / "index.json"
    if not idx_path.exists():
        print("(no jobs registered)")
        return 0
    jobs = json.loads(idx_path.read_text(encoding="utf-8")).get("jobs") or []
    for j in jobs:
        session = j.get("research_session") or "-"
        print(f"{j['job']:<28} {j['type']:<10} {j['status']:<10} {j['owner']:<18} {session}")
    print(f"{len(jobs)} jobs")
    return 0


def cmd_check(args) -> int:
    bad = 0
    for f in sorted(JOBS_DIR.glob("*.json")):
        if f.name == "index.json":
            continue
        try:
            job = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            print(f"! {f.name}: unreadable ({e})")
            bad += 1
            continue
        problems = problems_of(job)
        if problems:
            bad += 1
            print(f"! {f.name}:")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"  ok {f.name} ({job.get('status')})")
    if bad:
        print(f"{bad} invalid record(s)")
        return 1
    print("all job records valid")
    return 0


def main():
    ap = argparse.ArgumentParser(description="HPF Job Status Registry v0")
    sub = ap.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("update", help="create or update a job record")
    u.add_argument("job")
    u.add_argument("--type", required=True, choices=TYPES)
    u.add_argument("--owner", required=True)
    u.add_argument("--status", required=True, choices=STATUSES)
    u.add_argument("--progress", default=None)
    u.add_argument("--session", default=None)
    u.add_argument("--outputs", default=None)
    u.set_defaults(fn=cmd_update)
    sub.add_parser("list", help="list registered jobs").set_defaults(fn=cmd_list)
    sub.add_parser("check", help="validate every job record").set_defaults(fn=cmd_check)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
