# Epistemic Symmetry

## Identity
- id: epistemic-symmetry
- type: concept
- title: Epistemic Symmetry Between Analyst and Designer
- tags: [epistemic symmetry, mutual modeling, analyst, designer, artifact analysis, closed loop]
- entities: [epistemic symmetry, mutual modeling, analyst-designer symmetry, recursive anticipation, closed epistemic loop]
- concepts: [artifact, concealed-intent, attribution, belief-state, surface-ambiguity]

## Claims
- claim: "The analyst and the designer model each other — the designer anticipated the analyst, and the analyst reconstructs the designer; the artifact is the intersection of two analyses."
  certainty: high
  evidence: Adversarial analysis practice
  scope: cross-domain
- claim: "The symmetry is structural — the two parties model each other through the artifact, and the artifact is where both models meet."
  certainty: high
  evidence: Adversarial analysis practice
  scope: cross-domain
- claim: "The analysis closes onto itself in this domain — the creator's reality is itself only accessible as a claim, and the analyst's position matches the modelled system's."
  certainty: high
  evidence: Adversarial analysis practice
  scope: cross-domain
- claim: "The designer's anticipation shapes the artifact's surface — the ambiguity the analyst reads is the designer's prediction of reading."
  certainty: high
  evidence: Concealment practice, surface analysis
  scope: cross-domain
- claim: "Symmetry awareness is a qualification, not a paralysis — the analyst models the designer without modelling the model of the model."
  certainty: high
  evidence: Analysis practice, bounded recursion
  scope: cross-domain

## Relationships
- concept: artifact
  relationship: grounded_in
  description: "Epistemic symmetry is grounded in the artifact — the object is the intersection where the two analyses meet."
- concept: concealed-intent
  relationship: explains
  description: "Epistemic symmetry explains concealed intent — the designer's anticipation is why the intent is withheld."
- concept: attribution
  relationship: complicates
  description: "Epistemic symmetry complicates attribution — the designer anticipates attribution and shapes against it."
- concept: surface-ambiguity
  relationship: explains
  description: "Epistemic symmetry explains surface ambiguity — the designed ambiguity is the prediction of the analyst's reading."
- concept: belief-state
  relationship: analogous_to
  description: "Epistemic symmetry is analogous to belief-state — the analyst's position mirrors the modelled system's: qualified claims about an unobserved truth."

## Tradeoffs
- dimension: symmetry_awareness_vs_action
  options:
    model_the_designer:
      value: prediction
      rationale: "Modelling the designer predicts the artifact's traps but consumes the analyst's budget."
    act_on_the_artifact:
      value: progress
      rationale: "Acting on the artifact progresses analysis but walks into anticipated traps."
  importance: high
- dimension: recursion_depth_vs_boundedness
  options:
    deep_recursion:
      value: completeness
      rationale: "Deep recursive modelling is thorough but never terminates."
    bounded_recursion:
      value: actionability
      rationale: "Bounded recursion reaches conclusions but stops modelling early."
  importance: high

## Failure Modes
- name: symmetry_blindness
  description: "The designer's anticipation is ignored — the analyst reads the artifact as if it were not designed to be read."
  likelihood: high
  observable_evidence: "Designed surfaces accepted at face value; concealment trades unanalysed; 'too clean' artifacts unquestioned"
  detection: "Design-state review; concealment hypothesis in every reading set"
  recovery: "Model the designer explicitly; treat anticipated readings as suspect"
  retryable: true
- name: infinite_regress
  description: "Recursive modelling never terminates — the analyst models the designer modelling the analyst without bound."
  likelihood: medium
  observable_evidence: "Analyses consumed by self-reference; 'the designer knows I know' spirals; no conclusions"
  detection: "Recursion-depth review; conclusion-completeness checks"
  recovery: "Bound the recursion at the artifact; record the designer model as one level, not a ladder"
  retryable: true
- name: projection_through_symmetry
  description: "The analyst's own position is assumed to be the designer's — the mutual model is really a mirror."
  likelihood: medium
  observable_evidence: "Designer models that perfectly match the analyst's own reading set; symmetrical analyses with no surprises"
  detection: "Designer-model review; independent adversary modelling"
  recovery: "Model the designer from the artifact's trade, not from the analyst's habits"
  retryable: true

## Observations
- observation: "The mutual-modelling structure recurs across the analysis — concealed intent, designed surface, and anticipated attribution all carry the analyst↔designer loop."
  confidence: high
  source: Adversarial analysis practice
- observation: "The analysis begins and ends with claims about minds it never meets — the creator's reality is a claim exactly as the analyst's reading is."
  confidence: high
  source: Adversarial analysis practice
- observation: "The mutual model is a closed loop between two knowing parties — the analyst models the designer who modelled the analyst, and the artifact is where the two models meet."
  confidence: high
  source: Analysis practice
- observation: "Bounded recursion is the analyst's discipline — the designer model is one level deep, and the artifact is the ground that stops the spiral."
  confidence: high
  source: Analysis practice

## Constraints
- constraint: "The artifact is the intersection of two analyses — the designer's anticipation and the analyst's reconstruction — and the intersection is where both are grounded."
  type: invariant
  scope: cross-domain
- constraint: "The mutual model is one level deep — the designer's anticipation and the analyst's reconstruction are the only layers, and the artifact bounds them."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Model the designer one level deep — the artifact bounds the recursion."
  rationale: "One level of mutual modeling predicts the traps; further levels predict nothing."
  evidence_level: high
- heuristic: "Ask what the designer predicted the analyst would conclude."
  rationale: "The prediction is the design; the design is the evidence."
  evidence_level: high

## Recommendations
- recommendation: "Record the mutual model explicitly — who anticipated what — in every analysis."
  context: analysis
  certainty: strong
  rationale: "The designer's anticipation is the design; recording it keeps the prediction visible."
- recommendation: "Review the analyst↔designer loop explicitly at each analysis milestone."
  context: analysis
  certainty: strong
  rationale: "The loop is the analysis's permanent context; reviewing it keeps the designer's anticipation visible."
