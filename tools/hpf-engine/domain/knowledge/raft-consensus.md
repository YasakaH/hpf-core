# Raft Consensus

## Identity
- id: raft-consensus
- type: concept
- title: Raft Consensus
- tags: [distributed-systems, consensus, raft, replication, fault-tolerance, log-replication]
- entities: [raft, consensus, log replication, committed entry, term, log index, state machine]
- concepts: [quorum, leader-election, split-brain, network-partition-recovery]

## Claims
- claim: "Raft is a consensus algorithm that ensures all non-faulty nodes agree on the same sequence of log entries."
  certainty: high
  evidence: Raft dissertation (Ongaro), Raft spec
  scope: raft-specific
- claim: "Raft operates through three core subsystems: leader election, log replication, and safety guarantees."
  certainty: high
  evidence: Raft dissertation (Ongaro)
  scope: raft-specific
- claim: "Log entries flow from leader to followers — the leader accepts client requests and appends them to its local log before replicating."
  certainty: high
  evidence: Raft spec
  scope: raft-specific
- claim: "A log entry is committed when the leader has replicated it to a quorum of nodes — committed entries are durable and applied in order."
  certainty: high
  evidence: Raft spec
  scope: raft-specific
- claim: "Raft guarantees that committed entries are never lost and are applied in the same order on all nodes."
  certainty: high
  evidence: Raft spec, safety proof
  scope: raft-specific
- claim: "Raft restricts log writing to a single leader per term — only the leader decides what entries to append."
  certainty: high
  evidence: Raft spec
  scope: raft-specific
- claim: "The Raft safety property guarantees that if two logs contain the same entry at the same index, all prior entries are identical."
  certainty: high
  evidence: Raft spec, safety proof
  scope: raft-specific
- claim: "Raft's election restriction ensures a candidate can only win an election if its log is at least as up-to-date as a quorum of nodes — this prevents a stale leader from overwriting committed entries."
  certainty: high
  evidence: Raft dissertation (Ongaro)
  scope: raft-specific

## Relationships
- concept: quorum
  relationship: requires
  description: "Raft uses quorum for both leader election (quorum of votes) and log commitment (quorum of replicas)."
- concept: leader-election
  relationship: includes
  description: "Raft includes leader election as one of its three core subsystems."
- concept: split-brain
  relationship: prevents
  description: "Raft's single-leader and quorum-based commitment prevent split-brain — two leaders cannot coexist in the same term."
- concept: network-partition-recovery
  relationship: survives
  description: "Raft survives network partitions: the majority-side partition elects a leader and continues; the minority side stalls but re-joins safely."
- concept: cascading-failure
  relationship: vulnerable_to
  description: "Raft clusters under resource pressure can enter cascading leader-election loops when heartbeats are delayed by saturation."
- concept: circuit-breaker
  relationship: similar_to
  description: "Raft's leader-based model shares architectural assumptions with circuit breaker state management — both rely on single coordinators with failover."

## Tradeoffs
- dimension: consistency_vs_performance
  options:
    synchronous_replication:
      value: strong_consistency
      rationale: "Leader waits for quorum acknowledgement before responding to client — higher latency, guaranteed linearisability."
    asynchronous_replication:
      value: lower_latency
      rationale: "Leader responds before quorum acknowledgement — faster but can lose uncommitted entries on leader failure."
  importance: high
- dimension: cluster_size_vs_overhead
  options:
    three_nodes:
      value: minimal_overhead
      rationale: "Quorum = 2, tolerates 1 failure. Minimal network traffic but low fault tolerance."
    five_nodes:
      value: balanced
      rationale: "Quorum = 3, tolerates 2 failures. Standard production configuration."
    seven_nodes:
      value: high_tolerance
      rationale: "Quorum = 4, tolerates 3 failures. Increased replication overhead and election latency."
  importance: high
- dimension: read_consistency
  options:
    leader_reads:
      value: strong_consistency
      rationale: "All reads go through leader — guarantees linearisability but concentrates load on leader."
    follower_reads:
      value: read_scaling
      rationale: "Followers serve reads — distributes load but may return stale data if follower is behind."
  importance: operational

## Failure Modes
- name: leader_failure_no_quorum
  description: "Leader fails and remaining nodes cannot form quorum for election."
  likelihood: medium
  observable_evidence: "All nodes in candidate state; term spiking; no committed entries; cluster unavailable for writes"
  detection: "Monitor active node count; alert when below quorum threshold"
  recovery: "Restore failed leader; add new nodes; manual intervention for permanent quorum loss"
  retryable: true
