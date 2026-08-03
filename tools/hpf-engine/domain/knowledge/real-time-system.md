# Real-Time System

## Identity
- id: real-time-system
- type: concept
- title: Real-Time System
- tags: [real-time systems, deadlines, scheduling, temporal guarantees, correctness]
- entities: [real-time system, deadline, task, schedule, worst-case execution time]
- concepts: [deadline, task-scheduling, worst-case-execution-time, build-systems, deployment-risk]

## Claims
- claim: "A real-time system is a system whose correctness depends on the time at which results are produced — not only on what is produced."
  certainty: high
  evidence: Real-time systems practice and literature
  scope: cross-domain
- claim: "A deadline is a validity condition on completion — a result produced after its deadline is invalid regardless of its content."
  certainty: high
  evidence: Real-time correctness definitions
  scope: cross-domain
- claim: "Real-time correctness decomposes into logical correctness plus temporal correctness — the temporal part is carried by constraints."
  certainty: high
  evidence: Cross-domain comparison (Cycle 009 correctness decomposition)
  scope: cross-domain
- claim: "Guarantees in a real-time system are claims about future behaviour — valid only under stated conditions about load, timing, and environment."
  certainty: high
  evidence: Schedulability analysis practice
  scope: cross-domain
- claim: "Real-time guarantees are the unification-hypothesis test at the temporal pole — a guarantee is valid if its stated conditions hold, exactly as knowledge (008), transformations (009), and data (010) are."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-010)
  scope: cross-domain

## Relationships
- concept: deadline
  relationship: constrained_by
  description: "A real-time system is constrained by deadlines — timing requirements bound correctness."
- concept: task-scheduling
  relationship: requires
  description: "A real-time system requires task scheduling — allocation of execution time to tasks."
- concept: worst-case-execution-time
  relationship: evaluated_through
  description: "A real-time system is evaluated through WCET — the timing analysis basis for guarantees."
- concept: deployment-risk
  relationship: affected_by
  description: "A real-time system is affected by deployment risk — the Cycle 008 cross-domain link: environment conditions bound guarantees."
- concept: build-systems
  relationship: analogous_to
  description: "A real-time system is analogous to build systems — both bound validity by stated conditions — the Cycle 009 cross-domain link."

## Tradeoffs
- dimension: predictability_vs_utilization
  options:
    predictable_design:
      value: guarantee_strength
      rationale: "Predictable designs bound worst cases but leave capacity unused."
    high_utilization:
      value: efficiency
      rationale: "High utilization is efficient but pushes guarantees toward the edge."
  importance: high
- dimension: hard_vs_soft_posture
  options:
    hard_guarantees:
      value: correctness
      rationale: "Hard guarantees treat deadline misses as failures."
    soft_guarantees:
      value: resource_use
      rationale: "Soft guarantees tolerate misses but weaken the contract."
  importance: high

## Failure Modes
- name: deadline_miss
  description: "A task produces its result after its deadline — the result is invalid even if logically correct."
  likelihood: high
  observable_evidence: "Late outputs; timing violations; cascading downstream misses"
  detection: "Deadline monitoring; timing instrumentation; schedule verification"
  recovery: "Relax requirements; re-schedule; reduce load; re-verify analysis"
  retryable: true
- name: guarantee_erosion
  description: "Real-time guarantees silently weaken — analysis assumptions no longer match the running system."
  likelihood: medium
  observable_evidence: "Miss rate growth; analysis/runtime divergence; unexplained timing variance"
  detection: "Guarantee audits; assumption review; runtime vs analysis comparison"
  recovery: "Re-analyse with current assumptions; repair the mismatch"
  retryable: true
- name: timing_analysis_invalidity
  description: "The timing analysis itself is wrong — WCET underestimation or schedule analysis error invalidates the guarantee."
  likelihood: medium
  observable_evidence: "Under-approximated execution times; missed deadlines despite analysis"
  detection: "Measurement campaigns; analysis cross-check; bound review"
  recovery: "Correct the analysis; re-establish the guarantee"
  retryable: true

## Observations
- observation: "Real-time correctness is a guarantee claim, not a measured fact — it holds only under the analysis assumptions that produced it."
  confidence: high
  source: Schedulability analysis practice
- observation: "The hardest object in real-time is the system object itself — it must hold timing, scheduling, and resources together without a timing construct."
  confidence: high
  source: Cross-domain comparison (program-semantics 009, schema-design 010)
- observation: "Deadline misses are the observable — every guarantee in the system exists to prevent them, exactly as failures anchor guarantees elsewhere."
  confidence: high
  source: Real-time incident analyses

## Constraints
- constraint: "A result produced after its deadline is invalid — temporal correctness is a validity condition, not a quality preference."
  type: invariant
  scope: cross-domain
- constraint: "A real-time guarantee is valid only under its stated conditions — load, timing, and environment assumptions bound the claim."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Design for the worst case; measure the typical case."
  rationale: "Guarantees live at the worst case; observations describe the typical case."
  evidence_level: high
- heuristic: "Keep analysis assumptions explicit and re-audited."
  rationale: "Guarantee erosion is assumption drift in disguise."
  evidence_level: high

## Recommendations
- recommendation: "Express deadlines as constraints on completion, not as a special temporal category."
  context: modelling
  certainty: strong
  rationale: "The test is whether time requires new ontology — it does not; it requires constraints."
- recommendation: "Treat timing analyses as observations with confidence, not promises."
  context: engineering
  certainty: strong
  rationale: "WCET is an estimate; the guarantee is the claim that the estimate's conditions hold."
- recommendation: "Audit guarantee assumptions as the system changes."
  context: operations
  certainty: strong
  rationale: "A guarantee is valid only under stated conditions — unstated drift erodes it."
