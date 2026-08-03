"""
KnowledgeOS Pipeline — typed handoff between HPF (knowledge generation)
and Publishing (knowledge commercialization).

HPF produces KnowledgePackages by scanning canonical concepts, knowledge
objects, and derived insights. Publishing consumes KnowledgePackages to
plan editorial content.

Usage:
    # HPF side — produce a handoff
    python pipeline.py produce --out handoff/latest.json

    # Publishing side — consume (from JSON)
    pkg = KnowledgePackage.from_json("handoff/latest.json")

    # Feedback loop — HPF processes publishing signals
    python pipeline.py feedback --in feedback/inbox/ --out feedback/processed/
"""

import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


# ──────────────────────────────────────────────
# Types — shared contract between HPF and Publishing
# ──────────────────────────────────────────────


@dataclass
class Alias:
    text: str
    context: Optional[str] = None

    def to_dict(self) -> dict:
        return {"text": self.text, "context": self.context}

    @classmethod
    def from_dict(cls, d: dict) -> "Alias":
        return cls(text=d["text"], context=d.get("context"))


@dataclass
class CanonicalProblem:
    """A known automation problem — extracted from HPF knowledge objects.

    Every Failure Mode in a validated knowledge object produces a
    CanonicalProblem entry. These are the atomic units of the problem
    ontology that Publishing turns into problem pages, troubleshooting
    guides, and support content.
    """
    id: str
    title: str
    error_patterns: list[str]
    severity: str  # common | uncommon | rare
    primary_concept: str  # HPF concept ID this problem belongs to
    root_cause: str
    aliases: list[Alias] = field(default_factory=list)
    related_concepts: list[str] = field(default_factory=list)
    recovery_guide: Optional[str] = None
    recommendation: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "error_patterns": self.error_patterns,
            "severity": self.severity,
            "primary_concept": self.primary_concept,
            "root_cause": self.root_cause,
            "aliases": [a.to_dict() for a in self.aliases],
            "related_concepts": self.related_concepts,
            "recovery_guide": self.recovery_guide,
            "recommendation": self.recommendation,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "CanonicalProblem":
        return cls(
            id=d["id"],
            title=d["title"],
            error_patterns=d["error_patterns"],
            severity=d["severity"],
            primary_concept=d["primary_concept"],
            root_cause=d["root_cause"],
            aliases=[Alias.from_dict(a) for a in d.get("aliases", [])],
            related_concepts=d.get("related_concepts", []),
            recovery_guide=d.get("recovery_guide"),
            recommendation=d.get("recommendation"),
        )


@dataclass
class ArticleBrief:
    """An editorial brief — HPF identifies what to write, Publishing decides
    when, in what form, and in what order.

    Publishing never invents topics; it receives briefs.
    """
    id: str
    title: str
    audience: str  # beginner | intermediate | advanced
    primary_concept: str
    secondary_concepts: list[str] = field(default_factory=list)
    pain_points: list[str] = field(default_factory=list)
    goal: str = ""
    target_length: int = 1500
    cta: Optional[str] = None
    status: str = "draft"  # draft | approved | published | archived
    created: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "audience": self.audience,
            "primary_concept": self.primary_concept,
            "secondary_concepts": self.secondary_concepts,
            "pain_points": self.pain_points,
            "goal": self.goal,
            "target_length": self.target_length,
            "cta": self.cta,
            "status": self.status,
            "created": self.created or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "ArticleBrief":
        return cls(
            id=d["id"],
            title=d["title"],
            audience=d["audience"],
            primary_concept=d["primary_concept"],
            secondary_concepts=d.get("secondary_concepts", []),
            pain_points=d.get("pain_points", []),
            goal=d.get("goal", ""),
            target_length=d.get("target_length", 1500),
            cta=d.get("cta"),
            status=d.get("status", "draft"),
            created=d.get("created", ""),
        )


