# Uncertainty Estimation

## Identity
- id: uncertainty-estimation
- type: concept
- title: Uncertainty Estimation
- tags: [machine learning, uncertainty, aleatoric, epistemic, estimation, ensembles, bayesian]
- entities: [uncertainty estimation, aleatoric uncertainty, epistemic uncertainty, ensembles, bayesian methods, uncertainty quantification]
- concepts: [confidence-calibration, probabilistic-outputs, hallucination, likelihood, distribution-shift, retraining-decisions]

## Claims
- claim: "Uncertainty estimation quantifies what a model does not know — distinguishing aleatoric (irreducible data noise) from epistemic (reducible model ignorance) uncertainty."
  certainty: high
  evidence: Uncertainty quantification literature
  scope: cross-domain
- claim: "Uncertainty estimates are only useful when calibrated and validated against the true failure rate."
  certainty: high
  evidence: Uncertainty calibration research
  scope: cross-domain
- claim: "Epistemic uncertainty is actionable — it identifies where more data, better features, or different architecture would help."
  certainty: high
  evidence: Active learning and epistemic uncertainty research
  scope: cross-domain
- claim: "Aleatoric uncertainty sets a floor on achievable predictive accuracy — no model can reduce irreducible noise."
  certainty: high
  evidence: Uncertainty quantification theory
  scope: cross-domain
- claim: "Uncertainty estimates decay in validity as the input distribution shifts from training."
  certainty: high
  evidence: Out-of-distribution uncertainty research
  scope: cross-domain

## Relationships
- concept: confidence-calibration
  relationship: validated_by
  description: "Uncertainty estimates are validated by calibration — an estimate is only evidence if it tracks realized error."
- concept: probabilistic-outputs
  relationship: produces
  description: "Uncertainty estimation produces probabilistic outputs — the estimated distribution is the uncertainty carrier."
- concept: hallucination
  relationship: mitigates
  description: "Uncertainty estimation mitigates hallucination — epistemic uncertainty flags content the model cannot support."
- concept: likelihood
  relationship: quantifies
  description: "Uncertainty estimation quantifies likelihood — it turns qualitative uncertainty into quantitative evidence."
- concept: distribution-shift
  relationship: degrades_with
  description: "Uncertainty estimates degrade with distribution shift — estimates learned on one distribution do not transfer."
- concept: retraining-decisions
  relationship: informs
  description: "Uncertainty estimation informs retraining decisions — rising epistemic uncertainty signals the need for new data."

## Tradeoffs
- dimension: computational_cost_vs_quality
  options:
    ensemble_bayesian:
      value: estimate_quality
      rationale: "Ensembles and Bayesian methods produce reliable uncertainty but multiply inference cost."
    single_pass_heuristics:
      value: efficiency
      rationale: "Single-pass heuristics (softmax confidence, distance measures) are cheap but systematically overconfident."
  importance: high
- dimension: coverage_vs_precision
  options:
    wide_bands:
      value: honesty
      rationale: "Wide uncertainty bands rarely miss but carry little decision signal."
    narrow_bands:
      value: decisiveness
      rationale: "Narrow bands are decisive but mislead when the estimate is wrong."
  importance: medium

## Failure Modes
- name: false_precision
  description: "Model reports confident point estimates with no uncertainty — the failure mode uncertainty estimation exists to prevent."
  likelihood: high
  observable_evidence: "High-confidence errors in production; no uncertainty metadata on predictions; surprise failures"
  detection: "Uncertainty availability audit; error analysis on high-confidence predictions"
  recovery: "Adopt explicit uncertainty methods; expose uncertainty metadata; gate on uncertainty"
  retryable: true
- name: unvalidated_estimates
  description: "Uncertainty numbers are produced but never checked against realized error rates — they drift into fiction."
  likelihood: medium
  observable_evidence: "Uncertainty estimates inconsistent with realized outcomes; claims about reliability without measurement"
  detection: "Calibration check of uncertainty against realized error; periodic validation"
  recovery: "Validate uncertainty against outcomes; re-estimate on shift; retire unvalidated estimates"
  retryable: true
- name: epistemic_misclassification
  description: "Epistemic uncertainty is treated as aleatoric — the model concludes 'unknowable' when it is simply undertrained."
  likelihood: medium
  observable_evidence: "Missed improvement opportunities; data collection stopped while errors remain reducible; wrong 'ceiling' claims"
  detection: "Error reducibility analysis; probe with additional data; uncertainty decomposition review"
  recovery: "Decompose uncertainty sources; act on epistemic component with data; document aleatoric floor honestly"
  retryable: true

## Observations
- observation: "Ensemble-based uncertainty estimates reliably outperform single-model confidence in detecting failure."
  confidence: high
  source: Uncertainty quantification evaluations
- observation: "Models are poorly calibrated about their own uncertainty — uncertainty estimates need independent validation."
  confidence: high
  source: Calibration research across model families
- observation: "Uncertainty estimation is rarely validated against realized error rates in practice."
  confidence: high
  source: Production ML practice reviews

## Constraints
- constraint: "Uncertainty estimates are only meaningful to the extent they are calibrated to realized outcomes."
  type: invariant
  scope: cross-domain
- constraint: "Epistemic uncertainty can be reduced by data; aleatoric cannot — the two must be distinguished for action."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Use ensembles or native uncertainty models when uncertainty is decision-relevant."
  rationale: "Single-model confidence is systematically overconfident; ensemble disagreement is a reliable proxy."
  evidence_level: high
- heuristic: "Always validate uncertainty estimates against realized error rates before relying on them."
  rationale: "Unvalidated uncertainty is assertion, not evidence."
  evidence_level: high
- heuristic: "Route on uncertainty — abstain, escalate, or fetch more evidence when uncertainty exceeds thresholds."
  rationale: "Uncertainty only pays off when it changes action; routing is the mechanism."
  evidence_level: high

## Recommendations
- recommendation: "Distinguish aleatoric from epistemic uncertainty in any uncertainty reporting."
  context: evaluation
  certainty: strong
  rationale: "The distinction determines the action — more data for epistemic, acceptance or redesign for aleatoric."
- recommendation: "Gate automation on validated uncertainty estimates, not raw model confidence."
  context: deployment
  certainty: strong
  rationale: "Raw confidence is a ranking; only validated uncertainty is evidence."
- recommendation: "Re-estimate uncertainty after distribution shifts — old estimates are stale evidence."
  context: operational_ml
  certainty: strong
  rationale: "Uncertainty validity decays with shift; stale estimates mislead routing decisions."
