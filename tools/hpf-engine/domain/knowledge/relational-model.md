# Relational Model

## Identity
- id: relational-model
- type: concept
- title: Relational Model
- tags: [databases, relational model, relations, tuples, keys, data model]
- entities: [relational model, relation, tuple, attribute, key, data model]
- concepts: [schema-design, data-integrity, normalization, transactions, query-planning, query-optimization]

## Claims
- claim: "The relational model represents data as relations — sets of tuples over named attributes — with keys defining identity and integrity rules bounding validity."
  certainty: high
  evidence: Relational model literature, database practice
  scope: cross-domain
- claim: "The model separates logical structure from physical storage — queries are written against the logical schema, independent of how data is laid out."
  certainty: high
  evidence: Relational database design, SQL practice
  scope: cross-domain
- claim: "Keys are the identity mechanism — primary keys define what a tuple is, foreign keys define what references it."
  certainty: high
  evidence: Relational model theory, database practice
  scope: cross-domain
- claim: "The model's vocabulary — entities and relationships — coincides with knowledge-graph vocabulary because both model structured reality; the coincidence is the model's power, not an accident."
  certainty: high
  evidence: Entity-relationship modelling practice
  scope: cross-domain
- claim: "Set semantics give the model its mathematical base — relation operations (selection, projection, join) are closed and composable."
  certainty: high
  evidence: Relational algebra theory
  scope: cross-domain

## Relationships
- concept: schema-design
  relationship: governs
  description: "The relational model governs schema design — relations, keys, and integrity rules are the design vocabulary."
- concept: data-integrity
  relationship: enables
  description: "The relational model enables data integrity — keys and integrity rules are the model's guarantee mechanisms."
- concept: normalization
  relationship: rationalized_by
  description: "The relational model is rationalized by normalization — normal forms evaluate the model's structure."
- concept: transactions
  relationship: manipulated_by
  description: "The relational model is manipulated by transactions — data changes happen as units of work over relations."
- concept: query-planning
  relationship: operated_upon_by
  description: "The relational model is operated upon by query planning — queries against relations are compiled to plans."
- concept: query-optimization
  relationship: preserves
  description: "Query optimization preserves the relational model's semantics — rewrites must keep the same result relation."

## Tradeoffs
- dimension: structural_purity_vs_practical_flexibility
  options:
    strict_normalization:
      value: correctness
      rationale: "Strict relational structure guarantees integrity and consistent reasoning about data."
    pragmatic_flexibility:
      value: practicality
      rationale: "Flexible structures (schemaless, denormalized) serve real workloads but weaken the model's guarantees."
  importance: high
- dimension: model_expressiveness_vs_simplicity
  options:
    rich_models:
      value: representation_power
      rationale: "Richer models (types, constraints, views) represent more of the world but complicate the system."
    minimal_model:
      value: predictability
      rationale: "Minimal models are simple and predictable but push semantics into application code."
  importance: medium

## Failure Modes
- name: key_design_failure
  description: "Keys are chosen badly — natural keys that change, missing keys, or surrogate keys without meaning — undermining identity and referential integrity."
  likelihood: medium
  observable_evidence: "Identity drift in data; join anomalies; integrity violations on updates; duplicate entities"
  detection: "Key design review; data-quality audits; reference integrity checks"
  recovery: "Re-key the model; add surrogate keys; migrate references"
  retryable: true
- name: model_reality_mismatch
  description: "The relational model misrepresents the world it models — entities, attributes, or constraints disagree with reality."
  likelihood: medium
  observable_evidence: "Data that cannot represent real states; constraint violations on valid input; application workarounds"
  detection: "Model review against the domain; constraint conformance analysis; mapping audits"
  recovery: "Correct the model; migrate data; align constraints with reality"
  retryable: true
- name: logical_physical_leakage
  description: "Physical storage assumptions leak into logical design — queries and schemas depend on layout, breaking the separation the model promises."
  likelihood: medium
  observable_evidence: "Queries optimized for layout rather than logic; schema changes requiring query rewrites; storage-dependent results"
  detection: "Design review; abstraction-boundary audits"
  recovery: "Re-establish the logical layer; remove layout dependence"
  retryable: true

## Observations
- observation: "The relational model's entities/relationships vocabulary matches knowledge-graph vocabulary directly — the same ontology serves both."
  confidence: high
  source: Database practice, knowledge engineering
- observation: "The logical/physical separation is the model's enduring contribution — it survives every storage engine change."
  confidence: high
  source: Database history and practice
- observation: "Most long-lived data-quality problems trace to key or model design decisions made early."
  confidence: high
  source: Data engineering experience

## Constraints
- constraint: "Every tuple must satisfy the model's integrity rules — a relation that violates its constraints is not valid data."
  type: invariant
  scope: cross-domain
- constraint: "Keys must be stable and unique — identity that changes or duplicates is identity failure."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Choose surrogate keys for stable identity and natural keys for business mapping."
  rationale: "Natural keys drift; surrogates are stable but must be mapped."
  evidence_level: high
- heuristic: "Keep logical design independent of physical layout."
  rationale: "The separation is the model's power; violating it forfeits it."
  evidence_level: high

## Recommendations
- recommendation: "Model identity explicitly — keys are the load-bearing design decision."
  context: schema_design
  certainty: strong
  rationale: "Identity failures propagate to every join and reference."
- recommendation: "Validate the model against reality before building on it."
  context: modelling
  certainty: strong
  rationale: "A model that misrepresents its world fails silently and expensively."
- recommendation: "Maintain the logical/physical separation as an invariant."
  context: architecture
  certainty: strong
  rationale: "Layout dependence is how schemas become unmovable."
