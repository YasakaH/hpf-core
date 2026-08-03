# Threat Detection

## Identity
- id: threat-detection
- type: pattern
- title: Threat Detection
- tags: [security, detection, monitoring, SIEM, alerts, detection engineering, visibility]
- entities: [threat detection, detection, monitoring, alerting, SIEM, EDR, detection engineering, telemetry]
- concepts: [kill-chain, incomplete-evidence, confidence, incident-response, attacker-capability, threat-actor]

## Claims
- claim: "Threat detection is the practice of observing system and user behaviour to identify malicious activity — it is a continuous capability, not a tool."
  certainty: high
  evidence: Detection engineering literature, security operations practice
  scope: cross-domain
- claim: "Detection value is bounded by telemetry — no detection can see what is not observed; coverage gaps are detection gaps."
  certainty: high
  evidence: Detection engineering research, incident analysis
  scope: cross-domain
- claim: "Detection precision and recall trade off — precision optimising reduces alert noise but misses attacks; recall optimising catches attacks but floods analysts."
  certainty: high
  evidence: Detection engineering literature, operations practice
  scope: cross-domain
- claim: "Detection quality is measured by outcome — detection without response is noise; the metric is prevented or contained damage, not alert count."
  certainty: high
  evidence: Security operations research, detection ROI analysis
  scope: cross-domain
- claim: "Detection effectiveness decays — new attack techniques, tooling changes, and environment drift age detection rules."
  certainty: high
  evidence: Detection engineering practice, ATT&CK-based coverage research
  scope: cross-domain

## Relationships
- concept: kill-chain
  relationship: designed_against
  description: "Detection is designed against kill-chain stages — coverage mapping ties detections to attack stages."
- concept: incomplete-evidence
  relationship: limited_by
  description: "Telemetry gaps blind detection — incomplete evidence means attacks on uncovered surfaces are invisible."
- concept: confidence
  relationship: carries
  description: "Every alert carries confidence — confidence determines whether analysts act and how they prioritise."
- concept: incident-response
  relationship: triggers
  description: "Detection triggers response — the detection-to-response pipeline determines dwell time."
- concept: attacker-capability
  relationship: tracked_against
  description: "Detection tracks capability manifestation — TTPs are the observable layer of attacker capability."
- concept: threat-actor
  relationship: behaviour_based
  description: "Detection is behaviour-based — it observes what actors do, independent of attribution."

## Tradeoffs
- dimension: precision_vs_recall
  options:
    high_precision:
      value: analyst_capacity
      rationale: "Fewer, high-confidence alerts — analysts act on them but attacks slipping through are missed."
    high_recall:
      value: coverage
      rationale: "More alerts including false positives — broad coverage but alert fatigue and missed criticals in noise."
  importance: high
- dimension: telemetry_depth_vs_cost
  options:
    deep_telemetry:
      value: visibility
      rationale: "Rich endpoint and network data — maximum coverage but high cost, storage, and privacy burden."
    minimal_telemetry:
      value: efficiency
      rationale: "Focused essential signals — cheaper and quieter but blind on uncovered surfaces."
  importance: high

## Failure Modes
- name: alert_fatigue
  description: "Alert volume exceeds triage capacity — analysts dismiss alerts, including genuine ones."
  likelihood: high
  observable_evidence: "Alert backlog growth; low triage rates; missed genuine alerts in reviews; analysts desensitised"
  detection: "Triage metrics; alert-to-incident ratio; backlog age"
  recovery: "Reduce alert volume with precision tuning; automate routine triage; tier alerts by confidence and impact"
  retryable: true
- name: telemetry_blindspot
  description: "Attack path exists on an unobserved surface — no telemetry covers it, so detection is impossible."
  likelihood: high
  observable_evidence: "Incidents discovered outside monitored surfaces; detection coverage gaps identified in reviews"
  detection: "Telemetry coverage audit against attack surface; kill-chain coverage mapping"
  recovery: "Instrument uncovered surfaces; prioritise by attack path likelihood; document residual blind spots"
  retryable: true
- name: detection_decay
  description: "Rules age — new techniques, changed tooling, and environment drift make detections ineffective."
  likelihood: high
  observable_evidence: "Declining detection rates; missed attacks using evolving TTPs; stale rules referencing old tooling"
  detection: "Detection health metrics; periodic rule effectiveness review; ATT&CK coverage refresh"
  recovery: "Retire or refresh rules; adopt behaviour-based detection over signatures; continuous tuning"
  retryable: true

## Observations
- observation: "Detection coverage is the strongest controllable predictor of breach detection time — organisations detect what they instrument."
  confidence: high
  source: Incident research, breach statistics
- observation: "Behaviour-based detection outperforms signature-based detection against evolving attackers."
  confidence: high
  source: Detection engineering research, operations practice
- observation: "Most detection programmes measure alerts, not outcomes — few track detection-to-containment time."
  confidence: high
  source: Security operations assessment, industry surveys

## Constraints
- constraint: "Detection cannot observe what telemetry does not capture — coverage is the ceiling of detection capability."
  type: invariant
  scope: cross-domain
- constraint: "Detection without response capacity is noise — the pipeline is only as strong as the slowest stage."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Map detection coverage to kill-chain stages and attack paths — coverage mapping reveals gaps directly."
  rationale: "Stage-mapped coverage turns abstract 'coverage' into actionable gap lists."
  evidence_level: high
- heuristic: "Tier alerts by confidence and impact — high-confidence high-impact alerts demand immediate action; low tiers queue."
  rationale: "Tiering preserves analyst attention for what matters and manages fatigue."
  evidence_level: high
- heuristic: "Measure detection-to-containment time, not alert counts — outcome metrics drive real improvement."
  rationale: "Outcome measurement focuses the programme on realised protection."
  evidence_level: high

## Recommendations
- recommendation: "Instrument telemetry proportional to the attack surface — every high-risk surface should have corresponding visibility."
  context: detection_architecture
  certainty: strong
  rationale: "Telemetry coverage is the ceiling of detection capability — match it to the risk surface."
- recommendation: "Refresh detection coverage against current TTPs on a continuous basis — detect behaviour, not just signatures."
  context: detection_engineering
  certainty: strong
  rationale: "Behaviour-based detection survives tooling churn; signature-only detection decays."
- recommendation: "Review alert precision quarterly and retire noisy detections — alert fatigue is a detection failure mode."
  context: security_operations
  certainty: strong
  rationale: "Fatigued analysts miss genuine threats; precision tuning preserves the human layer."
