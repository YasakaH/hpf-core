"""Publishing adapter — Markdown report rendered from the export contract.

Contract-only consumer: reads a knowledge-export-core-v1 export and renders a
human-readable Markdown report of all valid objects. Imports nothing from the
engine, never reads the corpus or dossiers, never writes to the corpus.

This is the smallest possible consumer: if it can do useful work from the
export alone, the contract is sufficient for it.

Usage:
    python render_markdown.py --export export/latest.json --out report.md
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PRODUCER = "hpf-engine/consumers/render_markdown.py"


def render(export_path: Path) -> str:
    data = json.loads(Path(export_path).read_text(encoding="utf-8"))
    lines = [
        "# HPF Knowledge Report",
        "",
        f"_Generated {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} "
        f"from {data.get('contract')} (schema {data.get('schema_version')}). "
        f"Derived projection of the research corpus._",
        "",
        "## Contents",
        "",
    ]

    objects = [o for o in data.get("objects", []) if o.get("schema_validation") == "valid"]
    objects.sort(key=lambda o: o.get("id") or "")

    for i, o in enumerate(objects, start=1):
        lines.append(f"{i}. [{o.get('title')}](#{o.get('id')})")
    lines.append("")

    for o in objects:
        oid = o.get("id")
        lines.append(f"## {o.get('title')} (`{oid}`)")
        lines.append("")
        meta = {
            "kind": o.get("kind"),
            "domain": o.get("domain"),
            "research_cycle": o.get("research_cycle"),
            "origin": o.get("origin"),
            "authority": o.get("authority"),
            "status": o.get("status"),
        }
        lines.append("| Field | Value |")
        lines.append("|---|---|")
        for k, v in meta.items():
            lines.append(f"| {k} | {v or '—'} |")
        lines.append("")
        lines.append(f"Source: `{o.get('source')}`")
        lines.append("")

        claims = o.get("claims") or []
        if claims:
            lines.append("### Claims")
            lines.append("")
            for c in claims:
                lines.append(f"- {c.get('claim')} _(certainty: {c.get('certainty')})_")
            lines.append("")

        relationships = o.get("relationships") or []
        if relationships:
            lines.append("### Relationships")
            lines.append("")
            for r in relationships:
                lines.append(f"- **{r.get('relationship')}** → `{r.get('concept')}`")
            lines.append("")

        constraints = o.get("constraints") or []
        if constraints:
            lines.append("### Constraints")
            lines.append("")
            for c in constraints:
                lines.append(f"- {c.get('constraint')}")
            lines.append("")

        recommendations = o.get("recommendations") or []
        if recommendations:
            lines.append("### Recommendations")
            lines.append("")
            for r in recommendations:
                lines.append(f"- {r.get('recommendation')}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"Report covers {len(objects)} valid objects. "
                 "Invalid objects export metadata and errors only and are excluded here by design.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a Markdown report from the export contract")
    parser.add_argument("--export", default="export/latest.json")
    parser.add_argument("--out", default="report.md")
    args = parser.parse_args()

    report = render(Path(args.export))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"Wrote Markdown report ({len(report.splitlines())} lines) to {args.out}")


if __name__ == "__main__":
    main()
