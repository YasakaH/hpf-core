# Training Data

## Identity
- id: training-data
- type: concept
- title: Training Data
- tags: [machine learning, training data, data quality, data lineage, provenance, dataset]
- entities: [training data, dataset, data quality, data lineage, provenance, label noise, data distribution]
- concepts: [generalization, overfitting, distribution-shift, uncertainty-estimation, benchmark-validity, retraining-decisions]

## Claims
- claim: "Training data bounds model capability — a model cannot exceed the information content of its training data, regardless of architecture."
  certainty: high
  evidence: Machine learning theory and practice
  scope: cross-domain
- claim: "Training data distribution defines the model's validity domain — the model is only as reliable as the match between training distribution and deployment distribution."
  certainty: high
  evidence: Distribution shift research
  scope: cross-domain
- claim: "Data quality dominates architecture in determining model performance — clean representative data improves models more than model changes."
  certainty: high
  evidence: Empirical ML studies
  scope: cross-domain
- claim: "Data lineage matters — without provenance, data errors, leakage, and biases cannot be traced, diagnosed, or corrected."
  certainty: high
  evidence: Data governance practice, ML incident analysis
  scope: cross-domain
- claim: "Training data is a live system input — models retrained on evolving data inherit both its improvements and its degradations."
  certainty: high
  evidence: ML operations practice
  scope: cross-domain

## Relationships
- concept: distribution-shift
  relationship: defines_baseline
  description: "Training data defines the baseline distribution — shift is measured against the training distribution."
- concept: generalization
  relationship: bounds
  description: "Training data bounds generalization — performance on unseen data is limited by training information content."
- concept: overfitting
  relationship: facilitated_by
  description: "Noisy or unrepresentative training data facilitates overfitting — noise becomes something for the model to memorize."
- concept: uncertainty-estimation
  relationship: informs
  description: "Training data informs uncertainty estimation — epistemic uncertainty marks where training data is thin."
- concept: benchmark-validity
  relationship: risks_contamination
  description: "Training data risks benchmark contamination — benchmark content in training data invalidates evaluation."
- concept: retraining-decisions
  relationship: source_of
  description: "Training data is the source of retraining — retraining decisions are decisions about which data to learn from."

## Tradeoffs
- dimension: data_volume_vs_data_quality
  options:
    large_noisy_dataset:
      value: coverage
      rationale: "Volume covers more of the input space but adds noise the model will fit."
    small_clean_dataset:
      value: fidelity
      rationale: "Clean data trains tighter models but may under-cover the input space."
  importance: high
- dimension: freshness_vs_stability
  options:
    fresh_data:
      value: relevance
      rationale: "Recent data matches the current distribution but introduces regime-change noise."
    historical_data:
      value: stability
      rationale: "Stable historical data trains consistent models but ages against the live distribution."
  importance: high

## Failure Modes
- name: data_leakage
  description: "Information from the evaluation set reaches the training set — the model trains on what it is later scored against."
  likelihood: high
  observable_evidence: "Suspiciously high evaluation scores; performance collapses on fresh data; benchmark contamination patterns"
  detection: "Leakage audits; duplicate detection between train and eval; fresh-data validation"
  recovery: "Decontaminate data; re-split; maintain separation boundaries in the pipeline"
  retryable: true
- name: label_noise
  description: "Training labels are systematically wrong — the model learns incorrect mappings with confidence."
  likelihood: high
  observable_evidence: "Errors concentrated in classes with bad labels; model confident on mislabeled content; evaluation on clean data reveals it"
  detection: "Label quality audits; disagreement analysis; clean-held-out evaluation"
  recovery: "Relabel pipelines; confidence-weighted training; clean subsets"
  retryable: true
- name: provenance_loss
  description: "Data lineage is lost — errors, biases, and contamination cannot be traced to their source, making them uncorrectable."
  likelihood: high
  observable_evidence: "Inability to explain model behavior regressions; untraceable data errors; audit failures"
  detection: "Lineage completeness audit; provenance requirement on data pipelines"
  recovery: "Re-establish lineage; document data sources and transformations; gate data on provenance"
  retryable: true

## Observations
- observation: "Clean, representative data consistently beats model architecture improvements in realized performance."
  confidence: high
  source: Empirical ML studies, industry practice
- observation: "Data leakage and contamination are common causes of overstated model quality in practice."
  confidence: high
  source: ML incident analyses, evaluation audits
- observation: "Training data lineage is rarely documented to the standard that production debugging requires."
  confidence: high
  source: Data governance practice reviews

## Constraints
- constraint: "A model cannot exceed the information content of its training data."
  type: invariant
  scope: cross-domain
- constraint: "Evaluation data must never influence training — separation is an invariant, not a preference."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Audit data quality and lineage before trusting any model trained on it."
  rationale: "Model evidence inherits the quality of the data it was learned from."
  evidence_level: high
- heuristic: "Treat training data as production infrastructure — version it, document it, govern it."
  rationale: "Data is the highest-leverage component; treating it as infrastructure makes it auditable."
  evidence_level: high
- heuristic: "Check train-deployment distribution match before deployment, not after failures."
  rationale: "Distribution mismatch is predictable; checking upfront avoids surprise degradation."
  evidence_level: high

## Recommendations
- recommendation: "Document data lineage for every training run — sources, transformations, and exclusions."
  context: data_governance
  certainty: strong
  rationale: "Lineage is the prerequisite for diagnosing and correcting data-driven model failures."
- recommendation: "Enforce evaluation-data separation as a pipeline invariant, with contamination checks."
  context: pipeline_design
  certainty: strong
  rationale: "Leakage silently invalidates every quality claim made from evaluation."
- recommendation: "Measure and report the distribution match between training data and live deployment data."
  context: operational_ml
  certainty: strong
  rationale: "Distribution match is the precondition for model evidence remaining valid."
