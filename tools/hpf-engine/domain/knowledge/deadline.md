# Deadline

## Identity
- id: deadline
- type: concept
- title: Deadline
- tags: [real-time systems, deadline, temporal constraints, validity conditions, timing]
- entities: [deadline, completion time, timing requirement, deadline miss, release time]
- concepts: [real-time-system, task-scheduling, worst-case-execution-time, transactions, backup-recovery]

## Claims
- claim: "A deadline is a timing requirement on completion — a boundary that separates valid from invalid results."
  certainty: high
  evidence: Real-time systems literature
  scope: cross-domain
- claim: "A deadline is a constraint whose content happens to mention time — not a new evidence kind."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-010)
  scope: cross-domain
- claim: "A deadline miss is a correctness failure — the result is invalid regardless of its logical content."
  certainty: high
  evidence: Real-time correctness definitions
  scope: cross-domain
- claim: "Deadline validity is the unification-hypothesis test at the temporal pole — completion <= T is a validity condition on the result, exactly as schema validity is on data."
  certainty: high
  evidence: Cross-domain comparison (validity-as-derivation 010)
  scope: cross-domain
- claim: "Deadlines vary in strength — hard deadlines make misses failures; soft deadlines tolerate misses with bounded degradation."
  certainty: high
  evidence: Real-time systems practice
  scope: cross-domain

## Relationships
- concept: real-time-system
  relationship: constrains
  description: "A deadline constrains the real-time system — timing requirements bound correctness."
- concept: task-scheduling
  relationship: guides
  description: "A deadline guides task scheduling — allocation decisions serve deadline satisfaction."
- concept: worst-case-execution-time
  relationship: compared_with
  description: "A deadline is compared with WCET — the analysis checks completion within the bound."
- concept: transactions
  relationship: analogous_to
  description: "A deadline is analogous to transaction boundaries — both are constraints on outcome validity, not durations — the Cycle 010 cross-domain link."
- concept: backup-recovery
  relationship: analogous_to
  description: "A deadline is analogous to recovery contracts — both are time-bounded validity conditions — the Cycle 010 cross-domain link."

## Tradeoffs
- dimension: deadline_tightness_vs_feasibility
  options:
    tight_deadline:
      value: responsiveness
      rationale: "Tight deadlines bound response time but may be infeasible under load."
    loose_deadline:
      value: schedulability
      rationale: "Loose deadlines are schedulable but weaken the timing contract."
  importance: high
- dimension: hard_vs_soft_deadline
  options:
    hard_deadline:
      value: correctness
      rationale: "Hard deadlines make misses failures — strong but rigid."
    soft_deadline:
      value: resource_use
      rationale: "Soft deadlines tolerate misses — flexible but weaker."
  importance: high

## Failure Modes
- name: deadline_miss
  description: "Completion time exceeds the deadline — the result is invalid even if logically correct."
  likelihood: high
  observable_evidence: "Late results; timing violations; downstream timing failures"
  detection: "Deadline monitoring; completion-time instrumentation"
  recovery: "Relax the requirement; re-schedule; reduce load"
  retryable: true
- name: implied_deadline
  description: "A deadline exists but is unstated — consumers assume timing the system does not promise."
  likelihood: medium
  observable_evidence: "Surprise timing failures; implicit timing expectations; missed promises"
  detection: "Contract audits; consumer expectation review"
  recovery: "State the deadline explicitly; align expectations"
  retryable: true
- name: deadline_erosion
  description: "The deadline stays fixed while the system slows — the constraint becomes infeasible by drift."
  likelihood: medium
  observable_evidence: "Growing miss rate; feasibility loss over time; late regressions"
  detection: "Feasibility re-checks; miss-rate monitoring"
  recovery: "Re-analyse; re-negotiate the contract; repair the drift"
  retryable: true

## Observations
- observation: "A deadline is a validity condition, not a duration — 'completion <= T' bounds the outcome, exactly like transaction outcomes (010)."
  confidence: high
  source: Cross-domain comparison (temporal-trap resolutions 005/008/009/010)
- observation: "Deadlines are the temporal pole of the unification hypothesis — if completion <= T resolves as a constraint, time joins validity conditions."
  confidence: high
  source: Cross-domain comparison (validity conditions 008-010)
- observation: "The word 'time' appearing in constraint content is not ontology — the test is whether time requires a new category, and it does not."
  confidence: high
  source: Hidden-primitive-through-language watch (Cycle 011 pre-registration)

## Constraints
- constraint: "A result produced after its deadline is invalid — temporal correctness is a validity condition."
  type: invariant
  scope: cross-domain
- constraint: "Deadline validity is bound by stated conditions — load, timing, and environment assumptions qualify the deadline."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "State deadlines explicitly; assume nothing about implied timing."
  rationale: "Implied deadlines are surprise failures."
  evidence_level: high
- heuristic: "Re-check feasibility when the system changes."
  rationale: "Deadline erosion is drift that must be repaired, not accepted."
  evidence_level: high

## Recommendations
- recommendation: "Model a deadline as a constraint on completion — never as a temporal primitive."
  context: modelling
  certainty: strong
  rationale: "The unification hypothesis requires time to resolve as a condition, not a category."
- recommendation: "Treat deadline misses as correctness failures, not quality issues."
  context: engineering
  certainty: strong
  rationale: "A deadline miss invalidates the result; the failure mode is the anchor."
- recommendation: "Bind deadlines by their stated conditions and audit them."
  context: operations
  certainty: strong
  rationale: "An unstated or drifted condition voids the deadline's validity."
