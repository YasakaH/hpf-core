# Fail-Safe

## Identity
- id: fail-safe
- type: pattern
- title: Fail-Safe
- tags: [fail-safe, failure posture, degraded mode, safety, recovery]
- entities: [fail-safe posture, degraded state, failure mode, recovery]
- concepts: [cyber-physical-system, safety-case, hard-vs-soft-real-time, debug-vs-release-modes, actuation]

## Claims
- claim: "Fail-safe is the posture a system takes under failure — a degraded-but-valid state, chosen by design, not a new construct."
  certainty: high
  evidence: Safety engineering practice
  scope: cross-domain
- claim: "A fail-safe posture is a mode-divergence result — the same pattern as debug-vs-release (009) and hard-vs-soft (011): the system changes posture by decision."
  certainty: high
  evidence: Cross-domain comparison (mode-divergence pattern 009, 011)
  scope: cross-domain
- claim: "Fail-safe validity is conditional — the degraded state is valid under its stated conditions (the failure), and its own claims hold under those conditions."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain
- claim: "The fail-safe structure is failure modes + postures + recovery relationships — composition of existing destinations."
  certainty: high
  evidence: Pattern structure (006, 010 precedent)
  scope: cross-domain
- claim: "Fail-safe is not safety — it is the bounded response to failure: the system remains valid, degraded, under stated conditions."
  certainty: high
  evidence: Safety engineering practice (P8)
  scope: cross-domain

## Relationships
- concept: cyber-physical-system
  relationship: serves
  description: "Fail-safe serves the cyber-physical system — the posture that keeps the system valid under failure."
- concept: safety-case
  relationship: supports
  description: "Fail-safe supports safety-case — the case covers the fail-safe posture and its conditions."
- concept: hard-vs-soft-real-time
  relationship: analogous_to
  description: "Fail-safe is analogous to hard-vs-soft real-time — posture chosen by decision — the Cycle 011 cross-domain link."
- concept: debug-vs-release-modes
  relationship: analogous_to
  description: "Fail-safe is analogous to debug-vs-release modes — the mode-divergence structure — the Cycle 009 cross-domain link."
- concept: actuation
  relationship: constrains
  description: "Fail-safe constrains actuation — the degraded posture bounds what the system may command."

## Tradeoffs
- dimension: availability_vs_safety_posture
  options:
    stay_available:
      value: service
      rationale: "Staying available keeps the system useful."
    shut_down:
      value: safety
      rationale: "Shutting down removes the hazard."
  importance: high
- dimension: degradation_depth_vs_recovery_speed
  options:
    deep_degradation:
      value: safety_margin
      rationale: "Deep degradation maximizes the safety margin."
    shallow_degradation:
      value: recovery_speed
      rationale: "Shallow degradation recovers faster."
  importance: medium

## Failure Modes
- name: unsafe_fallacy
  description: "The fail-safe posture is not actually safe — the degraded state still permits the hazard it was meant to prevent."
  likelihood: low
  observable_evidence: "Hazard reachable in degraded mode; assumptions violated; fail-safe masking"
  detection: "Posture audits; hazard analysis in degraded modes; assumption review"
  recovery: "Redesign the posture; add interlocks; re-verify the case"
  retryable: true
- name: stuck_in_degraded
  description: "The system never recovers from its fail-safe posture — the degraded state becomes permanent."
  likelihood: medium
  observable_evidence: "Prolonged degraded operation; missing recovery; silent degradation"
  detection: "Posture monitoring; recovery tracking; degraded-duration alerts"
  recovery: "Diagnose the cause; repair; restore full posture"
  retryable: true
- name: no_safe_state
  description: "The system has no valid degraded state — every posture is unsafe under the failure."
  likelihood: low
  observable_evidence: "No acceptable response; all postures hazardous; design gap"
  detection: "Posture enumeration; hazard review; design analysis"
  recovery: "Add a safe state; restrict the envelope; redesign"
  retryable: false

## Observations
- observation: "Fail-safe resolved as posture under failure — the mode-divergence pattern applied to failure, not a new construct."
  confidence: high
  source: Mode-divergence pattern (009, 011)
- observation: "The degraded state is itself a valid state under its conditions — fail-safe is bounded response, the circuit-breaker structure (006) in posture form."
  confidence: high
  source: Cross-domain comparison (006)
- observation: "Epistemic Distance at the fail-safe posture is low — the posture is a direct response to observable failure conditions."
  confidence: high
  source: Epistemic Distance metric (Cycle 012)
- observation: "The unsafe fallacy is the fail-safe characteristic failure — the posture is believed safe without being verified safe."
  confidence: high
  source: Safety incident analyses

## Constraints
- constraint: "The degraded posture is valid under its stated conditions — its own validity conditions hold in failure."
  type: invariant
  scope: cross-domain
- constraint: "Fail-safe is bounded response to failure — the posture must be verified, not assumed."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Verify the fail-safe posture, not only the nominal one."
  rationale: "The unsafe fallacy lives in the degraded state — the case must cover it."
  evidence_level: high
- heuristic: "Design the recovery with the failure."
  rationale: "A fail-safe without recovery is a permanent degradation."
  evidence_level: high

## Recommendations
- recommendation: "Represent fail-safe as failure modes + postures + recovery relationships."
  context: modelling
  certainty: strong
  rationale: "The posture structure is composition — the mode-divergence pattern in failure form."
- recommendation: "Verify the degraded state under its failure conditions."
  context: engineering
  certainty: strong
  rationale: "The unsafe fallacy is the failure mode that assumes without evidence."
- recommendation: "Track degraded duration as an operating signal."
  context: operations
  certainty: strong
  rationale: "Stuck-in-degraded is silent — duration monitoring makes it visible."
