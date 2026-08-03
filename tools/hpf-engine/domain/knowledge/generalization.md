# Generalization

## Identity
- id: generalization
- type: concept
- title: Generalization
- tags: [machine learning, generalization, held-out evaluation, capacity, bias, variance, robustness]
- entities: [generalization, generalization gap, held-out performance, model capacity, bias-variance tradeoff, robustness]
- concepts: [training-data, overfitting, distribution-shift, benchmark-validity, confidence-calibration, uncertainty-estimation]

## Claims
- claim: "Generalization is the ability to perform on unseen data from the same distribution — it is a property inferred from observations, not a mechanism."
  certainty: high
  evidence: Statistical learning theory
  scope: cross-domain
- claim: "Generalization cannot be directly measured — it is estimated from held-out evaluation, which is itself evidence subject to validity conditions."
  certainty: high
  evidence: Evaluation methodology literature
  scope: cross-domain
- claim: "Generalization claims are distribution-bound — a model that generalizes within its training distribution may not generalize across distribution shift."
  certainty: high
  evidence: Out-of-distribution generalization research
  scope: cross-domain
- claim: "Generalization trades against memorization — capacity beyond what the data supports is absorbed as memorization of noise."
  certainty: high
  evidence: Bias-variance theory, double descent research
  scope: cross-domain
- claim: "Apparent generalization can be an artifact of evaluation design — leakage, overlapping splits, and contamination inflate generalization estimates."
  certainty: high
  evidence: Evaluation audit literature, benchmark contamination research
  scope: cross-domain

## Relationships
- concept: training-data
  relationship: learned_from
  description: "Generalization is learned from training data — the data defines what generalizes."
- concept: overfitting
  relationship: contrasts_with
  description: "Generalization contrasts with overfitting — the two are the endpoints of the capacity spectrum."
- concept: distribution-shift
  relationship: limited_by
  description: "Generalization is limited by distribution shift — claims hold only within the training distribution."
- concept: benchmark-validity
  relationship: measured_by
  description: "Generalization is measured by benchmark validity — evaluation evidence inherits benchmark limits."
- concept: confidence-calibration
  relationship: affects
  description: "Generalization affects calibration — good generalization is a precondition for stable calibration."
- concept: uncertainty-estimation
  relationship: interacts_with
  description: "Generalization interacts with uncertainty estimation — epistemic uncertainty marks the boundary of generalization."

## Tradeoffs
- dimension: model_capacity_vs_robustness
  options:
    high_capacity:
      value: expressiveness
      rationale: "High capacity fits complex patterns but risks fitting noise."
    low_capacity:
      value: robustness
      rationale: "Low capacity resists noise but underfits real structure."
  importance: high
- dimension: memorization_vs_generalization
  options:
    memorize:
      value: training_fit
      rationale: "Memorization maximizes training performance at the expense of unseen performance."
    generalize:
      value: unseen_performance
      rationale: "Generalization sacrifices exact training fit for performance on new data."
  importance: high

## Failure Modes
- name: inflated_generalization_claims
  description: "Generalization estimates are inflated by evaluation artifacts — leakage, overlap, or contamination masquerade as real generalization."
  likelihood: high
  observable_evidence: "Evaluation far exceeding fresh-data performance; benchmark scores collapsing in production"
  detection: "Fresh-data validation; contamination audits; evaluation design review"
  recovery: "Clean evaluation; separate holdsets; fresh-data checks in production"
  retryable: true
- name: distribution_mismatch
  description: "Generalization is claimed across distributions where it does not hold — deployment data diverges from the training distribution."
  likelihood: high
  observable_evidence: "Deployment performance below evaluation; drift metrics diverging; failure clusters in new input types"
  detection: "Train-deployment distribution monitoring; drift detection; per-segment performance tracking"
  recovery: "Retrain on current distribution; restrict deployment scope; document validity boundary"
  retryable: true
- name: false_transfer_assumption
  description: "Generalization from one task or domain is assumed for another — capabilities are assumed to transfer without evidence."
  likelihood: medium
  observable_evidence: "Unexpected failures in new domains; assumed capabilities absent in production"
  detection: "Transfer testing; capability probing per target domain"
  recovery: "Measure per-domain; scope claims to tested domains"
  retryable: true

## Observations
- observation: "Held-out evaluation systematically overestimates production performance — the generalization gap between evaluation and deployment is a stable finding."
  confidence: high
  source: Industry deployment studies, evaluation audits
- observation: "Generalization quality varies by data region — models generalize well in dense regions of the training distribution and poorly at its edges."
  confidence: high
  source: OOD and robustness research
- observation: "Capacity increases have reduced training error but generalization claims remain distribution-bound."
  confidence: high
  source: Modern ML practice

## Constraints
- constraint: "Generalization cannot be directly measured — only estimated, under validity conditions that must be stated."
  type: invariant
  scope: cross-domain
- constraint: "Generalization claims are valid only within the training distribution."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Evaluate on data that has never influenced training, including during tuning."
  rationale: "Any contact between evaluation data and training invalidates the estimate."
  evidence_level: high
- heuristic: "Treat generalization as a claim with validity conditions — state the distribution, not just the score."
  rationale: "An unqualified generalization number is an assertion without a validity domain."
  evidence_level: high
- heuristic: "Check distribution match before trusting evaluation as evidence of production performance."
  rationale: "Evaluation evidence only transfers where the distributions match."
  evidence_level: high

## Recommendations
- recommendation: "Report generalization estimates with their validity conditions — distribution, data source, and evaluation design."
  context: evaluation
  certainty: strong
  rationale: "A generalization number without validity conditions is not evidence."
- recommendation: "Validate generalization on fresh production-like data before deployment, not only on held-out splits."
  context: deployment
  certainty: strong
  rationale: "Held-out estimates systematically overstate production performance."
- recommendation: "Bound deployment scope to the distribution where generalization was demonstrated."
  context: operational_ml
  certainty: strong
  rationale: "Distribution-bound claims reduce surprise failures outside the evidence domain."
