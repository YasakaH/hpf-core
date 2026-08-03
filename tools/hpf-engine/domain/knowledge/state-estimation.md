# State Estimation

## Identity
- id: state-estimation
- type: concept
- title: State Estimation
- tags: [state estimation, estimation, inference, observers, belief]
- entities: [state estimate, estimator, measurement, innovation, filter]
- concepts: [belief-state, sensing, physical-state, query-planning, deadline]

## Claims
- claim: "State estimation is inference of a system's state from observations through a model — a claim built from qualified observations under stated conditions."
  certainty: high
  evidence: Estimation theory and practice
  scope: cross-domain
- claim: "An estimator is a relationship structure — observations flow into belief through a model — not a new knowledge type."
  certainty: high
  evidence: Cross-domain comparison (relationships as structure)
  scope: cross-domain
- claim: "The estimate is an observation of the model, qualified by its confidence — the epistemic chain at work: reality → sensor → model → belief."
  certainty: high
  evidence: State estimation theory (P5 epistemic separation)
  scope: cross-domain
- claim: "An estimate is a hypothesis about state, exactly as a plan is a hypothesis about cost — runtime evidence can falsify it."
  certainty: high
  evidence: Cross-domain comparison (query-planning 010, WCET 011 — prediction-object family)
  scope: cross-domain
- claim: "An estimate is valid only under its model's stated conditions — model mismatch invalidates the belief, exactly as schema mismatch invalidates data."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 010)
  scope: cross-domain

## Relationships
- concept: belief-state
  relationship: produces
  description: "State estimation produces belief-state — the internal model of the world that decisions operate on."
- concept: sensing
  relationship: evaluated_through
  description: "State estimation is evaluated through sensing — observations flow into the estimate."
- concept: query-planning
  relationship: analogous_to
  description: "State estimation is analogous to query planning — the estimate is a hypothesis about state, the plan a hypothesis about cost — the Cycle 010 cross-domain link."
- concept: physical-state
  relationship: describes
  description: "State estimation describes physical state — the belief is about the state, never the state itself."
- concept: deadline
  relationship: constrained_by
  description: "State estimation is constrained by deadlines — the estimate is valid only within the loop period — the Cycle 011 cross-domain link."

## Tradeoffs
- dimension: model_richness_vs_tractability
  options:
    rich_model:
      value: estimate_quality
      rationale: "Rich models capture more dynamics."
    tractable_model:
      value: computability
      rationale: "Tractable models run within the loop period."
  importance: high
- dimension: speed_vs_confidence
  options:
    fast_estimate:
      value: freshness
      rationale: "Fast estimates act within the loop."
    confident_estimate:
      value: accuracy
      rationale: "Confident estimates wait for more evidence."
  importance: medium

## Failure Modes
- name: estimator_divergence
  description: "The estimate departs from the physical state — the belief and reality separate beyond the model's stated conditions."
  likelihood: medium
  observable_evidence: "Innovation growth; prediction/observation mismatch; belief drift"
  detection: "Innovation monitoring; divergence tests; cross-source comparison"
  recovery: "Re-initialize the estimator; correct the model; restrict the envelope"
  retryable: true
- name: unobservable_dimensions
  description: "Some state dimensions are outside the sensing channel — the belief on those dimensions is prior guess, not evidence."
  likelihood: medium
  observable_evidence: "Uncertainty growth on unobserved dimensions; blind behaviour"
  detection: "Observability analysis; per-dimension uncertainty tracking"
  recovery: "Add sensing; widen uncertainty; constrain actions on unobserved dimensions"
  retryable: false
- name: model_mismatch
  description: "The estimator's model no longer matches the physical plant — every future estimate inherits the error."
  likelihood: medium
  observable_evidence: "Systematic bias; residual structure; performance decay"
  detection: "Residual analysis; model-vs-plant comparison; audit"
  recovery: "Re-identify the model; re-calibrate; restrict operations"
  retryable: true

## Observations
- observation: "The estimate is an observation of the model, not of reality — Epistemic Distance at estimation is 2–3: reality → sensor → model → belief."
  confidence: high
  source: Epistemic Distance metric (Cycle 012 pre-registration)
- observation: "Estimation pressure maps into qualification — the confidence on the estimate carries the entire epistemic gap."
  confidence: high
  source: P5 test (Cycle 012)
- observation: "The prediction-object structure holds at n=4 — estimates join benchmarks (008), plans (010), and WCET (011) as models of the world feeding a decision."
  confidence: high
  source: Cross-domain comparison (008, 010, 011)
- observation: "Estimator divergence is the estimation form of model mismatch — the failure family is one structure across the corpus."
  confidence: high
  source: Cross-domain comparison (failure modes)

## Constraints
- constraint: "An estimate is valid only under its model's stated conditions — divergence invalidates the belief."
  type: invariant
  scope: cross-domain
- constraint: "The estimate is never the state — belief and reality remain separated by the model, and the separation is carried by qualification."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Carry the model's assumptions with the estimate."
  rationale: "An estimate without its stated conditions is an unbounded claim."
  evidence_level: high
- heuristic: "Monitor innovation — it is the evidence of divergence."
  rationale: "Prediction/observation mismatch is the earliest signal of model failure."
  evidence_level: high

## Recommendations
- recommendation: "Represent estimation as claim + qualified observations + constraints, not as an estimator construct."
  context: modelling
  certainty: strong
  rationale: "The estimator is a relationship structure; the confidence carries the distance."
- recommendation: "Treat the estimate as a hypothesis that runtime evidence can falsify."
  context: engineering
  certainty: strong
  rationale: "The prediction-object structure (008/010/011) applies unchanged."
- recommendation: "Widen uncertainty before acting on distant belief."
  context: operations
  certainty: strong
  rationale: "Overconfidence at distance is the qualification failure that produces physical surprises."
