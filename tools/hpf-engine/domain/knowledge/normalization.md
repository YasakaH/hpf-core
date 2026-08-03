# Normalization

## Identity
- id: normalization
- type: pattern
- title: Normalization
- tags: [databases, normalization, normal forms, schema design, redundancy, anomaly]
- entities: [normalization, normal form, functional dependency, redundancy, anomaly, denormalization]
- concepts: [relational-model, schema-design, data-integrity, query-optimization, schema-migration]

## Claims
- claim: "Normalization is the disciplined evaluation of schema structure against normal forms — each form eliminates a class of redundancy and its update anomalies."
  certainty: high
  evidence: Relational design theory and practice
  scope: cross-domain
- claim: "Normal forms are constraints on structure — they define what counts as well-formed relations, not as a separate design vocabulary."
  certainty: high
  evidence: Relational theory
  scope: cross-domain
- claim: "Normalization eliminates anomalies — redundancy, update anomalies, and deletion anomalies — by distributing facts across correctly structured relations."
  certainty: high
  evidence: Relational design literature
  scope: cross-domain
- claim: "Denormalization is a deliberate tradeoff, not an accident — reintroducing redundancy for query performance requires compensating discipline."
  certainty: high
  evidence: Data engineering practice
  scope: cross-domain
- claim: "The value of normalization degrades past the point of diminishing returns — beyond a practical form, purity costs complexity without integrity gain."
  certainty: high
  evidence: Database design practice
  scope: cross-domain

## Relationships
- concept: relational-model
  relationship: evaluates
  description: "Normalization evaluates the relational model — normal forms judge the model's structure."
- concept: schema-design
  relationship: guides
  description: "Normalization guides schema design — normal forms are the design discipline."
- concept: data-integrity
  relationship: reinforces
  description: "Normalization reinforces data integrity — well-structured relations cannot exhibit update anomalies."
- concept: query-optimization
  relationship: shapes
  description: "Normalization shapes query optimization — join-heavy normalized schemas trade query cost for integrity."
- concept: schema-migration
  relationship: complicates
  description: "Normalization complicates schema migration — many relations mean many migration targets."

## Tradeoffs
- dimension: normalization_depth_vs_query_cost
  options:
    fully_normalized:
      value: integrity
      rationale: "Full normalization eliminates anomalies but requires joins for almost every query."
    pragmatically_denormalized:
      value: query_speed
      rationale: "Deliberate denormalization speeds queries but reintroduces redundancy to manage."
  importance: high
- dimension: structure_purity_vs_agility
  options:
    strict_forms:
      value: correctness
      rationale: "Strict normal forms are provably anomaly-free but rigid under change."
    pragmatic_structure:
      value: agility
      rationale: "Pragmatic structures adapt faster but accumulate redundancy debt."
  importance: high

## Failure Modes
- name: over_normalization
  description: "Schema is normalized beyond practical need — every fact is atomized and every query requires many joins."
  likelihood: medium
  observable_evidence: "Join-heavy queries; slow reads; complexity disproportionate to domain"
  detection: "Query cost analysis; schema review; workload profiling"
  recovery: "Selectively denormalize; add materialized views; reassess forms"
  retryable: true
- name: undisciplined_denormalization
  description: "Redundancy is introduced without compensating controls — copies drift and integrity claims become false."
  likelihood: medium
  observable_evidence: "Inconsistent copies; update anomalies in production; 'which version is right' disputes"
  detection: "Redundancy audit; consistency checks; drift monitoring"
  recovery: "Centralize the source of truth; add sync discipline; reconcile copies"
  retryable: true
- name: hidden_dependency
  description: "Functional dependencies are implicit — structure claims no redundancy, but updates still cause anomalies."
  likelihood: medium
  observable_evidence: "Unexplained anomalies in 'normalized' schemas; update bugs; data-quality incidents"
  detection: "Dependency analysis; anomaly reproduction; structure audit"
  recovery: "Explicitly model dependencies; restructure; document decisions"
  retryable: true

## Observations
- observation: "Normal forms convert design taste into checkable criteria — the discipline's value is its testability."
  confidence: high
  source: Relational design practice
- observation: "Practical schemas stop at third normal form — higher forms buy little integrity for much complexity."
  confidence: high
  source: Database design practice
- observation: "Denormalization fails only when undisciplined — deliberate redundancy with controls is standard practice."
  confidence: high
  source: Data engineering practice

## Constraints
- constraint: "Every redundant fact requires a compensating control — denormalization without discipline is corruption in waiting."
  type: invariant
  scope: cross-domain
- constraint: "Normal forms are structural constraints — a relation that violates its declared form is structurally unsound."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Normalize to third normal form by default; denormalize by decision, not drift."
  rationale: "The default protects; the decision is auditable."
  evidence_level: high
- heuristic: "Document every denormalization with its compensating control."
  rationale: "Undocumented redundancy is future inconsistency."
  evidence_level: high

## Recommendations
- recommendation: "Apply normal forms as checkable criteria, not as ideology."
  context: schema_design
  certainty: strong
  rationale: "Forms test structure; ideology prevents pragmatism."
- recommendation: "Pair every denormalization with a consistency control."
  context: design
  certainty: strong
  rationale: "The control is what makes the tradeoff legal."
- recommendation: "Revisit normalization decisions when workloads change."
  context: governance
  certainty: strong
  rationale: "The right depth is workload-dependent, not timeless."
