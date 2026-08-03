# Scheduling Policy

## Identity
- id: scheduling-policy
- type: decision
- title: Scheduling Policy
- tags: [real-time systems, scheduling, policy, priorities, allocation]
- entities: [scheduling policy, priority, preemption, allocation rule, deadline priority]
- concepts: [task-scheduling, deadline, fixed-priority-scheduling, earliest-deadline-first, isolation-levels]
- decision-factors:
  - deadline_priority
  - utilization_target
  - task_criticality
  - preemption_allowance

## Claims
- claim: "A scheduling policy is the decision of how execution time is allocated among tasks — the choice of the allocation rule."
  certainty: high
  evidence: Real-time scheduling practice
  scope: cross-domain
- claim: "Policy selection is a decision, not a discovery — the same task set can be scheduled under different policies with different guarantee outcomes."
  certainty: high
  evidence: Cross-domain comparison (decision objects 007-010)
  scope: cross-domain
- claim: "A policy's validity is bound by stated conditions — workload, priorities, and preemption assumptions qualify the guarantee it provides."
  certainty: high
  evidence: Schedulability analysis practice
  scope: cross-domain
- claim: "A scheduling policy is structurally identical to every other decision object — it varies with deadline_priority, utilization_target, task_criticality, and preemption_allowance."
  certainty: high
  evidence: Cross-domain comparison (decision objects 007-010)
  scope: cross-domain
- claim: "Policy is the allocation rule; scheduling is the discipline; the two are not separate knowledge kinds."
  certainty: high
  evidence: Tier 1 task-scheduling resolution
  scope: cross-domain

## Relationships
- concept: task-scheduling
  relationship: guides
  description: "A scheduling policy guides task scheduling — the allocation rule is the policy's decision."
- concept: deadline
  relationship: serves
  description: "A scheduling policy serves deadlines — the rule exists to satisfy timing requirements."
- concept: fixed-priority-scheduling
  relationship: realized_by
  description: "A scheduling policy is realized by fixed-priority scheduling — one instantiation of the decision."
- concept: earliest-deadline-first
  relationship: alternative_to
  description: "A scheduling policy is alternative to earliest-deadline-first — competing instantiations of the decision."
- concept: isolation-levels
  relationship: analogous_to
  description: "A scheduling policy is analogous to isolation levels — both are concurrency posture decisions — the Cycle 010 cross-domain link."

## Tradeoffs
- dimension: predictability_vs_optimality
  options:
    fixed_priority:
      value: predictability
      rationale: "Fixed priority is predictable and analysable but suboptimal."
    dynamic_priority:
      value: schedulability
      rationale: "Dynamic priority is optimal but less predictable."
  importance: high
- dimension: preemption_vs_overhead
  options:
    preemptive:
      value: schedulability
      rationale: "Preemption improves schedulability but adds overhead and complexity."
    non_preemptive:
      value: simplicity
      rationale: "Non-preemption is simple but weakens guarantees."
  importance: high

## Failure Modes
- name: policy_mismatch
  description: "The policy does not fit the workload — the allocation rule contradicts the tasks' timing characteristics."
  likelihood: high
  observable_evidence: "Misses despite feasible analysis; policy/workload divergence"
  detection: "Feasibility re-analysis; workload-policy review"
  recovery: "Re-decide the policy; re-verify the guarantee"
  retryable: true
- name: starvation
  description: "The policy starves tasks — low-priority work never executes."
  likelihood: medium
  observable_evidence: "Low-priority misses; unbounded delays; watchdog triggers"
  detection: "Starvation monitoring; allocation distribution review"
  recovery: "Adjust priority; add aging; change policy"
  retryable: true
- name: factor_drift
  description: "The decision factors change without a re-decision — the policy persists after its conditions expired."
  likelihood: medium
  observable_evidence: "Stale policy; mismatch with new workload; guarantee erosion"
  detection: "Factor audits; condition review"
  recovery: "Re-decide; re-verify; repair the drift"
  retryable: true

## Observations
- observation: "Policy choice is a decision — the decision-object pattern absorbs it without a scheduling construct."
  confidence: high
  source: Cross-domain comparison (decision objects 007-010)
- observation: "The arbitration structure appears: contenders + selection rule + allocation + guarantee — but it is graph topology, not a construct."
  confidence: high
  source: Arbitration watch (Tier 2 pre-registration)
- observation: "Factor count held at 4 — the decision-object pattern continues to stabilize at four Decision Factors."
  confidence: high
  source: Cross-domain comparison (decision objects 007-010)

## Constraints
- constraint: "A policy's guarantee is valid only under its stated conditions — workload, priority, and preemption assumptions bound the claim."
  type: invariant
  scope: cross-domain
- constraint: "A policy must remain feasible — a policy that cannot meet its task set's deadlines is invalid under those conditions."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Choose the policy for the workload, not for its reputation."
  rationale: "Policy fit is workload-specific; the decision is the discipline."
  evidence_level: high
- heuristic: "Re-decide the policy when workload or priorities change."
  rationale: "A stale policy is a drift in progress."
  evidence_level: high

## Recommendations
- recommendation: "Treat policy selection as a decision with stated factors."
  context: engineering
  certainty: strong
  rationale: "Policy is a decision; decisions need explicit factors and re-decision."
- recommendation: "Verify feasibility after choosing the policy."
  context: engineering
  certainty: strong
  rationale: "The choice is a claim until analysis makes it evidence."
- recommendation: "Document the policy's conditions with the decision."
  context: governance
  certainty: strong
  rationale: "An undocumented condition is an unverified claim."
