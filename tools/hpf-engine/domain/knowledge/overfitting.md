# Overfitting

## Identity
- id: overfitting
- type: concept
- title: Overfitting
- tags: [machine learning, overfitting, regularization, capacity, bias-variance, train-val gap]
- entities: [overfitting, regularization, training error, validation error, model capacity, bias-variance tradeoff]
- concepts: [generalization, training-data, benchmark-validity, uncertainty-estimation, model-monitoring, distribution-shift]

## Claims
- claim: "Overfitting is the absorption of noise from training data — the model fits patterns that exist in the sample but not in the distribution."
  certainty: high
  evidence: Statistical learning theory
  scope: cross-domain
- claim: "The train-validation gap is the primary observable signal — growing gap with training progress indicates overfitting."
  certainty: high
  evidence: ML practice and theory
  scope: cross-domain
- claim: "Overfitting risk increases with capacity relative to information in the data — excess capacity has nowhere to go but noise."
  certainty: high
  evidence: Bias-variance theory
  scope: cross-domain
- claim: "Overfitting is mitigated by regularization, data volume, and early stopping — each trades expressiveness for stability."
  certainty: high
  evidence: Regularization literature
  scope: cross-domain
- claim: "Overfitting is undetectable from training performance alone — training error approaching zero is consistent with either excellent fit or total memorization."
  certainty: high
  evidence: Statistical learning theory
  scope: cross-domain

## Relationships
- concept: generalization
  relationship: degrades
  description: "Overfitting degrades generalization — noise-fitted patterns do not transfer to unseen data."
- concept: training-data
  relationship: depends_on
  description: "Overfitting depends on training data quality — noisier data provides more noise to absorb."
- concept: benchmark-validity
  relationship: masked_by
  description: "Overfitting can be masked by benchmark validity issues — contaminated evaluation cannot distinguish fit from memorization."
- concept: uncertainty-estimation
  relationship: interacts_with
  description: "Overfitting interacts with uncertainty estimation — overfit models are overconfident on training-like inputs."
- concept: model-monitoring
  relationship: detected_by
  description: "Overfitting in production is detected by model monitoring — deployment gaps between expected and realized performance."
- concept: distribution-shift
  relationship: worsens_with
  description: "Overfitting worsens with distribution shift — noise-fitted patterns fail first on shifted inputs."

## Tradeoffs
- dimension: capacity_vs_regularization
  options:
    high_capacity_light_regularization:
      value: expressiveness
      rationale: "Fits complex true patterns but absorbs noise as memorization."
    low_capacity_heavy_regularization:
      value: stability
      rationale: "Resists noise but risks underfitting real structure."
  importance: high
- dimension: train_fit_vs_heldout_robustness
  options:
    minimize_training_error:
      value: benchmark_performance
      rationale: "Maximizes measured performance but overfits the training sample."
    prioritize_heldout:
      value: true_robustness
      rationale: "Sacrifices training fit for performance on unseen data."
  importance: high

## Failure Modes
- name: silent_overfit
  description: "Overfitting is present but hidden — evaluation artifacts or weak validation mask the train-validation gap."
  likelihood: high
  observable_evidence: "Strong training and validation performance collapsing in production; gap appears only on fresh data"
  detection: "Fresh-data validation; evaluation design audit; gap monitoring across data regions"
  recovery: "Clean evaluation; fresh holdsets; regularization; capacity reduction"
  retryable: true
- name: evaluation_leakage
  description: "Validation or test data leaks into training (directly or through tuning) — the model overfits the evaluation itself."
  likelihood: high
  observable_evidence: "Scores far above production performance; tuning history reveals repeated eval-set contact; contamination patterns"
  detection: "Leakage audits; repeated-evaluation analysis; fresh-data checks"
  recovery: "Re-split; freeze evaluation sets; separation invariants in pipelines"
  retryable: true
- name: regularization_overreach
  description: "Anti-overfitting measures overcorrect — the model underfits real structure, trading noise for lost signal."
  likelihood: medium
  observable_evidence: "High bias errors; underperformance on both training and held-out data; over-smoothed predictions"
  detection: "Bias error analysis; capacity sweep comparison; learning curve review"
  recovery: "Reduce regularization; increase capacity; early stopping at the right epoch"
  retryable: true

## Observations
- observation: "Overfitting is the dominant failure mode in small-data regimes and disappears at sufficient data scale."
  confidence: high
  source: ML practice, learning theory
- observation: "Train-validation gap is a reliable early signal — models rarely hide overfitting from a clean held-out split."
  confidence: high
  source: ML operations practice
- observation: "Evaluation leakage is a more common cause of overstated quality than genuine generalization strength."
  confidence: high
  source: Evaluation audits, ML incident analyses

## Constraints
- constraint: "Training performance is not evidence of deployment performance."
  type: invariant
  scope: cross-domain
- constraint: "Evaluation data must never influence training, tuning, or model selection."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Watch the train-validation gap during training — divergence is the earliest overfitting signal."
  rationale: "The gap is observable before deployment failure."
  evidence_level: high
- heuristic: "Freeze evaluation sets and never tune against them."
  rationale: "Tuning against evaluation converts it into training data."
  evidence_level: high
- heuristic: "Prefer the simpler model when evidence is equal — capacity not justified by data is overfitting risk."
  rationale: "Unused capacity is absorbed as noise."
  evidence_level: high

## Recommendations
- recommendation: "Monitor the train-validation gap as a training-time quality gate."
  context: model_development
  certainty: strong
  rationale: "Early detection is cheaper than post-deployment diagnosis."
- recommendation: "Enforce evaluation-set separation as an invariant across the entire pipeline, including tuning."
  context: pipeline_design
  certainty: strong
  rationale: "Leakage through tuning is the subtle path to invalid evidence."
- recommendation: "Validate final models on a fresh holdout never touched during development."
  context: evaluation
  certainty: strong
  rationale: "Only untouched data produces an unbiased generalization estimate."
