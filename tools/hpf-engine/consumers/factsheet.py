"""Marketing adapter — compact fact sheet rendered from the export contract.

Contract-only consumer: reads a knowledge-export-core-v1 export and renders a
one-line-per-object fact sheet. Imports nothing from the engine, never reads
the corpus or dossiers, never writes to the corpus.

Usage:
    python factsheet.py --export export/latest.json --out factsheet.md
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCER = "hpf-engine/consumers/factsheet.py"


def render(export_path: Path) -> str:
    data = json.loads(Path(export_path).read_text(encoding="utf-8"))
    objects = sorted(data.get("objects", []), key=lambda o: o.get("id") or "")

    lines = [
        "# HPF Knowledge Fact Sheet",
        "",
        f"_Generated {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} "
        f"from {data.get('contract')} (schema {data.get('schema_version')})._",
        "",
        "| id | title | kind | domain | cycle | origin | authority | status | valid |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for o in objects:
        if o.get("schema_validation") != "valid":
            continue
        lines.append(
            "| {id} | {title} | {kind} | {domain} | {cycle} | {origin} | {authority} | {status} | ✓ |".format(
                id=o.get("id") or "",
                title=(o.get("title") or "").replace("|", "/"),
                kind=o.get("kind") or "",
                domain=o.get("domain") or "",
                cycle=o.get("research_cycle") or "",
                origin=o.get("origin") or "",
                authority=o.get("authority") or "",
                status=o.get("status") or "",
            )
        )
    lines.append("")
    lines.append(f"{sum(1 for o in objects if o.get('schema_validation') == 'valid')} valid objects. "
                 "Derived from the export contract only.")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a fact sheet from the export contract")
    parser.add_argument("--export", default="export/latest.json")
    parser.add_argument("--out", default="factsheet.md")
    args = parser.parse_args()

    sheet = render(Path(args.export))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(sheet, encoding="utf-8")
    print(f"Wrote fact sheet ({len(sheet.splitlines())} lines) to {args.out}")


if __name__ == "__main__":
    main()
