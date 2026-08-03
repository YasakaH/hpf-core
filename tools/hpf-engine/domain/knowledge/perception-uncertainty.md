# Perception Uncertainty

## Identity
- id: perception-uncertainty
- type: concept
- title: Perception Uncertainty
- tags: [perception, uncertainty, confidence, calibration, interpretation]
- entities: [perception, uncertainty, confidence, calibration, interpretation]
- concepts: [belief-state, sensing, confidence-calibration, uncertainty-estimation, incomplete-evidence]

## Claims
- claim: "Perception uncertainty is the qualification of observations at epistemic distance — confidence metadata over the chain from sensor to belief."
  certainty: high
  evidence: Perception and estimation practice
  scope: cross-domain
- claim: "Uncertainty in perception is the same structure as uncertainty everywhere — the 007/008 qualification model applies unchanged."
  certainty: high
  evidence: Cross-domain comparison (qualification model 007/008)
  scope: cross-domain
- claim: "Perception is inference, and inference carries its uncertainty — the interpretation is a claim, qualified by confidence, never a fact."
  certainty: high
  evidence: Perception literature (P5)
  scope: cross-domain
- claim: "Uncertainty is not a failure of perception — it is the correct description of indirect observation."
  certainty: high
  evidence: Calibration practice (008)
  scope: cross-domain
- claim: "Perception claims are valid only under stated conditions — environment, sensor state, and model bound the interpretation."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain

## Relationships
- concept: belief-state
  relationship: afflicts
  description: "Perception uncertainty afflicts belief-state — the belief inherits the chain's uncertainty."
- concept: sensing
  relationship: constrained_by
  description: "Perception uncertainty is constrained by sensing — the chain's uncertainty begins at the sensor."
- concept: confidence-calibration
  relationship: analogous_to
  description: "Perception uncertainty is analogous to confidence calibration — honesty of the qualification — the Cycle 008 cross-domain link."
- concept: uncertainty-estimation
  relationship: analogous_to
  description: "Perception uncertainty is analogous to uncertainty estimation — measuring the distance — the Cycle 008 cross-domain link."
- concept: incomplete-evidence
  relationship: constrained_by
  description: "Perception uncertainty is constrained by incomplete evidence — perception interprets a partial world."

## Tradeoffs
- dimension: sharpness_vs_calibration
  options:
    sharp_interpretation:
      value: decisive_action
      rationale: "Sharp interpretations act decisively."
    calibrated_interpretation:
      value: honesty
      rationale: "Calibrated interpretations report the true distance."
  importance: high
- dimension: computation_vs_uncertainty_tightness
  options:
    heavy_computation:
      value: tight_bounds
      rationale: "Heavy computation tightens the uncertainty estimate."
    light_computation:
      value: loop_speed
      rationale: "Light computation keeps the loop fast."
  importance: medium

## Failure Modes
- name: overconfidence
  description: "The perception is sharper than its evidence — confidence exceeds what the observation chain justifies."
  likelihood: medium
  observable_evidence: "Surprise despite confidence; sharp interpretations on weak evidence; misclassification at speed"
  detection: "Calibration audits; confidence-vs-outcome tracking; ambiguity review"
  recovery: "Widen uncertainty; recalibrate; slow the interpretation"
  retryable: true
- name: unmodeled_uncertainty
  description: "Uncertainty sources outside the model — the reported confidence does not cover what the world actually varies."
  likelihood: medium
  observable_evidence: "Errors beyond stated bounds; unexpected environment effects; model under-coverage"
  detection: "Residual analysis; out-of-distribution checks; bound audits"
  recovery: "Extend the model; widen bounds; restrict the operating envelope"
  retryable: true
- name: ambiguity_misclassification
  description: "The interpretation commits to one reading of an ambiguous signal — the belief collapses before the evidence does."
  likelihood: medium
  observable_evidence: "Wrong-but-confident interpretations; sensitivity to noise; disagreement across contexts"
  detection: "Ambiguity tracking; multi-hypothesis checks; entropy monitoring"
  recovery: "Hold the ambiguity; gather evidence; delay commitment"
  retryable: true

## Observations
- observation: "Perception uncertainty is the qualification pole re-test — the 007/008 uncertainty model at the epistemic chain, unchanged."
  confidence: high
  source: Cross-domain comparison (007, 008)
- observation: "Epistemic Distance at perception is 2+ — the interpretation sits two or more layers above reality, and confidence carries the distance."
  confidence: high
  source: Epistemic Distance metric (Cycle 012 pre-registration)
- observation: "Calibration is the honesty of perception — overconfidence is a qualification failure, not a perception failure."
  confidence: high
  source: Calibration practice (008)
- observation: "Ambiguity is information — holding it is a decision, collapsing it early is a failure."
  confidence: high
  source: Perception practice

## Constraints
- constraint: "Calibration is the honesty of the belief — overconfidence is a qualification failure, not a perception failure."
  type: invariant
  scope: cross-domain
- constraint: "Uncertainty is metadata about the observation chain — it describes the distance, it does not remove it."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Report uncertainty with the perception."
  rationale: "A perception without its confidence is an unbounded claim at distance."
  evidence_level: high
- heuristic: "Assume what is not modelled is unknown."
  rationale: "Unmodeled uncertainty is the failure that out-of-distribution events expose."
  evidence_level: high

## Recommendations
- recommendation: "Represent perception uncertainty as qualification of observation — confidence metadata, not a perception construct."
  context: modelling
  certainty: strong
  rationale: "The qualification model from 007/008 carries the chain's distance."
- recommendation: "Audit calibration, and treat overconfidence as the priority failure mode."
  context: engineering
  certainty: strong
  rationale: "Overconfidence at distance produces the physical surprises the domain is known for."
- recommendation: "Hold ambiguity until the evidence resolves it."
  context: operations
  certainty: strong
  rationale: "Committing on ambiguity is a belief collapse; the evidence is never complete."
