# Concealed Intent

## Identity
- id: concealed-intent
- type: concept
- title: Concealed Intent of Artifacts
- tags: [intent, design intent, creator, artifact analysis, concealment, reconstruction]
- entities: [concealed intent, design intent, creator's purpose, withheld intent, why the artifact is shaped this way]
- concepts: [artifact, inference-from-behavior, design-under-concealment, attribution, threat-actor]

## Claims
- claim: "The artifact's intent is the creator's design state — why the artifact is shaped this way — and it is withheld by design, never presented with the artifact."
  certainty: high
  evidence: Adversarial artifact analysis practice
  scope: cross-domain
- claim: "Intent is accessed only through the artifact — every claim about the creator's purpose is an inference through the object, never a direct observation."
  certainty: high
  evidence: Adversarial artifact analysis practice
  scope: cross-domain
- claim: "Intent claims stand furthest removed from direct observation — an inference about a creator's state, inferred from an artifact, inferred from behaviour, observed."
  certainty: high
  evidence: Adversarial artifact analysis practice
  scope: cross-domain
- claim: "Intent is reconstructed from the artifact's form — the purpose is read from the object's sacrifices, choices, and structure, never from a direct account."
  certainty: high
  evidence: Adversarial artifact analysis practice
  scope: cross-domain
- claim: "The intent claim is the weakest-evidenced and highest-stakes claim in the analysis — it decides response, and its evidence is the thinnest."
  certainty: high
  evidence: Attribution and response practice, adversarial analysis
  scope: cross-domain

## Relationships
- concept: artifact
  relationship: grounded_in
  description: "Concealed intent is grounded in the artifact — the object is the only access to the creator's design state."
- concept: inference-from-behavior
  relationship: derived_from
  description: "Concealed intent is derived from behavioural inference — the reading of what the artifact does is the base the intent claim stands on."
- concept: design-under-concealment
  relationship: constrained_by
  description: "Concealed intent is constrained by design under concealment — the shape of the artifact is the evidence of the intent."
- concept: attribution
  relationship: informs
  description: "Concealed intent informs attribution — the claim about purpose narrows the claim about origin."
- concept: threat-actor
  relationship: describes
  description: "Concealed intent describes the threat actor — the creator's design state is the actor in material form."

## Tradeoffs
- dimension: intent_reach_vs_confidence
  options:
    deep_intent_claim:
      value: insight
      rationale: "Deep intent claims explain the artifact's shape but stand on the thinnest evidence in the chain."
    surface_intent_claim:
      value: honesty
      rationale: "Modest intent claims stay within the evidence but explain less."
  importance: high
- dimension: intent_specificity_vs_attribution_risk
  options:
    specific_intent:
      value: decision_support
      rationale: "Specific intent claims support specific responses but risk over-attribution."
    general_intent:
      value: safety
      rationale: "General intent claims stay safe but guide response less."
  importance: high

## Failure Modes
- name: over_attribution_of_intent
  description: "Purpose is claimed where the evidence supports only shape — teleological reading of the artifact as if its design state were visible."
  likelihood: high
  observable_evidence: "Intent claims without behavioural support; designs read as deliberate where accident explains them"
  detection: "Intent-claim evidence audit; alternative-explanation review"
  recovery: "Demote intent claims to their evidence; record alternative design states"
  retryable: true
- name: projection_of_intent
  description: "The analyst's own reading is attributed to the creator — the intent claim describes the analyst, not the designer."
  likelihood: medium
  observable_evidence: "Intent claims that mirror the analyst's conclusions; purposes that conveniently justify the analysis"
  detection: "Second-reader review; intent-vs-evidence mapping"
  recovery: "Ground intent claims in the artifact's shape; separate reading from purpose"
  retryable: true
- name: intent_as_evidence_confusion
  description: "The intent claim is treated as evidence — the purpose is cited as a fact when it is an inference."
  likelihood: medium
  observable_evidence: "Intent claims cited as givens in later reasoning; purposes treated as properties of the artifact"
  detection: "Claim-status review; inference marking discipline"
  recovery: "Mark intent claims as derived; qualify them by their evidence chain"
  retryable: true

## Observations
- observation: "Intent is never given — every purpose reading is reconstructed from the artifact's form and recorded as a derived claim."
  confidence: high
  source: Artifact analysis practice
- observation: "The intent claim is the analysis's most derived claim — the analyst claims what the designer intended, having seen only what the artifact did."
  confidence: high
  source: Artifact analysis practice
- observation: "The creator's design state is the analysis's first object — and it is itself only a claim, inferred from the artifact the analyst holds."
  confidence: high
  source: Artifact analysis practice

## Constraints
- constraint: "The creator's intent is accessed only through the artifact — intent claims are inferences, never direct observations."
  type: invariant
  scope: cross-domain
- constraint: "An intent claim is derived and marked as derived — purpose treated as a fact is the corruption the analysis is most vulnerable to."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Ground every intent claim in the artifact's shape — what in the object supports this purpose reading?"
  rationale: "The artifact is the only access; the shape is the evidence."
  evidence_level: high
- heuristic: "Record alternative design states alongside the claimed intent."
  rationale: "Alternative states keep the intent claim honest and revisable."
  evidence_level: high

## Recommendations
- recommendation: "Record alternative design states alongside the claimed intent."
  context: analysis
  certainty: strong
  rationale: "Alternative states keep the intent claim honest and revisable."
- recommendation: "Qualify intent claims by their full evidence chain."
  context: analysis
  certainty: strong
  rationale: "The most derived claims need the most explicit grounding."
- recommendation: "Treat intent claims as derived, always — never as facts about the artifact."
  context: analysis
  certainty: strong
  rationale: "Intent-as-evidence is the corruption that propagates through the whole chain."
