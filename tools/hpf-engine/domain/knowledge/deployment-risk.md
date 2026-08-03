# Deployment Risk

## Identity
- id: deployment-risk
- type: concept
- title: Deployment Risk
- tags: [machine learning, deployment, risk, rollout, canary, rollback, staged deployment]
- entities: [deployment risk, model rollout, canary deployment, rollback, staging, residual risk]
- concepts: [risk-acceptance, model-monitoring, retraining-decisions, distribution-shift, uncertainty-estimation, benchmark-validity]

## Claims
- claim: "Deployment risk is the exposure created by putting a model into production — failure likelihood and impact, under validity conditions."
  certainty: high
  evidence: Risk management practice, deployment research
  scope: cross-domain
- claim: "Deployment risk is reducible by evidence — validation, monitoring, rollback, and staged rollout convert unknown risk into managed risk."
  certainty: high
  evidence: Deployment practice, incident analyses
  scope: cross-domain
- claim: "Deployment risk changes over time — drift, context change, and model updates alter the risk profile after deployment."
  certainty: high
  evidence: ML operations practice
  scope: cross-domain
- claim: "Deployment risk is partially residual — acceptable residual risk is a decision, informed by monitoring and response capability."
  certainty: high
  evidence: Risk management practice
  scope: cross-domain
- claim: "Deployment risk composes with existing risk knowledge — model risk is a case of the risk-acceptance structure, not a new kind of risk."
  certainty: high
  evidence: Cycle 008 authoring evidence, risk management practice
  scope: cross-domain

## Relationships
- concept: risk-acceptance
  relationship: informs
  description: "Deployment risk informs risk acceptance — residual model risk is accepted or mitigated by the standard risk structure."
- concept: model-monitoring
  relationship: reduced_by
  description: "Deployment risk is reduced by model monitoring — observability converts unknown risk into managed risk."
- concept: retraining-decisions
  relationship: modifies
  description: "Retraining decisions modify deployment risk — every update changes the risk profile."
- concept: distribution-shift
  relationship: increased_by
  description: "Deployment risk is increased by distribution shift — drift raises failure likelihood."
- concept: uncertainty-estimation
  relationship: quantified_by
  description: "Deployment risk is quantified by uncertainty estimation — estimated failure likelihood feeds the risk calculation."
- concept: benchmark-validity
  relationship: assessed_by
  description: "Deployment risk is assessed by benchmark validity — pre-deployment evaluation is part of the risk assessment."

## Tradeoffs
- dimension: deployment_speed_vs_assurance
  options:
    fast_deployment:
      value: velocity
      rationale: "Quick deployment captures value sooner but ships less-validated risk."
    verified_deployment:
      value: assurance
      rationale: "Verified deployment reduces risk but delays value capture."
  importance: high
- dimension: staged_vs_all_at_once
  options:
    staged_rollout:
      value: blast_radius_control
      rationale: "Canary stages contain failure to a small blast radius."
    full_rollout:
      value: simplicity
      rationale: "Full rollout is simpler but exposes the entire surface to failure."
  importance: high

## Failure Modes
- name: unknown_risk_deployment
  description: "The model is deployed without evidence about its failure modes — risk is unmeasured because nothing was assessed."
  likelihood: high
  observable_evidence: "Deployment without evaluation evidence; no failure-mode analysis; surprise production failures"
  detection: "Deployment readiness audit; evidence coverage check"
  recovery: "Require evaluation and failure-mode evidence before deployment; gate releases on readiness"
  retryable: true
- name: unmonitored_rollout
  description: "Deployment without monitoring or rollback capability — recoverable failures become incidents."
  likelihood: high
  observable_evidence: "Incidents during rollout; no rollback path exercised; monitoring absent at deployment"
  detection: "Rollout capability audit; rollback drill results"
  recovery: "Require monitoring and rollback before production; exercise rollback in staging"
  retryable: true
- name: residual_risk_amnesia
  description: "Accepted residual risk is forgotten as conditions change — the acceptance decision ages into unexamined exposure."
  likelihood: medium
  observable_evidence: "Accepted risks without review dates; conditions changed since acceptance; surprise exposure"
  detection: "Acceptance review audit; condition-change monitoring"
  recovery: "Time-box acceptances; re-review on context change; track acceptance expiry"
  retryable: true

## Observations
- observation: "Staged rollouts dominate incident-free deployments."
  confidence: high
  source: Deployment practice, incident analyses
- observation: "Deployment without rollback capability converts recoverable failures into incidents."
  confidence: high
  source: Incident post-mortems
- observation: "Risk assessments decay with deployment age — acceptances and assumptions age with the system."
  confidence: high
  source: Risk management practice

## Constraints
- constraint: "Deployment risk cannot be reduced beyond the coverage of validation and monitoring evidence."
  type: invariant
  scope: cross-domain
- constraint: "Accepted risk must be revisited when conditions change — acceptance expires with its conditions."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Deploy the smallest blast radius first — canary before broad rollout."
  rationale: "Staged exposure converts large failures into small learnable ones."
  evidence_level: high
- heuristic: "Verify the rollback before the rollout — untested rollback is not a rollback."
  rationale: "The fallback must be proven before the risk is taken."
  evidence_level: high
- heuristic: "Document residual risk with an expiry — acceptance decays with its conditions."
  rationale: "Time-boxed acceptance forces re-evaluation when conditions change."
  evidence_level: high

## Recommendations
- recommendation: "Stage rollouts with canary segments and measured outcomes between stages."
  context: rollout_design
  certainty: strong
  rationale: "Staging bounds blast radius and generates the evidence for the next stage."
- recommendation: "Require monitoring and a verified rollback path before any production deployment."
  context: deployment_governance
  certainty: strong
  rationale: "These are the capabilities that convert unknown risk into managed risk."
- recommendation: "Re-assess accepted residual risk whenever context or model conditions change."
  context: risk_governance
  certainty: strong
  rationale: "Acceptance expires with its conditions; re-assessment keeps residual risk visible."
