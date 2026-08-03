# Disclosure Decision

## Identity
- id: disclosure-decision
- type: decision
- title: Disclosure Decision on Incomplete Reconstruction
- tags: [disclosure, decision, artifact analysis, incomplete reconstruction, sharing, response]
- entities: [disclosure decision, sharing decision, disclosure call, information release decision]
- concepts: [attribution, concealed-intent, reconstruction-confidence, competing-hypotheses, risk-acceptance]

## Claims
- claim: "The disclosure decision is whether, what, and to whom to reveal about the artifact — a decision taken on a reconstruction that is still open."
  certainty: high
  evidence: Incident response and disclosure practice
  scope: cross-domain
- claim: "Disclosure is irreversible — once revealed, the reconstruction's claims leave the analyst's control, and the decision prices that."
  certainty: high
  evidence: Disclosure practice
  scope: cross-domain
- claim: "Disclosure decisions are qualified by the reconstruction's confidence — what is disclosed carries the chain's qualification, and the disclosure carries its limits."
  certainty: high
  evidence: Decision analysis practice
  scope: cross-domain
- claim: "Disclosure decisions are made on open reconstructions — what is revealed inherits what the analysis still does not know."
  certainty: high
  evidence: Decision analysis practice
  scope: cross-domain
- claim: "The disclosure decision is the point where the analysis's epistemic limits become public — the reader of the disclosure inherits the chain's openness."
  certainty: high
  evidence: Disclosure practice
  scope: cross-domain

## Relationships
- concept: attribution
  relationship: informed_by
  description: "The disclosure decision is informed by attribution — the origin claim shapes what is safe to reveal."
- concept: concealed-intent
  relationship: informed_by
  description: "The disclosure decision is informed by concealed intent — the purpose claim shapes the disclosure's content."
- concept: reconstruction-confidence
  relationship: qualified_by
  description: "The disclosure decision is qualified by reconstruction confidence — the disclosure inherits the chain's qualification."
- concept: competing-hypotheses
  relationship: constrained_by
  description: "The disclosure decision is constrained by competing hypotheses — the open reading set bounds what can be asserted."
- concept: risk-acceptance
  relationship: serves
  description: "The disclosure decision serves risk acceptance — revealing or withholding is an accepted-risk act."

## Tradeoffs
- dimension: disclosure_breadth_vs_chain_openness
  options:
    broad_disclosure:
      value: transparency
      rationale: "Broad disclosure shares the findings but shares the open chain."
    narrow_disclosure:
      value: control
      rationale: "Narrow disclosure controls the record but withholds context."
  importance: high
- dimension: disclose_now_vs_reconstruct_first
  options:
    disclose_early:
      value: warning
      rationale: "Early disclosure warns while the artifact is active."
    reconstruct_first:
      value: accuracy
      rationale: "Closed reconstructions disclose accurately but late."
  importance: high

## Failure Modes
- name: disclosure_overconfidence
  description: "The disclosure asserts more than the chain carries — the open reading set is disclosed as a closed conclusion."
  likelihood: high
  observable_evidence: "Disclosures presenting single readings on open chains; attribution asserted without qualification; disclosed conclusions later reversed"
  detection: "Disclosure-vs-chain audit; qualification consistency review"
  recovery: "Carry the chain's qualification into the disclosure; disclose reading sets as reading sets"
  retryable: false
- name: disclosure_irreversibility_ignored
  description: "The disclosure is treated as revisable — the decision prices none of the loss of control that revelation causes."
  likelihood: medium
  observable_evidence: "Disclosures made as if they could be recalled; post-disclosure corrections without disclosure context"
  detection: "Disclosure-reversibility review"
  recovery: "Price irreversibility as a factor; draft disclosures as final"
  retryable: true
- name: disclosure_paralysis
  description: "The open chain blocks disclosure entirely — the reader is never warned because the reconstruction is never closed."
  likelihood: medium
  observable_evidence: "No disclosure on active artifacts; warnings withheld pending 'completion'"
  detection: "Disclosure-latency review"
  recovery: "Disclose the chain's openness as part of the disclosure; warn with qualification"
  retryable: true

## Observations
- observation: "Openness and irreversibility are carried in the disclosure's factors — the open reconstruction is priced with the call, and the record shows the loss of control."
  confidence: high
  source: Decision analysis practice
- observation: "Disclosure is where the chain becomes public — the reader inherits the reconstruction's limits, and the disclosure's honesty is the chain's honesty."
  confidence: high
  source: Decision analysis practice
- observation: "Irreversibility is the disclosure's signature — every other decision in the cycle can be revised; disclosure cannot."
  confidence: high
  source: Disclosure practice

## Constraints
- constraint: "A disclosure inherits its chain's qualification — what is revealed carries the reconstruction's openness, and the reader is told so."
  type: invariant
  scope: cross-domain
- constraint: "Disclosure is irreversible — the decision prices the loss of control, and nothing disclosed is treated as revisable."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: chain_openness
  question: "How open is the reconstruction this disclosure would present?"
  supporting: "Disclosed openness keeps the reader honest about the chain."
  contradictory: "Disclosed closure asserts what the chain does not carry."
  weight: high
- factor: irreversibility
  question: "What is lost by revealing this, and can it never be taken back?"
  supporting: "Priced irreversibility disciplines the disclosure's content."
  contradictory: "Unpriced irreversibility treats revelation as reversible."
  weight: high
- factor: reader_consequence
  question: "What will the reader do with this disclosure, and at what risk?"
  supporting: "Visible reader consequence shapes content and timing."
  contradictory: "Ignored reader consequence lets the disclosure misfire."
  weight: high
- factor: timing_window
  question: "When must the warning arrive to be useful?"
  supporting: "Timing analysis balances warning value against chain openness."
  contradictory: "Late disclosure is a disclosure about a past artifact."
  weight: medium

## Heuristics
- heuristic: "Disclose the chain's openness with the disclosure."
  rationale: "The reader inherits the chain; telling them so is the honesty."
  evidence_level: high
- heuristic: "Draft every disclosure as final."
  rationale: "Irreversibility is the decision's signature; drafting as final prices it."
  evidence_level: high

## Recommendations
- recommendation: "Carry the reconstruction's confidence into the disclosure text."
  context: analysis
  certainty: strong
  rationale: "The reader inherits the chain's limits; the disclosure must say so."
- recommendation: "Carry the chain's qualification into every disclosure."
  context: operations
  certainty: strong
  rationale: "The reader inherits the chain's limits; the disclosure must say so."
- recommendation: "Price irreversibility explicitly in every disclosure decision."
  context: operations
  certainty: strong
  rationale: "Unpriced irreversibility is the disclosure's corruption."
