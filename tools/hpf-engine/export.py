"""HPF Knowledge Export — core contract (knowledge-export-core-v1), provenance-preserving.

Consumers (publishing, marketing, documentation, website, sales, API) depend
ONLY on this contract — never on dossiers, programme state, or engine internals.
Consumers are READ-ONLY: no downstream system ever mutates the corpus or any
research artifact. Flow is one-way: Corpus -> Export -> Index -> Consumers.

Two concerns are kept orthogonal per record:
  - Where did this knowledge come from?  -> origin
  - What evidential status does it hold?  -> authority + status
Never conflated with pipeline integrity (schema_validation), which records
whether the object passed the corpus schema validator.

Invariants (recorded in research/PROGRAMME_STATE.md, "Knowledge Export Contract";
experimental implementation 2026-08-03; architectural status pending R1):
  1. No new claims — exports reformat validated corpus content only; every
     output record is a derived projection of a parsed knowledge object.
  2. Every exported record carries provenance: source file, object id, kind,
     domain, research cycle (where recorded in the object).
  3. Pipeline integrity travels with every record (schema_validation:
     valid | invalid). Invalid records are metadata-only: they carry their
     errors and NO semantic content, so downstream claims can never outpace
     evidence. Consumers filter on schema_validation == "valid" before use.
  4. The export is regenerable from the corpus — the corpus remains the
     single source of truth. This file is never hand-edited.
  5. Stable core exported here: objects, relationships, claims, constraints,
     recommendations. The provisional extension namespace (methodology terms,
     motif candidates, decomposition metrics, authority layer) is NOT exported
     until admitted by the vocabulary admission/removal rules.
  6. No downstream system may mutate the corpus or research artifacts.
     HPF never writes into the export; consumers never write into HPF.

The name is knowledge-export-CORE-v1 deliberately: it omits the methodology
namespace, motifs, discoveries, and the full authority layer, which are
planned but not yet admitted.

Usage:
    python export.py --out export/latest.json
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

ENGINE_ROOT = Path(__file__).parent
sys.path.insert(0, str(ENGINE_ROOT))
sys.path.insert(0, str(ENGINE_ROOT / "domain"))

from models import BLOCK_TO_FIELD  # noqa: E402
from parser import parse  # noqa: E402
from validate import SchemaValidator  # noqa: E402

SCHEMA_VERSION = "1.2"
CONTRACT = "knowledge-export-core-v1"
PRODUCER = "hpf-engine/export.py"
PRODUCER_VERSION = "0.3.0"
SCHEMA_VALIDATION_VALUES = ["valid", "invalid"]
AXES = {
    "origin": ["hpf", "nist", "cert", "rfc", "academic", "internal"],
    "authority": ["hpf_experiment", "external_curated", "imported", "unverified"],
    "status": ["observed", "replicated", "provisional", "retired"],
}
STABLE_CORE_BLOCKS = [
    "claims",
    "relationships",
    "constraints",
    "recommendations",
]


@dataclass
class ExportedObject:
    """One corpus object as exposed by the contract (stable core)."""

    id: str
    title: str
    kind: str
    domain: Optional[str]
    research_cycle: Optional[str]
    source: str
    origin: str
    authority: str
    status: str
    schema_validation: str
    errors: list[str] = field(default_factory=list)
    blocks: dict = field(default_factory=dict)
    claims: list[dict] = field(default_factory=list)
    relationships: list[dict] = field(default_factory=list)
    constraints: list[dict] = field(default_factory=list)
    recommendations: list[dict] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "kind": self.kind,
            "domain": self.domain,
            "research_cycle": self.research_cycle,
            "source": self.source,
            "origin": self.origin,
            "authority": self.authority,
            "status": self.status,
            "schema_validation": self.schema_validation,
            "errors": self.errors,
            "blocks": self.blocks,
            "claims": self.claims,
            "relationships": self.relationships,
            "constraints": self.constraints,
            "recommendations": self.recommendations,
        }


@dataclass
class KnowledgeExport:
    schema_version: str = SCHEMA_VERSION
    contract: str = CONTRACT
    producer: str = PRODUCER
    producer_version: str = PRODUCER_VERSION
    generated_at: str = ""
    corpus: dict = field(default_factory=dict)
    axes: dict = field(default_factory=lambda: {k: list(v) for k, v in AXES.items()})
    schema_validation_values: list[str] = field(
        default_factory=lambda: list(SCHEMA_VALIDATION_VALUES)
    )
    objects: list[ExportedObject] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "schema_version": self.schema_version,
            "contract": self.contract,
            "producer": self.producer,
            "producer_version": self.producer_version,
            "generated_at": self.generated_at
            or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "corpus": self.corpus,
            "axes": self.axes,
            "schema_validation_values": self.schema_validation_values,
            "objects": [o.to_dict() for o in self.objects],
        }

    def to_json(self, path: Optional[Path | str] = None, indent: int = 2) -> Optional[str]:
        dumped = json.dumps(self.to_dict(), indent=indent)
        if path:
            p = Path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(dumped, encoding="utf-8")
            return None
        return dumped


def _block_counts(obj) -> dict:
    counts = {}
    for section_name, field_name in BLOCK_TO_FIELD.items():
        counts[section_name] = len(getattr(obj, field_name, []) or [])
    return counts


def _provenance_cycle(obj) -> Optional[str]:
    cycle = None
    try:
        cycle = obj.identity.research_cycle
    except AttributeError:
        cycle = None
    return cycle


def produce(knowledge_dir: Path, validator: SchemaValidator) -> KnowledgeExport:
    files = sorted(Path(knowledge_dir).glob("*.md"))
    objects = []
    parsed = valid = invalid = error_count = 0
    cycles = set()

    for f in files:
        try:
            obj = parse(f)
        except Exception:
            continue
        if obj is None:
            continue
        parsed += 1
        try:
            oid = obj.identity.id
        except AttributeError:
            oid = None
        if oid is None:
            continue
        res = validator.validate(f)
        schema_validation = "valid" if res.valid else "invalid"
        if res.valid:
            valid += 1
        else:
            invalid += 1
            error_count += len(res.errors)
        cycle = _provenance_cycle(obj)
        if cycle:
            cycles.add(cycle)
        blocks = _block_counts(obj)
        content = {}
        if res.valid:
            for block in STABLE_CORE_BLOCKS:
                content[block] = getattr(obj, block, []) or []
        objects.append(
            ExportedObject(
                id=oid,
                title=obj.identity.title or oid,
                kind=obj.identity.type or None,
                domain=obj.identity.domain,
                research_cycle=cycle,
                source=str(Path(f).resolve().relative_to(ENGINE_ROOT.resolve())).replace("\\", "/"),
                origin="hpf",
                authority="hpf_experiment",
                status="observed",
                schema_validation=schema_validation,
                errors=res.errors if not res.valid else [],
                blocks=blocks,
                claims=content.get("claims", []),
                relationships=content.get("relationships", []),
                constraints=content.get("constraints", []),
                recommendations=content.get("recommendations", []),
            )
        )

    export = KnowledgeExport()
    export.corpus = {
        "total_files": len(files),
        "parsed": parsed,
        "valid": valid,
        "invalid": invalid,
        "error_count": error_count,
        "cycle_count": len(cycles),
        "cycles": sorted(cycles) if cycles else [],
    }
    export.objects = objects
    return export


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Produce the Knowledge Export Contract from the HPF corpus"
    )
    parser.add_argument(
        "--out",
        default=str(Path(__file__).parent / "export" / "latest.json"),
        help="Output path for KnowledgeExport JSON",
    )
    parser.add_argument(
        "--knowledge-dir",
        default=str(Path(__file__).parent / "domain" / "knowledge"),
        help="Corpus directory",
    )
    args = parser.parse_args()

    export = produce(Path(args.knowledge_dir), SchemaValidator())
    export.to_json(args.out)
    c = export.corpus
    print(f"Wrote KnowledgeExport v{export.schema_version} (contract {export.contract}) to {args.out}")
    print(f"  corpus: {c['total_files']} files, {c['parsed']} parsed")
    print(f"  valid: {c['valid']}   invalid: {c['invalid']} (errors: {c['error_count']})")
    print(f"  cycles recorded: {c['cycle_count']}")


if __name__ == "__main__":
    main()
