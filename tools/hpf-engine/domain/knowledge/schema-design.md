# Schema Design

## Identity
- id: schema-design
- type: concept
- title: Schema Design
- tags: [databases, schema, data model, design, tables, columns, constraints]
- entities: [schema, schema design, table, column, data model, constraint]
- concepts: [relational-model, data-integrity, normalization, schema-migration, query-optimization, data-governance]

## Claims
- claim: "A schema is a claim about the world — what exists, what properties it has, and what constraints hold over it."
  certainty: high
  evidence: Data modelling practice
  scope: cross-domain
- claim: "Schema design is a modelling act with correctness obligations — a schema that misrepresents its domain produces data that cannot represent real states."
  certainty: high
  evidence: Data modelling practice, data-quality analyses
  scope: cross-domain
- claim: "Schema decisions trade expressiveness against integrity — permissive schemas accept more data but weaken guarantees; strict schemas enforce more but reject more."
  certainty: high
  evidence: Schema design practice
  scope: cross-domain
- claim: "A schema is never finished — domain understanding evolves, and the schema must evolve with it under migration discipline."
  certainty: high
  evidence: Schema evolution practice
  scope: cross-domain
- claim: "The schema is the contract between data producers and consumers — every query and every write is interpreted against it."
  certainty: high
  evidence: Data engineering practice
  scope: cross-domain

## Relationships
- concept: relational-model
  relationship: instantiates
  description: "Schema design instantiates the relational model — relations and keys are realized as tables and constraints."
- concept: data-integrity
  relationship: shapes
  description: "Schema design shapes data integrity — integrity rules are schema decisions."
- concept: normalization
  relationship: guided_by
  description: "Schema design is guided by normalization — normal forms evaluate schema quality."
- concept: schema-migration
  relationship: evolves
  description: "Schema design evolves through schema migration — change is a disciplined operation, not an edit."
- concept: query-optimization
  relationship: bounded_by
  description: "Query optimization is bounded by schema design — the schema determines which query shapes are possible and optimizable."
- concept: data-governance
  relationship: constrained_by
  description: "Schema design is constrained by data governance — retention, lineage, and access requirements shape the schema."

## Tradeoffs
- dimension: strictness_vs_flexibility
  options:
    strict_schema:
      value: integrity
      rationale: "Strict schemas enforce guarantees but reject flexible real-world data."
    flexible_schema:
      value: acceptance
      rationale: "Flexible schemas accept more data but push validation into application code."
  importance: high
- dimension: completeness_vs_simplicity
  options:
    rich_schema:
      value: fidelity
      rationale: "Rich schemas represent more of the world but are costly to maintain and migrate."
    lean_schema:
      value: agility
      rationale: "Lean schemas are cheap to maintain but under-represent the domain."
  importance: high

## Failure Modes
- name: schema_reality_divergence
  description: "The schema drifts from the world it models — data can no longer represent real states, or valid states are unrepresentable."
  likelihood: medium
  observable_evidence: "Workarounds in application code; constraint violations on valid input; forced hacks for real states"
  detection: "Domain-model review; data-quality analysis; application-schema mapping audits"
  recovery: "Revise the schema; migrate data; align with reality"
  retryable: true
- name: premature_flexibility
  description: "The schema is made flexible to avoid future changes — generality without a requirement complicates queries and weakens guarantees."
  likelihood: medium
  observable_evidence: "Generic columns (type, value); query complexity exploding; integrity enforced in code instead of schema"
  detection: "Schema review; query complexity analysis; integrity-dispersion audits"
  recovery: "Concretize the schema; move integrity back into constraints"
  retryable: true
- name: contract_break
  description: "A schema change breaks consumers — queries, applications, and reports depend on the old contract."
  likelihood: high
  observable_evidence: "Post-migration failures; query breakage; consumer complaints after schema changes"
  detection: "Consumer impact analysis; contract testing; migration rehearsals"
  recovery: "Versioned schemas; additive migration; consumer coordination"
  retryable: true

## Observations
- observation: "The schema is the most durable artifact in a data system — applications come and go; the schema and its data outlive them."
  confidence: high
  source: Data engineering experience
- observation: "Schema debt (premature flexibility, deferred constraints) is the slow poison of data platforms."
  confidence: high
  source: Data platform practice
- observation: "The best schemas are built from the domain outward, not from the storage inward."
  confidence: high
  source: Data modelling practice

## Constraints
- constraint: "The schema must faithfully represent its domain — a schema that misrepresents reality invalidates every query's interpretation."
  type: invariant
  scope: cross-domain
- constraint: "Integrity rules belong in the schema — validation scattered in application code is integrity without a contract."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Design from the domain outward."
  rationale: "Storage-first schemas optimize layout and misrepresent the world."
  evidence_level: high
- heuristic: "Prefer concrete schemas over premature generality."
  rationale: "Generality without a requirement is schema debt."
  evidence_level: high

## Recommendations
- recommendation: "Treat the schema as a contract — version it, document it, and change it under migration discipline."
  context: schema_governance
  certainty: strong
  rationale: "The schema is the interface every consumer compiles against."
- recommendation: "Move integrity into schema constraints wherever possible."
  context: design
  certainty: strong
  rationale: "Schema-enforced integrity is verifiable; code-enforced integrity is not."
- recommendation: "Review the schema against its domain periodically."
  context: governance
  certainty: strong
  rationale: "Divergence accumulates silently until data cannot represent reality."
