# Real-Time Throughput Tradeoff

## Identity
- id: real-time-throughput-tradeoff
- type: decision
- title: Real-Time Throughput Tradeoff
- tags: [real-time systems, throughput, performance, timing, tradeoff]
- entities: [real-time throughput tradeoff, throughput, deadline margin, resource budget]
- concepts: [real-time-guarantee, deadline, hard-vs-soft-real-time, optimization-tradeoffs, compiler-performance]
- decision-factors:
  - timing_sensitivity
  - throughput_target
  - resource_budget
  - deadline_margin

## Claims
- claim: "The real-time throughput tradeoff is a decision — how much throughput to trade for timing guarantee — not a property of the system."
  certainty: high
  evidence: Cross-domain comparison (decision objects 007-011)
  scope: cross-domain
- claim: "Timing and throughput are in tension — headroom for guarantees costs throughput; throughput pressure erodes guarantees."
  certainty: high
  evidence: Real-time systems practice
  scope: cross-domain
- claim: "The decision carries four factors — timing_sensitivity, throughput_target, resource_budget, and deadline_margin — the decision-object pattern at 4."
  certainty: high
  evidence: Cross-domain comparison (decision objects 007-011)
  scope: cross-domain
- claim: "The decision is structurally identical to optimization-tradeoffs — a performance posture decision — the Cycle 009 cross-domain link."
  certainty: high
  evidence: Cross-domain comparison (optimization-tradeoffs 009)
  scope: cross-domain
- claim: "Throughput is measured; the guarantee is claimed — the two live in different evidence layers, so the tradeoff is between an observation and a claim."
  certainty: high
  evidence: Cross-domain comparison (performance as observation 009)
  scope: cross-domain

## Relationships
- concept: real-time-guarantee
  relationship: trades_against
  description: "The real-time throughput tradeoff trades throughput against the real-time guarantee — the tension is the decision."
- concept: deadline
  relationship: preserves
  description: "The real-time throughput tradeoff preserves the deadline — the margin is the protection."
- concept: hard-vs-soft-real-time
  relationship: depends_on
  description: "The real-time throughput tradeoff depends on the posture — hard and soft systems trade differently."
- concept: optimization-tradeoffs
  relationship: analogous_to
  description: "The real-time throughput tradeoff is analogous to optimization tradeoffs — a performance posture decision — the Cycle 009 cross-domain link."
- concept: compiler-performance
  relationship: analogous_to
  description: "The real-time throughput tradeoff is analogous to compiler performance — throughput vs quality of service — the Cycle 009 cross-domain link."

## Tradeoffs
- dimension: deadline_margin_vs_throughput
  options:
    wide_margin:
      value: guarantee_strength
      rationale: "Wide margins protect guarantees but reduce throughput."
    tight_margin:
      value: throughput
      rationale: "Tight margins maximize throughput but risk misses."
  importance: high
- dimension: resource_budget_vs_timing
  options:
    budget_for_timing:
      value: guarantee
      rationale: "Budgeting for timing reserves capacity for the guarantee."
    budget_for_throughput:
      value: performance
      rationale: "Budgeting for throughput uses capacity for work."
  importance: high

## Failure Modes
- name: margin_erosion
  description: "Deadline margin silently shrinks — throughput pressure consumes the protection."
  likelihood: medium
  observable_evidence: "Growing miss probability; shrinking slack; late regressions"
  detection: "Margin monitoring; slack tracking"
  recovery: "Restore margin; re-balance the tradeoff"
  retryable: true
- name: throughput_illusion
  description: "Throughput is pursued at the cost of guarantees — the measured rate improves while the claim erodes."
  likelihood: medium
  observable_evidence: "Good throughput with eroding timing; miss growth"
  detection: "Dual-layer review; guarantee audits"
  recovery: "Re-balance; re-verify the guarantee"
  retryable: true
- name: undecided_tradeoff
  description: "The tradeoff is never decided — the system drifts between postures without a policy."
  likelihood: medium
  observable_evidence: "Inconsistent performance; unowned tradeoff; drift"
  detection: "Decision audits; posture review"
  recovery: "Make the decision; document the factors"
  retryable: true

## Observations
- observation: "Throughput is measured, the guarantee is claimed — the tradeoff crosses evidence layers."
  confidence: high
  source: Cross-domain comparison (performance as observation 009)
- observation: "The decision-object pattern holds at four factors across every domain — the factor count is the pattern."
  confidence: high
  source: Cross-domain comparison (decision objects 007-011)
- observation: "Margin is the real protection — the tradeoff is really about how much margin the system keeps."
  confidence: high
  source: Real-time systems practice

## Constraints
- constraint: "The guarantee is valid only with its margin — a margin below its stated bound invalidates the claim."
  type: invariant
  scope: cross-domain
- constraint: "The tradeoff must be decided — an undecided tradeoff is a drift in progress."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Protect the margin; measure the throughput."
  rationale: "The margin is the guarantee's protection; the throughput is its cost."
  evidence_level: high
- heuristic: "Re-decide the tradeoff when workload changes."
  rationale: "A stale tradeoff is an eroding guarantee."
  evidence_level: high

## Recommendations
- recommendation: "Treat the tradeoff as a decision with stated factors."
  context: engineering
  certainty: strong
  rationale: "The tradeoff is a decision; decisions need factors and re-decision."
- recommendation: "Monitor margin as a first-class signal."
  context: operations
  certainty: strong
  rationale: "Margin erosion is the guarantee's early warning."
- recommendation: "Keep throughput measurement separate from guarantee claims."
  context: engineering
  certainty: strong
  rationale: "Mixing the observation layer with the claim layer is the illusion."
