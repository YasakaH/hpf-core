"""
HPF domain model — typed dataclasses for validation and analysis.

These types are the single source of truth for what the validator produces,
what the analyzer consumes, and what downstream tooling (CI, benchmark,
dashboard) depends on.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BlockInfo:
    count: int


@dataclass
class Identity:
    id: Optional[str] = None
    type: Optional[str] = None
    title: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    entities: list[str] = field(default_factory=list)
    concepts: list[str] = field(default_factory=list)
    domain: Optional[str] = None
    version: Optional[str] = None
    research_cycle: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title,
            "tags": self.tags,
            "entities": self.entities,
            "concepts": self.concepts,
            "domain": self.domain,
            "version": self.version,
            "research_cycle": self.research_cycle,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Identity":
        return cls(
            id=d.get("id"),
            type=d.get("type"),
            title=d.get("title"),
            tags=d.get("tags", []),
            entities=d.get("entities", []),
            concepts=d.get("concepts", []),
            domain=d.get("domain"),
            version=d.get("version"),
            research_cycle=d.get("research_cycle"),
        )


@dataclass
class ValidationResult:
    file: str
    object_id: Optional[str]
    valid: bool
    errors: list[str]
    warnings: list[str]
    blocks: dict[str, BlockInfo]
    identity: Identity

    def to_dict(self) -> dict:
        return {
            "file": self.file,
            "object_id": self.object_id,
            "valid": self.valid,
            "errors": self.errors,
            "warnings": self.warnings,
            "blocks": {k: {"count": v.count} for k, v in self.blocks.items()},
            "identity": self.identity.to_dict(),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "ValidationResult":
        blocks = {}
        for k, v in d.get("blocks", {}).items():
            blocks[k] = BlockInfo(count=v["count"])
        return cls(
            file=d["file"],
            object_id=d.get("object_id"),
            valid=d["valid"],
            errors=d.get("errors", []),
            warnings=d.get("warnings", []),
            blocks=blocks,
            identity=Identity.from_dict(d.get("identity", {})),
        )


ALL_BLOCKS = [
    "Claims", "Relationships", "Tradeoffs", "Failure Modes",
    "Decision Factors", "Observations", "Constraints", "Heuristics",
    "Recommendations",
]

# Maps Markdown section names to KnowledgeObject field names
BLOCK_TO_FIELD = {
    "Claims": "claims",
    "Relationships": "relationships",
    "Tradeoffs": "tradeoffs",
    "Failure Modes": "failure_modes",
    "Decision Factors": "decision_factors",
    "Observations": "observations",
    "Constraints": "constraints",
    "Heuristics": "heuristics",
    "Recommendations": "recommendations",
}


@dataclass
class KnowledgeObject:
    """A parsed HPF knowledge object — the central type of the system.

    Every downstream consumer (validator, reasoner, renderer, benchmark)
    operates on this type. Markdown is one way to author it.
    """
    identity: Identity
    claims: list[dict] = field(default_factory=list)
    relationships: list[dict] = field(default_factory=list)
    tradeoffs: list[dict] = field(default_factory=list)
    failure_modes: list[dict] = field(default_factory=list)
    decision_factors: list[dict] = field(default_factory=list)
    observations: list[dict] = field(default_factory=list)
    constraints: list[dict] = field(default_factory=list)
    heuristics: list[dict] = field(default_factory=list)
    recommendations: list[dict] = field(default_factory=list)
    _section_names: set[str] = field(default_factory=set)

    def to_dict(self) -> dict:
        return {
            "identity": self.identity.to_dict(),
            "claims": self.claims,
            "relationships": self.relationships,
            "tradeoffs": self.tradeoffs,
            "failure_modes": self.failure_modes,
            "decision_factors": self.decision_factors,
            "observations": self.observations,
            "constraints": self.constraints,
            "heuristics": self.heuristics,
            "recommendations": self.recommendations,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "KnowledgeObject":
        return cls(
            identity=Identity.from_dict(d.get("identity", {})),
            claims=d.get("claims", []),
            relationships=d.get("relationships", []),
            tradeoffs=d.get("tradeoffs", []),
            failure_modes=d.get("failure_modes", []),
            decision_factors=d.get("decision_factors", []),
            observations=d.get("observations", []),
            constraints=d.get("constraints", []),
            heuristics=d.get("heuristics", []),
            recommendations=d.get("recommendations", []),
        )

    @property
    def block_counts(self) -> dict[str, int]:
        """Returns {section_name: count} for each block with items."""
        return {
            name: len(getattr(self, field_name))
            for name, field_name in BLOCK_TO_FIELD.items()
        }

    @property
    def object_id(self) -> Optional[str]:
        return self.identity.id
