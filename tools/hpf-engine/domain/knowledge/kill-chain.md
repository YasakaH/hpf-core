# Kill Chain

## Identity
- id: kill-chain
- type: concept
- title: Kill Chain
- tags: [security, kill chain, attack lifecycle, detection, response, cyber]
- entities: [kill chain, cyber kill chain, attack chain, reconnaissance, weaponisation, delivery, exploitation, command and control]
- concepts: [attacker-capability, threat-actor, attack-surface, threat-detection, incident-response]

## Claims
- claim: "The kill chain models an attack as a sequence of stages — from initial reconnaissance through delivery and exploitation to actions on objectives."
  certainty: high
  evidence: Lockheed Martin cyber kill chain framework, security literature
  scope: cross-domain
- claim: "Kill-chain stage progression is not linear — attackers can loop stages, skip stages, and combine them, making stage detection valuable but not deterministic."
  certainty: high
  evidence: Security research, MITRE ATT&CK critique literature
  scope: cross-domain
- claim: "Detection and response value increases the earlier in the chain an attack is interrupted — each earlier stage prevents all subsequent stages."
  certainty: high
  evidence: Security operations literature, kill chain framework
  scope: cross-domain
- claim: "Kill chains are increasingly automated — commodity tooling executes multiple stages autonomously, compressing chain duration dramatically."
  certainty: high
  evidence: Security research, automated attack tooling analysis
  scope: cross-domain
- claim: "The kill chain is adversary-observable — defenders can infer stage progression from observable artefacts (phishing emails, C2 traffic, lateral movement)."
  certainty: high
  evidence: Detection engineering practice, incident response analysis
  scope: cross-domain

## Relationships
- concept: attacker-capability
  relationship: determines_progression
  description: "Capability determines which stages can be completed — low capability often stops at early stages like delivery."
- concept: threat-actor
  relationship: executes
  description: "The kill chain describes what threat actors do — chain analysis is the behaviour layer of actor modelling."
- concept: attack-surface
  relationship: entered_through
  description: "The kill chain enters through the attack surface — surface reduction prevents chain initiation."
- concept: threat-detection
  relationship: informs
  description: "Kill-chain stage models drive detection design — each stage has observable artefacts that can be detected."
- concept: incident-response
  relationship: guided_by
  description: "Kill-chain position determines response actions — where the chain is interrupted dictates the response playbook."

## Tradeoffs
- dimension: early_detection_investment_vs_detection_cost
  options:
    early_stage:
      value: prevention_leverage
      rationale: "Detecting reconnaissance and delivery prevents later stages entirely but is noisy (false positives on benign activity)."
    late_stage:
      value: high_signal
      rationale: "Detecting exploitation and C2 is high-signal but the attacker is already inside."
  importance: high
- dimension: chain_fidelity_vs_operational_simplicity
  options:
    detailed_chain:
      value: precision
      rationale: "Fine-grained stage models enable precise detection mapping but are complex to maintain."
    coarse_chain:
      value: usability
      rationale: "Coarse stages (pre-compromise, compromise, post-compromise) are simple and robust but lose discriminating power."
  importance: high

## Failure Modes
- name: stage_missing_detection
  description: "A kill-chain stage has no corresponding detection — attackers can pass through that stage unseen."
  likelihood: high
  observable_evidence: "Incident reviews find stages with no detection coverage; kill-chain mapping shows gaps"
  detection: "Kill-chain coverage audit — map every stage to detection capability"
  recovery: "Add detection for uncovered stages; prioritise gaps by stage leverage"
  retryable: true
- name: linear_chain_assumption
  description: "Detection designed on the assumption of linear stage progression — attackers looping or skipping stages evade the model."
  likelihood: medium
  observable_evidence: "Detection misses attacks with non-linear progression; incident analyses show attackers bypassing assumed stage order"
  detection: "Attack simulation testing against detection; review of incidents for non-linear paths"
  recovery: "Redesign detection around stage-independent indicators; use behaviour-based detection alongside chain models"
  retryable: true
- name: false_chain_completion
  description: "Detection fires on artefacts that appear to be a later chain stage but are benign — false positives drive alert fatigue."
  likelihood: high
  observable_evidence: "High false-positive rates on C2-like traffic; analysts dismiss real C2 signals after repeated false alarms"
  detection: "Detection precision metrics; analyst feedback on alert usefulness"
  recovery: "Add context and correlation before alerting; tier alerts by chain-stage confidence"
  retryable: true

## Observations
- observation: "Chain compression is the dominant trend — automated tooling collapses attack timelines from weeks to minutes."
  confidence: high
  source: Security research, incident response data
- observation: "Most successful detection happens at delivery and C2 stages — reconnaissance detection remains largely impractical."
  confidence: high
  source: Detection engineering research, incident statistics
- observation: "Chain models are most valuable as detection-design tools, not as predictive models of attacker behaviour."
  confidence: high
  source: Security literature, detection engineering practice

## Constraints
- constraint: "Reconnaissance is not reliably detectable — defenders should not depend on detecting pre-intrusion surveillance."
  type: invariant
  scope: cross-domain
- constraint: "Chain progression is observable only through artefacts — undetectable stages remain black boxes regardless of the model."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Use the kill chain to design detection coverage, not to predict attacker behaviour."
  rationale: "As a design tool it guarantees coverage; as a predictive model it fails on non-linear attacks."
  evidence_level: high
- heuristic: "Invest detection budget in order of chain leverage — earlier stages prevent more downstream damage."
  rationale: "Interrupting early stages eliminates all subsequent stages — the highest-leverage detection investments."
  evidence_level: high
- heuristic: "Design detection to be stage-independent where possible — behaviour-based signals survive non-linear attacks."
  rationale: "Stage-independent detection is robust to attackers skipping or looping stages."
  evidence_level: high

## Recommendations
- recommendation: "Maintain a kill-chain coverage map that ties every stage to concrete detection capability and owners."
  context: detection_engineering
  certainty: strong
  rationale: "A coverage map reveals gaps directly and makes detection investment decisions auditable."
- recommendation: "Prioritise detection and response at the earliest feasible stages — target delivery and initial access before C2."
  context: security_operations
  certainty: strong
  rationale: "Earlier interruption prevents all later stages — the highest-leverage response position."
- recommendation: "Rehearse response per kill-chain stage — the response playbook should differ by where the chain is interrupted."
  context: incident_response
  certainty: strong
  rationale: "A stage-aware playbook responds proportionately — containment early in the chain differs from late-stage containment."
