# Network Partition Recovery

## Identity
- id: network-partition-recovery
- type: pattern
- title: Network Partition Recovery
- tags: [distributed-systems, partition, recovery, reconciliation, operational, resilience]
- entities: [network partition, partition recovery, reconciliation, split brain, heal, rejoin]
- concepts: [split-brain, raft-consensus, cap-theorem, eventual-consistency, quorum, cascading-failure]

## Claims
- claim: "Network partition recovery is the process of detecting that a partition has resolved, reconnecting separated nodes, and reconciling any state that diverged during the partition."
  certainty: high
  evidence: Distributed systems literature, production operational experience
  scope: cross-system
- claim: "The duration of a partition directly affects recovery complexity — longer partitions produce more divergent state and higher reconciliation cost."
  certainty: high
  evidence: Production incident analysis, distributed systems literature
  scope: cross-system
- claim: "Recovery from a partition requires three phases: detection (partition healed), stabilisation (nodes rejoin safely), and reconciliation (divergent state resolved)."
  certainty: high
  evidence: Operational experience, distributed systems literature
  scope: cross-system
- claim: "In quorum-based systems, recovery is simpler because the minority partition could not make progress — only the majority side has authoritative state."
  certainty: high
  evidence: Raft spec, distributed systems theory
  scope: quorum-based
- claim: "In availability-preferring systems, recovery requires conflict resolution because both partitions accepted writes."
  certainty: high
  evidence: Dynamo paper, eventual consistency literature
  scope: availability-oriented

## Relationships
- concept: split-brain
  relationship: resolves
  description: "Partition recovery must detect and resolve split-brain conditions when partitions rejoin."
- concept: raft-consensus
  relationship: simplifies
  description: "Raft simplifies partition recovery because only the majority partition has committed entries — the minority partition's state is overwritten on rejoin."
- concept: cap-theorem
  relationship: determines
  description: "CAP theorem determines the recovery strategy — consistency-preferring systems recover differently from availability-preferring systems."
- concept: eventual-consistency
  relationship: requires
  description: "Eventually consistent systems require reconciliation logic during partition recovery to resolve divergent state."
- concept: quorum
  relationship: affects
  description: "Quorum configuration determines which side of a partition has authoritative state — the majority side's state wins on recovery."
- concept: cascading-failure
  relationship: risk_during
  description: "Partition recovery can trigger cascading failures if rejoining nodes create load spikes through state synchronisation."

## Tradeoffs
- dimension: recovery_speed_vs_data_integrity
  options:
    fast_recovery:
      value: quick_restoration
      rationale: "Accept last-write-wins or majority-side state to recover quickly — faster but may lose minority-side writes."
    integrity_first:
      value: data_preservation
      rationale: "Analyse divergent state manually or through application-level reconciliation — preserves data but extends recovery time."
  importance: high
- dimension: automated_vs_manual_recovery
  options:
    fully_automated:
      value: speed
      rationale: "System detects partition heal and initiates recovery automatically — faster but risks incorrect reconciliation."
    operator_approved:
      value: control
      rationale: "Operator validates partition heal and approves recovery — slower but provides human judgement for edge cases."
  importance: operational

## Failure Modes
- name: recovery_storm
  description: "Rejoining nodes trigger a load storm as they synchronise state, overwhelming the cluster and causing secondary failures."
  likelihood: high
  observable_evidence: "Network saturation spikes during rejoin; CPU utilisation surges; replication queue depth grows; secondary component failures"
  detection: "Monitor network utilisation and replication metrics during rejoin; alert on utilisation exceeding pre-partition baseline"
  recovery: "Rate-limit replication; prioritise critical data streams; rejoin nodes incrementally rather than simultaneously"
  retryable: true
- name: oscillation_rejoin
  description: "Nodes rejoin, trigger instability, disconnect again, and repeat — creating a cycle of partition and recovery."
  likelihood: medium
  observable_evidence: "Repeated join-leave cycles for the same node; cluster membership flapping; intermittent availability degradation"
  detection: "Monitor node rejoin frequency; flag nodes with N rejoin events within time window"
  recovery: "Temporarily ban flapping node; investigate root cause of disconnection; verify network stability and configuration"
  retryable: true
