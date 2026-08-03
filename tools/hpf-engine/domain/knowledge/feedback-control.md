# Feedback Control

## Identity
- id: feedback-control
- type: concept
- title: Feedback Control
- tags: [feedback control, closed loop, control, error signal, controller]
- entities: [closed loop, controller, reference, error signal, correction]
- concepts: [cyber-physical-system, sensing, belief-state, actuation, model-monitoring, deadline]

## Claims
- claim: "Feedback control is the closed-loop structure — observation, comparison against a reference, and corrective action, repeated."
  certainty: high
  evidence: Control systems practice
  scope: cross-domain
- claim: "The error signal is an observation of divergence — the difference between belief and reference, qualified by measurement uncertainty."
  certainty: high
  evidence: Control theory (P5 — error as observation)
  scope: cross-domain
- claim: "A controller is a relationship structure — the mapping from observed error to corrective command — not a new knowledge type."
  certainty: high
  evidence: Cross-domain comparison (relationships as structure)
  scope: cross-domain
- claim: "The closed loop is the unit of cyber-physical knowledge — each cycle senses, compares, acts, and observes again."
  certainty: high
  evidence: Epistemic Chain watch (Cycle 012)
  scope: cross-domain
- claim: "Feedback control is valid only under its stated conditions — plant model, measurement quality, and timing bound the loop's correctness."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain

## Relationships
- concept: cyber-physical-system
  relationship: serves
  description: "Feedback control serves the cyber-physical system — the loop that keeps the plant within its envelope."
- concept: actuation
  relationship: directs
  description: "Feedback control directs actuation — the corrective command is the loop's output to the world."
- concept: belief-state
  relationship: evaluated_through
  description: "Feedback control is evaluated through belief-state — the loop compares the internal model against the reference."
- concept: model-monitoring
  relationship: analogous_to
  description: "Feedback control is analogous to model monitoring — the observe-compare-act loop — the Cycle 008 cross-domain link."
- concept: deadline
  relationship: constrained_by
  description: "Feedback control is constrained by deadlines — the loop period bounds when corrections are valid — the Cycle 011 cross-domain link."

## Tradeoffs
- dimension: gain_vs_stability_margin
  options:
    high_gain:
      value: responsiveness
      rationale: "High gain corrects errors fast."
    low_gain:
      value: stability_margin
      rationale: "Low gain keeps the loop stable."
  importance: high
- dimension: measurement_use_vs_delay
  options:
    fresh_measurement:
      value: accuracy
      rationale: "Fresh measurements correct accurately."
    fast_cycle:
      value: loop_speed
      rationale: "Fast cycles act quickly."
  importance: medium

## Failure Modes
- name: loop_instability
  description: "The loop amplifies rather than corrects — the closed loop diverges from the reference."
  likelihood: medium
  observable_evidence: "Growing oscillations; divergent response; correction overshoot"
  detection: "Stability monitoring; gain audits; oscillation detection"
  recovery: "Reduce gain; re-tune; verify stability analysis"
  retryable: true
- name: windup
  description: "The correction accumulates past what the actuator can apply — the loop holds error it can no longer act on."
  likelihood: medium
  observable_evidence: "Sustained error at saturation; slow recovery after saturation ends; actuator limit"
  detection: "Saturation tracking; integral-state monitoring"
  recovery: "Anti-windup; reset the accumulated correction; re-plan"
  retryable: true
- name: delayed_correction
  description: "The correction arrives after its validity window — the loop acts on stale error."
  likelihood: medium
  observable_evidence: "Lag between error and effect; temporal violations; degraded tracking"
  detection: "Timing monitoring; loop-period checks; staleness tracking"
  recovery: "Speed the cycle; re-schedule; widen the period validity"
  retryable: true

## Observations
- observation: "The closed loop is the Epistemic Chain in operation — each cycle passes through sensing, belief, decision, and actuation."
  confidence: high
  source: Epistemic Chain watch (Cycle 012)
- observation: "The error signal is the loop's observation — divergence is measured, qualified, and corrected, never reified."
  confidence: high
  source: Control theory
- observation: "Epistemic Distance at the loop's belief is 2–3 — the correction acts on the internal model, at the same distance as estimation."
  confidence: high
  source: Epistemic Distance metric (Cycle 012)
- observation: "The loop is valid only under its timing conditions — control is where temporal guarantees (011) meet physical interaction (012)."
  confidence: high
  source: Cross-domain comparison (011, 012)

## Constraints
- constraint: "The closed loop is valid only under its stated conditions — plant model, measurement quality, and timing bound the loop's correctness."
  type: invariant
  scope: cross-domain
- constraint: "Every cycle of the loop acts on qualified belief — the epistemic gap is never closed by the loop, only managed within its conditions."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Tune for the stability margin, not the peak gain."
  rationale: "The loop must remain stable across the envelope, not just fast at one point."
  evidence_level: high
- heuristic: "Model the loop period as a condition on the correction."
  rationale: "A correction outside its timing window is invalid, exactly as a late result is."
  evidence_level: high

## Recommendations
- recommendation: "Represent feedback control as a relationship structure over observation and action — no controller construct."
  context: modelling
  certainty: strong
  rationale: "The loop is composition of existing primitives: sense, compare, act."
- recommendation: "Treat the error signal as qualified observation of divergence."
  context: engineering
  certainty: strong
  rationale: "The error carries measurement uncertainty — qualification, not a new type."
- recommendation: "State the loop's timing conditions with the loop."
  context: operations
  certainty: strong
  rationale: "Control is the temporal-epistemic junction — unstated timing invalidates the loop's claims."
