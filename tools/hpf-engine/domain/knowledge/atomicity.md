# Atomicity

## Identity
- id: atomicity
- type: concept
- title: Atomicity
- tags: [databases, atomicity, ACID, all-or-nothing, write-ahead logging, crash safety]
- entities: [atomicity, all-or-nothing, commit, rollback, write-ahead log, crash recovery]
- concepts: [transactions, data-integrity, transaction-failures, relational-model, schema-migration]

## Claims
- claim: "Atomicity is the guarantee that a transaction applies fully or not at all — no partial states are observable."
  certainty: high
  evidence: Database theory
  scope: cross-domain
- claim: "Atomicity is a scoped guarantee — it holds for the transaction boundary, not for work outside it."
  certainty: high
  evidence: Transaction theory and practice
  scope: cross-domain
- claim: "Atomicity is implemented through write-ahead logging — durability of the intent log makes rollback and recovery possible."
  certainty: high
  evidence: Database implementation practice
  scope: cross-domain
- claim: "Atomicity converts crash exposure into a recovery procedure — the guarantee is about observable outcome, not about the failure event itself."
  certainty: high
  evidence: Crash recovery theory and practice
  scope: cross-domain
- claim: "Atomicity's value is compositional — multi-step operations become testable units; partial failure becomes a contradiction, not a case."
  certainty: high
  evidence: Transaction practice
  scope: cross-domain

## Relationships
- concept: transactions
  relationship: defines
  description: "Atomicity defines the transaction — all-or-nothing is the unit's core property."
- concept: data-integrity
  relationship: protects
  description: "Atomicity protects data integrity — partial states would violate integrity rules."
- concept: transaction-failures
  relationship: contained_by
  description: "Transaction failures are contained by atomicity — abort leaves no partial effect."
- concept: relational-model
  relationship: preserves
  description: "Atomicity preserves the relational model's invariants — relations never expose partial work."
- concept: schema-migration
  relationship: required_by
  description: "Atomicity is required by schema migration — structural changes must be all-or-nothing."

## Tradeoffs
- dimension: atomicity_granularity_vs_overhead
  options:
    fine_grained_atomicity:
      value: isolation_freedom
      rationale: "Fine units reduce contention but multiply commit overhead and boundary decisions."
    coarse_grained_atomicity:
      value: fewer_boundaries
      rationale: "Coarse units minimize boundary decisions but amplify contention and recovery scope."
  importance: medium
- dimension: durability_strength_vs_write_cost
  options:
    fsync_every_commit:
      value: crash_safety
      rationale: "Durable commits survive crashes but pay the full flush cost per commit."
    group_commit:
      value: throughput
      rationale: "Grouped commits are fast but widen the loss window."
  importance: high

## Failure Modes
- name: partial_commit
  description: "A transaction's effects are partially visible — the atomicity guarantee is violated by a system defect."
  likelihood: low
  observable_evidence: "Half-applied changes; integrity violations after failure; inconsistent state in recovery"
  detection: "Integrity checks; recovery testing; write-path audits"
  recovery: "Repair the violated state; fix the logging or commit logic; restore from backup if needed"
  retryable: true
- name: recovery_gap
  description: "Recovery cannot reconstruct the atomic state — the log is incomplete, corrupted, or misapplied."
  likelihood: medium
  observable_evidence: "Recovery failures after crash; log corruption; lost committed work"
  detection: "Log integrity checks; recovery drills; checksum verification"
  recovery: "Replay from valid log prefix; restore from backup; repair logging"
  retryable: true
- name: atomicity_scope_mismatch
  description: "Work spans multiple transactions but is treated as one unit — partial success of the overall operation is possible."
  likelihood: medium
  observable_evidence: "Multi-step operations failing midway; business inconsistencies; compensating code everywhere"
  detection: "Boundary analysis; failure-path review; saga audit"
  recovery: "Restructure boundaries; add compensation; align units with business atomicity"
  retryable: true

## Observations
- observation: "Atomicity is the guarantee that makes every other transaction property discussable — without it, failure classes multiply."
  confidence: high
  source: Transaction theory
- observation: "Crash recovery is where atomicity is actually proven — the guarantee is meaningless if it does not survive failure."
  confidence: high
  source: Database engineering practice
- observation: "Distributed systems rediscover atomicity as sagas and compensation — the guarantee becomes a design problem at scale."
  confidence: high
  source: Distributed systems practice (cross-ref: Cycle 006)

## Constraints
- constraint: "A transaction's effects are either fully observable or not at all — partial visibility is a correctness failure."
  type: invariant
  scope: cross-domain
- constraint: "Atomicity holds within the transaction boundary — work outside the boundary has no claim to the guarantee."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Align transaction boundaries with business atomicity."
  rationale: "Units that split business-atomic operations force compensation logic."
  evidence_level: high
- heuristic: "Test recovery as a first-class scenario."
  rationale: "The guarantee is proven at recovery time, not commit time."
  evidence_level: high

## Recommendations
- recommendation: "Treat atomicity as a scoped guarantee — state what is inside the boundary."
  context: design
  certainty: strong
  rationale: "An unscoped guarantee is a claim without a contract."
- recommendation: "Rehearse crash recovery with integrity verification."
  context: operations
  certainty: strong
  rationale: "The failure path is where the guarantee lives or dies."
- recommendation: "Use sagas or compensation when atomicity is unachievable across boundaries — explicitly."
  context: distributed_design
  certainty: strong
  rationale: "Implicit non-atomicity is the failure; explicit compensation is the design."
