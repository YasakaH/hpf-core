# Attribution

## Identity
- id: attribution
- type: concept
- title: Attribution of Artifacts
- tags: [attribution, origin, threat actor, artifact analysis, evidence chain, attribution confidence]
- entities: [attribution, origin claim, actor identification, attribution verdict, source claim]
- concepts: [concealed-intent, threat-actor, reconstruction-confidence, incomplete-evidence, artifact]

## Claims
- claim: "Attribution is the claim about the artifact's origin — who or what built it — and it is an inference over the whole evidence chain, never an observation."
  certainty: high
  evidence: Attribution practice in adversarial analysis
  scope: cross-domain
- claim: "Attribution stands at the analysis's furthest inferential reach — origin is inferred from intent, inferred from the artifact, inferred from behaviour, observed."
  certainty: high
  evidence: Attribution practice in adversarial analysis
  scope: cross-domain
- claim: "Attribution carries the highest stakes and the lowest evidence — it decides response, and its evidence is the thinnest in the chain."
  certainty: high
  evidence: Attribution and response practice
  scope: cross-domain
- claim: "Attribution carries no evidence of its own — the origin claim carries confidence like any other, and the chain is its only evidence."
  certainty: high
  evidence: Attribution practice
  scope: cross-domain
- claim: "Attribution is strengthened by the evidence chain, never by the verdict — a confident attribution is a confidence in a long derived claim, not a fact."
  certainty: high
  evidence: Calibration practice, attribution case studies
  scope: cross-domain

## Relationships
- concept: concealed-intent
  relationship: informed_by
  description: "Attribution is informed by concealed intent — the purpose claim narrows the origin claim."
- concept: threat-actor
  relationship: describes
  description: "Attribution describes the threat actor — the origin claim is a claim about the builder."
- concept: reconstruction-confidence
  relationship: qualified_by
  description: "Attribution is qualified by reconstruction confidence — the origin claim carries the interpretation-anchored qualification."
- concept: incomplete-evidence
  relationship: constrained_by
  description: "Attribution is constrained by incomplete evidence — the capture bounds every origin claim."
- concept: artifact
  relationship: applies_to
  description: "Attribution applies to the artifact's origin — the claim addresses the object's provenance."

## Tradeoffs
- dimension: attribution_specificity_vs_certainty
  options:
    specific_attribution:
      value: response_focus
      rationale: "Specific origin claims focus the response but stand on thinner evidence."
    general_attribution:
      value: honesty
      rationale: "General origin claims stay within the evidence but guide response less."
  importance: high
- dimension: attribution_speed_vs_evidence
  options:
    early_attribution:
      value: tempo
      rationale: "Early attribution supports fast response but risks misattribution."
    evidence_complete:
      value: accuracy
      rationale: "Evidence-complete attribution is accurate but delays the response it should guide."
  importance: high

## Failure Modes
- name: attribution_overreach
  description: "A named actor is claimed on evidence that supports only a general origin — the verdict outruns the chain."
  likelihood: high
  observable_evidence: "Named-actor claims on thin chains; origin verdicts without intent support; confident attributions later reversed"
  detection: "Attribution-vs-evidence audit; chain-strength review"
  recovery: "Demote to the evidence-supported origin claim; record what evidence would raise it"
  retryable: true
- name: misattribution_cascade
  description: "A wrong origin claim propagates — response, confidence, and later readings all inherit the error."
  likelihood: medium
  observable_evidence: "Responses justified by origin claims that collapse under review; later claims citing the wrong attribution"
  detection: "Claim-dependency mapping; attribution review at response time"
  recovery: "Correct the origin claim; audit claims derived from it"
  retryable: true
- name: attribution_politicization
  description: "The origin claim is shaped by what the conclusion should be — attribution becomes the verdict in search of evidence."
  likelihood: medium
  observable_evidence: "Attributions that track organisational expectation; origin claims immune to contradicting evidence"
  detection: "Independent review; evidence-direction audits"
  recovery: "Separate the attribution from the response decision; re-run with blind evidence review"
  retryable: true

## Observations
- observation: "Attribution is never direct — the origin is a qualified claim over the full chain, and its confidence is the chain's confidence."
  confidence: high
  source: Attribution practice in adversarial analysis
- observation: "The attribution claim is the decision-maker's favourite — it is the claim most likely to be asked for, and the least evidenced one."
  confidence: high
  source: Attribution practice
- observation: "The evidence chain is the attribution's only strength — the verdict is the chain, and the chain is derived claims."
  confidence: high
  source: Attribution practice in adversarial analysis

## Constraints
- constraint: "Attribution is a claim about origin, never a fact — the verdict is a qualified derived claim and is always revisable."
  type: invariant
  scope: cross-domain
- constraint: "Attribution requires the evidence chain, not the verdict — an origin claim without its chain is an assertion."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Demand the chain with the attribution — origin claims cite their intent, artifact, and behavioural bases."
  rationale: "The chain is the claim's evidence; without it the claim is an assertion."
  evidence_level: high
- heuristic: "Keep attribution and response separate decisions."
  rationale: "Politicization lives where the verdict drives the response and the evidence follows."
  evidence_level: high

## Recommendations
- recommendation: "Build every attribution from its evidence chain — origin claims cite their bases."
  context: analysis
  certainty: strong
  rationale: "The chain is the claim's only strength."
- recommendation: "Never raise an attribution claim without its evidence chain."
  context: analysis
  certainty: strong
  rationale: "The chain is the claim's only strength."
- recommendation: "Treat every attribution as revisable — record what evidence would change it."
  context: analysis
  certainty: strong
  rationale: "Revisability is what keeps the highest-stakes claim honest."
