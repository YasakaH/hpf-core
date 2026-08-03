# Control-Scheduling Interaction

## Identity
- id: control-scheduling-interaction
- type: pattern
- title: Control-Scheduling Interaction
- tags: [control, scheduling, jitter, sampling period, temporal interaction]
- entities: [control loop, scheduling, sampling jitter, delay, period]
- concepts: [feedback-control, task-scheduling, deadline, closed-loop-guarantee, cyber-physical-system]

## Claims
- claim: "The control-scheduling interaction is where temporal guarantees (011) meet physical control (012) — the loop's correctness depends on when computations complete."
  certainty: high
  evidence: Real-time control systems practice
  scope: cross-domain
- claim: "Sampling jitter and delay are temporal constraints on the loop — the 011 deadline structure applied inside the control cycle."
  certainty: high
  evidence: Cross-domain comparison (deadline 011)
  scope: cross-domain
- claim: "The interaction is a composition pattern — scheduling constrains control timing, control demands scheduling service, neither is a new construct."
  certainty: high
  evidence: Pattern structure (temporal-isolation 011 precedent)
  scope: cross-domain
- claim: "The interaction's failure is temporal — jitter, missed periods, and delayed actuation degrade the loop before the logic fails."
  certainty: high
  evidence: Real-time control incident analyses
  scope: cross-domain
- claim: "Temporal constraint density rises at this tier — the interaction tier is the temporal-epistemic junction, reconnecting 012 to the 011 signal."
  certainty: high
  evidence: Temporal Constraint Density metric (Cycle 012)
  scope: cross-domain

## Relationships
- concept: feedback-control
  relationship: afflicts
  description: "The control-scheduling interaction afflicts feedback control — scheduling degradation disturbs the loop."
- concept: task-scheduling
  relationship: analogous_to
  description: "The control-scheduling interaction is analogous to task scheduling — allocation of computation to timing — the Cycle 011 cross-domain link."
- concept: deadline
  relationship: constrained_by
  description: "The control-scheduling interaction is constrained by deadlines — the loop period bounds validity — the Cycle 011 cross-domain link."
- concept: closed-loop-guarantee
  relationship: supports
  description: "The control-scheduling interaction supports closed-loop-guarantee — timing conditions are part of the scoped claim."
- concept: cyber-physical-system
  relationship: serves
  description: "The control-scheduling interaction serves the cyber-physical system — the junction where computation meets physical timing."

## Tradeoffs
- dimension: determinism_vs_utilization
  options:
    deterministic_schedule:
      value: guarantee_strength
      rationale: "Deterministic schedules hold the loop's timing."
    high_utilization:
      value: efficiency
      rationale: "High utilization packs more work."
  importance: high
- dimension: period_vs_responsiveness
  options:
    short_period:
      value: loop_speed
      rationale: "Short periods sample the world faster."
    long_period:
      value: resource_use
      rationale: "Long periods free computation."
  importance: medium

## Failure Modes
- name: jitter_induced_instability
  description: "Sampling jitter disturbs the loop enough to push it toward instability — the temporal variation degrades the physical guarantee."
  likelihood: medium
  observable_evidence: "Oscillation correlated with schedule variation; degraded margins under load"
  detection: "Jitter monitoring; stability margin tracking; schedule variation checks"
  recovery: "Stabilize the schedule; widen the margin; re-verify"
  retryable: true
- name: missed_period
  description: "The loop misses its period — a control update is not produced in time, and the world runs on stale commands."
  likelihood: medium
  observable_evidence: "Late or absent updates; degraded tracking; temporal violations"
  detection: "Period monitoring; deadline checks; update tracking"
  recovery: "Re-schedule; reduce load; degrade the loop's mode"
  retryable: true
- name: delayed_actuation
  description: "The correction arrives after its validity window — actuation acts on stale error."
  likelihood: medium
  observable_evidence: "Lag between error and effect; temporal violations; degraded tracking"
  detection: "Timing monitoring; loop-period checks; staleness tracking"
  recovery: "Speed the cycle; re-schedule; widen the period validity"
  retryable: true

## Observations
- observation: "The interaction resolved as composition — the 011 deadline structure applied inside the control cycle, no interaction construct."
  confidence: high
  source: P4 test (Cycle 012)
- observation: "The temporal-epistemic junction is real — the loop's timing conditions are stated conditions on its guarantee, and the temporal density reading reflects it."
  confidence: high
  source: Temporal Constraint Density metric (Cycle 012)
- observation: "Jitter is the interaction's signature failure — it is the temporal form of disturbance, degrading the loop before logic fails."
  confidence: high
  source: Real-time control practice
- observation: "Epistemic Distance at the interaction is 1–2 — timing is the directly observable dimension of the loop, closer to reality than the belief it carries."
  confidence: high
  source: Epistemic Distance metric (Cycle 012)

## Constraints
- constraint: "The control loop's temporal behaviour is a stated condition on its guarantees — jitter and delay bound the claim."
  type: invariant
  scope: cross-domain
- constraint: "A loop whose timing conditions are unstated has no guarantee."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Schedule the loop before tuning the loop."
  rationale: "Timing conditions bound the guarantee — they are part of the claim, not an afterthought."
  evidence_level: high
- heuristic: "Measure jitter as a disturbance."
  rationale: "Jitter is temporal variation — a disturbance the stability margin must absorb."
  evidence_level: high

## Recommendations
- recommendation: "Represent the interaction as relationships between the control and scheduling corpora — no interaction construct."
  context: modelling
  certainty: strong
  rationale: "The junction is composition of existing structures (011 + 012)."
- recommendation: "Declare the loop's timing conditions with the guarantee."
  context: engineering
  certainty: strong
  rationale: "An unstated timing condition is an unbounded claim."
- recommendation: "Monitor jitter as a first-class disturbance."
  context: operations
  certainty: strong
  rationale: "The temporal failure appears before the logical one — timing monitoring is early warning."
