# Sensing

## Identity
- id: sensing
- type: concept
- title: Sensing
- tags: [sensing, sensors, observation, measurement, noise, perception]
- entities: [sensor, measurement, noise, calibration, sensor model]
- concepts: [cyber-physical-system, physical-state, model-monitoring, deployment-risk, deadline]

## Claims
- claim: "A sensor is the source of observation — its output is the first evidence about the physical world, always qualified by noise and calibration."
  certainty: high
  evidence: Measurement and sensing practice
  scope: cross-domain
- claim: "Sensing is observation at its epistemic limit — the sensor never reports reality, only a measurement of it under stated conditions."
  certainty: high
  evidence: State estimation theory (P5 epistemic separation)
  scope: cross-domain
- claim: "Sensor uncertainty is qualification of observation — noise and drift are confidence metadata, not a new evidence type."
  certainty: high
  evidence: Cross-domain comparison (qualification 007, uncertainty 008)
  scope: cross-domain
- claim: "Sensing is the base of the Epistemic Chain — every claim about the physical world derives from observations that begin here."
  certainty: high
  evidence: Epistemic Chain watch (Cycle 012 pre-registration)
  scope: cross-domain
- claim: "A measurement is valid only under stated conditions — calibration, environment, and the sensor model bound the observation."
  certainty: high
  evidence: Cross-domain comparison (observation-model scoping 009)
  scope: cross-domain

## Relationships
- concept: cyber-physical-system
  relationship: serves
  description: "Sensing serves the cyber-physical system — the only evidence channel about the world."
- concept: physical-state
  relationship: informs
  description: "Sensing informs physical state — observations feed the state representation."
- concept: model-monitoring
  relationship: analogous_to
  description: "Sensing is analogous to model monitoring — both derive observations about a system from indirect signals — the Cycle 008 cross-domain link."
- concept: deployment-risk
  relationship: affected_by
  description: "Sensing is affected by deployment risk — physical environment conditions bound sensor validity — the Cycle 008 cross-domain link."
- concept: deadline
  relationship: constrained_by
  description: "Sensing is constrained by deadlines — measurements are valid only within their sampling windows — the Cycle 011 cross-domain link."

## Tradeoffs
- dimension: measurement_frequency_vs_bandwidth
  options:
    high_frequency:
      value: freshness
      rationale: "Frequent sampling keeps the world current."
    low_frequency:
      value: resource_use
      rationale: "Sparse sampling conserves bandwidth and power."
  importance: high
- dimension: sensitivity_vs_robustness
  options:
    sensitive_sensor:
      value: signal_detail
      rationale: "Sensitive sensors capture weak signals."
    robust_sensor:
      value: noise_rejection
      rationale: "Robust sensors tolerate harsh environments."
  importance: medium

## Failure Modes
- name: sensor_failure
  description: "The sensor produces no usable measurement — the observation channel to the world is broken."
  likelihood: medium
  observable_evidence: "Missing or frozen measurements; invalid readings; sensor health alarms"
  detection: "Health monitoring; plausibility checks; cross-sensor agreement"
  recovery: "Degraded estimation; sensor replacement; safe posture"
  retryable: true
- name: measurement_noise
  description: "The measurement carries error beyond its stated model — the observation's confidence metadata no longer bounds reality."
  likelihood: high
  observable_evidence: "Jitter; outliers; variance beyond the sensor model"
  detection: "Innovation monitoring; residual tests; noise estimation"
  recovery: "Reject outliers; widen uncertainty; recalibrate"
  retryable: true
- name: calibration_drift
  description: "The sensor model drifts from the physical sensor — the measurement is systematically wrong while appearing valid."
  likelihood: medium
  observable_evidence: "Slow bias; systematic mismatch with other sensors; performance decay"
  detection: "Cross-sensor comparison; calibration audits; drift tests"
  recovery: "Recalibrate; update the sensor model; mark measurements suspect"
  retryable: true

## Observations
- observation: "The sensor is where observation begins and where the epistemic gap is born — its output is a qualified measurement, not reality."
  confidence: high
  source: Measurement theory
- observation: "Epistemic Distance at sensing is exactly one — the measurement is the first inferential layer above physical reality."
  confidence: medium
  source: Epistemic Distance metric (Cycle 012 pre-registration)
- observation: "Noise and drift are the same qualification problem as uncertainty elsewhere — confidence metadata, never a new evidence type."
  confidence: high
  source: Cross-domain comparison (007, 008)
- observation: "Sensing failure is the entry point of the cyber-physical failure chain — sensor denial propagates to state, decision, and actuation."
  confidence: high
  source: Cyber-physical incident analyses

## Constraints
- constraint: "A measurement is valid only under its sensor model and calibration — unstated drift invalidates it."
  type: invariant
  scope: cross-domain
- constraint: "Observation never touches reality directly — every claim about the world carries the epistemic gap from sensor to belief."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Model the sensor before trusting the measurement."
  rationale: "A measurement without a stated sensor model is an unbounded claim."
  evidence_level: high
- heuristic: "Cross-check sensors against each other."
  rationale: "Calibration drift is invisible in a single channel; agreement across channels bounds it."
  evidence_level: high

## Recommendations
- recommendation: "Represent sensor output as qualified observation — the measurement is evidence with confidence, not a fact."
  context: modelling
  certainty: strong
  rationale: "The sensor is an observation source; the qualification carries noise and calibration."
- recommendation: "Track calibration drift as a failure mode, not an adjustment."
  context: engineering
  certainty: strong
  rationale: "Drift is systematic invalidation of the observation — it must be visible."
- recommendation: "Bound every claim about the world with the sensing conditions it rests on."
  context: operations
  certainty: strong
  rationale: "Measurement validity is a stated-condition claim — the observation-model scoping from 009."
