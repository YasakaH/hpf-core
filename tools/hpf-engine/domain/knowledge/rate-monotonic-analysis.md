# Rate-Monotonic Analysis

## Identity
- id: rate-monotonic-analysis
- type: concept
- title: Rate-Monotonic Analysis
- tags: [real-time systems, scheduling, rate monotonic, feasibility, utilization]
- entities: [rate-monotonic analysis, utilization bound, feasibility test, schedulability]
- concepts: [fixed-priority-scheduling, worst-case-execution-time, deadline, equivalence-checking, benchmark-validity]

## Claims
- claim: "Rate-monotonic analysis is a feasibility test — a claim about whether a task set meets its deadlines under fixed-priority scheduling."
  certainty: high
  evidence: Rate-monotonic scheduling literature
  scope: cross-domain
- claim: "The utilization bound is the analysis core — a sufficient condition expressed as a constraint on total utilization."
  certainty: high
  evidence: Liu & Layland analysis
  scope: cross-domain
- claim: "The analysis is a claim with evidence and conditions — the bound holds under periodic, independent, deadline-equals-period assumptions."
  certainty: high
  evidence: Rate-monotonic scheduling theory
  scope: cross-domain
- claim: "The analysis result is an observation about feasibility, not a guarantee about runtime — runtime evidence can diverge from the bound's assumptions."
  certainty: high
  evidence: Cross-domain comparison (WCET as observation, Tier 1)
  scope: cross-domain
- claim: "Rate-monotonic analysis is structurally identical to equivalence checking — a mechanical verification that makes a property claim — the Cycle 009 cross-domain link."
  certainty: high
  evidence: Cross-domain comparison (verification objects 009)
  scope: cross-domain

## Relationships
- concept: fixed-priority-scheduling
  relationship: verifies
  description: "Rate-monotonic analysis verifies fixed-priority scheduling — the feasibility check on the pattern."
- concept: worst-case-execution-time
  relationship: consumes
  description: "Rate-monotonic analysis consumes WCET — the analysis input."
- concept: deadline
  relationship: bounded_by
  description: "Rate-monotonic analysis is bounded by deadlines — feasibility is judged against timing requirements."
- concept: equivalence-checking
  relationship: analogous_to
  description: "Rate-monotonic analysis is analogous to equivalence checking — both are mechanical property verification — the Cycle 009 cross-domain link."
- concept: benchmark-validity
  relationship: analogous_to
  description: "Rate-monotonic analysis is analogous to benchmark validity — both bound a claim by measurement conditions — the Cycle 008 cross-domain link."

## Tradeoffs
- dimension: bound_safety_vs_tightness
  options:
    sufficient_bound:
      value: guarantee_strength
      rationale: "The sufficient bound is safe but pessimistic — it can reject feasible task sets."
    exact_test:
      value: precision
      rationale: "Exact tests are precise but cost more analysis."
  importance: high
- dimension: analysis_cost_vs_coverage
  options:
    simple_bound:
      value: tractability
      rationale: "The simple bound is cheap but conservative."
    detailed_test:
      value: accuracy
      rationale: "Detailed tests are accurate but expensive."
  importance: medium

## Failure Modes
- name: bound_pessimism
  description: "The sufficient bound rejects a task set that is actually schedulable — a false negative."
  likelihood: medium
  observable_evidence: "Feasible task sets rejected; wasted design effort"
  detection: "Exact-test comparison; simulation cross-check"
  recovery: "Use an exact test; relax the bound's assumptions"
  retryable: true
- name: assumption_mismatch
  description: "The analysis assumptions do not match the task set — periodic, independent, deadline-equals-period violated."
  likelihood: medium
  observable_evidence: "Analysis/runtime divergence; unexpected misses"
  detection: "Assumption audits; model review"
  recovery: "Correct the model; re-analyse; repair the mismatch"
  retryable: true
- name: wcet_underestimation_propagation
  description: "The analysis inherits a bad WCET — underestimation propagates into a false feasibility claim."
  likelihood: medium
  observable_evidence: "Misses despite passed analysis"
  detection: "WCET cross-check; bound review"
  recovery: "Correct WCET; re-analyse; re-establish the claim"
  retryable: true

## Observations
- observation: "The analysis is evidence, not a promise — the bound holds under its conditions or not at all."
  confidence: high
  source: Cross-domain comparison (WCET as observation, Tier 1)
- observation: "Feasibility is a property claim — mechanically established like equivalence, judged under a model."
  confidence: high
  source: Cross-domain comparison (verification objects 009)
- observation: "The pessimism is the price of sufficiency — the bound trades precision for guarantee strength."
  confidence: high
  source: Rate-monotonic scheduling theory

## Constraints
- constraint: "The bound is valid only under its stated conditions — periodic, independent tasks with deadline equal to period."
  type: invariant
  scope: cross-domain
- constraint: "The analysis result is bound by its inputs — a bad WCET propagates into a false feasibility claim."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Use the simple bound first; escalate to exact tests when it rejects."
  rationale: "The cheap test catches most cases; escalation resolves the boundary."
  evidence_level: high
- heuristic: "Audit the model assumptions with the task set."
  rationale: "Assumption mismatch is the silent invalidation of feasibility."
  evidence_level: high

## Recommendations
- recommendation: "Treat feasibility analysis as a claim with evidence and conditions."
  context: engineering
  certainty: strong
  rationale: "The bound is a sufficient condition, not a runtime guarantee."
- recommendation: "Cross-check the bound against the actual task model."
  context: engineering
  certainty: strong
  rationale: "Assumption mismatch is where false feasibility lives."
- recommendation: "Propagate WCET confidence into the analysis result."
  context: engineering
  certainty: strong
  rationale: "The analysis inherits its inputs' confidence."
