# Eventual Consistency

## Identity
- id: eventual-consistency
- type: concept
- title: Eventual Consistency
- tags: [distributed-systems, consistency, availability, replication, dynamo]
- entities: [eventual consistency, weak consistency, convergent state, conflict resolution, dynamo]
- concepts: [cap-theorem, strong-consistency, availability, quorum, network-partition-recovery]

## Claims
- claim: "Eventual consistency guarantees that if no new writes are made to a data item, all replicas will eventually return the same value."
  certainty: high
  evidence: Distributed systems literature, Dynamo paper (Amazon)
  scope: cross-system
- claim: "Eventual consistency does not guarantee when convergence will occur — the window of inconsistency is unbounded."
  certainty: high
  evidence: Distributed systems literature
  scope: cross-system
- claim: "Eventual consistency allows stale reads — a read may return an older value if the replica has not yet received the latest write."
  certainty: high
  evidence: Distributed systems literature, Dynamo paper
  scope: cross-system
- claim: "Eventual consistency maintains availability during partitions — all replicas accept writes regardless of partition state."
  certainty: high
  evidence: CAP theorem, Dynamo paper
  scope: cross-system
- claim: "Conflict resolution is required when multiple replicas accept concurrent writes — last-write-wins (LWW) is the most common strategy."
  certainty: high
  evidence: Dynamo paper, production systems
  scope: cross-system
- claim: "Eventual consistency is not a single model — read-after-write, monotonic reads, and causal consistency are stronger forms that bound inconsistency."
  certainty: high
  evidence: Distributed systems literature
  scope: cross-system

## Relationships
- concept: cap-theorem
  relationship: realises
  description: "Eventual consistency realises the availability-over-consistency choice during partitions — writes are always accepted."
- concept: strong-consistency
  relationship: contrasts_with
  description: "Eventual consistency accepts temporary inconsistency for availability; strong consistency guarantees immediate correctness at the cost of availability during partitions."
- concept: availability
  relationship: provides
  description: "Eventual consistency provides maximum availability — all nodes accept writes under all conditions."
- concept: quorum
  relationship: may_use
  description: "Eventually consistent systems can use relaxed quorums (e.g. write quorum = 1) for maximum availability."
- concept: network-partition-recovery
  relationship: requires
  description: "Eventually consistent systems require reconciliation logic during partition recovery to resolve divergent state."

## Tradeoffs
- dimension: staleness_vs_availability
  options:
    tight_staleness:
      value: bounded_inconsistency
      rationale: "Configure replication lag limits — reject reads if replica is too far behind. Better consistency, reduced availability."
    unbounded_staleness:
      value: maximum_availability
      rationale: "Accept any replica for reads — maximum availability but unbounded staleness."
  importance: high
- dimension: conflict_resolution_strategy
  options:
    last_write_wins:
      value: simplicity
      rationale: "Timestamps or version vectors determine the winning write — simple but potentially loses data."
    application_resolved:
      value: correctness
      rationale: "Application receives conflicting versions and resolves semantically — correct but adds application complexity."
    crdt_based:
      value: automatic_resolution
      rationale: "Conflict-free replicated data types resolve automatically through mathematical properties — correct and automatic but limited to specific data structures."
  importance: high
- dimension: read_your_writes
  options:
    session_guarantees:
      value: user_experience
      rationale: "Read-after-write per session (read from authoritative replica) — improves user experience without global consistency."
    no_guarantees:
      value: maximum_scaling
      rationale: "No read-after-write guarantees — simplest to implement but users may see stale data after their own writes."
  importance: operational

## Failure Modes
- name: unbounded_divergence
  description: "Replicas diverge and never converge because conflict resolution is insufficient or writes continue indefinitely during a long partition."
  likelihood: medium
  observable_evidence: "Replicas show permanently different state after partition resolves; reconciliation process never completes; data integrity violations"
  detection: "Cross-replica comparison after partition; reconciliation completion metrics; staleness monitoring"
  recovery: "Manual reconciliation; accept data loss from one side; application-level repair scripts"
  retryable: false
