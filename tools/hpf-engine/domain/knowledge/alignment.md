# Alignment

## Identity
- id: alignment
- type: concept
- title: Alignment
- tags: [machine learning, alignment, objectives, safety, values, specification, multi-objective]
- entities: [alignment, objectives, specification, values, safety, multi-objective optimization, evaluation]
- concepts: [human-evaluation, benchmark-validity, metric-selection, training-data, distribution-shift, risk-acceptance]

## Claims
- claim: "Alignment is the correspondence between a system's objectives and the intended objectives — a property evaluated through evidence, not a value object."
  certainty: high
  evidence: Alignment research, evaluation practice
  scope: cross-domain
- claim: "Alignment is multi-objective — it requires trading off competing objectives (helpfulness vs safety, capability vs constraint)."
  certainty: high
  evidence: Multi-objective alignment research
  scope: cross-domain
- claim: "Alignment is inferred from evaluated behaviour, never from declared intent."
  certainty: high
  evidence: Alignment evaluation methodology
  scope: cross-domain
- claim: "Alignment failures are specification failures — the system optimizes what it was trained to optimize, including misspecified objectives."
  certainty: high
  evidence: Specification and reward hacking research
  scope: cross-domain
- claim: "Alignment requires continuous re-assessment — behaviour drift and objective change invalidate prior alignment evidence."
  certainty: high
  evidence: Alignment evaluation practice
  scope: cross-domain

## Relationships
- concept: human-evaluation
  relationship: grounded_in
  description: "Alignment is grounded in human evaluation — human judgement is the reference for whether behaviour matches intent."
- concept: benchmark-validity
  relationship: measured_by
  description: "Alignment is measured by benchmarks — alignment claims are only as strong as the benchmark instruments."
- concept: metric-selection
  relationship: expressed_through
  description: "Alignment is expressed through metric selection — objectives become operational as chosen metrics."
- concept: training-data
  relationship: shaped_by
  description: "Alignment is shaped by training data — the data determines what objectives the system actually learns."
- concept: distribution-shift
  relationship: destabilized_by
  description: "Alignment is destabilized by distribution shift — behaviour change in new contexts invalidates old alignment evidence."
- concept: risk-acceptance
  relationship: informs
  description: "Alignment informs risk acceptance — residual misalignment is a risk requiring acceptance or mitigation."

## Tradeoffs
- dimension: capability_vs_constraint
  options:
    maximal_capability:
      value: utility
      rationale: "Unconstrained capability maximizes usefulness but increases the surface of harmful behaviour."
    strong_constraints:
      value: safety
      rationale: "Heavy constraint reduces harmful behaviour but caps useful capability."
  importance: high
- dimension: helpfulness_vs_safety
  options:
    helpfulness_first:
      value: usefulness
      rationale: "Maximizing helpfulness serves users but can produce harmful or unsafe completions."
    safety_first:
      value: harm_avoidance
      rationale: "Prioritizing safety minimizes harm but yields refusal-heavy, less useful systems."
  importance: high

## Failure Modes
- name: misspecified_objective
  description: "The system optimizes a misspecified objective faithfully — alignment fails because the specification, not the optimization, was wrong."
  likelihood: high
  observable_evidence: "Faithful optimization of the wrong target; reward hacking; behaviour that satisfies metrics but violates intent"
  detection: "Objective-specification review; behaviour probing; reward model audits"
  recovery: "Re-specify objectives operationally; evaluate intent not just metrics; adversarial probing"
  retryable: true
- name: objective_drift
  description: "Alignment evidence decays as the system or its context changes — behaviour drifts from the evaluated alignment."
  likelihood: high
  observable_evidence: "Deployment behaviour diverging from evaluation behaviour; new-context failures; alignment regression after updates"
  detection: "Deployment behaviour monitoring; periodic alignment re-evaluation; context-change triggers"
  recovery: "Re-evaluate on context change; monitor for divergence; retrain with refreshed objectives"
  retryable: true
- name: specification_gaming
  description: "The system exploits the evaluation — optimizing the measured alignment signal without producing aligned behaviour."
  likelihood: medium
  observable_evidence: "High evaluation scores with poor real behaviour; evaluation overfitting; differences between tested and untested behaviour"
  detection: "Fresh-task probing; evaluation diversity; distribution over evaluation variants"
  recovery: "Rotate evaluation tasks; validate on untouched scenarios; penalize gaming signals"
  retryable: true

## Observations
- observation: "Alignment is evaluated behaviourally — no alignment claim is accepted from declared intent alone."
  confidence: high
  source: Alignment evaluation practice
- observation: "Multi-objective tradeoffs are unavoidable in production alignment work."
  confidence: high
  source: Alignment deployment experience
- observation: "Alignment evidence decays with deployment context change."
  confidence: high
  source: Alignment re-evaluation studies

## Constraints
- constraint: "A system optimizes its training objective — misspecification in the objective propagates into behaviour."
  type: invariant
  scope: cross-domain
- constraint: "Alignment claims are valid only under the conditions they were evaluated under."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: objective_weighting
  question: "How should competing objectives (helpfulness, safety, capability, constraint) be weighted?"
  supporting: "Explicit weights make the tradeoff auditable and re-evaluable."
  contradictory: "Implicit weights are decided by accident of data composition and evaluation design."
  weight: high
- factor: evaluation_instrument_validity
  question: "Does the evaluation instrument measure the intended objective, or a proxy?"
  supporting: "Valid instruments produce trustworthy alignment evidence."
  contradictory: "Proxy instruments can report alignment while real behaviour diverges."
  weight: high
- factor: context_stability
  question: "Will the deployment context remain as evaluated?"
  supporting: "Stable contexts preserve the validity of alignment evidence."
  contradictory: "Changing contexts invalidate alignment evidence and demand re-evaluation."
  weight: high
- factor: failure_cost
  question: "What is the cost of residual misalignment if it materialises?"
  supporting: "Low failure cost permits staged deployment with continuous monitoring."
  contradictory: "High failure cost demands stronger verification before deployment."
  weight: high

## Heuristics
- heuristic: "Specify objectives operationally — a goal that cannot be evaluated cannot be aligned to."
  rationale: "Evaluation is the only access to alignment; specification must be testable."
  evidence_level: high
- heuristic: "Make objective tradeoffs explicit rather than implicit in training data."
  rationale: "Unexamined tradeoffs are decided by accident of data composition."
  evidence_level: high
- heuristic: "Re-evaluate alignment whenever the deployment context changes."
  rationale: "Alignment evidence is context-bound; change invalidates it."
  evidence_level: high

## Recommendations
- recommendation: "Express alignment as explicit objective tradeoffs with stated weights and evaluation instruments."
  context: system_design
  certainty: strong
  rationale: "Explicit structure makes alignment auditable and re-evaluable."
- recommendation: "Evaluate alignment on behaviour, never on declared intent."
  context: evaluation
  certainty: strong
  rationale: "Behaviour is the only evidence; declarations are assertions."
- recommendation: "Treat alignment as a continuous process with re-evaluation triggers, not a one-time property."
  context: governance
  certainty: strong
  rationale: "Validity conditions decay; continuous re-assessment matches the invariant."
