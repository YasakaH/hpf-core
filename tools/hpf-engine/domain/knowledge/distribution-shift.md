# Distribution Shift

## Identity
- id: distribution-shift
- type: concept
- title: Distribution Shift
- tags: [machine learning, distribution shift, drift, covariate shift, concept drift, model decay]
- entities: [distribution shift, drift, covariate shift, concept drift, data drift, model decay]
- concepts: [training-data, generalization, confidence-calibration, uncertainty-estimation, model-monitoring, retraining-decisions]

## Claims
- claim: "Distribution shift is the divergence between the input distribution a model was trained on and the distribution it operates on — the primary cause of model decay."
  certainty: high
  evidence: Drift research and ML operations practice
  scope: cross-domain
- claim: "Shift invalidates evidence about a model — observations, calibration, and generalization claims all decay as the distribution moves."
  certainty: high
  evidence: OOD research, calibration drift studies
  scope: cross-domain
- claim: "Covariate shift (input change) and concept drift (input-output mapping change) demand different responses — misclassifying the shift type misdirects remediation."
  certainty: high
  evidence: Drift classification literature
  scope: cross-domain
- claim: "Shift is detectable from monitoring data before it causes visible failures — drift metrics lead degradation."
  certainty: high
  evidence: ML monitoring practice
  scope: cross-domain
- claim: "Shift is partially correctable by retraining, but retraining on shifted data without validation risks learning new failure modes."
  certainty: high
  evidence: Retraining practice, ML operations research
  scope: cross-domain

## Relationships
- concept: training-data
  relationship: deviates_from
  description: "Distribution shift is measured as deviation from the training distribution baseline."
- concept: generalization
  relationship: limits
  description: "Distribution shift limits generalization — claims hold only within the training distribution."
- concept: confidence-calibration
  relationship: degrades
  description: "Distribution shift degrades calibration — calibrated confidence becomes miscalibrated as inputs move."
- concept: uncertainty-estimation
  relationship: degrades
  description: "Distribution shift degrades uncertainty estimates — old estimates are stale evidence."
- concept: model-monitoring
  relationship: detected_by
  description: "Distribution shift is detected by model monitoring — drift metrics are monitoring signals."
- concept: retraining-decisions
  relationship: triggers
  description: "Distribution shift triggers retraining decisions — verified shift is the retraining trigger."

## Tradeoffs
- dimension: adaptation_speed_vs_stability
  options:
    frequent_retraining:
      value: freshness
      rationale: "Fast adaptation tracks the moving distribution but amplifies noise into the model."
    conservative_retraining:
      value: stability
      rationale: "Slow adaptation is stable but leaves the model stale against a moving distribution."
  importance: high
- dimension: detection_sensitivity_vs_noise_tolerance
  options:
    high_sensitivity:
      value: early_warning
      rationale: "Sensitive detection catches shift early but triggers on routine fluctuations."
    high_tolerance:
      value: stability
      rationale: "Tolerant detection avoids noise-triggered retraining but misses early shift."
  importance: high

## Failure Modes
- name: silent_shift
  description: "Deployment distribution drifts with no detection — the model degrades quietly while evaluation evidence stays stale."
  likelihood: high
  observable_evidence: "Gradual performance decline; rising error on specific segments; no monitoring signal because none is configured"
  detection: "Drift monitoring on input features; per-segment performance tracking; prediction-vs-outcome drift"
  recovery: "Deploy drift monitoring; baseline distribution reference; alert on verified divergence"
  retryable: true
- name: shift_type_misclassification
  description: "Covariate shift is mistaken for concept drift or vice versa — remediation targets the wrong mechanism."
  likelihood: medium
  observable_evidence: "Retraining fails to restore performance; remediation chosen for the wrong shift type; root cause analysis confusion"
  detection: "Shift type diagnosis; label availability analysis; feature-relation change detection"
  recovery: "Diagnose shift type before acting; respond per type (resample for covariate, re-label for concept)"
  retryable: true
- name: retraining_on_noise
  description: "Routine fluctuation is treated as shift — the model retrains on noise and its quality degrades."
  likelihood: medium
  observable_evidence: "Performance oscillation after frequent retraining; models worse than previous versions; alert fatigue"
  detection: "Retraining outcome validation; drift severity thresholds; retrospective retraining analysis"
  recovery: "Verify shift before retraining; validate retrained models against fresh holdsets; threshold discipline"
  retryable: true

## Observations
- observation: "Distribution shift is the most common cause of production model degradation after deployment."
  confidence: high
  source: ML operations studies, incident analyses
- observation: "Drift metrics lead visible performance decay — monitoring detects shift before users experience failure."
  confidence: high
  source: ML monitoring practice
- observation: "Retraining without shift validation is a common source of new failure modes."
  confidence: high
  source: ML operations practice

## Constraints
- constraint: "Model validity is bound to its training distribution — shift invalidates model evidence until re-validated."
  type: invariant
  scope: cross-domain
- constraint: "Shift must be verified and typed before remediation — untyped shift response is a guess."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Monitor drift against a fixed reference distribution, not a moving window."
  rationale: "A moving reference cannot distinguish shift from routine change."
  evidence_level: high
- heuristic: "Distinguish covariate shift from concept drift before choosing remediation."
  rationale: "The two mechanisms require different fixes; treating them alike fails."
  evidence_level: high
- heuristic: "Validate retrained models against a fresh holdout before release — verify the response, not just the trigger."
  rationale: "Retraining is an intervention; interventions need outcome validation."
  evidence_level: high

## Recommendations
- recommendation: "Instrument drift monitoring with a fixed reference distribution and alert thresholds."
  context: operational_ml
  certainty: strong
  rationale: "Undetected shift is the dominant silent failure mode of deployed models."
- recommendation: "Diagnose shift type (covariate vs concept) before triggering remediation."
  context: incident_response
  certainty: strong
  rationale: "Type-specific response is the difference between effective and wasted remediation."
- recommendation: "Treat every shift-triggered retraining as an experiment — validate against fresh data before deployment."
  context: retraining_governance
  certainty: strong
  rationale: "Retraining on unvalidated shift is a common source of new failure modes."
