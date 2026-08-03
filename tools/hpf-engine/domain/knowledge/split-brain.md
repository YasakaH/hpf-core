# Split Brain

## Identity
- id: split-brain
- type: concept
- title: Split Brain
- tags: [distributed-systems, fault-tolerance, partition, consistency, consensus]
- entities: [split brain, network partition, quorum, inconsistency, divergent state]
- concepts: [quorum, leader-election, network-partition-recovery, raft-consensus]

## Claims
- claim: "Split brain occurs when a distributed system continues operating in two or more disconnected partitions, with each partition independently modifying state."
  certainty: high
  evidence: Distributed systems literature, production incident reports
  scope: cross-system
- claim: "Split brain is prevented by requiring quorum for writes — the minority partition cannot make progress because it cannot form quorum."
  certainty: high
  evidence: Distributed systems theory, Raft spec
  scope: quorum-based
- claim: "Systems without quorum-based write coordination (asynchronous replication, multi-master) are vulnerable to split brain during network partitions."
  certainty: high
  evidence: Production incident analysis, distributed systems literature
  scope: cross-system
- claim: "Split brain produces divergent state that requires reconciliation or manual resolution when partitions rejoin."
  certainty: high
  evidence: Production experience, operational literature
  scope: cross-system
- claim: "The duration of a split brain condition correlates with the volume of divergent state — longer partitions produce more divergence."
  certainty: high
  evidence: Operational experience, distributed systems literature
  scope: cross-system

## Relationships
- concept: quorum
  relationship: prevents
  description: "Quorum-based writes prevent split brain by ensuring only the partition with majority membership can accept writes."
- concept: leader-election
  relationship: vulnerable_to
  description: "Without quorum-based election, two partitions could each elect a leader, creating split brain."
- concept: network-partition-recovery
  relationship: causes
  description: "Network partitions are the root cause of split brain — the partition creates independent operational groups."
- concept: raft-consensus
  relationship: avoids
  description: "Raft prevents split brain by requiring quorum for both leader election and log commitment, ensuring at most one active leader."
- concept: cascading-failure
  relationship: worsens
  description: "Split brain can trigger cascading failures when rejoining partitions attempt to reconcile divergent state under load."

## Tradeoffs
- dimension: consistency_vs_availability_during_partition
  options:
    quorum_required:
      value: consistency
      rationale: "Minority partition halts writes — prevents divergence at cost of availability."
    multi_master:
      value: availability
      rationale: "All partitions accept writes — maintains availability but risks divergence that requires reconciliation."
  importance: high
- dimension: auto_reconciliation_vs_manual_resolution
  options:
    automatic:
      value: speed
      rationale: "Last-write-wins or timestamp-based merge resolves quickly but may lose data."
    manual:
      value: correctness
      rationale: "Human review ensures correct merge but extends recovery time and requires operational expertise."
  importance: operational

## Failure Modes
- name: silent_split_brain
  description: "System enters split brain without detection — both partitions continue operating, believing they have full authority."
  likelihood: medium
  observable_evidence: "Conflicting writes accepted in different partitions; clients observe inconsistent state; data integrity violations on rejoin"
  detection: "Heartbeat monitoring across all node pairs; quorum membership tracking; cross-partition state comparison after partition"
  recovery: "Designate authoritative partition via operator intervention; replay logs from authoritative side; manual reconciliation of divergent state"
  retryable: false
- name: unresolved_divergence
  description: "Partitions rejoin but divergent state cannot be automatically reconciled, requiring data loss or manual resolution."
  likelihood: medium
  observable_evidence: "Rejoin fails with conflict errors; reconciliation process stalls; data integrity checks fail"
  detection: "Monitor reconciliation success rate; alert on unresolved conflicts exceeding threshold"
  recovery: "Manual analysis of divergent state; application-level conflict resolution; acceptance of data loss in worst case"
  retryable: true
- name: split_brain_replication_storm
  description: "Rejoining partitions trigger a replication storm as divergent state is synchronised, overwhelming system capacity."
  likelihood: low
  observable_evidence: "Network saturation during rejoin; increased replication latency; secondary failures from resource exhaustion"
  detection: "Monitor network utilisation and replication queue depth during rejoin events"
  recovery: "Rate-limit reconciliation; prioritise critical data; schedule rejoin during low-load periods"
  retryable: false

## Observations
- observation: "Split brain is most dangerous in systems that lack detection — operators discover it through data integrity failures rather than direct monitoring."
  confidence: high
  source: Production incident analysis, post-mortems
- observation: "The majority of split brain incidents in production are caused by misconfiguration (incorrect quorum settings) rather than network partitions."
  confidence: medium
  source: Operational incident reviews
- observation: "Quorum-based systems are not immune to split brain — they prevent write-split-brain but read-split-brain can occur when followers serve stale data."
  confidence: medium
  source: Distributed systems analysis

## Constraints
- constraint: "In a system with N nodes, any partition with fewer than (N/2 + 1) nodes cannot make progress under quorum-based consistency."
  type: invariant
  scope: quorum-based
- constraint: "Split brain reconciliation requires a total order of operations across partitions — without it, conflict resolution is ambiguous."
  type: invariant
  scope: cross-system

## Heuristics
- heuristic: "Implement split brain detection at the application layer even when the consensus layer guarantees quorum safety."
  rationale: "Application-level detection catches misconfiguration and edge cases that consensus layer safety proofs may not cover."
  evidence_level: high
- heuristic: "Design reconciliation strategies before deployment — split brain is not the time to design conflict resolution."
  rationale: "Ad-hoc reconciliation under incident pressure increases error rate and recovery time."
  evidence_level: high
- heuristic: "Prefer systems with automatic split brain prevention (quorum-based) over detection-based approaches."
  rationale: "Prevention is more reliable than detection; detection systems have false negatives."
  evidence_level: high

## Recommendations
- recommendation: "Never deploy a distributed system without testing split brain behaviour under controlled partition conditions."
  context: pre_production
  certainty: strong
  rationale: "Split brain behaviour differs dramatically between theory and production — network characteristics and timing affect outcomes."
- recommendation: "Implement cross-datacenter quorum awareness to prevent split brain across geo-distributed deployments."
  context: architecture_design
  certainty: strong
  rationale: "Geo-distributed deployments add latency asymmetry that can trigger false partition detection and unintended split brain."
- recommendation: "Audit split brain detection and reconciliation procedures during each major deployment cycle."
  context: operations
  certainty: moderate
  rationale: "Configuration changes, topology changes, and version upgrades can alter split brain behaviour without obvious signals."
