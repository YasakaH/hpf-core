# Fixed-Priority Scheduling

## Identity
- id: fixed-priority-scheduling
- type: pattern
- title: Fixed-Priority Scheduling
- tags: [real-time systems, scheduling, priority, preemption, rate monotonic]
- entities: [fixed-priority scheduling, priority, preemption rule, rate-monotonic analysis]
- concepts: [scheduling-policy, task-scheduling, deadline, rate-monotonic-analysis, leader-election]

## Claims
- claim: "Fixed-priority scheduling is a pattern — tasks carry static priorities and the highest-priority ready task executes."
  certainty: high
  evidence: Real-time scheduling literature
  scope: cross-domain
- claim: "Priority is a constraint plus a relationship — priority ordering constrains the schedule; priority assignment relates tasks to the policy."
  certainty: high
  evidence: Cross-domain comparison (constraints + relationships)
  scope: cross-domain
- claim: "The pattern's validity is bound by stated conditions — priority assignment, preemption rules, and workload assumptions qualify the guarantee."
  certainty: high
  evidence: Schedulability analysis practice
  scope: cross-domain
- claim: "Fixed-priority scheduling is one realization of the scheduling-policy decision — the pattern instantiates the decision object."
  certainty: high
  evidence: Cross-domain comparison (pattern instantiation 009-010)
  scope: cross-domain
- claim: "Rate-monotonic analysis verifies the pattern — feasibility is a claim established by analysis, not assumed by the policy."
  certainty: high
  evidence: Rate-monotonic scheduling literature
  scope: cross-domain

## Relationships
- concept: scheduling-policy
  relationship: realizes
  description: "Fixed-priority scheduling realizes the scheduling policy — one instantiation of the decision."
- concept: task-scheduling
  relationship: allocates_within
  description: "Fixed-priority scheduling allocates within task scheduling — the execution-time discipline."
- concept: deadline
  relationship: serves
  description: "Fixed-priority scheduling serves deadlines — priority ordering exists to satisfy timing."
- concept: rate-monotonic-analysis
  relationship: verified_by
  description: "Fixed-priority scheduling is verified by rate-monotonic analysis — the feasibility check."
- concept: leader-election
  relationship: analogous_to
  description: "Fixed-priority scheduling is analogous to leader election — both are arbitration structures: contenders + selection rule + outcome — the Cycle 006 cross-domain link."

## Tradeoffs
- dimension: static_vs_dynamic_priority
  options:
    static_priority:
      value: predictability
      rationale: "Static priorities are analysable but rigid."
    dynamic_priority:
      value: flexibility
      rationale: "Dynamic priorities adapt but are less predictable."
  importance: high
- dimension: preemptive_vs_non_preemptive
  options:
    preemptive:
      value: schedulability
      rationale: "Preemption improves schedulability but adds overhead."
    non_preemptive:
      value: simplicity
      rationale: "Non-preemption is simpler but weakens guarantees."
  importance: high

## Failure Modes
- name: priority_inversion
  description: "A low-priority task holds a resource a high-priority task needs — the high-priority task waits on the low-priority task."
  likelihood: high
  observable_evidence: "High-priority misses; unbounded blocking; priority-order violations"
  detection: "Blocking analysis; priority-inversion detection"
  recovery: "Priority inheritance; priority ceiling; resource discipline"
  retryable: true
- name: starvation
  description: "Low-priority tasks never execute — the fixed priority order starves them."
  likelihood: medium
  observable_evidence: "Low-priority misses; unbounded delays"
  detection: "Starvation monitoring; priority distribution review"
  recovery: "Add aging; adjust priorities; re-decide policy"
  retryable: true
- name: priority_assignment_error
  description: "Priorities are assigned incorrectly — the ordering contradicts the tasks' criticality or timing."
  likelihood: medium
  observable_evidence: "Misses despite feasible analysis; inverted priority order"
  detection: "Assignment audits; feasibility re-analysis"
  recovery: "Re-assign; re-verify; repair the ordering"
  retryable: true

## Observations
- observation: "Priority is a constraint plus a relationship — never a construct; the ordering lives in the graph."
  confidence: high
  source: Cross-domain comparison (constraints + relationships)
- observation: "The arbitration structure repeats: contenders + selection rule (priority order) + allocation + guarantee — matching leader election (006), isolation levels (010), and now scheduling."
  confidence: high
  source: Arbitration watch (Tier 2)
- observation: "Rate monotonic is the analysis twin of the pattern — the pattern is a claim until analysis verifies it."
  confidence: high
  source: Rate-monotonic scheduling literature

## Constraints
- constraint: "Priority ordering is an invariant — the schedule must respect the assigned priority order."
  type: invariant
  scope: cross-domain
- constraint: "The pattern's guarantee is valid only under stated conditions — priority assignment, preemption rules, and workload assumptions."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Assign priorities by rate or criticality, then verify."
  rationale: "Assignment is a hypothesis until analysis confirms feasibility."
  evidence_level: high
- heuristic: "Watch for priority inversion whenever resources are shared."
  rationale: "Inversion is the characteristic failure of fixed-priority systems."
  evidence_level: high

## Recommendations
- recommendation: "Model priority as constraint plus relationship, not a construct."
  context: modelling
  certainty: strong
  rationale: "The ordering lives in the graph; the discipline lives in the pattern."
- recommendation: "Verify fixed-priority feasibility with rate-monotonic analysis."
  context: engineering
  certainty: strong
  rationale: "The pattern is a claim until analysis makes it evidence."
- recommendation: "Apply priority inheritance when resources are shared."
  context: engineering
  certainty: strong
  rationale: "Inversion is the failure; inheritance is the mitigation."
