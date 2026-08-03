# Containment Decision

## Identity
- id: containment-decision
- type: decision
- title: Containment Decision on Incomplete Reconstruction
- tags: [containment, decision, artifact analysis, incomplete reconstruction, isolation, response]
- entities: [containment decision, isolation decision, containment call, quarantine decision]
- concepts: [detection-decision, concealed-intent, reconstruction-confidence, incomplete-evidence, incident-response]

## Claims
- claim: "The containment decision is whether and how far to isolate the artifact — a decision taken while the reconstruction is still open."
  certainty: high
  evidence: Incident response practice, adversarial analysis
  scope: cross-domain
- claim: "Containment is decided before the reconstruction is complete — the point of containment is to act while the artifact's reach is still unknown."
  certainty: high
  evidence: Incident response practice
  scope: cross-domain
- claim: "Containment decisions are qualified by the reconstruction's confidence and bounded by its gaps — the unknown reach is part of the decision's evidence."
  certainty: high
  evidence: Decision analysis practice
  scope: cross-domain
- claim: "Containment is a decision about unknown reach — what isolation cannot see is what isolation must bound."
  certainty: high
  evidence: Decision analysis practice
  scope: cross-domain
- claim: "Containment can be staged — the decision is not binary; isolation depth is chosen against the reconstruction's openness."
  certainty: high
  evidence: Incident response practice
  scope: cross-domain

## Relationships
- concept: detection-decision
  relationship: triggered_by
  description: "The containment decision is triggered by the detection decision — the containment call comes after the detection call."
- concept: concealed-intent
  relationship: informed_by
  description: "The containment decision is informed by concealed intent — the reach claim shapes the isolation depth."
- concept: reconstruction-confidence
  relationship: qualified_by
  description: "The containment decision is qualified by reconstruction confidence — the decision inherits the chain's qualification."
- concept: incomplete-evidence
  relationship: constrained_by
  description: "The containment decision is constrained by incomplete evidence — unknown reach bounds every isolation call."
- concept: incident-response
  relationship: serves
  description: "The containment decision serves incident response — isolation is the response's first act."

## Tradeoffs
- dimension: isolation_depth_vs_operational_cost
  options:
    deep_isolation:
      value: safety
      rationale: "Deep isolation contains unknown reach but disrupts the environment."
    shallow_isolation:
      value: continuity
      rationale: "Shallow isolation preserves operations but risks the unknown reach."
  importance: high
- dimension: contain_early_vs_reconstruct_first
  options:
    contain_now:
      value: containment
      rationale: "Containing now bounds the artifact's reach while it is still bounded."
    reconstruct_first:
      value: precision
      rationale: "Reconstruction-first containment is precise but may be too late."
  importance: high

## Failure Modes
- name: containment_underreach
  description: "Isolation is shallower than the unknown reach — the artifact's uncovered scope is assumed contained."
  likelihood: high
  observable_evidence: "Post-isolation discovery of spread; containment scopes matched to known reach only"
  detection: "Reach-vs-scope review; containment boundary audits"
  recovery: "Widen isolation to the unknown reach's bound; treat known-reach containment as provisional"
  retryable: true
- name: containment_overreach
  description: "Isolation exceeds what the evidence supports — the environment pays for a reach the reconstruction does not carry."
  likelihood: medium
  observable_evidence: "Isolation scope far beyond any reconstructed reach; operational damage from over-containment"
  detection: "Scope-vs-chain audit; cost review"
  recovery: "Stage containment downward as the reconstruction improves"
  retryable: true
- name: qualification_loss_at_decision
  description: "The containment call is more certain than its chain — the unknown reach is acted on as if it were known."
  likelihood: high
  observable_evidence: "Decisive containment on open reading sets; unknown reach unrecorded in the decision"
  detection: "Chain-to-decision audit"
  recovery: "Attach the chain's qualification; stage containment by confidence"
  retryable: true

## Observations
- observation: "The unknown reach is carried in the decision's factors — bounding what is not known is priced like any other input, and the record shows the bound with the call."
  confidence: high
  source: Decision analysis practice
- observation: "Staging is the containment decision's natural structure — isolation depth follows confidence, and the decision is revisable as the reconstruction closes."
  confidence: high
  source: Incident response practice
- observation: "Underreach is the concealment-designed failure — the artifact's unknown scope is exactly what isolation must bound."
  confidence: high
  source: Containment analysis

## Constraints
- constraint: "Containment inherits the reconstruction's qualification — a containment call cannot be more certain than the reach claim it bounds."
  type: invariant
  scope: cross-domain
- constraint: "Containment is staged by confidence — isolation depth is chosen against the openness of the reconstruction, and is revisable as it closes."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: unknown_reach
  question: "How far can the artifact's reach extend beyond what is known?"
  supporting: "Bounding the unknown reach sets the isolation scope's floor."
  contradictory: "Assuming known reach equals actual reach is the underreach failure."
  weight: high
- factor: reconstruction_confidence
  question: "What is the confidence in the reconstruction this containment is built on?"
  supporting: "Calibrated confidence stages isolation depth honestly."
  contradictory: "Uncalibrated confidence over- or under-isolates."
  weight: high
- factor: operational_cost
  question: "What does isolation depth cost the environment?"
  supporting: "Visible operational cost disciplines overreach."
  contradictory: "Hidden cost lets containment exceed its evidence."
  weight: high
- factor: staging_ability
  question: "Can containment be deepened or lightened as the reconstruction improves?"
  supporting: "Staged containment is revisable and therefore safe to start."
  contradictory: "Binary containment locks the environment to one isolation depth."
  weight: medium

## Heuristics
- heuristic: "Bound the unknown reach before choosing isolation depth."
  rationale: "The unknown reach is the containment's real target."
  evidence_level: high
- heuristic: "Stage containment by confidence — start where the chain supports, deepen as it closes."
  rationale: "Staging makes containment revisable and honest."
  evidence_level: high

## Recommendations
- recommendation: "Record the unknown reach explicitly before choosing isolation depth."
  context: analysis
  certainty: strong
  rationale: "The unknown reach is the containment's real target."
- recommendation: "Set isolation scope from the unknown reach's bound, not the known reach."
  context: operations
  certainty: strong
  rationale: "Known-reach containment is the underreach failure."
- recommendation: "Stage containment and revise as the reconstruction closes."
  context: operations
  certainty: strong
  rationale: "Revisable containment is safe containment."
