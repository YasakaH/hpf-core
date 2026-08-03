# Replication

## Identity
- id: replication
- type: pattern
- title: Replication
- tags: [databases, replication, consistency, divergence, master-slave, consensus]
- entities: [replication, replica, consistency model, divergence, replication lag, failover]
- concepts: [strong-consistency, eventual-consistency, split-brain, transactions, atomicity]

## Claims
- claim: "Replication is the maintenance of multiple copies of data across nodes — a redundancy pattern with consistency obligations."
  certainty: high
  evidence: Distributed systems practice and literature
  scope: cross-domain
- claim: "Replica semantics are defined by the consistency model — the model states what divergence is permitted between copies."
  certainty: high
  evidence: Consistency research (CAP, linearizability)
  scope: cross-domain
- claim: "Replication trades availability and latency against consistency — the tradeoff shape is chosen, not discovered."
  certainty: high
  evidence: Distributed systems practice, CAP theorem analyses
  scope: cross-domain
- claim: "Replication lag is an observable condition — stale reads are the cost of asynchronous propagation and must be part of the contract."
  certainty: high
  evidence: Database replication practice
  scope: cross-domain
- claim: "Replication failure modes are divergence and split-brain — copies disagree, or the system splits into isolated writers."
  certainty: high
  evidence: Distributed systems incident analyses
  scope: cross-domain

## Relationships
- concept: strong-consistency
  relationship: constrained_by
  description: "Replication is constrained by strong consistency — the strongest models require synchronous propagation."
- concept: eventual-consistency
  relationship: allows
  description: "Replication allows eventual consistency — divergence converges under the model's terms."
- concept: split-brain
  relationship: subject_to
  description: "Replication is subject to split-brain — the cross-domain link to the Cycle 006 corpus."
- concept: transactions
  relationship: supports
  description: "Replication supports transactions — distributed transaction semantics depend on replication."
- concept: atomicity
  relationship: complicates
  description: "Replication complicates atomicity — atomicity across copies requires coordination."

## Tradeoffs
- dimension: consistency_strength_vs_latency
  options:
    synchronous_replication:
      value: consistency
      rationale: "Synchronous replication guarantees consistency but pays latency on every write."
    asynchronous_replication:
      value: latency
      rationale: "Asynchronous replication is fast but allows stale reads."
  importance: high
- dimension: replica_count_vs_operational_cost
  options:
    many_replicas:
      value: durability_availability
      rationale: "More replicas improve durability and read capacity but multiply cost and divergence risk."
    few_replicas:
      value: simplicity
      rationale: "Fewer replicas are simpler but weaken durability and availability."
  importance: high

## Failure Modes
- name: divergence
  description: "Replicas disagree beyond the consistency model's terms — copies have different data with no convergence."
  likelihood: medium
  observable_evidence: "Stale reads beyond contract; inconsistent query results across replicas; reconciliation needs"
  detection: "Consistency checks; replica comparison; lag monitoring"
  recovery: "Re-sync replicas; identify the divergence source; restore the model's terms"
  retryable: true
- name: split_brain
  description: "Network partition splits the system into isolated writers — both sides accept writes and cannot reconcile."
  likelihood: medium
  observable_evidence: "Conflicting writes after partition; unreconcilable divergence; failover surprises"
  detection: "Partition detection; quorum analysis; write-conflict monitoring"
  recovery: "Quorum enforcement; conflict resolution; survivor selection"
  retryable: true
- name: lag_surprise
  description: "Replication lag violates consumer expectations — applications read through stale replicas and act on old data."
  likelihood: medium
  observable_evidence: "Stale reads in production; read-your-write violations; lag-dependent behaviour"
  detection: "Lag monitoring; consistency-expectation audit; read-path analysis"
  recovery: "Route reads appropriately; align expectations with the model; add read-after-write handling"
  retryable: true

## Observations
- observation: "Consistency model choice is the replication decision — everything else follows from the chosen tradeoff."
  confidence: high
  source: Distributed systems practice
- observation: "Lag is a contract term — consumers who assume its absence are assuming a stronger model than configured."
  confidence: high
  source: Database replication experience
- observation: "The corpus already models the consistency spectrum (strong-consistency, eventual-consistency, split-brain) — replication adds the operational layer, not a new construct."
  confidence: high
  source: Cross-domain composition (Cycle 006)

## Constraints
- constraint: "Replica semantics are bound by the consistency model — divergence beyond the model's terms is a failure."
  type: invariant
  scope: cross-domain
- constraint: "Every replica is a maintained copy — replication without monitoring is divergence in progress."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Choose the consistency model first; everything else follows."
  rationale: "The model defines the contract, the tradeoffs, and the failure classes."
  evidence_level: high
- heuristic: "Monitor lag and divergence as first-class signals."
  rationale: "Replication failures are silent until a consumer notices."
  evidence_level: high

## Recommendations
- recommendation: "Document the consistency model as the replication contract."
  context: architecture
  certainty: strong
  rationale: "The model is the contract; undocumented models are divergence in progress."
- recommendation: "Monitor lag against consumer expectations."
  context: operations
  certainty: strong
  rationale: "Stale reads are only failures relative to what consumers assume."
- recommendation: "Enforce quorum to prevent split-brain."
  context: architecture
  certainty: strong
  rationale: "Split-brain is unrecoverable divergence; quorum prevents it."
