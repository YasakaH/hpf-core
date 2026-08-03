# Task Scheduling

## Identity
- id: task-scheduling
- type: concept
- title: Task Scheduling
- tags: [real-time systems, scheduling, tasks, allocation, execution time]
- entities: [task, schedule, scheduler, execution time, allocation]
- concepts: [deadline, real-time-system, worst-case-execution-time, quorum, backpressure]

## Claims
- claim: "Task scheduling is the discipline of allocating execution time to tasks so that timing requirements are satisfied."
  certainty: high
  evidence: Real-time scheduling practice and literature
  scope: cross-domain
- claim: "A schedule is an allocation of time to tasks — a plan whose outcome is bound by deadlines."
  certainty: high
  evidence: Scheduling theory
  scope: cross-domain
- claim: "Scheduling resolves as relationships plus constraints — task-to-time allocation expressed as graph edges with timing bounds — not a distinct construct."
  certainty: high
  evidence: Cross-domain comparison (relationships + constraints across cycles)
  scope: cross-domain
- claim: "Scheduling feasibility is a claim about the schedule under stated conditions — load and timing assumptions qualify it."
  certainty: high
  evidence: Schedulability analysis practice
  scope: cross-domain
- claim: "Scheduling is the discipline; the policy is the decision — policy selection is the Tier 2 decision object, not a new knowledge kind."
  certainty: high
  evidence: Cross-domain comparison (decision objects 007-010)
  scope: cross-domain

## Relationships
- concept: deadline
  relationship: serves
  description: "Task scheduling serves deadlines — allocation decisions satisfy timing requirements."
- concept: real-time-system
  relationship: operates_within
  description: "Task scheduling operates within the real-time system — it is the allocation layer."
- concept: worst-case-execution-time
  relationship: consumes
  description: "Task scheduling consumes WCET estimates — the input to allocation decisions."
- concept: quorum
  relationship: analogous_to
  description: "Task scheduling is analogous to quorum — both allocate limited resources under agreement — the Cycle 006 cross-domain link."
- concept: backpressure
  relationship: analogous_to
  description: "Task scheduling is analogous to backpressure — both manage contention — the Cycle 006 cross-domain link."

## Tradeoffs
- dimension: utilization_vs_guarantee
  options:
    full_utilization:
      value: efficiency
      rationale: "Full utilization uses all capacity but leaves no slack for guarantees."
    reserved_slack:
      value: guarantee_strength
      rationale: "Reserved slack protects guarantees but wastes capacity."
  importance: high
- dimension: fairness_vs_priority
  options:
    fair_allocation:
      value: equity
      rationale: "Fair allocation treats tasks equally but may miss critical deadlines."
    priority_allocation:
      value: correctness
      rationale: "Priority allocation protects critical deadlines but starves others."
  importance: high

## Failure Modes
- name: schedule_infeasibility
  description: "No valid allocation exists — the task set cannot meet its deadlines under the policy."
  likelihood: medium
  observable_evidence: "Feasibility analysis failure; miss cascades; unschedulable task sets"
  detection: "Feasibility analysis; schedule verification"
  recovery: "Relax requirements; change policy; reduce load"
  retryable: true
- name: starvation
  description: "Low-priority tasks never execute — the allocation starves them indefinitely."
  likelihood: medium
  observable_evidence: "Low-priority task misses; unbounded delays; watchdog triggers"
  detection: "Starvation monitoring; priority distribution review"
  recovery: "Adjust priority; add aging; re-balance allocation"
  retryable: true
- name: allocation_drift
  description: "The schedule drifts from reality — actual execution diverges from the allocated plan."
  likelihood: medium
  observable_evidence: "Schedule/runtime divergence; accumulating delay; jitter growth"
  detection: "Schedule audits; execution-time monitoring"
  recovery: "Re-schedule; re-analyse; repair the drift"
  retryable: true

## Observations
- observation: "Scheduling is allocation — the same structure as resource allocation everywhere; the temporal content lives in the constraints."
  confidence: high
  source: Cross-domain comparison (allocation patterns 006-010)
- observation: "The schedule is a plan, not a fact — runtime evidence validates or falsifies it."
  confidence: high
  source: Scheduling practice
- observation: "The policy temptation is the trap — scheduling as a discipline is a concept; the policy choice is the decision."
  confidence: high
  source: Cross-domain comparison (decision objects 007-010)

## Constraints
- constraint: "A schedule is valid only if all tasks meet their deadlines under the policy and its stated conditions."
  type: invariant
  scope: cross-domain
- constraint: "Scheduling guarantees are bound by load and timing assumptions — unstated conditions void the allocation's validity."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Analyze feasibility before committing to a schedule."
  rationale: "Infeasibility is cheaper to find in analysis than at runtime."
  evidence_level: high
- heuristic: "Reserve slack for guarantee strength."
  rationale: "Full utilization is where guarantees die."
  evidence_level: high

## Recommendations
- recommendation: "Model scheduling as relationships plus constraints, not a scheduling construct."
  context: modelling
  certainty: strong
  rationale: "Allocation is graph structure; the temporal content is constraint content."
- recommendation: "Keep the schedule's conditions explicit and audited."
  context: engineering
  certainty: strong
  rationale: "A schedule is valid under its conditions or not at all."
- recommendation: "Choose the policy deliberately; re-verify when load changes."
  context: engineering
  certainty: strong
  rationale: "Policy is a decision; decisions need re-decision as conditions change."
