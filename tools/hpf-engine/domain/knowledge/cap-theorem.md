# CAP Theorem

## Identity
- id: cap-theorem
- type: principle
- title: CAP Theorem
- tags: [distributed-systems, consistency, availability, partition-tolerance, trade-off, architecture]
- entities: [cap theorem, consistency, availability, partition tolerance, brewer's theorem, distributed trade-offs]
- concepts: [eventual-consistency, strong-consistency, availability, quorum, network-partition-recovery]

## Claims
- claim: "CAP theorem states that a distributed data store can simultaneously provide at most two of three guarantees: Consistency, Availability, and Partition Tolerance."
  certainty: high
  evidence: Brewer's conjecture (2000), Gilbert-Lynch proof (2002)
  scope: cross-system
- claim: "During a network partition, a distributed system must choose between consistency (return an error or timeout) and availability (return potentially stale data)."
  certainty: high
  evidence: Gilbert-Lynch proof
  scope: cross-system
- claim: "CAP theorem is often misinterpreted as 'choose 2 of 3 at all times' — the choice only applies during partitions; outside partitions, all three can be provided."
  certainty: high
  evidence: Distributed systems literature, Brewer's clarifications
  scope: cross-system
- claim: "Partition Tolerance is not a choice — distributed systems over a network must tolerate partitions because networks can fail."
  certainty: high
  evidence: Gilbert-Lynch proof, distributed systems literature
  scope: cross-system
- claim: "The real CAP trade-off is not 'pick two' but 'how to behave during a partition': reduce consistency or reduce availability."
  certainty: high
  evidence: Distributed systems literature, operational experience
  scope: cross-system
- claim: "CAP applies to state, not computation — stateless services are not constrained by CAP."
  certainty: high
  evidence: Distributed systems theory
  scope: cross-system

## Relationships
- concept: eventual-consistency
  relationship: explains
  description: "CAP theorem explains why eventually consistent systems exist — they choose availability over consistency during partitions."
- concept: strong-consistency
  relationship: explains
  description: "CAP theorem frames the trade-off that strongly consistent systems accept: lower availability during partitions in exchange for correctness."
- concept: availability
  relationship: frames
  description: "CAP theorem frames availability as a design choice rather than a binary property — systems can choose different availability behaviours during partitions."
- concept: quorum
  relationship: constrains
  description: "CAP theorem constrains quorum design — quorum-based systems choose consistency (require quorum for writes) at the cost of availability during partition."
- concept: network-partition-recovery
  relationship: relevant_to
  description: "CAP theorem defines the design space for partition recovery — the choice between consistency and availability determines recovery strategy."

## Tradeoffs
- dimension: consistency_vs_availability_during_partition
  options:
    prefer_consistency:
      value: correctness
      rationale: "Return errors during partitions to prevent stale reads and conflicting writes. Suitable for financial transactions, inventory systems."
    prefer_availability:
      value: uptime
      rationale: "Accept potentially stale data during partitions to maintain service. Suitable for content delivery, social feeds."
  importance: high
- dimension: cap_interpretation
  options:
    strict_cp:
      value: theoretical_purity
      rationale: "Treat CAP as a rigid constraint — always enforce consistency, accept partitions will reduce availability."
    pragmatic_cp:
      value: operational_reality
      rationale: "Recognise that partition duration is bounded — brief inconsistency during a partition window is acceptable for many workloads."
  importance: medium

## Failure Modes
- name: cap_misapplication
  description: "CAP theorem is applied where it does not apply — typically to stateless services or single-node systems."
  likelihood: high
  observable_evidence: "Architecture decisions justified by CAP theorem for non-distributed state or stateless services; CAP mentioned in design reviews for inappropriate contexts"
  detection: "Review architecture documentation for CAP references; verify that the system is actually a distributed stateful system"
  recovery: "Re-frame architectural decisions using appropriate constraints; replace CAP reasoning with system-specific trade-off analysis"
  retryable: false
- name: false_cap_trade_off
  description: "Design treats CAP as 'choose two and ignore the third' rather than understanding the partition-specific trade-off."
  likelihood: high
  observable_evidence: "System claims to be 'CA' (no partition tolerance) in a networked deployment; partition behaviour is undefined or untested"
  detection: "Architecture review; partition testing reveals undefined behaviour under network failure"
  recovery: "Redesign partition behaviour explicitly; test under controlled partition conditions"
  retryable: false

## Observations
- observation: "CAP theorem is the most cited and most misapplied concept in distributed systems architecture."
  confidence: high
  source: Architecture review experience, distributed systems literature
- observation: "In practice, most production systems choose consistency over availability during partitions — they prefer correctness to silent data corruption."
  confidence: high
  source: Production architecture survey, operational experience
- observation: "CAP theorem's real value is framing the design space, not prescribing solutions — it forces explicit discussion of partition behaviour."
  confidence: high
  source: Distributed systems literature, architectural practice

## Constraints
- constraint: "During a network partition, a distributed system must sacrifice either consistency or availability — this is provable, not a design preference."
  type: invariant
  scope: distributed-stateful
- constraint: "Outside of a partition, a distributed system can provide all three properties — CAP is a partition-specific constraint, not a universal one."
  type: invariant
  scope: distributed-stateful

## Decision Factors
- factor: correctness_requirement
  question: "Can the system tolerate returning stale or inconsistent data during a network partition?"
  supporting: "Strict correctness requirements justify consistency-over-availability during partitions."
  contradictory: "Many read-heavy workloads tolerate bounded staleness without user-visible impact."
  weight: high
- factor: partition_frequency
  question: "How frequently does the deployment environment experience network partitions?"
  supporting: "Environments with reliable networking rarely experience partitions, reducing the practical impact of choosing consistency."
  contradictory: "Multi-region deployments and unreliable networks experience partitions regularly, making availability-oriented design more practical."
  weight: high
- factor: recovery_time_requirement
  question: "How quickly must the system recover and reconcile after a partition resolves?"
  supporting: "Consistency-oriented systems recover faster because state divergence is prevented during the partition."
  contradictory: "Availability-oriented systems require reconciliation after partitions, extending recovery time."
  weight: medium

## Heuristics
- heuristic: "Never claim to be a 'CA system' in a networked deployment — partition tolerance is not optional."
  rationale: "Any system deployed over a network will experience partitions; claiming CA means partition behaviour is undefined."
  evidence_level: high
- heuristic: "Use CAP analysis to frame the trade-off space, not to make the final decision — system-specific factors determine the right choice."
  rationale: "CAP is a theoretical constraint; real systems have additional considerations (latency, cost, consistency model details) beyond the theorem's scope."
  evidence_level: high
- heuristic: "Test partition behaviour explicitly — theoretical CAP choices often differ from actual system behaviour under partition conditions."
  rationale: "Configuration, timeouts, and implementation details can produce unexpected CAP trade-offs regardless of design intent."
  evidence_level: high

## Recommendations
- recommendation: "Treat CAP as a partition-specific design constraint, not a universal property selection — the 'choose two' framing is misleading."
  context: architecture_design
  certainty: strong
  rationale: "Outside partitions, all three properties are achievable; during partitions, the choice is between consistency and availability — partition tolerance is always required."
- recommendation: "Document partition behaviour explicitly in architecture decisions — how the system behaves during a partition is a design choice, not an accident of implementation."
  context: architecture_documentation
  certainty: strong
  rationale: "Undefined partition behaviour is the most common source of production incidents related to CAP trade-offs."
- recommendation: "Validate CAP assumptions through partition testing (network fault injection) before production deployment."
  context: pre_production
  certainty: strong
  rationale: "Theoretical CAP analysis is necessary but insufficient — implementation details determine actual partition behaviour."
