"""
HPF Knowledge Object Schema Validator

Validates knowledge objects against the atomic evidence schema defined in SCHEMA.md.
Returns typed ValidationResult instances (see models.py).

Usage:
    python tools/hpf-engine/domain/validate.py [path]          # human-readable
    python tools/hpf-engine/domain/validate.py [path] --json   # JSON output

    Default: validates all objects in tools/hpf-engine/domain/knowledge/
    Single:  python tools/hpf-engine/domain/validate.py tools/hpf-engine/domain/knowledge/browser-profiles-concept.md
"""

import json
import sys
from pathlib import Path

from models import BLOCK_TO_FIELD, BlockInfo, ValidationResult
from parser import parse


class SchemaValidator:
    REQUIRED_IDENTITY_FIELDS = ["id", "title", "tags", "entities"]

    def __init__(self, verbose=False):
        self.verbose = verbose

    def validate(self, path: Path) -> ValidationResult:
        self.errors = []
        self.warnings = []

        obj = parse(path)

        obj.identity.id
        self._check_required_identity(obj.identity)

        blocks: dict[str, BlockInfo] = {}
        has_any_block = False

        for section_name, field_name in BLOCK_TO_FIELD.items():
            items = getattr(obj, field_name)
            if section_name not in obj._section_names:
                continue
            if items:
                has_any_block = True
            blocks[section_name] = BlockInfo(count=len(items))
            self._validate_block(section_name, items)

        if not has_any_block:
            self._error("No atomic evidence blocks found. Must have at least one.")

        return ValidationResult(
            file=str(path),
            object_id=obj.identity.id,
            valid=len(self.errors) == 0,
            errors=self.errors[:],
            warnings=self.warnings[:],
            blocks=blocks,
            identity=obj.identity,
        )

    def _error(self, msg):
        self.errors.append(msg)

    def _warn(self, msg):
        self.warnings.append(msg)

    def _check_required_identity(self, identity):
        for field in self.REQUIRED_IDENTITY_FIELDS:
            val = getattr(identity, field, None)
            if not val:
                self._error(f"Missing required identity field: {field}")

    def _validate_block(self, block_name, items):
        if not items:
            self._warn(f"Block '{block_name}' has no parseable items.")
            return

        validators = {
            "Claims": self._validate_claims,
            "Relationships": self._validate_relationships,
            "Tradeoffs": self._validate_tradeoffs,
            "Failure Modes": self._validate_failure_modes,
            "Decision Factors": self._validate_decision_factors,
            "Observations": self._validate_observations,
            "Constraints": self._validate_constraints,
            "Heuristics": self._validate_heuristics,
            "Recommendations": self._validate_recommendations,
        }

        validator = validators.get(block_name)
        if validator:
            validator(items)

    def _validate_claims(self, items):
        for i, item in enumerate(items):
            if "claim" not in item:
                self._error(f"Claims[{i}]: missing 'claim' field")
            if "certainty" not in item:
                self._warn(f"Claims[{i}]: missing 'certainty' field")
            if "evidence" not in item:
                self._warn(f"Claims[{i}]: missing 'evidence' field")
            if "scope" not in item:
                self._warn(f"Claims[{i}]: missing 'scope' field")

    def _validate_relationships(self, items):
        for i, item in enumerate(items):
            if "concept" not in item:
                self._error(f"Relationships[{i}]: missing 'concept' field")
            if "relationship" not in item:
                self._error(f"Relationships[{i}]: missing 'relationship' field")
            if "description" not in item:
                self._warn(f"Relationships[{i}]: missing 'description' field")

    def _validate_tradeoffs(self, items):
        for i, item in enumerate(items):
            if "dimension" not in item:
                self._error(f"Tradeoffs[{i}]: missing 'dimension' field")
            if "options" not in item:
                self._error(f"Tradeoffs[{i}]: missing 'options' field")
            if "importance" not in item:
                self._warn(f"Tradeoffs[{i}]: missing 'importance' field")

    def _validate_failure_modes(self, items):
        for i, item in enumerate(items):
            if "name" not in item:
                self._error(f"Failure Modes[{i}]: missing 'name' field")
            if "description" not in item:
                self._error(f"Failure Modes[{i}]: missing 'description' field")
            if "likelihood" not in item:
                self._warn(f"Failure Modes[{i}]: missing 'likelihood' field")
            if "observable_evidence" not in item:
                self._warn(f"Failure Modes[{i}]: missing 'observable_evidence' field")
            if "detection" not in item:
                self._warn(f"Failure Modes[{i}]: missing 'detection' field")
            if "recovery" not in item:
                self._warn(f"Failure Modes[{i}]: missing 'recovery' field")
            if "retryable" not in item:
                self._warn(f"Failure Modes[{i}]: missing 'retryable' field")

    def _validate_decision_factors(self, items):
        for i, item in enumerate(items):
            if "factor" not in item:
                self._error(f"Decision Factors[{i}]: missing 'factor' field")
            if "question" not in item:
                self._error(f"Decision Factors[{i}]: missing 'question' field")
            if "supporting" not in item:
                self._warn(f"Decision Factors[{i}]: missing 'supporting' field")
            if "contradictory" not in item:
                self._warn(f"Decision Factors[{i}]: missing 'contradictory' field")
            if "weight" not in item:
                self._warn(f"Decision Factors[{i}]: missing 'weight' field")

    def _validate_observations(self, items):
        for i, item in enumerate(items):
            if "observation" not in item:
                self._error(f"Observations[{i}]: missing 'observation' field")
            if "confidence" not in item:
                self._warn(f"Observations[{i}]: missing 'confidence' field")
            if "source" not in item:
                self._warn(f"Observations[{i}]: missing 'source' field")

    def _validate_constraints(self, items):
        for i, item in enumerate(items):
            if "constraint" not in item:
                self._error(f"Constraints[{i}]: missing 'constraint' field")
            if "type" not in item:
                self._warn(f"Constraints[{i}]: missing 'type' field")
            if "scope" not in item:
                self._warn(f"Constraints[{i}]: missing 'scope' field")

    def _validate_heuristics(self, items):
        for i, item in enumerate(items):
            if "heuristic" not in item:
                self._error(f"Heuristics[{i}]: missing 'heuristic' field")
            if "rationale" not in item:
                self._warn(f"Heuristics[{i}]: missing 'rationale' field")
            if "evidence_level" not in item:
                self._warn(f"Heuristics[{i}]: missing 'evidence_level' field")

    def _validate_recommendations(self, items):
        for i, item in enumerate(items):
            if "recommendation" not in item:
                self._error(f"Recommendations[{i}]: missing 'recommendation' field")
            if "context" not in item:
                self._warn(f"Recommendations[{i}]: missing 'context' field")
            if "certainty" not in item:
                self._warn(f"Recommendations[{i}]: missing 'certainty' field")