- name: staleness_amplification
  description: "A read chain amplifies staleness — each read in a multi-step operation reads from a different replica with progressively older data."
  likelihood: medium
  observable_evidence: "Application-level inconsistency that cannot be explained by single-operation staleness; user-visible anomalies in multi-step workflows"
  detection: "End-to-end tracing of multi-operation reads; consistency assertions at application level"
  recovery: "Pin reads to a single replica per request context; implement session-level read guarantees"
  retryable: false
- name: conflict_amplification
  description: "Frequent concurrent writes to the same key produce a high volume of conflicts that overwhelm the reconciliation system."
  likelihood: low
  observable_evidence: "Conflict resolution queue grows; reconciliation latency increases; some conflicts are dropped or merged incorrectly"
  detection: "Monitor conflict rate per key; alert on sustained high conflict rates"
  recovery: "Replicate less aggressively for hot keys; use stronger consistency for contended keys; redesign data model to reduce concurrent writes"
  retryable: true

## Observations
- observation: "Eventual consistency is the most common consistency model on the internet — DNS, CDNs, and social feeds all use it."
  confidence: high
  source: Systems architecture survey, production experience
- observation: "Most applications that claim to need strong consistency actually need read-your-writes consistency (session-level), not global linearisability."
  confidence: high
  source: Architecture review experience, application requirement analysis
- observation: "Conflict resolution is the most underestimated operational cost of eventual consistency — reconciliation logic is often designed after deployment."
  confidence: high
  source: Production incident analysis, architectural reviews

## Constraints
- constraint: "Eventual consistency provides no upper bound on staleness unless explicitly bounded by configuration or application logic."
  type: invariant
  scope: cross-system
- constraint: "Concurrent writes to the same key in different partitions will always produce conflicts that require resolution."
  type: invariant
  scope: cross-system

## Decision Factors
- factor: staleness_tolerance
  question: "How stale can data be before it causes user-visible or correctness problems?"
  supporting: "Content delivery, social feeds, analytics, and monitoring can tolerate seconds to minutes of staleness without issues."
  contradictory: "Financial transactions, inventory systems, and coordination services cannot tolerate any staleness."
  weight: high
- factor: conflict_handling_capacity
  question: "Can the application team implement and maintain conflict resolution logic?"
  supporting: "Teams with strong data modelling skills can implement application-level resolution for superior correctness."
  contradictory: "Last-write-wins is simpler but loses data; CRDTs are correct but limited to specific data structures and add complexity."
  weight: high
- factor: operational_complexity_budget
  question: "Does the team have the operational capacity to manage eventual consistency's reconciliation requirements?"
  supporting: "Well-resourced teams can manage the reconciliation overhead and build monitoring."
  contradictory: "Teams with limited operational capacity should prefer strong consistency (simpler operational model) or use managed services that abstract reconciliation."
  weight: medium

## Heuristics
- heuristic: "Use eventual consistency for data that has a bounded lifetime or where stale reads are acceptable."
  rationale: "Session data, cached content, and analytics have natural staleness bounds that align with eventual consistency."
  evidence_level: high
- heuristic: "Always implement read-your-writes guarantees at the session level — users expect to see their own writes reflected immediately."
  rationale: "Session-level consistency dramatically improves user experience without requiring global consistency."
  evidence_level: high
- heuristic: "Design conflict resolution before deployment — ad-hoc resolution under incident pressure produces incorrect results."
  rationale: "Conflict resolution requires domain knowledge and careful design; it cannot be implemented correctly during an incident."
  evidence_level: high

## Recommendations
- recommendation: "Never deploy eventually consistent systems without staleness monitoring — if you cannot measure staleness, you cannot reason about correctness."
  context: observability
  certainty: strong
  rationale: "Eventual consistency's unbounded staleness window is a correctness risk that requires active measurement."
- recommendation: "Use per-request consistency hints — allow reads to request stronger consistency when needed without making it the default."
  context: application_design
  certainty: strong
  rationale: "Per-request consistency gives applications the performance of eventual consistency with the option of strong consistency for critical operations."
- recommendation: "Test conflict resolution logic under concurrent write patterns that exceed expected production load."
  context: pre_production
  certainty: strong
  rationale: "Conflict resolution performance degrades under load; idle testing does not reveal merge throughput limitations."
