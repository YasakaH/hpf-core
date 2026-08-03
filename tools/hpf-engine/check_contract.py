"""Conformance check for knowledge-export-core-v1 (schema 1.2).

Read-only: asserts every record in a produced export conforms to the frozen
contract specification (EXPORT_CONTRACT.md). Never writes to the export.

Usage:
    python check_contract.py [path-to-export.json]
"""

import json
import sys
from pathlib import Path

CONTRACT = "knowledge-export-core-v1"
SCHEMA_VERSION = "1.2"
AXES = {
    "origin": ["hpf", "nist", "cert", "rfc", "academic", "internal"],
    "authority": ["hpf_experiment", "external_curated", "imported", "unverified"],
    "status": ["observed", "replicated", "provisional", "retired"],
}
SCHEMA_VALIDATION_VALUES = ["valid", "invalid"]
CONTENT_BLOCKS = ["claims", "relationships", "constraints", "recommendations"]


def main() -> int:
    path = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path(__file__).parent / "export" / "latest.json"
    )
    d = json.loads(path.read_text(encoding="utf-8"))
    failures: list[str] = []

    def check(cond: bool, msg: str) -> None:
        if not cond:
            failures.append(msg)

    check(d.get("contract") == CONTRACT, f"contract is {d.get('contract')!r}, expected {CONTRACT!r}")
    check(d.get("schema_version") == SCHEMA_VERSION, f"schema_version is {d.get('schema_version')!r}, expected {SCHEMA_VERSION!r}")
    check(d.get("axes") == AXES, f"axes mismatch: {d.get('axes')!r}")
    check(d.get("schema_validation_values") == SCHEMA_VALIDATION_VALUES, "schema_validation_values mismatch")

    objs = d.get("objects", [])
    corpus = d.get("corpus", {})
    check(corpus.get("total_files") == len(objs), f"corpus.total_files {corpus.get('total_files')} != objects {len(objs)}")
    check(corpus.get("parsed") == len(objs), f"corpus.parsed {corpus.get('parsed')} != objects {len(objs)}")

    counts = {"valid": 0, "invalid": 0}
    origins: dict[str, int] = {}
    error_count = 0
    for o in objs:
        oid = o.get("id")
        for axis, allowed in AXES.items():
            check(o.get(axis) in allowed, f"{oid}: {axis}={o.get(axis)!r} not in {allowed}")
        sv = o.get("schema_validation")
        check(sv in SCHEMA_VALIDATION_VALUES, f"{oid}: schema_validation={sv!r} not in {SCHEMA_VALIDATION_VALUES}")
        counts[sv] += 1
        origins[o.get("origin")] = origins.get(o.get("origin"), 0) + 1
        check(bool(oid), f"missing id for {o.get('source')!r}")
        check(bool(o.get("source")), f"missing source for {oid!r}")
        if sv == "valid":
            check(not o.get("errors"), f"{oid}: valid record carries errors {o.get('errors')!r}")
        else:
            check(bool(o.get("errors")), f"{oid}: invalid record carries no errors")
            error_count += len(o.get("errors") or [])
            for block in CONTENT_BLOCKS:
                check(not o.get(block), f"{oid}: invalid record exports {block} content")

    check(counts["valid"] == corpus.get("valid"), f"valid count {counts['valid']} != corpus.valid {corpus.get('valid')}")
    check(counts["invalid"] == corpus.get("invalid"), f"invalid count {counts['invalid']} != corpus.invalid {corpus.get('invalid')}")
    check(error_count == corpus.get("error_count"), f"error_count {error_count} != corpus.error_count {corpus.get('error_count')}")
    check(sum(origins.values()) == len(objs), f"origin missing on {len(objs) - sum(origins.values())} object(s)")

    if failures:
        print(f"FAIL: {len(failures)} violation(s) in {path}")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"PASS: {len(objs)} objects — {counts['valid']} valid / {counts['invalid']} invalid ({error_count} errors)")
    print(f"  origins: {origins}")
    print(f"  contract {d['contract']} schema {d['schema_version']} conforms to the frozen spec")
    return 0


if __name__ == "__main__":
    sys.exit(main())
