# Belief State

## Identity
- id: belief-state
- type: concept
- title: Belief State
- tags: [belief, belief state, world model, POMDP, confidence, internal representation]
- entities: [belief, belief state, world model, confidence, posterior]
- concepts: [state-estimation, actuation, probabilistic-outputs, incomplete-evidence, physical-state]

## Claims
- claim: "A belief state is the system's internal model of the world — a distribution over possible states, expressed as claims qualified by confidence."
  certainty: high
  evidence: Robotics and POMDP literature
  scope: cross-domain
- claim: "Belief is composition, not ontology — a belief state is a set of qualified observations combined through a model, never a new knowledge type."
  certainty: high
  evidence: P5 test (Cycle 012 — the danger object)
  scope: cross-domain
- claim: "The epistemic gap lives inside the belief — belief is about the model, never about reality directly."
  certainty: high
  evidence: State estimation theory (P5)
  scope: cross-domain
- claim: "Confidence is the qualification that carries distance — the same structure as uncertainty (007) and probabilistic outputs (008)."
  certainty: high
  evidence: Cross-domain comparison (qualification model 007/008)
  scope: cross-domain
- claim: "A belief state is valid only under the observations and model that produced it — stale or mismatched beliefs invalidate decisions."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain

## Relationships
- concept: state-estimation
  relationship: produced_by
  description: "Belief state is produced by state estimation — the internal model built from observations."
- concept: actuation
  relationship: informs
  description: "Belief state informs actuation — decisions act on the belief, never on reality directly."
- concept: probabilistic-outputs
  relationship: analogous_to
  description: "Belief state is analogous to probabilistic outputs — a distribution as a qualified claim — the Cycle 008 cross-domain link."
- concept: physical-state
  relationship: describes
  description: "Belief state describes physical state — the belief is about the state, at an epistemic distance."
- concept: incomplete-evidence
  relationship: constrained_by
  description: "Belief state is constrained by incomplete evidence — the belief is built from what the world permits observing."

## Tradeoffs
- dimension: confidence_vs_resolution
  options:
    confident_belief:
      value: decisive_action
      rationale: "Confident beliefs act decisively."
    wide_belief:
      value: honesty
      rationale: "Wide beliefs are honest about the gap."
  importance: high
- dimension: current_belief_vs_history
  options:
    current_only:
      value: responsiveness
      rationale: "Current beliefs react fast."
    historical_belief:
      value: robustness
      rationale: "Historical beliefs resist single-sensor errors."
  importance: medium

## Failure Modes
- name: belief_divergence
  description: "The belief departs from reality — the internal model no longer corresponds to the world it models."
  likelihood: medium
  observable_evidence: "Prediction/observation mismatch; unexpected behaviour; surprise events"
  detection: "Innovation monitoring; belief-vs-reality checks; divergence tests"
  recovery: "Re-estimate; reset the belief; correct the model"
  retryable: true
- name: overconfidence
  description: "The belief is sharper than its evidence supports — confidence exceeds the qualification the observations justify."
  likelihood: medium
  observable_evidence: "Surprise despite high confidence; underestimated uncertainty; sharp beliefs on weak evidence"
  detection: "Calibration audits; confidence-vs-outcome tracking; ensemble disagreement"
  recovery: "Widen uncertainty; recalibrate; treat overconfident beliefs as suspect"
  retryable: true
- name: stale_belief
  description: "The belief describes a past world — the model is older than the conditions it was valid under."
  likelihood: medium
  observable_evidence: "Actions on outdated conditions; lag behind physical events; invalidated beliefs"
  detection: "Update-timing checks; staleness monitoring; validity-window tracking"
  recovery: "Re-estimate; invalidate stale beliefs; reject decisions on them"
  retryable: true

## Observations
- observation: "Belief is the strongest candidate for a belief primitive in the programme — and it resolves as composition: qualified observations over a state space."
  confidence: high
  source: P5 test (Cycle 012 — danger object)
- observation: "Epistemic Distance at belief is 2–3 — the belief is two or three inferential layers above reality, and the distance is carried by confidence."
  confidence: high
  source: Epistemic Distance metric (Cycle 012 pre-registration)
- observation: "Overconfidence is the belief's characteristic failure — the qualification collapses before the model does."
  confidence: high
  source: Calibration practice (008)
- observation: "The belief is where the epistemic gap is acted upon — decisions act on belief, and verification closes the gap."
  confidence: high
  source: Epistemic Chain watch (Cycle 012)

## Constraints
- constraint: "A belief is valid only under the observations and model that produced it — overconfidence is a failure of qualification, not of perception."
  type: invariant
  scope: cross-domain
- constraint: "Decisions act on belief, never on reality directly — the epistemic gap is structural, closed only by verification."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Qualify every belief with its confidence before acting."
  rationale: "The qualification carries the distance from reality."
  evidence_level: high
- heuristic: "Audit calibration, not just accuracy."
  rationale: "A belief can be wrong and honest, or right and overconfident — only calibration audits distinguish them."
  evidence_level: high

## Recommendations
- recommendation: "Represent belief as qualified observation composition, never as a belief construct."
  context: modelling
  certainty: strong
  rationale: "The P5 test: belief is the distribution of possible states under evidence — composition, not ontology."
- recommendation: "Treat overconfidence as the belief failure mode to manage."
  context: engineering
  certainty: strong
  rationale: "Overconfident beliefs act with certainty across a gap they did not measure."
- recommendation: "Update belief on new observation — the loop closes at the next sensing."
  context: operations
  certainty: strong
  rationale: "A stale belief is invalid under current conditions; freshness is a validity condition."