- name: unreconciled_divergence
  description: "Reconciliation completes with undetected divergence — the system believes state is consistent but it is not."
  likelihood: low
  observable_evidence: "Data integrity violations surface after recovery; cross-replica comparison reveals mismatches"
  detection: "Post-recovery data integrity audit; checksum verification across replicas"
  recovery: "Identify divergence boundary; restore from authoritative backup; replay lost writes from application logs"
  retryable: false

## Observations
- observation: "Most partition recovery incidents take longer than the partition itself — recovery complexity dominates total partition impact."
  confidence: high
  source: Production incident analysis, operational experience
- observation: "Automated partition recovery is the norm in consensus-based systems; manual recovery is more common in eventually consistent systems."
  confidence: high
  source: Production architecture survey
- observation: "Partition recovery testing is the least-tested failure mode in distributed systems — most teams test partition detection but not recovery."
  confidence: high
  source: Chaos engineering survey, production experience

## Constraints
- constraint: "Recovery cannot begin until partition detection is confirmed — premature recovery attempts fail or cause oscillation."
  type: operational
  scope: cross-system
- constraint: "Reconciliation is bounded by the size of divergent state — longer partitions produce more divergence and longer recovery."
  type: invariant
  scope: cross-system

## Decision Factors
- factor: consistency_model_during_partition
  question: "Did the system sacrifice consistency or availability during the partition?"
  supporting: "Consistency-sacrificing systems (availability-preferring) require reconciliation — the recovery strategy must include conflict resolution."
  contradictory: "Availability-sacrificing systems (consistency-preferring) have a single authoritative state — recovery is simpler but must handle the write loss."
  weight: high
- factor: recovery_time_objective
  question: "What is the maximum acceptable time for partition recovery?"
  supporting: "Tight RTO justifies automated recovery with last-write-wins reconciliation, accepting potential data loss."
  contradictory: "Relaxed RTO allows manual reconciliation with full data preservation, at the cost of extended recovery duration."
  weight: high
- factor: state_volume
  question: "How much state diverged during the partition?"
  supporting: "Low divergence volumes can be reconciled quickly through automated mechanisms."
  contradictory: "High divergence volumes require rate-limited reconciliation and may need operator intervention."
  weight: medium

## Heuristics
- heuristic: "Test partition recovery under production-scale data volumes — recovery behaviour differs dramatically between test and production data sizes."
  rationale: "Reconciliation algorithms that work with small test datasets may not complete in acceptable time at production scale."
  evidence_level: high
- heuristic: "Implement partition detection at multiple levels (network, application, consensus) to reduce false positives."
  rationale: "Single-level detection can trigger false partition declarations from transient network issues, causing unnecessary recovery."
  evidence_level: high
- heuristic: "Design recovery to be incremental — recover critical data first, then backfill less critical state."
  rationale: "Incremental recovery reduces time-to-partial-recovery and prevents recovery storms."
  evidence_level: high

## Recommendations
- recommendation: "Define and document partition recovery procedures before deployment — designing recovery under incident pressure produces incorrect procedures."
  context: operations
  certainty: strong
  rationale: "Partition recovery requires coordinated action across multiple systems; ad-hoc recovery introduces coordination failures."
- recommendation: "Automate partition detection but require operator approval for recovery initiation in systems with manual reconciliation requirements."
  context: operations
  certainty: strong
  rationale: "Fully automated recovery can make things worse if the partition was caused by a misconfiguration that automated recovery will repeat."
- recommendation: "Run partition recovery drills quarterly — recovery procedures that are never exercised will fail when first attempted under incident conditions."
  context: reliability
  certainty: strong
  rationale: "Untested recovery procedures have a high failure rate; regular drills build operator familiarity and surface procedure gaps."
