# Data Integrity

## Identity
- id: data-integrity
- type: concept
- title: Data Integrity
- tags: [databases, integrity, constraints, referential integrity, consistency, guarantees]
- entities: [data integrity, integrity rule, referential integrity, entity integrity, constraint, data quality]
- concepts: [relational-model, schema-design, normalization, transactions, schema-migration, data-governance]

## Claims
- claim: "Data integrity is the guarantee that data conforms to its defining rules — integrity rules are invariants the data must satisfy at all times."
  certainty: high
  evidence: Database theory and practice
  scope: cross-domain
- claim: "Integrity is enforced by the schema, not the application — schema-enforced rules are verifiable and universal; application-enforced rules are optional."
  certainty: high
  evidence: Database practice, data-quality analyses
  scope: cross-domain
- claim: "Entity integrity (keys exist and are unique) and referential integrity (references resolve) are the foundational integrity classes."
  certainty: high
  evidence: Relational model theory
  scope: cross-domain
- claim: "Integrity failures are correctness failures with a trace — orphaned references, duplicate identity, and constraint violations signal model or process defects."
  certainty: high
  evidence: Data-quality incident analyses
  scope: cross-domain
- claim: "Integrity guarantees are scoped — the schema's rules define what integrity means for this data; rules outside the schema are outside the guarantee."
  certainty: high
  evidence: Database practice
  scope: cross-domain

## Relationships
- concept: relational-model
  relationship: guaranteed_by
  description: "Data integrity is guaranteed by the relational model — keys and rules are the model's integrity mechanisms."
- concept: schema-design
  relationship: shaped_by
  description: "Data integrity is shaped by schema design — integrity rules are schema decisions."
- concept: normalization
  relationship: reinforced_by
  description: "Data integrity is reinforced by normalization — normal forms eliminate integrity anomalies."
- concept: transactions
  relationship: protected_by
  description: "Data integrity is protected by transactions — atomicity prevents partial states."
- concept: schema-migration
  relationship: threatened_by
  description: "Data integrity is threatened by schema migration — bad migrations corrupt or orphan data."
- concept: data-governance
  relationship: audited_by
  description: "Data integrity is audited by data governance — integrity monitoring is a governance function."

## Tradeoffs
- dimension: integrity_strictness_vs_performance
  options:
    full_enforcement:
      value: correctness
      rationale: "Full enforcement guarantees conformance but costs every write."
    deferred_checks:
      value: write_speed
      rationale: "Deferred or batched checks are fast but allow invalid states between checks."
  importance: high
- dimension: schema_enforcement_vs_app_enforcement
  options:
    schema_rules:
      value: universality
      rationale: "Schema-enforced rules protect every consumer, including future ones."
    application_rules:
      value: flexibility
      rationale: "Application-enforced rules are flexible but apply only where the app runs."
  importance: high

## Failure Modes
- name: integrity_violation
  description: "Data enters a state that violates its rules — orphaned references, duplicates, or invalid values."
  likelihood: medium
  observable_evidence: "Referential orphans; duplicate identity; constraint errors on reads and writes"
  detection: "Integrity checks; referential audits; data-quality monitoring"
  recovery: "Clean the violation; fix the entry process; add blocking constraints"
  retryable: true
- name: silent_corruption
  description: "Data is corrupted without detection — the system serves wrong data with correct-looking interfaces."
  likelihood: low
  observable_evidence: "Wrong query results; checksum failures; integrity checks catching corruption late"
  detection: "Checksums; verification queries; periodic integrity audits"
  recovery: "Restore from backup; repair the corruption source; harden the write path"
  retryable: true
- name: integrity_bypass
  description: "Writes bypass the schema's rules — bulk loads, legacy paths, or privileged code insert data that violates constraints."
  likelihood: medium
  observable_evidence: "Invalid data appearing despite schema rules; violations clustered at load times; code paths that skip validation"
  detection: "Write-path audit; integrity re-checks after loads; constraint conformance monitoring"
  recovery: "Route bypass paths through validation; backfill fixes; enforce rules at every entry"
  retryable: true

## Observations
- observation: "Schema-enforced integrity is the only verifiable integrity — application-enforced rules are claims without a guarantee."
  confidence: high
  source: Database practice
- observation: "Integrity failures are the most common root cause of 'wrong data' incidents in data platforms."
  confidence: high
  source: Data-quality incident analyses
- observation: "Every integrity bypass accumulates as technical debt that a future incident cashes in."
  confidence: high
  source: Data engineering experience

## Constraints
- constraint: "Data must conform to its integrity rules at all times — a rule violated even once is a correctness failure."
  type: invariant
  scope: cross-domain
- constraint: "Integrity guarantees are scoped to the schema — rules not in the schema are not part of the guarantee."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Enforce integrity in the schema, not in the application."
  rationale: "Schema rules are universal and verifiable; app rules are optional by construction."
  evidence_level: high
- heuristic: "Treat every integrity bypass as an incident, not a convenience."
  rationale: "Bypasses are how guaranteed systems silently become unguaranteed."
  evidence_level: high

## Recommendations
- recommendation: "Express integrity rules as schema constraints with enforcement."
  context: schema_design
  certainty: strong
  rationale: "A rule without enforcement is a wish."
- recommendation: "Audit integrity continuously, not at migrations only."
  context: data_governance
  certainty: strong
  rationale: "Violations are cheap to fix at write time and expensive after propagation."
- recommendation: "Re-verify integrity after every migration and bulk load."
  context: operations
  certainty: strong
  rationale: "Bulk paths are where guaranteed systems break silently."
