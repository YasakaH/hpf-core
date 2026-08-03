# Quorum

## Identity
- id: quorum
- type: concept
- title: Quorum
- tags: [distributed-systems, consensus, fault-tolerance, availability, coordination]
- entities: [quorum, majority, consensus, fault tolerance, availability, intersection property]
- concepts: [leader-election, raft-consensus]

## Claims
- claim: "A quorum is the minimum number of nodes that must agree on a value for a distributed system to make progress."
  certainty: high
  evidence: Distributed systems literature (Lamport, Fischer-Lynch-Paterson)
  scope: cross-system
- claim: "A simple majority quorum requires more than N/2 nodes, where N is the total number of nodes."
  certainty: high
  evidence: Distributed systems literature
  scope: cross-system
- claim: "Quorum intersection property — any two quorums must share at least one node — ensures consistency across reads and writes."
  certainty: high
  evidence: Distributed systems literature
  scope: cross-system
- claim: "Read and write quorums can be configured independently as long as they intersect."
  certainty: high
  evidence: Dynamo paper, Cassandra documentation
  scope: configurable
- claim: "Without a quorum, the system cannot make progress — writes fail, elections stall, and state cannot be advanced."
  certainty: high
  evidence: Distributed systems literature, production experience
  scope: cross-system
- claim: "Larger quorums increase fault tolerance but reduce availability because more nodes must respond."
  certainty: high
  evidence: CAP theorem literature
  scope: cross-system
- claim: "A system cannot simultaneously tolerate N node failures and require (N+1)-node quorums — these constraints are incompatible."
  certainty: high
  evidence: FLP impossibility result, distributed systems theory
  scope: cross-system

## Relationships
- concept: leader-election
  relationship: required_by
  description: "Leader election requires quorum to select a leader — a candidate must receive votes from a majority of nodes."
- concept: raft-consensus
  relationship: required_by
  description: "Raft uses quorum for both leader election and log entry commitment."
- concept: network-partition-recovery
  relationship: affects
  description: "Network partitions split quorums — the minority side cannot make progress, which is a feature, not a bug."
- concept: eventual-consistency
  relationship: contrasts_with
  description: "Quorum-based systems favour strong consistency by requiring intersection; eventually consistent systems relax this requirement."

## Tradeoffs
- dimension: quorum_size_vs_availability
  options:
    majority:
      value: fault_tolerance
      rationale: "Tolerates up to (N/2 - 1) failures; requires (N/2 + 1) nodes to respond."
    supermajority:
      value: safety_margin
      rationale: "Larger quorum (e.g. 2N/3) tolerates fewer failures but provides stronger guarantees under Byzantine conditions."
    one_node:
      value: maximum_availability
      rationale: "Single-node quorum is always available but provides no fault tolerance."
  importance: high
- dimension: read_write_quorum
  options:
    write_all_read_one:
      value: read_optimised
      rationale: "Fast reads (single node); slow writes (all nodes). Used in some replicated databases."
    quorum_read_quorum_write:
      value: balanced
      rationale: "Read and write both require (N/2 + 1) — standard quorum intersection approach."
  importance: operational

## Failure Modes
- name: quorum_loss
  description: "Network partition or node failures prevent reaching quorum size."
  likelihood: medium
  observable_evidence: "Writes timeout with 'unable to reach quorum' errors; leader election cannot complete"
  detection: "Monitor active node count against quorum threshold; alert when available nodes approach quorum minimum"
  recovery: "Restore partitioned nodes; allow automatic rejoin; manual intervention if partition is permanent"
  retryable: true
- name: partial_quorum_inconsistency
  description: "Misconfigured read and write quorums that do not intersect, allowing stale reads."
  likelihood: low
  observable_evidence: "Reads return outdated data; stale reads follow a pattern observable under specific quorum configurations"
  detection: "Verify quorum configuration: read_quorum + write_quorum must exceed N"
  recovery: "Reconfigure to enforce intersection property (read_quorum + write_quorum > N)"
  retryable: false
- name: quorum_flapping
  description: "Nodes oscillate in and out of reachability, repeatedly crossing the quorum threshold."
  likelihood: low
  observable_evidence: "Intermittent progress, repeated leader elections, unstable commit status"
  detection: "Track quorum member count over time; flag repeated crossings of threshold"
  recovery: "Stabilise network; increase timeout thresholds; remove flapping node from cluster temporarily"
  retryable: true

## Observations
- observation: "In practice, most production systems use a 3- or 5-node configuration where quorum is 2 or 3 respectively."
  confidence: high
  source: Production deployment patterns, operational literature
- observation: "Quorum loss is the most common cause of write unavailability in quorum-based systems, not node failure."
  confidence: medium
  source: Production incident analysis, operational experience
- observation: "Elastic quorum adjustments (reducing quorum size when nodes are lost) can prevent availability loss but risk consistency violations."
  confidence: medium
  source: Distributed systems research literature

## Constraints
- constraint: "A system with quorum size Q can tolerate at most (N - Q) simultaneous failures."
  type: invariant
  scope: cross-system
- constraint: "Read and write quorums must satisfy R + W > N to guarantee read-after-write consistency."
  type: invariant
  scope: configurable

## Heuristics
- heuristic: "Use 3 nodes as the minimum cluster size — 2 nodes cannot form a majority in the event of any single failure."
  rationale: "With 2 nodes, quorum = 2; losing either node means quorum loss."
  evidence_level: high
- heuristic: "Configure write quorum = majority and read quorum = majority for strong consistency."
  rationale: "This guarantees quorum intersection for consistent reads."
  evidence_level: high
- heuristic: "Use read quorum = 1 only when eventual consistency is acceptable and stale reads have bounded impact."
  rationale: "Read quorum of 1 provides maximum read availability but can return stale results."
  evidence_level: high

## Recommendations
- recommendation: "Always verify quorum intersection property when configuring read and write quorums independently."
  context: cluster_configuration
  certainty: strong
  rationale: "Non-intersecting quorums silently produce stale reads — a correctness failure that operational monitoring may not catch."
- recommendation: "Set monitoring alerts at 2 * quorum_size available nodes, not at quorum_size."
  context: production_operations
  certainty: strong
  rationale: "Reacting at quorum threshold means the system can already lose availability on one more failure."
- recommendation: "Use odd-numbered clusters (3, 5, 7) to maximise the fault-tolerance-to-node ratio."
  context: cluster_design
  certainty: strong
  rationale: "An even-sized cluster uses more nodes for the same quorum size — 4 nodes tolerate 1 failure, same as 3 nodes."
