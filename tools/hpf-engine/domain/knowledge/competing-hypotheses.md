# Competing Hypotheses

## Identity
- id: competing-hypotheses
- type: concept
- title: Competing Hypotheses in Artifact Analysis
- tags: [hypotheses, competing readings, artifact analysis, evidence, interpretation, analysis of competing hypotheses]
- entities: [competing hypotheses, reading set, candidate readings, alternative reconstructions, hypothesis multiplicity]
- concepts: [artifact, surface-ambiguity, observable-evidence, inference-from-behavior, incomplete-evidence, likelihood]

## Claims
- claim: "The same evidence supports multiple reconstructions of the artifact — competing hypotheses are the normal state of analysis, not its failure."
  certainty: high
  evidence: Competing-hypothesis analysis practice (ACH), analysis methodology
  scope: cross-domain
- claim: "A hypothesis is a reading of the artifact evaluated against evidence — multiple readings of the same record are the normal state of analysis."
  certainty: high
  evidence: Competing-hypothesis analysis practice (ACH), analysis methodology
  scope: cross-domain
- claim: "Hypotheses are the analyst's reading set, not properties of the artifact — the artifact is one object; the plurality lives in the analyst's knowledge."
  certainty: high
  evidence: Epistemic framing in analysis practice
  scope: cross-domain
- claim: "Resolution comes from discriminative evidence — evidence that distinguishes between readings — not from more confidence in any single one."
  certainty: high
  evidence: Competing-hypothesis analysis practice
  scope: cross-domain
- claim: "An unbounded reading set is a failure of discipline, not of evidence — hypothesis proliferation is managed, not suffered."
  certainty: high
  evidence: Analysis practice, decision under uncertainty
  scope: cross-domain

## Relationships
- concept: observable-evidence
  relationship: based_on
  description: "Competing hypotheses are based on observable evidence — the record bounds every candidate reading."
- concept: artifact
  relationship: describes
  description: "Competing hypotheses describe the artifact — each candidate is a claim about what the artifact is."
- concept: surface-ambiguity
  relationship: resolves
  description: "Competing hypotheses resolve surface ambiguity — the reading set is the structured response to an ambiguous surface."
- concept: inference-from-behavior
  relationship: alternative_to
  description: "Competing hypotheses are alternatives to a single behavioural inference — the reading set holds the multiple inferences together."
- concept: incomplete-evidence
  relationship: constrained_by
  description: "Competing hypotheses are constrained by incomplete evidence — the reading set is bounded by what the capture shows."
- concept: likelihood
  relationship: informed_by
  description: "Competing hypotheses are informed by likelihood — each candidate's plausibility is estimated against the evidence."

## Tradeoffs
- dimension: hypothesis_breadth_vs_resolution_speed
  options:
    broad_set:
      value: completeness
      rationale: "A broad reading set resists premature commitment but slows resolution."
    narrow_set:
      value: tempo
      rationale: "A narrow set resolves quickly but risks excluding the true reading."
  importance: high
- dimension: hypothesis_independence_vs_evidence_fit
  options:
    independent_readings:
      value: discrimination
      rationale: "Independent readings discriminate on evidence; overlapping readings blur the test."
    best_fit_reading:
      value: plausibility
      rationale: "Fitting the best reading is efficient but rewards confirmation."
  importance: high

## Failure Modes
- name: premature_commitment
  description: "The reading set collapses to one candidate before discriminative evidence arrives."
  likelihood: high
  observable_evidence: "Single-reading analyses on ambiguous evidence; conclusions that predate discriminating observations"
  detection: "Reading-set review; commitment timestamps; per-candidate evidence counts"
  recovery: "Re-open the set; record which evidence would revive eliminated candidates"
  retryable: true
- name: confirmation_bias
  description: "Evidence is weighted by which reading it supports — the favoured candidate receives the benefit of every doubt."
  likelihood: high
  observable_evidence: "Favoured readings defended with weaker evidence than rivals; evidence classes unevenly investigated"
  detection: "Per-candidate evidence auditing; blind evaluation of new evidence"
  recovery: "Evaluate evidence against the reading set, not within it; weight by evidential force"
  retryable: true
- name: hypothesis_proliferation
  description: "The reading set grows without bound — every observation spawns new candidates and resolution never arrives."
  likelihood: medium
  observable_evidence: "Reading sets that grow with every capture; candidates without discriminative tests"
  detection: "Reading-set size tracking; per-candidate test availability"
  recovery: "Prune by discriminative testability; eliminate candidates the evidence cannot distinguish"
  retryable: true

## Observations
- observation: "Hypothesis multiplicity is the honest record of underdetermined evidence — a single confident reading on ambiguous evidence is a decision, not an observation."
  confidence: high
  source: Competing-hypothesis analysis practice
- observation: "Discriminative evidence is the scarce resource — analysts usually have enough confidence and not enough discrimination."
  confidence: high
  source: Analysis methodology
- observation: "The reading set is the working record — each candidate lives as a claim with its own confidence and evidence basis, and the set shrinks only when evidence discriminates."
  confidence: high
  source: Competing-hypothesis analysis practice

## Constraints
- constraint: "A hypothesis is a reading, never a fact — the reading set is structure over evidence, and the artifact is not changed by how it is read."
  type: invariant
  scope: cross-domain
- constraint: "Resolution requires discriminative evidence — eliminating a candidate is an evidence act, not a confidence act."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Maintain the reading set explicitly until evidence discriminates."
  rationale: "Explicit sets make commitment visible, revisable, and auditable."
  evidence_level: high
- heuristic: "Ask of every evidence item: which reading does this distinguish?"
  rationale: "Discriminative value is the evidence's real contribution."
  evidence_level: high

## Recommendations
- recommendation: "Evaluate new evidence against the reading set, not within it."
  context: analysis
  certainty: strong
  rationale: "Confirmation is the bias; discrimination is the discipline."
- recommendation: "Prune the reading set by discriminative testability."
  context: analysis
  certainty: strong
  rationale: "Candidates no evidence can distinguish do no work."
- recommendation: "Weight evidence by discriminative force, not by support for the favourite."
  context: analysis
  certainty: strong
  rationale: "Confirmation is the bias; discrimination is the discipline."
