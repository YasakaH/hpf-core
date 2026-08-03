# Confidence Threshold Decision

## Identity
- id: confidence-threshold
- type: decision
- title: Confidence Threshold Decision
- tags: [confidence, threshold, decision, artifact analysis, qualification, action]
- entities: [confidence threshold, action threshold, confidence cut-off, threshold decision]
- concepts: [reconstruction-confidence, detection-decision, competing-hypotheses, confidence, likelihood]

## Claims
- claim: "The confidence threshold decision is where the reconstruction's confidence becomes a decision rule — the qualification is operationalised into a cut-off for action."
  certainty: high
  evidence: Decision practice, calibration practice
  scope: cross-domain
- claim: "The threshold is a decision, not a property of confidence — confidence measures the chain; the threshold says what the organisation will act on."
  certainty: high
  evidence: Decision analysis practice
  scope: cross-domain
- claim: "The threshold inherits the asymmetry of the domain — under concealment, the cost of the two error directions is never equal, and the threshold prices it."
  certainty: high
  evidence: Concealment design analysis
  scope: cross-domain
- claim: "The threshold is qualified by the same evidence chain as the decisions it governs — a threshold is only as honest as the calibration behind it."
  certainty: high
  evidence: Calibration practice
  scope: cross-domain
- claim: "The threshold prices the error asymmetry — under concealment, the two error directions never cost the same."
  certainty: high
  evidence: Decision analysis practice
  scope: cross-domain

## Relationships
- concept: reconstruction-confidence
  relationship: operates_on
  description: "The confidence threshold operates on reconstruction confidence — the rule cuts the qualified claim."
- concept: detection-decision
  relationship: governs
  description: "The confidence threshold governs the detection decision — the cut-off sets the detection call's standard."
- concept: competing-hypotheses
  relationship: informed_by
  description: "The confidence threshold is informed by competing hypotheses — the reading set's structure shapes where the cut-off sits."
- concept: confidence
  relationship: applies_to
  description: "The confidence threshold applies to confidence — the attached confidence is the rule's substrate."
- concept: likelihood
  relationship: calibrates
  description: "The confidence threshold calibrates likelihood — the cut-off is set against the estimated plausibility of readings."

## Tradeoffs
- dimension: threshold_level_vs_error_direction
  options:
    high_threshold:
      value: false_negative_safety
      rationale: "High thresholds avoid acting on weak chains but let concealed artifacts through."
    low_threshold:
      value: false_positive_safety
      rationale: "Low thresholds catch more but act on thin reconstructions."
  importance: high
- dimension: threshold_stability_vs_calibration
  options:
    fixed_threshold:
      value: consistency
      rationale: "Fixed thresholds are consistent but insensitive to evidence quality."
    calibrated_threshold:
      value: honesty
      rationale: "Calibrated thresholds follow the evidence but move the goalposts."
  importance: high

## Failure Modes
- name: threshold_misprice
  description: "The threshold is set as if the two error directions were symmetric — under concealment, the asymmetry is exactly what the threshold must price."
  likelihood: high
  observable_evidence: "Thresholds set without error-cost analysis; false-negative tolerance equal to false-positive tolerance on concealed artifacts"
  detection: "Error-cost review; threshold-vs-concealment audit"
  recovery: "Price the error asymmetry; re-set the cut-off"
  retryable: true
- name: threshold_detachment
  description: "The threshold is set without the calibration it governs — the rule is more confident than the chain."
  likelihood: medium
  observable_evidence: "Thresholds derived from organisational posture rather than calibration; cut-offs above the chain's ceiling"
  detection: "Calibration-to-threshold audit"
  recovery: "Set the threshold against the calibration curve; record the chain's ceiling"
  retryable: true
- name: threshold_churn
  description: "The threshold moves with every reconstruction — the rule becomes noise and the governed decisions lose their standard."
  likelihood: medium
  observable_evidence: "Cut-offs changing across similar chains; decisions framed by whichever threshold was current"
  detection: "Threshold-change log review"
  recovery: "Freeze the threshold for a decision window; revise only on calibration evidence"
  retryable: true

## Observations
- observation: "The threshold operationalises confidence into a cut-off — the error asymmetry is priced inside the decision's own factors."
  confidence: high
  source: Decision analysis practice
- observation: "The threshold is the point where qualification becomes rule — the chain's confidence is a measure; the cut-off is a choice."
  confidence: high
  source: Decision analysis practice
- observation: "Error asymmetry is the concealment signature at the decision layer — the threshold that prices it is the threshold that works."
  confidence: high
  source: Concealment analysis

## Constraints
- constraint: "A threshold is a decision, never a property of confidence — the qualification measures, the organisation cuts."
  type: invariant
  scope: cross-domain
- constraint: "The threshold prices the error asymmetry of concealment — symmetric thresholds on concealed artifacts are mispriced."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: error_asymmetry
  question: "How different are the costs of the two error directions under this artifact?"
  supporting: "Priced asymmetry sets an honest cut-off."
  contradictory: "Assumed symmetry sets a cut-off that fails in one direction."
  weight: high
- factor: calibration_quality
  question: "How well calibrated is the reconstruction confidence the threshold cuts?"
  supporting: "Calibrated chains justify sharp thresholds."
  contradictory: "Uncalibrated chains make any threshold a guess."
  weight: high
- factor: action_stakes
  question: "What does acting above or below this threshold cost?"
  supporting: "Visible stakes discipline the threshold's level."
  contradictory: "Hidden stakes let the threshold drift from its purpose."
  weight: high
- factor: threshold_stability
  question: "How long can the organisation hold this cut-off?"
  supporting: "Stable thresholds give governed decisions a standard."
  contradictory: "Moving thresholds make the standard noise."
  weight: medium

## Heuristics
- heuristic: "Set the threshold against calibration, never against posture."
  rationale: "The cut-off is a decision about the chain; the chain's calibration is its evidence."
  evidence_level: high
- heuristic: "Price the two error directions separately."
  rationale: "Concealment makes the directions asymmetric; one price is wrong."
  evidence_level: high

## Recommendations
- recommendation: "Hold the threshold for a decision window; revise on calibration evidence."
  context: operations
  certainty: strong
  rationale: "Stability is the rule's power; churn is its corruption."
- recommendation: "Record the chain's calibration ceiling with every threshold."
  context: operations
  certainty: strong
  rationale: "The ceiling keeps the rule honest about its substrate."
