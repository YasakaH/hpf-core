# Schedulability Analysis

## Identity
- id: schedulability-analysis
- type: concept
- title: Schedulability Analysis
- tags: [real-time systems, schedulability, feasibility, verification, guarantees]
- entities: [schedulability analysis, feasibility, utilization bound, task model, schedulability]
- concepts: [rate-monotonic-analysis, worst-case-execution-time, real-time-guarantee, deadline, formal-verification]

## Claims
- claim: "Schedulability analysis is the discipline of establishing feasibility — whether a task set can meet its deadlines under a policy."
  certainty: high
  evidence: Real-time scheduling literature
  scope: cross-domain
- claim: "Schedulability is a property claim — established through analysis under a task model, valid only under that model's conditions."
  certainty: high
  evidence: Schedulability analysis methodology
  scope: cross-domain
- claim: "The analysis is evidence for a guarantee, not the guarantee itself — runtime conditions can diverge from the model."
  certainty: high
  evidence: Cross-domain comparison (WCET as observation, Tier 1)
  scope: cross-domain
- claim: "Schedulability analysis is the generalized form of rate-monotonic analysis — a family of feasibility tests, not a new construct."
  certainty: high
  evidence: Tier 2 rate-monotonic-analysis resolution
  scope: cross-domain
- claim: "The analysis is structurally analogous to formal verification — mechanical property establishment under a stated model — the Cycle 009 cross-domain link."
  certainty: high
  evidence: Cross-domain comparison (verification objects 009)
  scope: cross-domain

## Relationships
- concept: rate-monotonic-analysis
  relationship: generalizes
  description: "Schedulability analysis generalizes rate-monotonic analysis — one instance of the feasibility discipline."
- concept: worst-case-execution-time
  relationship: consumes
  description: "Schedulability analysis consumes WCET — the estimates feed the feasibility test."
- concept: real-time-guarantee
  relationship: establishes
  description: "Schedulability analysis establishes the real-time guarantee — analysis is the evidence for the claim."
- concept: deadline
  relationship: evaluated_against
  description: "Schedulability analysis is evaluated against deadlines — feasibility is judged on timing requirements."
- concept: formal-verification
  relationship: analogous_to
  description: "Schedulability analysis is analogous to formal verification — both are mechanical property establishment — the Cycle 009 cross-domain link."

## Tradeoffs
- dimension: precision_vs_tractability
  options:
    sufficient_tests:
      value: tractability
      rationale: "Sufficient tests are cheap but pessimistic."
    exact_tests:
      value: precision
      rationale: "Exact tests are precise but computationally expensive."
  importance: high
- dimension: model_fidelity_vs_abstraction
  options:
    faithful_model:
      value: validity
      rationale: "Faithful models match reality but are costly to build."
    abstract_model:
      value: simplicity
      rationale: "Abstract models are simple but risk assumption mismatch."
  importance: high

## Failure Modes
- name: false_feasibility
  description: "Analysis declares feasibility that runtime falsifies — model assumptions do not match the running system."
  likelihood: medium
  observable_evidence: "Misses despite passed analysis; analysis/runtime divergence"
  detection: "Assumption audits; runtime verification; measurement campaigns"
  recovery: "Correct the model; re-analyse; re-establish the guarantee"
  retryable: true
- name: false_infeasibility
  description: "Analysis rejects a task set that is actually schedulable — the pessimistic bound wastes capacity."
  likelihood: medium
  observable_evidence: "Rejected task sets; wasted design effort; unnecessary capacity"
  detection: "Exact-test comparison; simulation cross-check"
  recovery: "Use a tighter test; refine the model"
  retryable: true
- name: model_drift
  description: "The task model drifts from reality as the system evolves — the analysis claim decays."
  likelihood: medium
  observable_evidence: "Growing divergence; new workloads unmapped; stale models"
  detection: "Model audits; re-analysis triggers"
  recovery: "Re-model; re-analyse; repair the drift"
  retryable: true

## Observations
- observation: "Schedulability is a claim established under a model — the analysis is evidence, runtime is the test."
  confidence: high
  source: Cross-domain comparison (WCET as observation, Tier 1)
- observation: "The discipline is a family, not a construct — rate-monotonic is the instance; the family is the concept."
  confidence: high
  source: Tier 2 rate-monotonic-analysis resolution
- observation: "Mechanical property establishment is one pattern — schedulability, equivalence, and proof share it."
  confidence: high
  source: Cross-domain comparison (verification objects 009)

## Constraints
- constraint: "A schedulability claim is valid only under its task model's conditions — periodicity, independence, and timing assumptions bound it."
  type: invariant
  scope: cross-domain
- constraint: "The analysis inherits its inputs' confidence — a bad WCET propagates into a false feasibility claim."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Audit the task model with the running system."
  rationale: "Model drift is the silent invalidation of feasibility."
  evidence_level: high
- heuristic: "Use the cheapest sufficient test first; escalate to exact tests."
  rationale: "Tractability first, precision on demand."
  evidence_level: high

## Recommendations
- recommendation: "Treat feasibility as a claim bound by its model, not a fact."
  context: engineering
  certainty: strong
  rationale: "The analysis is evidence until runtime verifies it."
- recommendation: "Re-run analysis when the system changes."
  context: operations
  certainty: strong
  rationale: "Model drift is guarantee decay in disguise."
- recommendation: "Carry WCET confidence through the analysis."
  context: engineering
  certainty: strong
  rationale: "The guarantee inherits its evidence's confidence."
