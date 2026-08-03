# Strong Consistency

## Identity
- id: strong-consistency
- type: concept
- title: Strong Consistency
- tags: [distributed-systems, consistency, linearisability, correctness, transactions]
- entities: [strong consistency, linearisability, serialisability, read-after-write, quorum]
- concepts: [cap-theorem, eventual-consistency, availability, quorum, raft-consensus]

## Claims
- claim: "Strong consistency guarantees that every read returns the most recent write — all nodes agree on the order of operations."
  certainty: high
  evidence: Distributed systems literature, linearisability definition (Herlihy & Wing)
  scope: cross-system
- claim: "Linearisable consistency is the strongest form of strong consistency — operations appear to execute atomically at a single point between invocation and response."
  certainty: high
  evidence: Herlihy & Wing (1990), distributed systems literature
  scope: cross-system
- claim: "Strong consistency requires coordination between nodes — typically through quorum-based writes or consensus protocols."
  certainty: high
  evidence: Distributed systems literature
  scope: cross-system
- claim: "Strong consistency increases read and write latency because operations must wait for coordination to complete."
  certainty: high
  evidence: Distributed systems literature, production performance measurements
  scope: cross-system
- claim: "Strong consistency reduces availability during partitions because the minority partition cannot serve writes."
  certainty: high
  evidence: CAP theorem (Gilbert-Lynch), distributed systems literature
  scope: cross-system
- claim: "Strong consistency is not a single property — linearisability, sequential consistency, and causal consistency are distinct models with different guarantees."
  certainty: high
  evidence: Distributed systems literature, consistency model taxonomy
  scope: cross-system

## Relationships
- concept: cap-theorem
  relationship: constrained_by
  description: "CAP theorem constrains strong consistency — during a partition, strong consistency requires sacrificing availability."
- concept: eventual-consistency
  relationship: contrasts_with
  description: "Strong consistency guarantees immediate consistency; eventual consistency accepts temporary inconsistency in exchange for availability."
- concept: quorum
  relationship: requires
  description: "Strong consistency typically requires quorum-based writes (W > N/2) and quorum intersection for reads."
- concept: raft-consensus
  relationship: provides
  description: "Raft provides strong consistency for the replicated state machine — all nodes apply the same committed entries in order."
- concept: availability
  relationship: trades_off_against
  description: "Strong consistency trades availability for correctness — the system becomes unavailable for writes during partitions."

## Tradeoffs
- dimension: consistency_model_strength_vs_performance
  options:
    linearisable:
      value: strongest_guarantees
      rationale: "Every operation appears atomic — the highest correctness but requires the most coordination."
    sequential:
      value: balanced
      rationale: "Operations from each client appear in order — slightly relaxed for better performance."
    causal:
      value: performance_optimised
      rationale: "Causally related operations appear in order — higher throughput, suitable for many real-world workloads."
  importance: high
- dimension: read_consistency_overhead
  options:
    quorum_reads:
      value: strong_reads
      rationale: "Read from quorum to guarantee most recent write — higher read latency."
    leader_reads:
      value: leader_authority
      rationale: "Read from leader only — guaranteed consistency with single-node latency."
  importance: operational

## Failure Modes
- name: consistency_degradation
  description: "System degrades from strong consistency to a weaker model under load or partition without explicit operator awareness."
  likelihood: medium
  observable_evidence: "Reads return increasingly stale data; monitoring shows quorum size decreasing; reads redirected from leader to followers without notice"
  detection: "Monitor consistency model adherence; alert on read-source changes (leader → follower); track staleness metrics"
  recovery: "Restore quorum health; revert to strict leader reads; investigate root cause of degradation"
  retryable: true
- name: false_consistency
  description: "System claims strong consistency but implementation does not provide it — typically from misconfigured quorums or incorrect consistency mode."
  likelihood: medium
  observable_evidence: "Stale reads despite 'strongly consistent' configuration; read-after-write violations detected by application-level checks"
  detection: "Application-level read-after-write verification; consistency testing under concurrent access patterns"
  recovery: "Audit consistency configuration; verify quorum intersection (R + W > N); correct configuration or accept weaker model"
  retryable: false

## Observations
- observation: "Strong consistency is frequently claimed but infrequently verified — most 'strongly consistent' systems have edge cases that violate the guarantee."
  confidence: high
  source: Production architecture review, consistency testing experience
- observation: "The performance cost of strong consistency is overestimated — many workloads can tolerate the latency of quorum-based coordination."
  confidence: medium
  source: Performance benchmarking, production measurements
- observation: "Most applications do not need linearisability — causal consistency or read-after-write per session is sufficient."
  confidence: high
  source: Distributed systems literature, application requirement analysis

## Constraints
- constraint: "Strongly consistent reads require quorum intersection (R + W > N) or leader-based reads — otherwise consistency is not guaranteed."
  type: invariant
  scope: configurable
- constraint: "Strong consistency cannot be maintained during a network partition — the system must either stall (unavailable) or relax consistency."
  type: invariant
  scope: distributed-stateful

## Decision Factors
- factor: correctness_requirement
  question: "Does the application have correctness requirements that depend on immediate consistency?"
  supporting: "Financial transactions, inventory systems, and coordination services require strong consistency to function correctly."
  contradictory: "Content delivery, social feeds, and analytics tolerate eventual consistency without user-visible effects."
  weight: high
- factor: read_write_ratio
  question: "What is the ratio of reads to writes?"
  supporting: "Read-heavy workloads benefit from strong consistency because the coordination cost is amortised across many reads."
  contradictory: "Write-heavy workloads pay the coordination cost on every write, making strong consistency more expensive relative to weaker models."
  weight: medium
- factor: consistency_explicit
  question: "Does the consistency model need to be explicit and verifiable, or can it be probabilistic?"
  supporting: "Regulatory and auditing requirements often demand explicit consistency guarantees that can be verified."
  contradictory: "Many internal-facing systems can operate with probabilistic consistency guarantees verified through application-level checks."
  weight: high

## Heuristics
- heuristic: "Use strong consistency for coordination and metadata; use weaker consistency for user-facing read-heavy content."
  rationale: "Coordination services (locks, config, service discovery) require strong consistency; user-facing content can tolerate bounded staleness."
  evidence_level: high
- heuristic: "Verify consistency guarantees under concurrent access patterns — single-threaded testing does not surface consistency violations."
  rationale: "Consistency violations only appear under true concurrency; single-threaded tests mask them."
  evidence_level: high

## Recommendations
- recommendation: "Default to strong consistency for system-of-record data; relax only when performance requirements cannot otherwise be met."
  context: architecture_design
  certainty: strong
  rationale: "Strong consistency simplifies application logic; relaxing consistency should be a deliberate optimisation, not a default."
- recommendation: "Instrument consistency verification at the application layer — do not rely solely on the data store's consistency claims."
  context: observability
  certainty: strong
  rationale: "Data store consistency guarantees apply to single operations; application-level consistency (across multiple operations) must be verified independently."
- recommendation: "Document the chosen consistency model and its limitations explicitly — future maintainers need to know what guarantees they can rely on."
  context: architecture_documentation
  certainty: strong
  rationale: "Undocumented consistency assumptions are the leading cause of correctness failures in system migrations and upgrades."