def main():
    base = Path(__file__).parent / "knowledge"
    targets = []
    output_json = False

    args = [a for a in sys.argv[1:] if a != "--json"]
    if "--json" in sys.argv[1:]:
        output_json = True

    if args:
        path = Path(args[0])
        if path.is_file():
            targets.append(path)
        elif path.is_dir():
            targets.extend(sorted(path.glob("*.md")))
    else:
        targets.extend(sorted(base.glob("*.md")))

    if not targets:
        print("No knowledge objects found.")
        sys.exit(1)

    validator = SchemaValidator()
    all_results = []

    for target in targets:
        result = validator.validate(target)
        all_results.append(result)

    if output_json:
        print(json.dumps([r.to_dict() for r in all_results], indent=2))
        sys.exit(0 if all(r.valid for r in all_results) else 1)

    total_errors = sum(len(r.errors) for r in all_results)
    total_warnings = sum(len(r.warnings) for r in all_results)
    all_passed = all(r.valid for r in all_results)

    print(f"\nValidating {len(targets)} knowledge objects...\n")
    for result in all_results:
        status = "PASS" if result.valid else "FAIL"
        print(f"  [{status}] {result.object_id or '[no id]'}")
        blocks_list = list(result.blocks.keys())
        print(f"         Blocks: {blocks_list}")
        for w in result.warnings:
            print(f"         WARN: {w}")
        for e in result.errors:
            print(f"         ERROR: {e}")
        print()

    print(f"Summary: {len(targets)} objects, {total_errors} errors, {total_warnings} warnings\n")

    if not all_passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
