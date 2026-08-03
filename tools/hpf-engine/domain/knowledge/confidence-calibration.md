# Confidence Calibration

## Identity
- id: confidence-calibration
- type: concept
- title: Confidence Calibration
- tags: [machine learning, calibration, confidence, uncertainty, reliability, ECE]
- entities: [confidence calibration, calibration, reliability, expected calibration error, reliability diagram, temperature scaling, confidence score]
- concepts: [likelihood, uncertainty-estimation, probabilistic-outputs, hallucination, generalization, distribution-shift]

## Claims
- claim: "Confidence calibration is the alignment between a model's stated confidence and its observed accuracy — a calibrated model is accurate in proportion to its confidence."
  certainty: high
  evidence: Machine learning calibration literature
  scope: cross-domain
- claim: "Calibration is measurable independently of accuracy (expected calibration error, reliability diagrams) and degrades independently of raw accuracy."
  certainty: high
  evidence: Calibration research and evaluation practice
  scope: cross-domain
- claim: "Calibration is fragile across distribution shifts — a model calibrated on its training distribution is often miscalibrated elsewhere."
  certainty: high
  evidence: Out-of-distribution calibration research
  scope: cross-domain
- claim: "Calibration and accuracy are independent properties — an accurate model can be poorly calibrated and vice versa."
  certainty: high
  evidence: Calibration literature, empirical evaluations
  scope: cross-domain
- claim: "Calibration loss is typically invisible in aggregate metrics — average accuracy can remain high while per-prediction confidence is systematically wrong."
  certainty: high
  evidence: Evaluation practice, calibration studies
  scope: cross-domain

## Relationships
- concept: likelihood
  relationship: qualified_by
  description: "Calibration qualifies likelihood estimates — likelihood is only trustworthy to the degree the confidence attached to it is calibrated."
- concept: uncertainty-estimation
  relationship: validates
  description: "Calibration is the validation method for uncertainty estimates — uncertainty is only useful if it tracks realized error rates."
- concept: probabilistic-outputs
  relationship: evaluates
  description: "Calibration evaluates probabilistic outputs — a probability is a probability only if calibrated."
- concept: hallucination
  relationship: mitigates
  description: "Calibration mitigates hallucination risk — miscalibrated confidence defeats confidence-based hallucination gating."
- concept: generalization
  relationship: depends_on
  description: "Calibration depends on generalization — calibration learned on one distribution does not transfer to another."
- concept: distribution-shift
  relationship: degraded_by
  description: "Calibration is degraded by distribution shift — shifting inputs invalidate previously calibrated confidence."

## Tradeoffs
- dimension: sharpness_vs_calibration
  options:
    high_sharpness:
      value: decisiveness
      rationale: "Confident, peaked predictions are decisive and useful but tend toward overconfidence."
    high_calibration:
      value: reliability
      rationale: "Confidence tracks accuracy exactly, but distributions become less peaked and decisions less crisp."
  importance: high
- dimension: posthoc_vs_training_time_calibration
  options:
    posthoc_calibration:
      value: simplicity
      rationale: "Cheap, reversible, and effective (temperature scaling) but cannot fix all miscalibration patterns."
    training_time_calibration:
      value: robustness
      rationale: "Calibration learned during training is more robust but adds complexity and training cost."
  importance: medium

## Failure Modes
- name: overconfidence
  description: "Model assigns high confidence to wrong predictions — confidence systematically exceeds accuracy."
  likelihood: high
  observable_evidence: "Reliability diagram shows accuracy below confidence; ECE high; high-confidence errors surface in production"
  detection: "Reliability diagrams; per-bucket ECE analysis; error analysis on high-confidence predictions"
  recovery: "Post-hoc calibration (temperature scaling); re-calibration on shift; retrain with calibration-aware objectives"
  retryable: true
- name: underconfidence
  description: "Model confidence systematically below accuracy — predictions are correct but reported uncertainty is inflated."
  likelihood: medium
  observable_evidence: "Reliability diagram shows accuracy above confidence; overly broad uncertainty in downstream consumers"
  detection: "Reliability diagrams; comparison of confidence vs accuracy per bucket"
  recovery: "Re-calibration; review temperature and prior settings"
  retryable: true
- name: calibration_drift
  description: "Model was calibrated at deployment but becomes miscalibrated as the input distribution changes."
  likelihood: high
  observable_evidence: "Rising ECE on recent traffic; high-confidence errors increasing over time; stale calibration set"
  detection: "Ongoing calibration monitoring on production traffic; periodic ECE measurement"
  recovery: "Re-calibrate against recent distribution; detect shift and trigger recalibration pipeline"
  retryable: true

## Observations
- observation: "Large language models are systematically overconfident in many settings, with calibration varying strongly by domain and prompt format."
  confidence: high
  source: LLM calibration research, empirical evaluations
- observation: "Temperature scaling reliably improves calibration without changing accuracy — evidence that calibration is a separable property."
  confidence: high
  source: Post-hoc calibration literature
- observation: "Calibration performance on in-distribution benchmarks does not transfer to out-of-distribution settings."
  confidence: high
  source: Out-of-distribution calibration research

## Constraints
- constraint: "A model cannot be calibrated on distributions it has never seen — calibration is distribution-bound."
  type: invariant
  scope: cross-domain
- constraint: "Calibration cannot be inferred from accuracy — the two must be measured separately."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Measure calibration with reliability diagrams, not ECE alone — ECE hides systematic calibration patterns."
  rationale: "Aggregate error hides per-bucket structure that reliability diagrams expose."
  evidence_level: high
- heuristic: "Re-check calibration after any distribution shift event, not on a fixed schedule."
  rationale: "Shift is the dominant cause of calibration decay; schedule-based checks miss it."
  evidence_level: high
- heuristic: "Prefer post-hoc calibration for deployment-critical thresholds — it is cheap and reversible."
  rationale: "Post-hoc methods fix most deployment miscalibration without retraining risk."
  evidence_level: high

## Recommendations
- recommendation: "Report calibration metrics alongside accuracy for any confidence-scored model."
  context: evaluation
  certainty: strong
  rationale: "Accuracy alone hides systematic miscalibration that invalidates downstream confidence use."
- recommendation: "Re-calibrate after deployment whenever the input distribution changes."
  context: operational_ml
  certainty: strong
  rationale: "Calibration is distribution-bound; shift silently invalidates it."
- recommendation: "Set decision thresholds from calibration curves, not from point accuracy."
  context: decision_making
  certainty: strong
  rationale: "Thresholds chosen on calibrated probabilities realize the intended precision/recall tradeoff."
