# Probabilistic Outputs

## Identity
- id: probabilistic-outputs
- type: concept
- title: Probabilistic Outputs
- tags: [machine learning, probability, softmax, uncertainty, prediction, abstention, probability models]
- entities: [probabilistic outputs, probability distribution, softmax, logits, ensembles, abstention, probability model]
- concepts: [confidence-calibration, uncertainty-estimation, hallucination, likelihood, risk-acceptance, retraining-decisions]

## Claims
- claim: "Probabilistic outputs express a model's belief distribution over outcomes rather than a single point prediction."
  certainty: high
  evidence: Machine learning prediction literature
  scope: cross-domain
- claim: "Probabilistic outputs are only as useful as their calibration — an uncalibrated probability is a ranking, not a probability."
  certainty: high
  evidence: Calibration literature
  scope: cross-domain
- claim: "Probabilistic outputs enable downstream decisions that point predictions do not — abstention, risk-based thresholds, and uncertainty-aware routing."
  certainty: high
  evidence: Decision-focused ML research, deployment practice
  scope: cross-domain
- claim: "Probability output formats (softmax, logits, ensembles, native probability models) differ in how faithfully they represent underlying uncertainty."
  certainty: high
  evidence: Uncertainty quantification literature
  scope: cross-domain
- claim: "Probabilistic outputs compound — downstream decisions inherit the calibration of upstream probability estimates."
  certainty: high
  evidence: Pipeline error propagation research
  scope: cross-domain

## Relationships
- concept: confidence-calibration
  relationship: requires
  description: "Probabilistic outputs require calibration — without it they are rankings, not probabilities."
- concept: uncertainty-estimation
  relationship: enabled_by
  description: "Uncertainty estimation produces probabilistic outputs — the distribution is the carrier of uncertainty."
- concept: hallucination
  relationship: mitigates
  description: "Probabilistic outputs mitigate hallucination exposure — low-confidence outputs can be abstained or escalated."
- concept: likelihood
  relationship: expresses
  description: "Probabilistic outputs express likelihood — the output distribution is a likelihood statement about outcomes."
- concept: risk-acceptance
  relationship: informs
  description: "Probabilistic outputs inform risk acceptance — the probability of failure feeds the acceptance decision."
- concept: retraining-decisions
  relationship: informs
  description: "Probabilistic outputs inform retraining decisions — degraded probability quality signals model aging."

## Tradeoffs
- dimension: sharpness_vs_coverage
  options:
    sharp_distributions:
      value: decisiveness
      rationale: "Peaked distributions support crisp decisions but overstate certainty."
    broad_distributions:
      value: honesty
      rationale: "Wide distributions are honest about uncertainty but carry little decision signal."
  importance: high
- dimension: expressiveness_vs_interpretability
  options:
    full_distributions:
      value: completeness
      rationale: "Full distributions capture the shape of uncertainty but are hard to consume."
    point_estimates:
      value: simplicity
      rationale: "Point estimates with variance are easy to consume but lose distributional structure."
  importance: medium

## Failure Modes
- name: probability_misuse
  description: "Uncalibrated probabilities are treated as true probabilities in downstream decisions — thresholds and risk calculations silently wrong."
  likelihood: high
  observable_evidence: "Downstream decisions deviate from designed operating points; risk estimates disagree with realized outcomes"
  detection: "Calibration audit of probability sources feeding pipelines; realized-vs-expected rate comparison"
  recovery: "Calibrate probability sources; gate consumption on calibration state; document per-source calibration"
  retryable: true
- name: spurious_precision
  description: "Softmax distributions look confident but are arbitrary — normalization produces plausible probabilities without real uncertainty content."
  likelihood: high
  observable_evidence: "High-confidence softmax outputs on unrelated or adversarial inputs; calibration failure at extremes"
  detection: "Per-region calibration checks; OOD probing; reliability analysis at confidence extremes"
  recovery: "Replace softmax confidence with calibrated uncertainty; use OOD detection; ensemble outputs"
  retryable: true
- name: format_mismatch
  description: "Probability sources with different calibration properties are mixed in one pipeline — the weakest source sets effective quality."
  likelihood: medium
  observable_evidence: "Pipeline error concentrated in specific source segments; inconsistent confidence behavior across sources"
  detection: "Per-source calibration measurement; pipeline error attribution"
  recovery: "Harmonize sources; calibrate per source; isolate poorly calibrated sources"
  retryable: true

## Observations
- observation: "Softmax probabilities are often poorly calibrated and systematically overconfident."
  confidence: high
  source: Calibration research across model families
- observation: "Ensembles and native probability models generally produce better-calibrated outputs than single softmax networks."
  confidence: high
  source: Uncertainty quantification literature
- observation: "Downstream systems frequently consume probabilities without any calibration check."
  confidence: high
  source: ML system design reviews, production practice

## Constraints
- constraint: "A probability output is only meaningful relative to the distribution it was learned from."
  type: invariant
  scope: cross-domain
- constraint: "Decision thresholds must be set from calibrated probabilities, not raw output scores."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Always pair probability outputs with a calibration report."
  rationale: "A probability without calibration state is unusable as evidence."
  evidence_level: high
- heuristic: "Treat low-confidence outputs as abstention candidates rather than forced predictions."
  rationale: "Abstention converts uncertainty into a decision option instead of a silent failure."
  evidence_level: high
- heuristic: "Verify calibration per decision-relevant subset, not globally."
  rationale: "Global calibration hides the subset structure that decisions actually operate on."
  evidence_level: high

## Recommendations
- recommendation: "Prefer calibrated probability models for any decision pipeline that consumes confidence."
  context: model_selection
  certainty: strong
  rationale: "Uncalibrated probability sources invalidate every downstream threshold and risk calculation."
- recommendation: "Gate high-stakes automation on calibrated confidence thresholds."
  context: deployment
  certainty: strong
  rationale: "Confidence gating only works when confidence is calibrated."
- recommendation: "Record the calibration state of every probability source feeding a pipeline."
  context: system_design
  certainty: strong
  rationale: "Calibration state is the metadata that makes probability composition trustworthy."
