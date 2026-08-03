# Priority Inversion

## Identity
- id: priority-inversion
- type: concept
- title: Priority Inversion
- tags: [real-time systems, priority inversion, blocking, contention, mitigation]
- entities: [priority inversion, blocking, priority inheritance, resource contention]
- concepts: [fixed-priority-scheduling, scheduling-policy, deadline, task-scheduling, split-brain]

## Claims
- claim: "Priority inversion is a blocking failure — a low-priority task holds a resource a high-priority task needs, inverting the priority order."
  certainty: high
  evidence: Real-time systems literature (Mars Pathfinder incident)
  scope: cross-domain
- claim: "Priority inversion is a failure mode of the priority ordering invariant — the schedule violates the ordering it promises."
  certainty: high
  evidence: Cross-domain comparison (constraint violations as failure modes)
  scope: cross-domain
- claim: "Priority inversion is bounded — with priority inheritance or priority ceiling, blocking is bounded by the critical section, not by arbitrary delay."
  certainty: high
  evidence: Priority inheritance/ceiling protocols literature
  scope: cross-domain
- claim: "Priority inversion resolves as failure mode + constraint (priority ordering) + mitigation pattern (priority inheritance) — no concurrency-failure primitive."
  certainty: high
  evidence: Cross-domain comparison (failure-mode resolutions 009-010)
  scope: cross-domain
- claim: "Priority inversion is the strongest test of contention under guarantees — time + resources + competing tasks + blocking all at once."
  certainty: high
  evidence: Cycle 011 pre-registration (Tier 3 danger object)
  scope: cross-domain

## Relationships
- concept: fixed-priority-scheduling
  relationship: afflicts
  description: "Priority inversion afflicts fixed-priority scheduling — the characteristic failure of the pattern."
- concept: scheduling-policy
  relationship: challenges
  description: "Priority inversion challenges the scheduling policy — the allocation rule's guarantee is at stake."
- concept: deadline
  relationship: threatens
  description: "Priority inversion threatens deadlines — unbounded blocking causes misses."
- concept: task-scheduling
  relationship: emerges_in
  description: "Priority inversion emerges in task scheduling — the contention structure of the allocation."
- concept: split-brain
  relationship: analogous_to
  description: "Priority inversion is analogous to split-brain — both are coordination failures from contention — the Cycle 006 cross-domain link."

## Tradeoffs
- dimension: inheritance_vs_overhead
  options:
    priority_inheritance:
      value: bounded_blocking
      rationale: "Inheritance bounds blocking but adds protocol overhead."
    no_protocol:
      value: simplicity
      rationale: "No protocol is simple but permits unbounded blocking."
  importance: high
- dimension: boundedness_vs_flexibility
  options:
    priority_ceiling:
      value: strong_bound
      rationale: "Ceiling protocols give strong bounds but restrict flexibility."
    runtime_monitoring:
      value: flexibility
      rationale: "Monitoring is flexible but detects rather than prevents."
  importance: high

## Failure Modes
- name: unbounded_inversion
  description: "Blocking has no bound — the high-priority task waits indefinitely behind lower-priority work."
  likelihood: medium
  observable_evidence: "High-priority misses; unbounded latency; priority-order violations"
  detection: "Blocking analysis; priority-inversion detection; latency monitoring"
  recovery: "Apply inheritance/ceiling; restructure resource sharing"
  retryable: true
- name: inversion_chain
  description: "Multiple tasks form a blocking chain — the priority order is inverted through several layers."
  likelihood: medium
  observable_evidence: "Cascading priority inversions; deep blocking chains"
  detection: "Chain analysis; blocking-graph inspection"
  recovery: "Ceiling protocols; resource discipline; restructure"
  retryable: true
- name: silent_deadlock
  description: "Inversion escalates into deadlock — blocked tasks wait on each other permanently."
  likelihood: low
  observable_evidence: "System freeze; watchdog triggers; missed deadlines"
  detection: "Deadlock detection; timeout analysis"
  recovery: "Timeout recovery; resource discipline; restart"
  retryable: true

## Observations
- observation: "Priority inversion is the real-time form of a coordination failure — the same contention structure as split-brain (006), expressed as a failure mode."
  confidence: high
  source: Cross-domain comparison (coordination failures)
- observation: "The danger object resolved — the concurrency-failure primitive temptation did not materialize; it was a failure mode with constraints and mitigation."
  confidence: high
  source: Cycle 011 Tier 3 pre-registration
- observation: "The mitigation is a pattern, not a construct — priority inheritance is a bounded-blocking discipline, expressed as claims + constraints + relationships."
  confidence: high
  source: Cross-domain comparison (mitigation patterns 006-010)

## Constraints
- constraint: "Priority ordering is an invariant — the schedule must respect the priority order."
  type: invariant
  scope: cross-domain
- constraint: "Blocking must be bounded — unbounded priority inversion violates the guarantee."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Bound blocking wherever resources are shared."
  rationale: "Unbounded blocking is the inversion failure."
  evidence_level: high
- heuristic: "Detect inversion early; monitor blocking."
  rationale: "Detection bounds the damage of unbounded waiting."
  evidence_level: high

## Recommendations
- recommendation: "Model priority inversion as a failure mode with constraint and mitigation."
  context: modelling
  certainty: strong
  rationale: "The failure is the anchor; the mitigation is the discipline."
- recommendation: "Apply priority inheritance or ceiling when sharing resources."
  context: engineering
  certainty: strong
  rationale: "Bounded blocking is the difference between guarantee and collapse."
- recommendation: "Monitor for inversion chains under load."
  context: operations
  certainty: strong
  rationale: "Chains are the escalation path to deadlock."
