# Schema Migration

## Identity
- id: schema-migration
- type: concept
- title: Schema Migration
- tags: [databases, schema migration, schema evolution, versioning, contract, data transformation]
- entities: [schema migration, schema version, migration, contract break, data transformation]
- concepts: [schema-design, data-integrity, transactions, build-systems, query-optimization, atomicity]

## Claims
- claim: "Schema migration is a disciplined schema change — a versioned transition with validity conditions, not an edit."
  certainty: high
  evidence: Data engineering practice
  scope: cross-domain
- claim: "A schema version's validity is bound to stated conditions — the data, consumers, and operations that version supports."
  certainty: high
  evidence: Schema evolution practice
  scope: cross-domain
- claim: "Migrations carry correctness obligations — data must be transformed faithfully, and the post-migration schema must satisfy the new contract."
  certainty: high
  evidence: Migration incident analyses
  scope: cross-domain
- claim: "The schema is a contract — migration breaks contracts unless consumers move in step, making additive migration the default discipline."
  certainty: high
  evidence: Data engineering practice
  scope: cross-domain
- claim: "Migration validity is the artifact-validity pattern applied to data — a migrated schema is valid if derived from its predecessor under the migration's conditions."
  certainty: high
  evidence: Cross-domain comparison (Cycle 009 build artifacts)
  scope: cross-domain

## Relationships
- concept: schema-design
  relationship: evolves
  description: "Schema migration evolves schema design — change is a versioned operation."
- concept: data-integrity
  relationship: must_preserve
  description: "Schema migration must preserve data integrity — transformation must not corrupt data."
- concept: transactions
  relationship: executed_under
  description: "Schema migration is executed under transactions — structural change is transactional work."
- concept: build-systems
  relationship: analogous_to
  description: "Schema migration is analogous to build systems — both manage derived-state validity — the cross-domain link to the Cycle 009 corpus."
- concept: query-optimization
  relationship: affected_by
  description: "Query optimization is affected by schema migration — new structure changes query shapes and plans."

## Tradeoffs
- dimension: additive_vs_breaking_change
  options:
    additive_migration:
      value: compatibility
      rationale: "Additive changes keep consumers working but accumulate legacy structure."
    breaking_changes:
      value: cleanliness
      rationale: "Breaking changes clean the schema but break consumers and force coordination."
  importance: high
- dimension: migration_frequency_vs_stability
  options:
    frequent_migration:
      value: schema_freshness
      rationale: "Frequent migration tracks the domain closely but taxes every consumer."
    rare_migration:
      value: stability
      rationale: "Rare migration is stable but accumulates schema debt."
  importance: high

## Failure Modes
- name: contract_break
  description: "A migration breaks consumers — queries and applications compiled against the old schema fail."
  likelihood: high
  observable_evidence: "Post-migration failures; consumer breakage; rollbacks"
  detection: "Consumer impact analysis; contract testing; migration rehearsal"
  recovery: "Additive redesign; coordinated rollout; consumer updates"
  retryable: true
- name: data_loss
  description: "Migration transforms data incorrectly — rows are lost, mangled, or corrupted."
  likelihood: medium
  observable_evidence: "Row-count changes; data corruption; integrity violations after migration"
  detection: "Pre/post comparison; integrity re-checks; backup verification"
  recovery: "Restore from backup; correct the transform; re-migrate"
  retryable: true
- name: migration_failure_partial
  description: "A migration fails midway — the schema and data are in an inconsistent mixed state."
  likelihood: medium
  observable_evidence: "Version mismatches; half-applied changes; mixed-schema behaviour"
  detection: "Migration version checks; consistency verification; failover analysis"
  recovery: "Roll back or roll forward under transaction; repair mixed state"
  retryable: true

## Observations
- observation: "Schema validity is derivation — the migrated schema is valid if derived from its predecessor under stated conditions, exactly like build artifacts."
  confidence: high
  source: Cross-domain comparison (Cycle 009)
- observation: "Most migration incidents are contract breaks, not data loss — consumers are the usual casualty."
  confidence: high
  source: Migration incident analyses
- observation: "Migration is a permanent operational capability, not an occasional event — the discipline is the product."
  confidence: high
  source: Data engineering practice

## Constraints
- constraint: "A schema version's validity is bound to its stated conditions — use outside those conditions is unsupported."
  type: invariant
  scope: cross-domain
- constraint: "Migration must preserve data — a migration that loses or corrupts data is a correctness failure."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Prefer additive migrations with explicit deprecation."
  rationale: "Additive changes preserve contracts; deprecation removes debt on a schedule."
  evidence_level: high
- heuristic: "Rehearse migrations on copies of production data."
  rationale: "Rehearsal reveals contract breaks and data issues before users do."
  evidence_level: high

## Recommendations
- recommendation: "Treat migration as a versioned, rehearsed, verified operation."
  context: operations
  certainty: strong
  rationale: "Undisciplined migration is the standard source of data-platform incidents."
- recommendation: "Keep consumers moving with additive defaults and coordinated breaking changes."
  context: governance
  certainty: strong
  rationale: "The contract is the product; breaking it without coordination is the incident."
- recommendation: "Verify post-migration integrity and schema validity explicitly."
  context: operations
  certainty: strong
  rationale: "Migration validity is a claim until verification makes it evidence."
