# Human Evaluation

## Identity
- id: human-evaluation
- type: concept
- title: Human Evaluation
- tags: [machine learning, human evaluation, annotation, inter-rater agreement, preference, subjectivity]
- entities: [human evaluation, annotation, inter-rater agreement, preference judgment, subjectivity, rater]
- concepts: [benchmark-validity, alignment, metric-selection, hallucination, training-data, generalization]

## Claims
- claim: "Human evaluation is evidence about quality derived from human judgement — disagreement between raters is data, not noise."
  certainty: high
  evidence: Annotation methodology literature
  scope: cross-domain
- claim: "Human judgement is variable — inter-rater agreement must be measured for human evaluation results to be interpretable."
  certainty: high
  evidence: Inter-rater reliability research
  scope: cross-domain
- claim: "Human evaluation is the reference for qualities automated metrics cannot measure — fluency, preference, harm."
  certainty: high
  evidence: Generative evaluation practice
  scope: cross-domain
- claim: "Human evaluation is expensive and difficult to reproduce — reproducibility limits its evidentiary strength."
  certainty: high
  evidence: Evaluation reproducibility research
  scope: cross-domain
- claim: "Subjective judgement is structured evidence — preference, disagreement, and confidence are expressible as qualified observations and decision factors, not as a separate evidence type."
  certainty: high
  evidence: Cycle 008 authoring evidence, evaluation practice
  scope: cross-domain

## Relationships
- concept: benchmark-validity
  relationship: complements
  description: "Human evaluation complements benchmark validity — human judgement covers what automated measurement cannot."
- concept: alignment
  relationship: evaluates
  description: "Human evaluation evaluates alignment — alignment is grounded in human judgement of behaviour."
- concept: metric-selection
  relationship: informs
  description: "Human evaluation informs metric selection — human-judged qualities define what metrics must approximate."
- concept: hallucination
  relationship: verifies
  description: "Human evaluation verifies hallucination — human verification is the reference for factuality claims."
- concept: training-data
  relationship: biased_by
  description: "Human evaluation is biased by training-data contexts — rater judgement inherits the distributions raters come from."
- concept: generalization
  relationship: validates
  description: "Human evaluation validates generalization — human judgement on fresh content is deployment-like evidence."

## Tradeoffs
- dimension: evaluation_scale_vs_depth
  options:
    many_cheap_ratings:
      value: statistical_power
      rationale: "Large samples support statistical conclusions but shallow judgements miss nuance."
    few_deep_judgements:
      value: fidelity
      rationale: "Deep expert judgement captures nuance but yields small, fragile samples."
  importance: high
- dimension: agreement_vs_ground_truth
  options:
    consensus_as_truth:
      value: tractability
      rationale: "Consensus is measurable and standard but can be systematically wrong."
    verified_ground_truth:
      value: correctness
      rationale: "Verified truth is stronger but infeasible at scale."
  importance: high

## Failure Modes
- name: unmeasured_disagreement
  description: "Inter-rater disagreement is never measured — results look solid while raters disagree about what was evaluated."
  likelihood: high
  observable_evidence: "Conflicting evaluation outcomes across replications; score volatility; rater complaints about criteria"
  detection: "Inter-rater agreement measurement; per-rater analysis; criteria calibration checks"
  recovery: "Measure agreement; calibrate criteria; adjudicate disagreement explicitly"
  retryable: true
- name: evaluation_bias
  description: "Rater demographics, ordering, or framing bias the judgement — results reflect the evaluator population as much as the system."
  likelihood: high
  observable_evidence: "Score differences tracking rater demographics; order effects; framing-dependent results"
  detection: "Rater-population analysis; randomization; bias audits"
  recovery: "Match raters to deployment population; randomize presentation; document rater composition"
  retryable: true
- name: criteria_drift
  description: "Evaluation criteria shift during the study — later judgments apply different standards than earlier ones."
  likelihood: medium
  observable_evidence: "Score drift across study duration; time-correlated changes; inconsistent comment content"
  detection: "Time-series analysis of ratings; criteria log review"
  recovery: "Freeze criteria; periodic recalibration; pilot and retrain raters"
  retryable: true

## Observations
- observation: "Inter-rater agreement varies strongly by quality dimension — some qualities are reliably judgeable, others are not."
  confidence: high
  source: Annotation reliability research
- observation: "Human evaluation is the de facto reference for generative system quality."
  confidence: high
  source: LLM evaluation practice
- observation: "Preference judgments are more consistent across raters than absolute ratings."
  confidence: high
  source: Preference evaluation research

## Constraints
- constraint: "Human evaluation is evidence about the evaluators as much as about the system evaluated."
  type: invariant
  scope: cross-domain
- constraint: "Disagreement must be measured for human evaluation results to be interpretable."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: agreement_level
  question: "Is inter-rater agreement sufficient to support the intended conclusion?"
  supporting: "High agreement strengthens the evidentiary weight of the human evaluation."
  contradictory: "Low agreement demands adjudication, protocol change, or weaker conclusions."
  weight: high
- factor: evaluator_population_fit
  question: "Do the raters match the population the system will actually serve?"
  supporting: "Matched raters produce evidence that generalizes to deployment."
  contradictory: "Mismatched raters bias results toward non-deployment preferences."
  weight: high
- factor: sample_power
  question: "Is the judgement sample large enough for the conclusion drawn?"
  supporting: "Large samples support statistical conclusions about quality."
  contradictory: "Small samples limit conclusions to directional evidence."
  weight: medium

## Heuristics
- heuristic: "Measure inter-rater agreement on every human evaluation — an unreported agreement is an uninterpretable result."
  rationale: "Agreement is the validity condition of judgement evidence."
  evidence_level: high
- heuristic: "Prefer preference comparisons over absolute ratings where possible."
  rationale: "Comparisons are more reliable than absolutes in human judgement."
  evidence_level: high
- heuristic: "Sample raters from the deployment population, not convenience populations."
  rationale: "Evaluator composition determines whose judgement the evidence represents."
  evidence_level: high

## Recommendations
- recommendation: "Report inter-rater agreement with every human evaluation result."
  context: evaluation
  certainty: strong
  rationale: "Without agreement, judgement evidence cannot be weighed."
- recommendation: "Use preference-based protocols for qualities with low absolute-rating reliability."
  context: evaluation_design
  certainty: strong
  rationale: "Preference formats exploit the reliability humans actually have."
- recommendation: "Recruit raters matching the deployment population and document the composition."
  context: evaluation_governance
  certainty: strong
  rationale: "Evaluation evidence inherits the evaluator population."