@dataclass
class KnowledgePackage:
    """The typed handoff contract between HPF and Publishing.

    HPF produces KnowledgePackages. Publishing consumes them.
    Serialized as JSON for thread-crossing.

    Schema versioning ensures independent evolution:
      schema_version  — contract version (incremented on breaking changes)
      producer        — name of the producing system
      producer_version — version of the producer
      compatibility   — semver range that Publishing must satisfy
      generated_at    — timestamp of production
    """
    schema_version: str = "1.0"
    producer: str = "hpf-engine"
    producer_version: str = "0.1.0"
    compatibility: str = ">=0.4"
    generated_at: str = ""
    concepts: list[dict] = field(default_factory=list)
    problems: list[CanonicalProblem] = field(default_factory=list)
    briefs: list[ArticleBrief] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "schema_version": self.schema_version,
            "producer": self.producer,
            "producer_version": self.producer_version,
            "compatibility": self.compatibility,
            "generated_at": self.generated_at or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "concepts": self.concepts,
            "problems": [p.to_dict() for p in self.problems],
            "briefs": [b.to_dict() for b in self.briefs],
            "metadata": self.metadata,
        }

    def to_json(self, path: Optional[Path | str] = None, indent: int = 2) -> Optional[str]:
        dumped = json.dumps(self.to_dict(), indent=indent)
        if path:
            p = Path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(dumped, encoding="utf-8")
            return None
        return dumped

    @classmethod
    def from_dict(cls, d: dict) -> "KnowledgePackage":
        return cls(
            schema_version=d.get("schema_version", d.get("version", "0.1")),
            producer=d.get("producer", "unknown"),
            producer_version=d.get("producer_version", "0.0.0"),
            compatibility=d.get("compatibility", ">=0.1"),
            generated_at=d.get("generated_at", d.get("created", "")),
            concepts=d.get("concepts", []),
            problems=[CanonicalProblem.from_dict(p) for p in d.get("problems", [])],
            briefs=[ArticleBrief.from_dict(b) for b in d.get("briefs", [])],
            metadata=d.get("metadata", {}),
        )

    @classmethod
    def from_json(cls, path: Path | str) -> "KnowledgePackage":
        p = Path(path)
        return cls.from_dict(json.loads(p.read_text(encoding="utf-8")))


@dataclass
class FeedbackRecord:
    """A signal from Publishing back to HPF.

    Publishing continuously discovers new pain points, concept gaps,
    alias variants, and content opportunities. FeedbackRecords capture
    these signals for HPF to process in the next research cycle.
    """
    id: str
    source: str
    signal_type: str
    payload: dict
    received: str = ""
    processed: bool = False
    notes: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "source": self.source,
            "signal_type": self.signal_type,
            "payload": self.payload,
            "received": self.received or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "processed": self.processed,
            "notes": self.notes,
        }

    def to_json(self, path: Optional[Path | str] = None) -> Optional[str]:
        dumped = json.dumps(self.to_dict(), indent=2)
        if path:
            p = Path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(dumped, encoding="utf-8")
            return None
        return dumped

    @classmethod
    def from_dict(cls, d: dict) -> "FeedbackRecord":
        return cls(
            id=d["id"],
            source=d["source"],
            signal_type=d["signal_type"],
            payload=d["payload"],
            received=d.get("received", ""),
            processed=d.get("processed", False),
            notes=d.get("notes"),
        )

    @classmethod
    def from_json(cls, path: Path | str) -> "FeedbackRecord":
        p = Path(path)
        return cls.from_dict(json.loads(p.read_text(encoding="utf-8")))


# ──────────────────────────────────────────────
# Known mappings (curated, not scraped)
# ──────────────────────────────────────────────

# Problems known to exist as failure modes in knowledge objects
# These seed the problem ontology; new problems arrive via FeedbackRecords.
KNOWN_PROBLEMS: list[CanonicalProblem] = [
    CanonicalProblem(
        id="profile-locked",
        title="Chrome profile is already in use",
        error_patterns=[
            "profile is already in use",
            "SingletonLock",
            "cannot create profile",
            "profile locked",
            "user data directory is already in use",
            "profile directory in use",
        ],
        severity="common",
        primary_concept="browser-profile",
        root_cause="Two browser instances accessing the same user_data_dir "
                    "simultaneously; Chrome's filesystem lock prevents concurrent access.",
        aliases=[
            Alias(text="SingletonLock"),
            Alias(text="user_data_dir busy"),
            Alias(text="profile directory in use"),
        ],
        related_concepts=["browser-session-lifecycle", "memory-pressure"],
        recovery_guide="Kill existing browser process, wait for lock file release, "
                       "or use a different/unique profile path per session.",
        recommendation="Always use unique, ephemeral profiles per session in production.",
    ),
    CanonicalProblem(
        id="profile-corruption",
        title="Browser profile SQLite corruption",
        error_patterns=[
            "SQLite error",
            "database disk image is malformed",
            "unable to open database file",
            "profile corruption",
            "cookies database corruption",
        ],
        severity="uncommon",
        primary_concept="browser-profile",
        root_cause="Unexpected termination (SIGKILL, power loss) during SQLite write "
                    "operations on Cookies, History, or Login Data databases.",
        aliases=[
            Alias(text="SQLite malformed"),
            Alias(text="database disk image is malformed"),
        ],
        related_concepts=["browser-session-lifecycle", "navigation-lifecycle"],
        recovery_guide="Delete or restore the corrupted profile directory from backup. "
                       "Browser recreates it on next launch.",
        recommendation="Always use graceful shutdown (SIGTERM) and monitor process exit codes.",
    ),
]

