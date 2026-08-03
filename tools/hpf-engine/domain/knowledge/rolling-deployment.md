# Rolling Deployment

## Identity
- id: rolling-deployment
- type: pattern
- title: Rolling Deployment
- tags: [distributed-systems, deployment, release, operations, availability, zero-downtime]
- entities: [rolling deployment, zero-downtime deployment, canary deployment, blue-green deployment, release]
- concepts: [availability, backpressure, circuit-breaker, cascading-failure]

## Claims
- claim: "Rolling deployment updates nodes incrementally rather than simultaneously, maintaining system availability throughout the deployment."
  certainty: high
  evidence: Production deployment practices, SRE literature
  scope: cross-system
- claim: "The batch size in a rolling deployment determines the trade-off between deployment speed and risk — larger batches deploy faster but increase blast radius."
  certainty: high
  evidence: Deployment engineering literature, production experience
  scope: cross-system
- claim: "Rolling deployments require the system to support mixed versions during the deployment window — old and new versions must be interoperable."
  certainty: high
  evidence: Production deployment experience
  scope: cross-system
- claim: "Automated rollback is a critical component of rolling deployment — if the new version fails, the deployment system must revert the updated nodes."
  certainty: high
  evidence: SRE literature, production incident analysis
  scope: cross-system
- claim: "Rolling deployment cannot protect against data format or schema changes that are incompatible between versions."
  certainty: high
  evidence: Production deployment experience
  scope: cross-system

## Relationships
- concept: availability
  relationship: preserves
  description: "Rolling deployment preserves availability by updating nodes incrementally — the system never has all nodes down simultaneously."
- concept: circuit-breaker
  relationship: interacts_with
  description: "Circuit breaker configurations may need adjustment during rolling deployments to avoid false positives from mixed-version behaviour."
- concept: backpressure
  relationship: interacts_with
  description: "Rolling deployments reduce system capacity during the window — backpressure mechanisms may activate as capacity is temporarily reduced."
- concept: cascading-failure
  relationship: risk_during
  description: "Rolling deployments can trigger cascading failures if the new version has a defect that only manifests under partial deployment."

## Tradeoffs
- dimension: batch_size_vs_risk
  options:
    single_node:
      value: minimal_risk
      rationale: "Smallest blast radius — one node at a time — but longest deployment duration."
    batch_percent:
      value: speed
      rationale: "Update N% of nodes per batch — faster deployment but larger blast radius if the new version has issues."
  importance: high
- dimension: deploy_frequency_vs_stability
  options:
    frequent_small:
      value: incremental_change
      rationale: "Small changes deployed frequently — easier to isolate issues but higher deployment overhead."
    infrequent_large:
      value: batched_change
      rationale: "Large changes deployed rarely — lower deployment overhead but each deployment carries more risk."
  importance: high
- dimension: automated_vs_manual_gating
  options:
    fully_automated:
      value: speed
      rationale: "Automated health checks gate each batch — fastest but may not catch subtle issues."
    manual_approval:
      value: oversight
      rationale: "Human approval between batches — catches edge cases but significantly extends deployment time."
  importance: operational

## Failure Modes
- name: partial_deployment_failure
  description: "New version fails on a subset of nodes but deployment continues because health checks pass for the updated nodes individually."
  likelihood: medium
  observable_evidence: "System-level metrics degrade as deployment progresses; error rate increases proportionally with updated nodes; cross-node interactions fail"
  detection: "Monitor system-level metrics (not just per-node) during deployment; track error correlation with deployment progress"
  recovery: "Halt deployment; roll back updated nodes; investigate cross-node interaction issues"
  retryable: true
- name: version_incompatibility
  description: "Old and new versions cannot interoperate, causing failures during the mixed-version deployment window."
  likelihood: medium
  observable_evidence: "Failures limited to interactions between old and new nodes; error rate correlates with cross-version requests; RPC format errors"
  detection: "Monitor cross-version interaction failures; verify API compatibility before deployment"
  recovery: "Roll back to single version; redesign to support version interoperability; use feature flags instead of version-dependent behaviour"
  retryable: false
- name: rolling_rollback_failure
  description: "Automated rollback fails because the previous version cannot be restored or its state is incompatible."
  likelihood: low
  observable_evidence: "Rollback script errors; data migration cannot be reversed; old version crashes on updated state"
  detection: "Test rollback procedure before deployment; verify backward compatibility of data migrations"
  recovery: "Manual rollback with data restoration from backup; forward-fix instead of rolling back"
  retryable: false

## Observations
- observation: "The majority of rolling deployment incidents are caused by untested rollback procedures, not by the new version itself."
  confidence: high
  source: Production incident analysis, deployment post-mortems
- observation: "Deploy frequency correlates more strongly with system reliability than deploy size — teams that deploy frequently have fewer incidents."
  confidence: high
  source: DORA research, production experience
- observation: "Feature flags combined with rolling deployment provide the safest deployment pattern — features can be toggled independently of deployment."
  confidence: high
  source: Deployment engineering literature, production experience

## Constraints
- constraint: "Rolling deployment cannot update all nodes faster than the system's capacity to absorb node removals — removing too many nodes simultaneously reduces capacity below demand."
  type: operational
  scope: cross-system
- constraint: "Version interoperability must be maintained for the duration of the deployment window — incompatible changes require different deployment strategies."
  type: invariant
  scope: cross-system

## Decision Factors
- factor: deployment_risk_tolerance
  question: "How much deployment risk is acceptable?"
  supporting: "Low risk tolerance justifies blue-green deployment instead of rolling — complete isolation between versions."
  contradictory: "Rolling deployment is simpler and faster than blue-green — acceptable for systems with robust monitoring and automated rollback."
  weight: high
- factor: deployment_window
  question: "How quickly must the deployment complete?"
  supporting: "Short windows (minutes) require larger batch sizes or blue-green deployment."
  contradictory: "Extended windows allow single-node batches with maximum safety."
  weight: high
- factor: rollback_capability
  question: "Can the system reliably roll back a failed deployment?"
  supporting: "Reliable rollback makes rolling deployment safe — the primary risk is mitigated."
  contradictory: "Unreliable rollback increases the risk of rolling deployment — prefer blue-green for safer isolation."
  weight: high

## Heuristics
- heuristic: "Test rollback before every deployment — if rollback is untested, assume it will fail."
  rationale: "Untested rollback procedures have a documented high failure rate under incident conditions."
  evidence_level: high
- heuristic: "Deploy during low-traffic periods even with rolling deployment — reduced load provides a safety margin."
  rationale: "Lower load during deployment reduces the impact of partial deployment failures and provides headroom for automated recovery."
  evidence_level: high
- heuristic: "Use feature flags to decouple deployment from release — deploy code, but control feature activation independently."
  rationale: "Feature flags allow instant rollback of features without re-deployment, adding a safety layer beyond the deployment mechanism."
  evidence_level: high

## Recommendations
- recommendation: "Automate rollback testing in the deployment pipeline — every deployment candidate should have a verified rollback path."
  context: deployment_engineering
  certainty: strong
  rationale: "Untested rollback is the leading cause of deployment-related incidents."
- recommendation: "Monitor cross-node interaction failures specifically during rolling deployments — per-node health checks are insufficient."
  context: observability
  certainty: strong
  rationale: "Cross-version interaction failures are invisible in per-node monitoring and require correlation across versions."
- recommendation: "Always deploy with a canary batch first — update a single node or small percentage before committing to the full rollout."
  context: deployment_practice
  certainty: strong
  rationale: "Canary batches catch most deployment issues before they affect the majority of traffic."
