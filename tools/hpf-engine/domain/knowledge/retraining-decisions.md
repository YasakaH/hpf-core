# Retraining Decisions

## Identity
- id: retraining-decisions
- type: decision
- title: Retraining Decisions
- tags: [machine learning, retraining, model updates, feedback loop, scheduling, validation, rollback]
- entities: [retraining, retraining decision, model update, feedback loop, retraining trigger, model versioning]
- concepts: [distribution-shift, model-monitoring, drift-detection, training-data, deployment-risk, generalization]

## Claims
- claim: "Retraining is an intervention on a live system — it carries regression risk and must be decided, not scheduled by default."
  certainty: high
  evidence: ML operations practice, incident analyses
  scope: cross-domain
- claim: "Retraining should be triggered by evidence (verified shift, degraded performance, new data) rather than by calendar or habit."
  certainty: high
  evidence: Retraining practice and research
  scope: cross-domain
- claim: "Retraining is a feedback operation — the system updates its own behaviour from new observations."
  certainty: high
  evidence: Adaptive system practice
  scope: cross-domain
- claim: "Retraining outcomes must be validated before deployment — the retrained model is a hypothesis until evaluated on fresh data."
  certainty: high
  evidence: ML operations practice
  scope: cross-domain
- claim: "Retraining frequency trades freshness against stability — too frequent amplifies noise; too rare compounds staleness."
  certainty: high
  evidence: Retraining research, operations practice
  scope: cross-domain

## Relationships
- concept: distribution-shift
  relationship: triggered_by
  description: "Retraining is triggered by distribution shift — verified shift is the evidence-based trigger."
- concept: model-monitoring
  relationship: informed_by
  description: "Retraining is informed by model monitoring — degradation evidence drives the decision."
- concept: drift-detection
  relationship: triggered_by
  description: "Retraining is triggered by drift detection — the detector is the trigger channel."
- concept: training-data
  relationship: acts_on
  description: "Retraining acts on training data — the decision is about which data the model learns from next."
- concept: deployment-risk
  relationship: modifies
  description: "Retraining modifies deployment risk — each update changes the risk profile."
- concept: generalization
  relationship: revalidates
  description: "Retraining revalidates generalization — the updated model's generalization must be re-established by evidence."

## Tradeoffs
- dimension: freshness_vs_stability
  options:
    frequent_retraining:
      value: freshness
      rationale: "Fast adaptation tracks the moving distribution but amplifies noise into the model."
    conservative_retraining:
      value: stability
      rationale: "Rare updates are stable but compound staleness against the moving world."
  importance: high
- dimension: full_retraining_vs_incremental_update
  options:
    full_retraining:
      value: coherence
      rationale: "Full retraining produces a coherent model but costs compute and risks forgetting."
    incremental_update:
      value: efficiency
      rationale: "Incremental updates are cheap but accumulate drift and bias."
  importance: medium

## Failure Modes
- name: habitual_retraining
  description: "Retraining runs on calendar or habit rather than evidence — updates occur without a verified need."
  likelihood: high
  observable_evidence: "Scheduled retraining without trigger analysis; updates with no measured degradation; churn without gain"
  detection: "Retraining trigger audit; update-outcome comparison"
  recovery: "Gate retraining on verified triggers; measure update outcomes"
  retryable: true
- name: unvalidated_release
  description: "A retrained model is deployed without fresh-data validation — the update ships as an untested hypothesis."
  likelihood: high
  observable_evidence: "Post-update regressions; deployment incidents following retraining; no fresh holdout evidence in release records"
  detection: "Release validation audit; regression tracking across model versions"
  recovery: "Require fresh-holdout validation before release; staged rollout with rollback"
  retryable: true
- name: retraining_amplification
  description: "Retraining on unverified or noisy shift compounds errors — the model learns the noise and gets worse."
  likelihood: medium
  observable_evidence: "Performance oscillation across versions; models worse than predecessors; noise-triggered updates"
  detection: "Version-to-version performance comparison; trigger quality review"
  recovery: "Verify shift before triggering; validate against fresh data; roll back to best evidence"
  retryable: true

## Observations
- observation: "Evidence-triggered retraining outperforms scheduled retraining in realized model quality."
  confidence: high
  source: Retraining research, operations practice
- observation: "Retraining is a leading cause of post-deployment regressions."
  confidence: high
  source: ML incident analyses
- observation: "Validation gaps dominate retraining failures — most regressions trace to missing fresh-data checks."
  confidence: high
  source: ML operations reviews

## Constraints
- constraint: "A retrained model is unvalidated until evaluated on fresh data — release without validation is an untested claim."
  type: invariant
  scope: cross-domain
- constraint: "Retraining on unverified shift risks learning new failure modes."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: shift_verification
  question: "Is the triggering shift real, verified, and decision-relevant?"
  supporting: "Verified shift justifies the intervention and its risk."
  contradictory: "Unverified or noise-level shift makes retraining a gamble."
  weight: high
- factor: retrained_evidence
  question: "Does the retrained model show validated improvement on fresh data?"
  supporting: "Fresh-holdout evidence supports release."
  contradictory: "Absent or negative fresh-data evidence forbids release."
  weight: high
- factor: regression_risk
  question: "What is the cost if the update regresses in production?"
  supporting: "Low regression cost permits staged rollout with rollback."
  contradictory: "High regression cost demands stronger validation and canary coverage."
  weight: high
- factor: staleness_cost
  question: "What is the cost of keeping the current model while the world moves?"
  supporting: "High staleness cost justifies acting on partial evidence."
  contradictory: "Low staleness cost favours waiting for stronger evidence."
  weight: high

## Heuristics
- heuristic: "Trigger on evidence, not calendar — every update should name its verified cause."
  rationale: "Evidence triggers make updates auditable and prevent habitual churn."
  evidence_level: high
- heuristic: "Validate before deploy — the retrained model is a hypothesis until fresh data confirms it."
  rationale: "Release without validation is the dominant retraining failure path."
  evidence_level: high
- heuristic: "Keep a rollback path for every update — the previous model is the fallback evidence baseline."
  rationale: "Rollback converts a failed update from incident into experiment."
  evidence_level: high

## Recommendations
- recommendation: "Gate retraining on verified triggers and document the evidence for each update."
  context: retraining_governance
  certainty: strong
  rationale: "Evidence-gated updates are auditable; unverified updates are noise learning."
- recommendation: "Validate every retrained model against a fresh holdout before deployment."
  context: release_management
  certainty: strong
  rationale: "Fresh evidence is the only validity check on the updated behaviour."
- recommendation: "Treat each retraining as an experiment with measured outcomes and rollback capability."
  context: operations
  certainty: strong
  rationale: "Experiment framing makes updates learnable instead of risky."
