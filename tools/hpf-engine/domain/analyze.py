"""
HPF Knowledge Object Analyzer

Consumes validation JSON (from validate.py --json) and produces structured
markdown reports. This is a separate concern from validation — the validator
determines correctness; the analyzer determines state and trends.

Usage:
    python tools/hpf-engine/domain/validate.py --json > reports/validation.json
    python tools/hpf-engine/domain/analyze.py --input reports/validation.json --out reports/
    python tools/hpf-engine/domain/analyze.py --out reports/   # runs validate internally
"""

import json
import sys
import subprocess
from pathlib import Path
from models import ALL_BLOCKS


def load_validation_data(path=None):
    """Load validation results from JSON file or stdin."""
    if path:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)
    return data


def run_validate(objects_dir: Path) -> list[dict]:
    """Run validate.py --json and capture output."""
    objects_dir = objects_dir.resolve()
    validate_script = Path(__file__).parent / "validate.py"
    result = subprocess.run(
        [sys.executable, str(validate_script), str(objects_dir), "--json"],
        capture_output=True, text=True,
    )
    if result.returncode not in (0, 1):
        result.check_returncode()
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"Failed to parse validator output: {e}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)


def analyze(data: list[dict]) -> dict[str, str]:
    """Produce report texts from validation data."""
    reports = {}

    total = len(data)
    passed_count = sum(1 for d in data if d["valid"])
    failed_count = total - passed_count
    failed_objects = [d for d in data if not d["valid"]]

    # Per-block aggregation
    block_values: dict[str, list[int]] = {}
    for d in data:
        for block_name, metrics in d.get("blocks", {}).items():
            block_values.setdefault(block_name, []).append(metrics["count"])

    for b in ALL_BLOCKS:
        if b not in block_values:
            block_values[b] = [0] * total

    # Objects missing specific blocks
    objects_missing_blocks: dict[str, list[str]] = {}
    objects_with_zero_blocks = []
    for d in data:
        present = set(d.get("blocks", {}).keys())
        missing = [b for b in ALL_BLOCKS if b not in present]
        if missing:
            objects_missing_blocks[d["object_id"]] = missing
        if len(present) == 0:
            objects_with_zero_blocks.append(d["object_id"])

    # Domain distribution
    domains: dict[str, int] = {}
    for d in data:
        domain = d.get("identity", {}).get("domain", "unknown")
        domains[domain] = domains.get(domain, 0) + 1

    # === coverage.md ===
    reports["coverage"] = _coverage_report(
        total, passed_count, failed_count, failed_objects,
        block_values, objects_missing_blocks, objects_with_zero_blocks,
        domains,
    )

    # === density.md ===
    reports["density"] = _density_report(block_values, total)

    # === gaps.md ===
    reports["gaps"] = _gaps_report(objects_missing_blocks, objects_with_zero_blocks)

    return reports


def _coverage_report(total, passed, failed, failed_objs, block_values,
                     missing_blocks, zero_blocks, domains):
    lines = []
    lines.append("# Knowledge Object Coverage\n")
    lines.append(f"- **Total objects:** {total}")
    lines.append(f"- **Passed:** {passed}")
    lines.append(f"- **Failed:** {failed}")
    lines.append(f"- **Pass rate:** {passed / total * 100:.0f}%\n" if total else "")
    if failed_objs:
        lines.append("## Failed Objects\n")
        for d in failed_objs:
            lines.append(f"- `{d['object_id']}` — {len(d['errors'])} errors")
            for e in d["errors"]:
                lines.append(f"  - {e}")
        lines.append("")

    lines.append("## Block Coverage\n")
    lines.append("| Block | Objects With | Total Possible | Coverage |")
    lines.append("|-------|-------------|----------------|----------|")
    for b in ALL_BLOCKS:
        vals = block_values.get(b, [0] * total)
        with_block = sum(1 for v in vals if v > 0)
        pct = with_block / total * 100 if total else 0
        lines.append(f"| {b} | {with_block} | {total} | {pct:.0f}% |")
    lines.append("")

    lines.append("## Domain Distribution\n")
    lines.append("| Domain | Count |")
    lines.append("|--------|-------|")
    for domain, count in sorted(domains.items()):
        lines.append(f"| {domain} | {count} |")
    lines.append("")

    if zero_blocks:
        lines.append("## Objects With No Atomic Evidence Blocks\n")
        for oid in zero_blocks:
            lines.append(f"- `{oid}`")
        lines.append("")

    return "\n".join(lines)


def _density_report(block_values, total):
    lines = []
    lines.append("# Knowledge Density\n")
    lines.append("Average items per block type across all objects:\n")
    lines.append("| Block | Avg Count | Min | Max |")
    lines.append("|-------|-----------|-----|-----|")
    for b in ALL_BLOCKS:
        vals = block_values.get(b, [0] * total)
        avg = sum(vals) / len(vals) if vals else 0
        mn = min(vals)
        mx = max(vals)
        lines.append(f"| {b} | {avg:.1f} | {mn} | {mx} |")
    lines.append("")

    lines.append("## Aggregate Totals\n")
    for b in ALL_BLOCKS:
        vals = block_values.get(b, [0] * total)
        lines.append(f"- **{b}:** {sum(vals)} total across {total} objects")
    lines.append("")

    return "\n".join(lines)


def _gaps_report(missing_blocks, zero_blocks):
    lines = []
    lines.append("# Knowledge Gaps\n")

    by_block: dict[str, list[str]] = {}
    for oid, missing in missing_blocks.items():
        for b in missing:
            by_block.setdefault(b, []).append(oid)

    lines.append("## Objects Missing Specific Blocks\n")
    lines.append("| Missing Block | Object Count | Objects |")
    lines.append("|--------------|-------------|---------|")
    for b in ALL_BLOCKS:
        objs = by_block.get(b, [])
        lines.append(f"| {b} | {len(objs)} | {', '.join(objs[:5])}{'...' if len(objs) > 5 else ''} |")
    lines.append("")

    if zero_blocks:
        lines.append("## Objects With No Blocks (Legacy Format)\n")
        for oid in zero_blocks:
            lines.append(f"- `{oid}`")
        lines.append("")

    lines.append("## Recommendations\n")
    lines.append(f"1. Refactor {len(zero_blocks)} legacy objects ({', '.join(zero_blocks[:3])}...) to atomic evidence schema")
    lines.append(f"2. Add missing blocks: prioritize Claims, Relationships, and Decision Factors")
    lines.append(f"3. Review objects with lowest block counts for completeness")

    return "\n".join(lines)


def write_reports(reports: dict[str, str], out_dir: Path):
    """Write report texts to files."""
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = {}
    for name, text in reports.items():
        path = out_dir / f"{name}.md"
        path.write_text(text, encoding="utf-8")
        paths[name] = str(path)
    return paths


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Analyze HPF knowledge objects")
    parser.add_argument("--input", help="Path to validation JSON file (default: stdin)")
    parser.add_argument("--out", default="reports", help="Output directory for reports")
    parser.add_argument("--objects-dir", help="Run validate internally on this directory")
    args = parser.parse_args()

    if args.objects_dir:
        data = run_validate(Path(args.objects_dir))
    elif args.input:
        data = load_validation_data(args.input)
    else:
        data = load_validation_data()

    reports = analyze(data)
    paths = write_reports(reports, Path(args.out))

    print(f"Wrote {len(paths)} reports to {args.out}/")
    for name, path in paths.items():
        print(f"  {name}: {path}")


if __name__ == "__main__":
    main()
