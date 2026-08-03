# Autonomy Decision

## Identity
- id: autonomy-decision
- type: decision
- title: Autonomy Decision
- tags: [autonomy, decision, action generation, incomplete model, open world]
- entities: [autonomy decision, action generation, option set, oversight, risk]
- concepts: [belief-state, actuation, safety-case, risk-acceptance, scheduling-policy]

## Claims
- claim: "An autonomy decision is a decision under an incomplete world model — generating options, not choosing among predefined ones."
  certainty: high
  evidence: Robotics and autonomous systems practice (P6)
  scope: cross-domain
- claim: "Action generation is option creation under uncertainty — the decision structure extends to open action spaces without a new construct."
  certainty: high
  evidence: Cross-domain comparison (decision objects 007-011)
  scope: cross-domain
- claim: "The autonomy decision is the Epistemic Chain's decision node — belief informs the decision, the decision informs actuation."
  certainty: high
  evidence: Epistemic Chain watch (Cycle 012)
  scope: cross-domain
- claim: "Autonomy is posture, not property — the degree of autonomy is chosen per context, exactly as hard/soft posture is chosen."
  certainty: high
  evidence: Mode-divergence pattern (009, 011)
  scope: cross-domain
- claim: "Autonomy decisions are valid only under stated conditions — the world model's conditions bound the decision's claims."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain

## Decision Factors
- factor: information_gain
  question: "How much would the action's outcome improve the world model?"
  supporting: "Informative actions refine the model for future decisions."
  contradictory: "Uninformative actions consume physical resources without learning."
  weight: high
- factor: risk_tolerance
  question: "How much physical risk may this decision accept?"
  supporting: "Stated tolerance bounds the decision's reach."
  contradictory: "Unstated tolerance invites the decision to exceed its envelope."
  weight: high
- factor: action_irreversibility
  question: "How reversible is the action, and what does irreversibility cost?"
  supporting: "Reversible actions tolerate error; irreversible ones demand evidence."
  contradictory: "Irreversible actions convert a small error into a permanent state."
  weight: high
- factor: oversight_availability
  question: "Can oversight review the action before or after execution?"
  supporting: "Oversight catches overreach before it becomes harm."
  contradictory: "No oversight means the decision is the only gate."
  weight: high

## Relationships
- concept: belief-state
  relationship: constrained_by
  description: "The autonomy decision is constrained by belief-state — the world model's confidence bounds the decision."
- concept: actuation
  relationship: informs
  description: "The autonomy decision informs actuation — the chosen action becomes the command."
- concept: safety-case
  relationship: constrained_by
  description: "The autonomy decision is constrained by safety-case — the assurance envelope bounds what may be decided."
- concept: risk-acceptance
  relationship: analogous_to
  description: "The autonomy decision is analogous to risk acceptance — decision under uncertainty — the Cycle 007 cross-domain link."
- concept: scheduling-policy
  relationship: analogous_to
  description: "The autonomy decision is analogous to scheduling policy — posture chosen under constraints — the Cycle 011 cross-domain link."

## Tradeoffs
- dimension: autonomy_vs_oversight
  options:
    autonomous_action:
      value: responsiveness
      rationale: "Autonomous action reacts at physical speed."
    overseen_action:
      value: accountability
      rationale: "Oversight verifies before acting."
  importance: high
- dimension: action_speed_vs_evidence
  options:
    act_fast:
      value: timeliness
      rationale: "Fast action exploits the current opportunity."
    gather_evidence:
      value: confidence
      rationale: "More evidence reduces the epistemic gap."
  importance: medium

## Failure Modes
- name: overreach
  description: "The decision acts beyond its authority or its model's validity — autonomy exceeds its stated conditions."
  likelihood: medium
  observable_evidence: "Actions outside the envelope; decisions beyond the model; authority violations"
  detection: "Envelope monitoring; authority audits; decision review"
  recovery: "Restrict autonomy; re-scope; verify the envelope"
  retryable: true
- name: unsafe_option_generation
  description: "The generated option set includes unsafe actions — action generation produces what selection would reject."
  likelihood: medium
  observable_evidence: "Unsafe options in the set; generation/selection mismatch; hazard reachable"
  detection: "Option-set audits; hazard screening; generation review"
  recovery: "Constrain generation; add screening; restrict the action space"
  retryable: true
- name: decision_stall
  description: "The system cannot decide — under an incomplete model, the decision defers until the opportunity passes."
  likelihood: medium
  observable_evidence: "Inaction; missed opportunities; deliberation past the window"
  detection: "Decision-timing monitoring; stall detection; window checks"
  recovery: "Set decision deadlines; degrade to a default; re-scope the decision"
  retryable: true

## Observations
- observation: "Autonomy resolved as decision under an incomplete world model — the open action space did not require an action-generation construct."
  confidence: high
  source: P6 test (Cycle 012)
- observation: "Action generation is option creation under uncertainty — the decision structure held in open spaces, the factor count at 4."
  confidence: high
  source: Decision-object pattern (007-011)
- observation: "The decision node sits at the Epistemic Chain's end — belief informs decision, decision informs action, and the loop closes at sensing."
  confidence: high
  source: Epistemic Chain watch (Cycle 012)
- observation: "Decision stall is the open-world failure — the incomplete model is not a reason to defer past the window."
  confidence: high
  source: Autonomous systems practice

## Constraints
- constraint: "Autonomy is decision under an incomplete model — the model's confidence bounds the decision's claims."
  type: invariant
  scope: cross-domain
- constraint: "Every autonomous action is an action on belief — verification closes the gap, and the envelope bounds the action."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Scope autonomy to the verified envelope."
  rationale: "Autonomy is a posture decision — the envelope is its stated condition."
  evidence_level: high
- heuristic: "Give decisions deadlines too."
  rationale: "Decision stall is a failure mode — under an incomplete model, deferral is a decision."
  evidence_level: high

## Recommendations
- recommendation: "Represent autonomy as decision objects in open action spaces — generation is part of the decision, not a construct."
  context: modelling
  certainty: strong
  rationale: "The decision structure held at n=12 — option generation is uncertainty, not ontology."
- recommendation: "Bound autonomous action by the verified envelope."
  context: engineering
  certainty: strong
  rationale: "Overreach is the failure mode — the envelope is the stated condition."
- recommendation: "Audit the generated option set, not only the chosen action."
  context: operations
  certainty: strong
  rationale: "Unsafe generation is where hazard enters before selection."
