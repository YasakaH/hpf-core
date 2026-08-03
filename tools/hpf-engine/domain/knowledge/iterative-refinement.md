# Iterative Refinement

## Identity
- id: iterative-refinement
- type: concept
- title: Iterative Refinement of Reconstructions
- tags: [refinement, iteration, reconstruction, artifact analysis, evidence accumulation, revision]
- entities: [iterative refinement, revision, reconstruction iteration, evidence-driven revision, refined reading]
- concepts: [competing-hypotheses, observable-evidence, inference-from-behavior, artifact, incomplete-evidence]

## Claims
- claim: "Reconstruction knowledge revises itself as evidence accumulates — the reading of the artifact changes when the record changes."
  certainty: high
  evidence: Analysis practice, iterative hypothesis testing
  scope: cross-domain
- claim: "Refinement is the reading changing as the record changes — the revised reading stands on the new record, not on the old."
  certainty: high
  evidence: Analysis practice, iterative hypothesis testing
  scope: cross-domain
- claim: "Each revision carries its own qualification — the refined reading is a new claim about the artifact with its own evidence and confidence, not an edit of the old one."
  certainty: high
  evidence: Claim-level qualification discipline
  scope: cross-domain
- claim: "Refinement is convergent when discriminative evidence arrives — the reading set narrows because evidence decides, not because the analyst settles."
  certainty: high
  evidence: Competing-hypothesis analysis practice
  scope: cross-domain
- claim: "Revision without new evidence is churn — a refined reading must cite what changed in the record, or it is not refinement."
  certainty: high
  evidence: Analysis practice, decision under uncertainty
  scope: cross-domain

## Relationships
- concept: observable-evidence
  relationship: driven_by
  description: "Iterative refinement is driven by observable evidence — the record change motivates the reading change."
- concept: competing-hypotheses
  relationship: evolves
  description: "Iterative refinement evolves the reading set — candidates are added, strengthened, or eliminated as evidence accumulates."
- concept: inference-from-behavior
  relationship: improves
  description: "Iterative refinement improves behavioural inference — later readings stand on more evidence than earlier ones."
- concept: artifact
  relationship: characterises
  description: "Iterative refinement characterises the artifact — the refined reading is the best-evidenced claim set so far."
- concept: incomplete-evidence
  relationship: subject_to
  description: "Iterative refinement is subject to incomplete evidence — refinement approaches, never reaches, the withheld truth."

## Tradeoffs
- dimension: revision_rate_vs_stability
  options:
    fast_revision:
      value: responsiveness
      rationale: "Fast revision tracks the evidence closely but produces volatile conclusions."
    slow_revision:
      value: stability
      rationale: "Stable readings resist churn but lag behind new evidence."
  importance: high
- dimension: refinement_depth_vs_analysis_cost
  options:
    deep_refinement:
      value: fidelity
      rationale: "Deep refinement approaches the true reading but consumes time and evidence budget."
    bounded_refinement:
      value: tempo
      rationale: "Bounded refinement reaches decision-ready readings sooner but may stop early."
  importance: high

## Failure Modes
- name: refinement_drift
  description: "Revisions continue without convergence — the reading changes without the record changing."
  likelihood: medium
  observable_evidence: "Repeated re-readings of unchanged evidence; readings that fluctuate across reviewers"
  detection: "Revision-cause tracking; per-revision evidence delta"
  recovery: "Require an evidence delta for every revision; anchor revisions to the record"
  retryable: true
- name: premature_convergence
  description: "The reading set closes before discriminative evidence arrives — refinement stops at the first settled reading."
  likelihood: high
  observable_evidence: "Conclusions unchanged across new captures; reading sets closed without discrimination tests"
  detection: "Convergence-cause review; evidence arrival vs conclusion timestamps"
  recovery: "Re-open refinement when discriminative evidence is pending; treat closure as provisional"
  retryable: true
- name: revision_without_evidence
  description: "Readings are revised by persuasion rather than by record — churn disguised as refinement."
  likelihood: medium
  observable_evidence: "Revisions citing no new evidence; conclusion changes accompanying personnel or preference changes"
  detection: "Revision-evidence audit; change-log review"
  recovery: "Require cited evidence for every revision; document the record delta"
  retryable: true

## Observations
- observation: "Refinement replaces readings, it does not accumulate them — the record grows a better-evidenced member and the older reading is revised out."
  confidence: high
  source: Competing-hypothesis analysis practice
- observation: "The convergent case is the one worth instrumenting — refinement that narrows because evidence decided is the discipline's signature."
  confidence: high
  source: Competing-hypothesis analysis practice
- observation: "Revision without evidence is the quiet corruptor — churn reads like refinement in the log."
  confidence: high
  source: Analysis practice review

## Constraints
- constraint: "A revision is valid only under the evidence that motivated it — refinement without a record delta is churn."
  type: invariant
  scope: cross-domain
- constraint: "Refinement approaches the withheld truth but never closes it — the artifact's hidden semantics are reached by convergence, not by arrival."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Record the evidence delta with every revision."
  rationale: "The delta is what makes a revision refinement rather than churn."
  evidence_level: high
- heuristic: "Treat convergence as provisional until discriminative evidence is exhausted."
  rationale: "Premature convergence is commitment wearing a conclusion's clothes."
  evidence_level: high

## Recommendations
- recommendation: "Anchor every revised reading to the record delta that motivated it."
  context: analysis
  certainty: strong
  rationale: "The delta is what makes a revision refinement rather than churn."
- recommendation: "Require a cited evidence delta for every refined reading."
  context: analysis
  certainty: strong
  rationale: "The delta separates refinement from churn in the record."
- recommendation: "Instrument convergence — record why the reading set closed."
  context: analysis
  certainty: strong
  rationale: "Closure by evidence is refinement; closure by preference is bias."
