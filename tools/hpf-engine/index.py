"""Knowledge Index builder — a derived projection of the Knowledge Export.

Contract-only consumer: reads an export produced by export.py (knowledge-export-
core-v1) and aggregates it into a queryable index. Never imports engine
internals, never reads the corpus or dossiers, never writes to the corpus.

The index is regenerable and disposable; the export remains its input, the
corpus remains the single source of truth.

Usage:
    python index.py --export export/latest.json --out export/index.json
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

PRODUCER = "hpf-engine/index.py"
PRODUCER_VERSION = "0.1.0"


def build(export_path: Path) -> dict:
    data = json.loads(Path(export_path).read_text(encoding="utf-8"))
    objs = data.get("objects", [])

    summary = {
        "total": len(objs),
        "valid": 0,
        "invalid": 0,
        "error_count": 0,
        "kinds": Counter(),
        "origins": Counter(),
        "authorities": Counter(),
        "statuses": Counter(),
        "domains": Counter(),
        "cycles": set(),
    }

    objects = []
    edges = []
    cross_domain_edges = []
    invalid = []
    domain_of = {}

    for o in objs:
        valid = o.get("schema_validation") == "valid"
        if valid:
            summary["valid"] += 1
        else:
            summary["invalid"] += 1
            summary["error_count"] += len(o.get("errors") or [])
            invalid.append(
                {"id": o.get("id"), "title": o.get("title"), "source": o.get("source"),
                 "errors": o.get("errors") or []}
            )
        kind = o.get("kind") or "unknown"
        domain = o.get("domain")
        cycle = o.get("research_cycle")
        summary["kinds"][kind] += 1
        summary["origins"][o.get("origin")] += 1
        summary["authorities"][o.get("authority")] += 1
        summary["statuses"][o.get("status")] += 1
        if domain:
            summary["domains"][domain] += 1
        if cycle:
            summary["cycles"].add(cycle)
        domain_of[o.get("id")] = domain

        objects.append(
            {
                "id": o.get("id"),
                "title": o.get("title"),
                "kind": kind,
                "domain": domain,
                "cycle": cycle,
                "origin": o.get("origin"),
                "authority": o.get("authority"),
                "status": o.get("status"),
                "valid": valid,
                "source": o.get("source"),
            }
        )

        if valid:
            for rel in o.get("relationships") or []:
                target = rel.get("concept")
                edge = {
                    "source": o.get("id"),
                    "source_title": o.get("title"),
                    "target": target,
                    "relationship": rel.get("relationship"),
                    "description": rel.get("description"),
                }
                edges.append(edge)
                if target and domain and domain_of.get(target) and domain != domain_of[target]:
                    cross_domain_edges.append(edge)

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "producer": PRODUCER,
        "producer_version": PRODUCER_VERSION,
        "source_contract": data.get("contract"),
        "source_schema_version": data.get("schema_version"),
        "summary": {
            "total": summary["total"],
            "valid": summary["valid"],
            "invalid": summary["invalid"],
            "error_count": summary["error_count"],
            "kinds": dict(sorted(summary["kinds"].items())),
            "origins": dict(sorted(summary["origins"].items())),
            "authorities": dict(sorted(summary["authorities"].items())),
            "statuses": dict(sorted(summary["statuses"].items())),
            "domains": dict(sorted(summary["domains"].items())),
            "cycles": sorted(summary["cycles"]),
        },
        "objects": objects,
        "edges": edges,
        "cross_domain_edges": cross_domain_edges,
        "invalid": invalid,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the knowledge index from the export contract")
    parser.add_argument("--export", default="export/latest.json", help="Input export JSON")
    parser.add_argument("--out", default="export/index.json", help="Output index JSON")
    args = parser.parse_args()

    index = build(Path(args.export))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(index, indent=2), encoding="utf-8")

    s = index["summary"]
    print(f"Wrote knowledge index ({index['source_contract']}) to {args.out}")
    print(f"  objects: {s['total']} ({s['valid']} valid / {s['invalid']} invalid, {s['error_count']} errors)")
    print(f"  edges: {len(index['edges'])}  cross-domain edges: {len(index['cross_domain_edges'])}")
    print(f"  kinds: {s['kinds']}")


if __name__ == "__main__":
    main()
