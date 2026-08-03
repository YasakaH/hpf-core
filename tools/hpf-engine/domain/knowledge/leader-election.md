# Leader Election

## Identity
- id: leader-election
- type: concept
- title: Leader Election
- tags: [distributed-systems, consensus, coordination, raft, fault-tolerance]
- entities: [leader election, leader, term, heartbeat, request-vote, candidate]
- concepts: [quorum, raft-consensus, split-brain]

## Claims
- claim: "Leader election selects a single node to coordinate decisions in a distributed system — without it, competing nodes cannot converge."
  certainty: high
  evidence: Distributed systems literature, Raft dissertation (Ongaro)
  scope: cross-system
- claim: "In Raft, leader election uses a request-vote mechanism: candidates request votes from all nodes and win if they receive a quorum."
  certainty: high
  evidence: Raft dissertation (Ongaro), Raft spec
  scope: raft-specific
- claim: "Every leader election is associated with a strictly increasing term number — terms act as a logical clock for leadership epoch."
  certainty: high
  evidence: Raft dissertation (Ongaro)
  scope: raft-specific
- claim: "Nodes vote for at most one candidate per term on a first-come-first-served basis."
  certainty: high
  evidence: Raft spec
  scope: raft-specific
- claim: "Heartbeats maintain leader authority — followers reset their election timeout on receiving a heartbeat from the current leader."
  certainty: high
  evidence: Raft spec, distributed systems literature
  scope: cross-system
- claim: "Election timeout is randomised across nodes (typically 150-300ms) to reduce the probability of simultaneous candidate announcements."
  certainty: high
  evidence: Raft dissertation (Ongaro)
  scope: raft-specific
- claim: "A leader continuously asserts authority through periodic heartbeats — silence triggers a new election."
  certainty: high
  evidence: Raft spec, distributed systems literature
  scope: cross-system
- claim: "Split-brain — the condition where two nodes both believe they are leader — is prevented by quorum-based election."
  certainty: high
  evidence: Distributed systems theory, Raft spec
  scope: cross-system

## Relationships
- concept: quorum
  relationship: requires
  description: "Leader election requires quorum — a candidate must receive votes from a majority of nodes to become leader."
- concept: raft-consensus
  relationship: part_of
  description: "Leader election is one of the three core subsystems of Raft (leader election, log replication, safety)."
- concept: split-brain
  relationship: prevents
  description: "Quorum-based election prevents split-brain by ensuring only one candidate can win a given term."
- concept: network-partition-recovery
  relationship: affects
  description: "During a partition, the majority side can elect a leader; the minority side cannot — this prevents split-brain."
- concept: cascading-failure
  relationship: triggers
  description: "Repeated leader elections under load can amplify into cascading failures as heartbeats are delayed by resource exhaustion."

## Tradeoffs
- dimension: election_timeout_vs_responsiveness
  options:
    short_timeout:
      value: fast_failover
      rationale: "System detects leader failure quickly but triggers more false elections under transient network delay."
    long_timeout:
      value: stability
      rationale: "Fewer false elections but slower recovery when leader actually fails."
  importance: operational
- dimension: leader_stability_vs_load_balancing
  options:
    stable_leader:
      value: predictable_performance
      rationale: "Single leader accumulates state and cache affinity; avoids election overhead."
    periodic_re_election:
      value: load_distribution
      rationale: "Different leaders distribute write load but at the cost of election overhead and potential instability."
  importance: medium

## Failure Modes
- name: election_timeout_starvation
  description: "Repeated elections fail because no candidate can reach quorum within timeout windows."
  likelihood: medium
  observable_evidence: "Cluster in constant election state; term number increases rapidly without a stable leader; no writes commit"
  detection: "Track election events per unit time; alert on sustained election state beyond expected duration"
  recovery: "Check quorum health; restore partitioned nodes; verify network stability; reduce election timeout if too aggressive"
  retryable: true
- name: leader_loop
  description: "Leader is elected but rapidly loses authority due to flapping heartbeats, triggering continuous re-election."
  likelihood: low
  observable_evidence: "Alternating leaders across short time windows; unstable term progression; intermittent commit activity"
  detection: "Monitor leader changes over time; flag if leadership changes more than N times per minute"
  recovery: "Stabilise network; adjust heartbeat interval; investigate node-specific timing issues"
  retryable: true
- name: stale_leader
  description: "A partitioned leader continues to accept requests while unable to commit, then re-joins and serves stale state."
  likelihood: low
  observable_evidence: "Leader accepts writes during partition; after rejoin, clients receive redirected reads with outdated data"
  detection: "Track epoch/term on client side; verify leader identity before accepting writes"
  recovery: "Leader steps down on partition detection; clients reconnect and discover new leader; stale leader is corrected by log replication"
  retryable: false

## Observations
- observation: "In practice, leader election is the most common source of instability in Raft clusters, not log replication."
  confidence: high
  source: Production operational experience, cluster incident analysis
- observation: "Randomised election timeouts are effective — production clusters rarely experience split elections despite theoretical possibility."
  confidence: high
  source: Raft deployment experience, empirical observation
- observation: "Leader election is often the bottleneck for cluster recovery time after a failure — not data recovery."
  confidence: medium
  source: Production post-mortems, operational literature

## Constraints
- constraint: "At most one leader can exist per term — this is enforced by the quorum requirement, not by mutual exclusion."
  type: invariant
  scope: cross-system
- constraint: "A candidate cannot vote for itself and must request votes from other nodes — a leader cannot be elected without external agreement."
  type: invariant
  scope: raft-specific
- constraint: "Election timeout must be greater than heartbeat interval to prevent premature elections."
  type: operational
  scope: raft-specific
- constraint: "Clock skew between nodes must be bounded — excessive skew breaks timeout-based election logic."
  type: operational
  scope: cross-system

## Heuristics
- heuristic: "Set election timeout base to 2x the maximum expected network round-trip time."
  rationale: "This prevents transient network delay from triggering false elections."
  evidence_level: high
- heuristic: "Monitor election rate as a health signal — even occasional elections indicate network or node instability."
  rationale: "A healthy cluster should have zero elections over long periods."
  evidence_level: high
- heuristic: "Prefer stable leaders over rebalancing — election overhead costs more than uneven load distribution."
  rationale: "Elections block writes, increase latency, and risk cascading failures."
  evidence_level: moderate

## Recommendations
- recommendation: "Never deploy a single-leader distributed system without monitoring the election rate."
  context: production_operations
  certainty: strong
  rationale: "Election rate is the earliest indicator of cluster instability — it precedes data loss, split-brain, and availability failures."
- recommendation: "Set up pre-emptive alerts at 1 election event — the first election may indicate a pattern."
  context: production_monitoring
  certainty: strong
  rationale: "In healthy clusters, elections are rare events. A single election is worth investigating."
- recommendation: "Test leader election under load before production deployment — election timeouts behave differently under resource contention."
  context: pre_production
  certainty: strong
  rationale: "CPU saturation and network congestion increase heartbeat latency, which can trigger false elections that don't appear in idle testing."