# Briefs derived from known concepts with clear pain points
KNOWN_BRIEFS: list[ArticleBrief] = [
    ArticleBrief(
        id="why-browser-profiles-break",
        title="Why Browser Profiles Break (and How to Fix It)",
        audience="intermediate",
        primary_concept="browser-profile",
        secondary_concepts=["browser-session-lifecycle", "memory-pressure"],
        pain_points=["profile-locked", "profile-corruption"],
        goal="Explain profile mechanics, common failure modes, and recovery strategies.",
        target_length=1800,
        cta="cookbook-profile-recipes",
    ),
    ArticleBrief(
        id="automation-detection-signals",
        title="What Automation Detection Looks Like in 2026",
        audience="intermediate",
        primary_concept="automation-detection-surface",
        secondary_concepts=["browser-fingerprint", "anti-detection-strategy"],
        pain_points=["navigator.webdriver flag", "cdp detection", "permission query signals"],
        goal="Catalog current detection signals and their mitigation trade-offs.",
        target_length=2200,
        cta="cookbook-browser-automation",
    ),
    ArticleBrief(
        id="fresh-vs-persistent-profiles",
        title="Fresh vs Persistent Browser Profiles: When to Use Which",
        audience="beginner",
        primary_concept="browser-profile",
        secondary_concepts=["automation-detection-surface", "browser-session-lifecycle"],
        pain_points=["profile-locked", "cross-session tracking"],
        goal="Help readers choose the right profile strategy for their use case.",
        target_length=1500,
        cta="cookbook-profile-recipes",
    ),
    ArticleBrief(
        id="browser-fingerprint-primer",
        title="How Browser Fingerprinting Works",
        audience="beginner",
        primary_concept="browser-fingerprint",
        secondary_concepts=["automation-detection-surface", "anti-detection-strategy"],
        pain_points=["canvas fingerprint", "WebGL fingerprint", "audio fingerprint"],
        goal="Explain fingerprinting mechanisms and their role in automation detection.",
        target_length=2000,
        cta="cookbook-browser-automation",
    ),
    ArticleBrief(
        id="anti-detection-strategy-guide",
        title="Anti-Detection Strategy: What Works, What Doesn't",
        audience="advanced",
        primary_concept="anti-detection-strategy",
        secondary_concepts=["automation-detection-surface", "browser-fingerprint", "browser-profile"],
        pain_points=["navigator.webdriver", "cdp detection", "permission queries", "canvas fingerprint"],
        goal="Systematic approach to reducing automation detection risk.",
        target_length=3000,
        cta="cookbook-advanced-techniques",
    ),
]


# ──────────────────────────────────────────────
# HPF-side functions
# ──────────────────────────────────────────────


def get_concept_refs(concepts_dir: Path) -> list[dict]:
    """Scan canonical concepts directory for concept metadata."""
    if not concepts_dir.is_dir():
        return []

    refs = []
    for f in sorted(concepts_dir.glob("*.md")):
        if f.name == "README.md":
            continue
        content = f.read_text(encoding="utf-8")
        lines = content.splitlines()

        title = f.stem.replace("-", " ").title()
        for line in lines:
            m = re.match(r"^# (.+)", line)
            if m:
                title = m.group(1).strip()
                break

        domain = "unknown"
        for line in lines:
            m = re.match(r"\*\*Domain\*\*:\s*(.+)", line)
            if m:
                domain = m.group(1).strip()
                break

        refs.append({"id": f.stem, "title": title, "domain": domain})

    return refs


