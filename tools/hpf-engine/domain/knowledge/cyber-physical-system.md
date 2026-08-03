# Cyber-Physical System

## Identity
- id: cyber-physical-system
- type: concept
- title: Cyber-Physical System
- tags: [cyber-physical systems, robotics, physical dynamics, sensing, actuation, autonomous systems]
- entities: [cyber-physical system, plant, controller, sensor, actuator, physical world]
- concepts: [physical-state, sensing, actuation, real-time-system, schema-design, deployment-risk]

## Claims
- claim: "A cyber-physical system is a system whose correctness depends on continuous interaction with an external physical world — sensing, computation, and actuation in one loop."
  certainty: high
  evidence: Robotics and control systems practice
  scope: cross-domain
- claim: "The physical plant is part of the system: the boundary between computer and world is architectural, not epistemic — no new knowledge type separates them."
  certainty: high
  evidence: Cyber-physical systems literature (P9 layering test)
  scope: cross-domain
- claim: "Correctness in a cyber-physical system is a claim about behaviour in the physical world, bound by stated conditions about dynamics, environment, and timing."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain
- claim: "The system's knowledge about the world is always indirect — internal belief is derived from sensors through models, never observed directly."
  certainty: high
  evidence: State estimation theory (P5 epistemic separation)
  scope: cross-domain
- claim: "Cyber-physical guarantees are the unification-hypothesis test at the physical pole — valid if stated conditions hold, exactly as knowledge (008), actions (009), data (010), and completion (011) are."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain

## Relationships
- concept: physical-state
  relationship: requires
  description: "A cyber-physical system requires a representation of its state — the model of reality that decisions operate on."
- concept: sensing
  relationship: requires
  description: "A cyber-physical system requires sensing — observation of the world is the only evidence channel."
- concept: actuation
  relationship: requires
  description: "A cyber-physical system requires actuation — decisions must act on the physical world."
- concept: real-time-system
  relationship: analogous_to
  description: "A cyber-physical system is analogous to a real-time system — correctness bound by stated conditions — the Cycle 011 cross-domain link."
- concept: schema-design
  relationship: analogous_to
  description: "A cyber-physical system is analogous to schema design — both hold a model of the world together — the Cycle 010 cross-domain link."

## Tradeoffs
- dimension: model_fidelity_vs_cost
  options:
    rich_model:
      value: correctness_margin
      rationale: "Rich models bound reality more tightly but cost more to maintain and verify."
    lean_model:
      value: tractability
      rationale: "Lean models are tractable but leave physical behaviour unmodelled."
  importance: high
- dimension: autonomy_vs_oversight
  options:
    autonomous_action:
      value: responsiveness
      rationale: "Autonomous action reacts at physical speed but acts on belief."
    human_oversight:
      value: accountability
      rationale: "Oversight verifies before acting but adds latency."
  importance: high

## Failure Modes
- name: sensor_denial
  description: "The system loses its observation channel — sensing fails or is blocked, and all knowledge about the world becomes stale."
  likelihood: medium
  observable_evidence: "Missing or frozen measurements; estimator divergence; confidence collapse"
  detection: "Sensor health monitoring; measurement plausibility checks; cross-sensor comparison"
  recovery: "Fall back to degraded estimation; invoke safe posture; declare degraded operation"
  retryable: true
- name: actuation_failure
  description: "A command is not applied to the world — the decision has no physical consequence."
  likelihood: medium
  observable_evidence: "No effect despite command; actuator error; mismatch between commanded and actual state"
  detection: "Actuator feedback; state divergence from expectation; effect monitoring"
  recovery: "Retry with idempotency discipline; switch actuation path; enter safe state"
  retryable: true
- name: model_mismatch
  description: "The system's model of the physical world diverges from reality — the epistemic gap widens past the model's stated conditions."
  likelihood: medium
  observable_evidence: "Prediction/observation mismatch; unexpected physical behaviour; estimator error growth"
  detection: "Innovation monitoring; model-vs-reality comparison; divergence checks"
  recovery: "Re-estimate with a better model; widen uncertainty; restrict operating envelope"
  retryable: true

## Observations
- observation: "The hardest object in cyber-physical systems is the system object itself — it must hold the physical world, sensing, and actuation together without a physical construct."
  confidence: high
  source: Cross-domain comparison (real-time-system 011, schema-design 010)
- observation: "Every claim the system makes about its world is built on belief, not direct knowledge — the epistemic gap is the cycle's central pressure."
  confidence: high
  source: State estimation theory
- observation: "Physical failure consequences are modelled as failure modes with physical effect — severity changes, structure does not."
  confidence: high
  source: Cyber-physical incident analyses
- observation: "Sensing and actuation bookend the epistemic chain: observation enters at sensing, action leaves at actuation, and the loop is the unit of knowledge."
  confidence: medium
  source: Epistemic Chain watch (Cycle 012 pre-registration)

## Constraints
- constraint: "Internal belief about the world is valid only under its model's stated conditions — model mismatch invalidates decisions, not the schema."
  type: invariant
  scope: cross-domain
- constraint: "Every physical action is taken on a belief, never on direct knowledge of reality — the epistemic gap is closed by verification, not eliminated."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Model the plant as part of the system."
  rationale: "The boundary between computer and world is architectural; excluding the plant hides the conditions that bound correctness."
  evidence_level: high
- heuristic: "Close the epistemic gap with verification, not with stronger beliefs alone."
  rationale: "Better models reduce the gap; only verification against the world closes it."
  evidence_level: high

## Recommendations
- recommendation: "Express dynamics as constraints on state evolution, not as a continuous-state category."
  context: modelling
  certainty: strong
  rationale: "The test is whether continuous interaction requires new ontology — it does not; it requires constraints."
- recommendation: "Treat every internal belief as an observation of a model, qualified by confidence."
  context: engineering
  certainty: strong
  rationale: "Estimation is observation at an epistemic distance — qualification carries the distance."
- recommendation: "Verify against the physical world — the model is a claim, the world is the evidence."
  context: operations
  certainty: strong
  rationale: "Model mismatch is the failure mode behind the others; verification against reality is its only remedy."
