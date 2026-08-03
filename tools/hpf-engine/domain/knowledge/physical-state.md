# Physical State

## Identity
- id: physical-state
- type: concept
- title: Physical State
- tags: [physical state, dynamics, state representation, continuous systems, estimation]
- entities: [state, state variables, dynamics, trajectory, snapshot]
- concepts: [cyber-physical-system, sensing, actuation, schema-design, deadline]

## Claims
- claim: "State is a snapshot of a system's condition at a point in time — a set of claims about the system, not a new knowledge type."
  certainty: high
  evidence: Control systems practice
  scope: cross-domain
- claim: "A differential equation is a constraint governing state evolution — dynamics bind how state may change, exactly as invariants bind data."
  certainty: high
  evidence: Cross-domain comparison (constraints as invariants)
  scope: cross-domain
- claim: "State is never directly known in a cyber-physical system — it is always estimated from observations through a model."
  certainty: high
  evidence: State estimation theory (P5 epistemic separation)
  scope: cross-domain
- claim: "A state representation is a model of the world under stated conditions — the same structure as a schema."
  certainty: high
  evidence: Cross-domain comparison (schema-design 010)
  scope: cross-domain
- claim: "Continuous evolution is expressible as constraint relationships over discrete observations — continuity is mathematics, not ontology."
  certainty: high
  evidence: Discrete-time control and estimation practice
  scope: cross-domain

## Relationships
- concept: cyber-physical-system
  relationship: describes
  description: "Physical state describes the condition of the cyber-physical system over time."
- concept: sensing
  relationship: evaluated_through
  description: "Physical state is evaluated through sensing — indirect observation through models."
- concept: schema-design
  relationship: analogous_to
  description: "Physical state is analogous to schema design — both are models of the world under stated conditions — the Cycle 010 cross-domain link."
- concept: deadline
  relationship: constrained_by
  description: "State is constrained by deadlines — state updates are valid only within their timing windows — the Cycle 011 cross-domain link."
- concept: actuation
  relationship: informs
  description: "Physical state informs actuation — decisions act on the represented state."

## Tradeoffs
- dimension: fidelity_vs_observability
  options:
    rich_state:
      value: decision_quality
      rationale: "Rich state models support better decisions."
    observable_state:
      value: estimability
      rationale: "Only what can be observed from the world can be estimated."
  importance: high
- dimension: update_frequency_vs_cost
  options:
    frequent_updates:
      value: freshness
      rationale: "Frequent updates keep state current."
    sparse_updates:
      value: resource_use
      rationale: "Sparse updates conserve computation and bandwidth."
  importance: medium

## Failure Modes
- name: state_divergence
  description: "The represented state drifts from the physical state — the model's belief about the world no longer matches reality."
  likelihood: medium
  observable_evidence: "Prediction/observation mismatch; unexpected behaviour; estimator error growth"
  detection: "Innovation monitoring; cross-check against direct observations; divergence tests"
  recovery: "Re-initialize estimation; correct the model; restrict the operating envelope"
  retryable: true
- name: unobservable_state
  description: "Part of the state cannot be observed — some dimension of reality is outside the sensing channel."
  likelihood: medium
  observable_evidence: "Uncertainty growth on unobserved dimensions; blind spots in behaviour"
  detection: "Observability analysis; uncertainty tracking per state dimension"
  recovery: "Add sensing; accept the uncertainty; constrain actions on unobserved dimensions"
  retryable: false
- name: stale_state
  description: "The state snapshot is older than its validity window — decisions act on an outdated model of the world."
  likelihood: medium
  observable_evidence: "Timing violations in the control loop; actions based on outdated conditions"
  detection: "Update-timing monitoring; staleness checks against the sampling window"
  recovery: "Re-estimate; tighten the loop; reject decisions on stale state"
  retryable: true

## Observations
- observation: "State evolution under constraints is the discrete form of continuous dynamics — the differential equation is data, not ontology."
  confidence: high
  source: Cross-domain comparison (constraints 010, deadlines 011)
- observation: "The state representation carries the epistemic gap — every claim about state is a belief from a model, not a fact from the world."
  confidence: high
  source: State estimation theory
- observation: "Epistemic Distance for state is low but nonzero — the state claim sits one or two model layers above direct observation."
  confidence: medium
  source: Epistemic Distance metric (Cycle 012 pre-registration)

## Constraints
- constraint: "State evolution is governed by stated dynamics — the constraint set is the model, not a continuous primitive."
  type: invariant
  scope: cross-domain
- constraint: "A state claim is valid only for its stated instant and model — staleness or model change invalidates it."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Represent state as claims and constraints, never as a state block."
  rationale: "A snapshot is a set of claims; dynamics are constraints — both already exist."
  evidence_level: high
- heuristic: "Track which state dimensions are observable."
  rationale: "Unobservable dimensions accumulate uncertainty; knowing them bounds the claim."
  evidence_level: high

## Recommendations
- recommendation: "Model continuous dynamics as constraint relationships over state, not as a continuous category."
  context: modelling
  certainty: strong
  rationale: "Continuity is mathematics; constraints carry it into the graph."
- recommendation: "Qualify every state claim with its estimation confidence."
  context: engineering
  certainty: strong
  rationale: "State is belief from a model — confidence is the qualification that carries the epistemic gap."
- recommendation: "Reject decisions on stale state."
  context: operations
  certainty: strong
  rationale: "A state claim outside its validity window is invalid, exactly as a late result is."