def produce(
    concepts_dir: Optional[Path] = None,
    out_path: Optional[Path] = None,
    version: str = "0.1.0",
    schema_version: str = "1.0",
) -> KnowledgePackage:
    """Produce a KnowledgePackage from canonical concepts and known problem/brief mappings.

    In a full implementation this would also scan and validate all knowledge
    objects, extract problems from Failure Mode blocks, and generate briefs
    from coverage gaps. The current version starts with curated seed data and
    concept scanning — the automated extraction comes as knowledge objects
    are validated at scale.
    """
    concepts = get_concept_refs(concepts_dir) if concepts_dir else []

    pkg = KnowledgePackage(
        schema_version=schema_version,
        producer="hpf-engine",
        producer_version=version,
        compatibility=">=0.4",
        generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        concepts=concepts,
        problems=list(KNOWN_PROBLEMS),
        briefs=list(KNOWN_BRIEFS),
        metadata={
            "generator": "hpf-engine/pipeline.py",
            "problem_count": len(KNOWN_PROBLEMS),
            "brief_count": len(KNOWN_BRIEFS),
            "concept_count": len(concepts),
        },
    )

    if out_path:
        pkg.to_json(out_path)
        print(f"Wrote KnowledgePackage v{version} (schema {schema_version}) to {out_path}")
        print(f"  concepts: {len(concepts)}")
        print(f"  problems: {len(KNOWN_PROBLEMS)}")
        print(f"  briefs:   {len(KNOWN_BRIEFS)}")

    return pkg


def intake_feedback(inbox: Path, processed_dir: Optional[Path] = None) -> list[FeedbackRecord]:
    """Scan a feedback inbox for unprocessed FeedbackRecords.

    HPF processes feedback signals from Publishing to discover new
    pain points, concept gaps, and content opportunities for the
    next research cycle.

    Records are flat *.json files with domain/source metadata inside.
    """
    if not inbox.is_dir():
        print(f"Feedback inbox not found: {inbox}")
        return []

    records = []
    for f in sorted(inbox.glob("*.json")):
        try:
            record = FeedbackRecord.from_json(f)
            if not record.processed:
                records.append(record)
                if processed_dir:
                    processed_dir.mkdir(parents=True, exist_ok=True)
                    dest = processed_dir / f.name
                    record.processed = True
                    record.to_json(dest)
                    f.unlink()
                    domain = record.payload.get("domain") or record.to_dict().get("domain", "unknown")
                    print(f"  Processed: {f.name} ({domain}/{record.signal_type})")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"  Skipped {f.name}: {e}")

    return records


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "produce":
        import argparse
        parser = argparse.ArgumentParser(description="Produce a KnowledgePackage handoff")
        parser.add_argument("--concepts", help="Path to canonical concepts directory")
        parser.add_argument("--out", default="handoff/latest.json", help="Output path for KnowledgePackage JSON")
        parser.add_argument("--version", default="0.1.0", help="Producer version")
        parser.add_argument("--schema-version", default="1.0", help="Schema contract version")
        args = parser.parse_args(sys.argv[2:])

        if args.concepts:
            concepts_dir = Path(args.concepts)
        else:
            engine_dir = Path(__file__).resolve().parent
            for up in [engine_dir, engine_dir.parent, engine_dir.parent.parent,
                       engine_dir.parent.parent.parent, engine_dir.parent.parent.parent.parent]:
                candidate = up / "canon" / "concepts"
                if candidate.is_dir():
                    concepts_dir = candidate
                    break
            else:
                print("Warning: canon/concepts/ not found. Specify --concepts.")
                concepts_dir = None

        produce(
            concepts_dir=concepts_dir,
            out_path=Path(args.out),
            version=args.version,
            schema_version=args.schema_version,
        )

    elif command == "feedback":
        import argparse
        parser = argparse.ArgumentParser(description="Process publishing feedback")
        parser.add_argument("--inbox", default="feedback/inbox", help="Feedback inbox directory")
        parser.add_argument("--out", default="feedback/processed", help="Processed feedback directory")
        args = parser.parse_args(sys.argv[2:])

        records = intake_feedback(
            inbox=Path(args.inbox),
            processed_dir=Path(args.out),
        )
        print(f"Processed {len(records)} feedback records.")

    else:
        print(f"Unknown command: {command}")
        print("Available: produce, feedback")
        sys.exit(1)


if __name__ == "__main__":
    main()