- name: log_inconsistency_after_rejoin
  description: "Partitioned node re-joins with conflicting log entries that must be overwritten."
  likelihood: medium
  observable_evidence: "Re-joining node has log entries at higher term but lower index than leader; entries are truncated and replaced"
  detection: "Normal Raft behaviour — not an error condition; monitor log mismatch metrics"
  recovery: "Automatic — Raft's log matching property ensures convergence without manual intervention"
  retryable: true
- name: cascading_election_under_load
  description: "High resource utilisation delays heartbeats, triggering false elections that consume more resources."
  likelihood: medium
  observable_evidence: "CPU saturation correlates with repeated elections; cluster cycles through leaders; write throughput collapses"
  detection: "Correlate resource utilisation with election events; alert on election frequency exceeding threshold"
  recovery: "Add capacity; reduce request rate; adjust election timeout; consider priority scheduling for Raft RPCs"
  retryable: true
- name: unbounded_log_growth
  description: "Log grows without compaction, eventually exhausting disk or causing excessive replication latency."
  likelihood: medium
  observable_evidence: "Increasing replication latency; disk utilisation growth; slow node recovery after restart"
  detection: "Monitor log size per node; alert on growth rate exceeding compaction throughput"
  recovery: "Enable snapshotting (log compaction); increase compaction frequency; add disk capacity"
  retryable: false

## Observations
- observation: "Raft's understandability-oriented design (decomposition into leader election, log replication, safety) maps naturally to independent knowledge objects."
  confidence: high
  source: Raft dissertation (Ongaro), authoring observation
- observation: "In production, Raft's most common failure mode is cascading elections under load, not data loss."
  confidence: high
  source: Operational incident reviews, etcd and Consul deployment experience
- observation: "Raft's leader-based design is a single point of bottleneck — the leader handles all writes and consistent reads."
  confidence: high
  source: Raft spec, performance analysis
- observation: "Read-only operations can be scaled by using follower reads with periodic leader verification, at the cost of potential staleness."
  confidence: high
  source: Raft spec, production patterns

## Constraints
- constraint: "Only one leader may exist per term — enforced by quorum-based election, not by mutual exclusion primitives."
  type: invariant
  scope: raft-specific
- constraint: "Committed entries are never lost — once an entry reaches quorum, it is durable regardless of subsequent leader changes."
  type: invariant
  scope: raft-specific
- constraint: "Log entries are committed in order — entry at index I is committed only after all entries with lower index are committed."
  type: invariant
  scope: raft-specific
- constraint: "A candidate cannot become leader unless its log is at least as up-to-date as a quorum of nodes."
  type: invariant
  scope: raft-specific

## Heuristics
- heuristic: "Use Raft for strongly consistent replicated state machines (configuration stores, coordination services)."
  rationale: "Raft provides linearisable writes and a well-understood safety model."
  evidence_level: high
- heuristic: "Monitor the Raft leader's sustained RPC rate as a capacity planning signal."
  rationale: "Leader RPC rate directly correlates with write throughput and is the primary bottleneck."
  evidence_level: high
- heuristic: "Enable read-only follower serving for workloads where near-consistent reads are acceptable."
  rationale: "Follower reads distribute load away from leader without adding significant staleness."
  evidence_level: moderate
- heuristic: "Snapshot frequently enough that log replay after restart takes seconds, not minutes."
  rationale: "Slow recovery extends failure windows and increases vulnerability to cascading failures."
  evidence_level: high

## Recommendations
- recommendation: "Always run Raft clusters in odd-numbered configurations (3, 5, or 7 nodes)."
  context: cluster_design
  certainty: strong
  rationale: "Even-numbered clusters provide no additional fault tolerance — 4 nodes tolerate 1 failure, same as 3 nodes."
- recommendation: "Implement leader-based read isolation at the application level to guarantee linearisable reads."
  context: application_design
  certainty: strong
  rationale: "Follower reads can return stale data; leader reads guarantee the most recent committed state."
- recommendation: "Pre-allocate and monitor disk space for Raft logs to prevent unbounded-growth-induced failures."
  context: production_operations
  certainty: strong
  rationale: "Exhausted disk causes leader to stall, triggering elections and potentially cascading across the cluster."
- recommendation: "Test Raft cluster behaviour under network latency variation during pre-production validation."
  context: pre_production_testing
  certainty: moderate
  rationale: "Raft's heartbeat-based failure detection is sensitive to latency spikes — test with injected delay to surface election instability."
