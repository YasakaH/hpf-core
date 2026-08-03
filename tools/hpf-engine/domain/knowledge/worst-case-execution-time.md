# Worst-Case Execution Time

## Identity
- id: worst-case-execution-time
- type: concept
- title: Worst-Case Execution Time
- tags: [real-time systems, WCET, timing analysis, measurement, bounds]
- entities: [worst-case execution time, WCET, timing analysis, execution time bound, measurement]
- concepts: [deadline, real-time-system, schedulability-analysis, benchmark-validity, query-planning]

## Claims
- claim: "WCET is an estimate of the longest execution time a task can exhibit — a claim about the future, not a measured fact."
  certainty: high
  evidence: Timing analysis literature
  scope: cross-domain
- claim: "WCET is an observation with confidence, not a guarantee — underestimation is the characteristic failure."
  certainty: high
  evidence: WCET analysis practice and incident analyses
  scope: cross-domain
- claim: "WCET validity is bound by stated conditions — architecture, inputs, and analysis assumptions qualify the bound."
  certainty: high
  evidence: Timing analysis methodology
  scope: cross-domain
- claim: "A WCET estimate is a hypothesis about execution that runtime evidence can falsify — the query-planning finding applied to timing."
  certainty: high
  evidence: Cross-domain comparison (query-planning 010)
  scope: cross-domain
- claim: "The bound's usefulness depends on its confidence — a safe over-approximation and a tight approximation differ in certainty, not kind."
  certainty: high
  evidence: WCET analysis tradeoff practice
  scope: cross-domain

## Relationships
- concept: deadline
  relationship: bounded_by
  description: "WCET is bounded by the deadline — feasibility requires the estimate to fit the constraint."
- concept: schedulability-analysis
  relationship: feeds
  description: "WCET feeds schedulability analysis — the estimate is the input to the guarantee."
- concept: benchmark-validity
  relationship: analogous_to
  description: "WCET is analogous to benchmark validity — both are measurement-quality claims — the Cycle 008 cross-domain link."
- concept: query-planning
  relationship: analogous_to
  description: "WCET is analogous to query planning — both are hypotheses about future behaviour — the Cycle 010 cross-domain link."
- concept: real-time-system
  relationship: underpins
  description: "WCET underpins the real-time system's guarantees — analysis is the evidence base."

## Tradeoffs
- dimension: safety_vs_tightness
  options:
    safe_upper_bound:
      value: guarantee_strength
      rationale: "Safe upper bounds protect the guarantee but are pessimistic."
    tight_estimate:
      value: resource_efficiency
      rationale: "Tight estimates are efficient but risk underestimation."
  importance: high
- dimension: analysis_vs_measurement
  options:
    static_analysis:
      value: coverage
      rationale: "Static analysis covers all paths but is conservative."
    runtime_measurement:
      value: realism
      rationale: "Measurement is realistic but covers observed paths only."
  importance: high

## Failure Modes
- name: wcet_underestimation
  description: "The estimate is lower than the true worst case — the guarantee is invalid and misses appear at runtime."
  likelihood: medium
  observable_evidence: "Deadline misses despite passing analysis; underestimated bounds"
  detection: "Measurement campaigns; analysis cross-checks; bound review"
  recovery: "Re-analyse; increase the bound; repair the analysis"
  retryable: true
- name: wcet_overestimation
  description: "The estimate is far above the true worst case — resources are wasted on an unrealistically safe bound."
  likelihood: medium
  observable_evidence: "Low utilization; wasted capacity; unnecessarily tight feasibility"
  detection: "Measurement comparison; bound-efficiency review"
  recovery: "Refine the analysis; tighten the bound"
  retryable: true
- name: assumption_decay
  description: "The analysis assumptions no longer hold — the bound silently stops describing the running system."
  likelihood: medium
  observable_evidence: "Analysis/runtime divergence; changed hardware or input patterns"
  detection: "Assumption audits; divergence monitoring"
  recovery: "Re-analyse with current assumptions; re-establish the bound"
  retryable: true

## Observations
- observation: "WCET is an observation with confidence — the strongest guarantee in real-time rests on an estimate, exactly as plans rest on cost models (010)."
  confidence: high
  source: Cross-domain comparison (query-planning 010)
- observation: "The bound's validity is a claim about future behaviour — it holds under stated conditions or it does not hold at all."
  confidence: high
  source: Timing analysis methodology
- observation: "Underestimation is the dangerous failure — it makes the guarantee a false promise."
  confidence: high
  source: WCET incident analyses

## Constraints
- constraint: "WCET validity is bound by stated conditions — architecture, inputs, and analysis assumptions qualify the estimate."
  type: invariant
  scope: cross-domain
- constraint: "A guarantee built on an unstated or drifted WCET assumption is invalid — the estimate's conditions must hold."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Treat WCET as an estimate with confidence, not a promise."
  rationale: "The failure mode is underestimation; the discipline is confidence."
  evidence_level: high
- heuristic: "Cross-check analysis with measurement when possible."
  rationale: "The two methods bound each other's blind spots."
  evidence_level: high

## Recommendations
- recommendation: "State WCET conditions explicitly with the estimate."
  context: engineering
  certainty: strong
  rationale: "An unstated condition is an unverified claim."
- recommendation: "Treat a passed feasibility check as evidence, not proof."
  context: engineering
  certainty: strong
  rationale: "The analysis is a hypothesis about future behaviour."
- recommendation: "Re-validate WCET when the system changes."
  context: operations
  certainty: strong
  rationale: "Assumption decay is the silent invalidation of guarantees."
