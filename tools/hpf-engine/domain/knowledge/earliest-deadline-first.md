# Earliest-Deadline-First

## Identity
- id: earliest-deadline-first
- type: concept
- title: Earliest-Deadline-First
- tags: [real-time systems, scheduling, EDF, deadline, optimality]
- entities: [earliest-deadline-first, EDF, deadline ordering, optimality]
- concepts: [scheduling-policy, deadline, task-scheduling, leader-election, quorum]

## Claims
- claim: "Earliest-deadline-first is a scheduling policy that orders tasks by deadline — the earliest deadline executes first."
  certainty: high
  evidence: Real-time scheduling literature
  scope: cross-domain
- claim: "EDF is optimal among dynamic policies — if any policy can schedule a task set, EDF can — the optimality claim."
  certainty: high
  evidence: Optimality proofs in scheduling theory
  scope: cross-domain
- claim: "The optimality claim is bound by stated conditions — preemptive, uniprocessor assumptions qualify the guarantee."
  certainty: high
  evidence: Scheduling theory
  scope: cross-domain
- claim: "EDF's deadline ordering is a constraint — the schedule must respect the ordering, exactly as priority ordering constrains fixed-priority scheduling."
  certainty: high
  evidence: Cross-domain comparison (ordering as graph property 009, priority as constraint Tier 2)
  scope: cross-domain
- claim: "EDF is one realization of the scheduling-policy decision — optimality is the decision's content, not a new construct."
  certainty: high
  evidence: Cross-domain comparison (decision objects 007-010)
  scope: cross-domain

## Relationships
- concept: scheduling-policy
  relationship: realizes
  description: "EDF realizes the scheduling policy — one instantiation of the decision."
- concept: deadline
  relationship: orders_by
  description: "EDF orders by deadline — the timing requirement is the ordering key."
- concept: task-scheduling
  relationship: allocates_within
  description: "EDF allocates within task scheduling — the execution-time discipline."
- concept: leader-election
  relationship: analogous_to
  description: "EDF is analogous to leader election — both are selection rules over contenders — the Cycle 006 cross-domain link."
- concept: quorum
  relationship: analogous_to
  description: "EDF is analogous to quorum — both resolve contention with a rule — the Cycle 006 cross-domain link."

## Tradeoffs
- dimension: optimality_vs_predictability
  options:
    edf:
      value: schedulability
      rationale: "EDF is optimal but dynamic — behaviour is less predictable."
    fixed_priority:
      value: predictability
      rationale: "Fixed priority is predictable but suboptimal."
  importance: high
- dimension: dynamic_ordering_vs_overhead
  options:
    dynamic_ordering:
      value: optimality
      rationale: "Dynamic ordering achieves optimality but costs runtime overhead."
    static_ordering:
      value: simplicity
      rationale: "Static ordering is cheap but weaker."
  importance: medium

## Failure Modes
- name: overload_domino
  description: "Under overload EDF misses many deadlines at once — the optimal policy collapses under saturation."
  likelihood: medium
  observable_evidence: "Cascading misses under overload; domino effect"
  detection: "Overload monitoring; miss-pattern analysis"
  recovery: "Admission control; load shedding; relax requirements"
  retryable: true
- name: deadline_tie_mishandling
  description: "Deadline ties are broken arbitrarily — the ordering rule is incomplete."
  likelihood: low
  observable_evidence: "Inconsistent ordering on ties; surprise misses"
  detection: "Tie-break review; schedule audits"
  recovery: "Define the tie-break rule; document the ordering"
  retryable: true
- name: assumption_violation
  description: "The optimality conditions do not hold — preemptive uniprocessor assumptions violated."
  likelihood: medium
  observable_evidence: "Suboptimal behaviour; misses despite optimality claim"
  detection: "Assumption audits; model review"
  recovery: "Correct the model; change policy; re-verify"
  retryable: true

## Observations
- observation: "Optimality is a conditional claim — EDF is optimal under its conditions, not in general."
  confidence: high
  source: Scheduling theory
- observation: "The selection-rule structure repeats: contenders + ordering rule + allocation + guarantee — the arbitration watch continues to show graph topology, not constructs."
  confidence: high
  source: Arbitration watch (Tier 2)
- observation: "EDF and fixed-priority are alternative realizations of one decision — the policy decision absorbs both."
  confidence: high
  source: Cross-domain comparison (decision objects 007-010)

## Constraints
- constraint: "Deadline ordering is an invariant — the schedule must respect the deadline ordering under EDF."
  type: invariant
  scope: cross-domain
- constraint: "The optimality claim is valid only under its stated conditions — preemptive, uniprocessor assumptions."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Choose EDF when schedulability is the binding constraint."
  rationale: "Optimality buys the most feasibility under saturation."
  evidence_level: high
- heuristic: "Define the tie-break rule explicitly."
  rationale: "An undefined ordering is a hidden decision."
  evidence_level: high

## Recommendations
- recommendation: "Model EDF as a policy decision with an ordering constraint."
  context: modelling
  certainty: strong
  rationale: "Optimality is decision content, not a new construct."
- recommendation: "Verify the optimality conditions before relying on the claim."
  context: engineering
  certainty: strong
  rationale: "The optimality claim holds under its conditions or not at all."
- recommendation: "Plan for overload despite optimality."
  context: operations
  certainty: strong
  rationale: "EDF's domino under overload is the characteristic failure."
