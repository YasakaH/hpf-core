# Incident Response

## Identity
- id: incident-response
- type: pattern
- title: Incident Response
- tags: [security, incident response, response, containment, recovery, IR, forensics]
- entities: [incident response, incident, containment, eradication, recovery, post-incident, IR plan]
- concepts: [threat-detection, kill-chain, incomplete-evidence, threat-actor, defense-in-depth, risk-acceptance]

## Claims
- claim: "Incident response is the disciplined process of detecting, containing, eradicating, and recovering from security incidents — defined phases, not improvisation."
  certainty: high
  evidence: NIST SP 800-61, incident response literature
  scope: cross-domain
- claim: "Response quality is determined before the incident — preparation (plans, runbooks, trained teams, exercised scenarios) is the strongest predictor of outcome."
  certainty: high
  evidence: Incident response research, post-incident analysis
  scope: cross-domain
- claim: "Time is the critical resource — faster containment directly reduces attacker dwell time and realised damage."
  certainty: high
  evidence: Breach statistics, incident response research
  scope: cross-domain
- claim: "Incidents are investigated under incomplete evidence — responders must act on partial information while evidence collection continues."
  certainty: high
  evidence: Incident response practice, forensics literature
  scope: cross-domain
- claim: "Post-incident review converts incidents into learning — without review, the organisation repeats the same response mistakes."
  certainty: high
  evidence: SRE and incident response literature (blameless postmortems)
  scope: cross-domain

## Relationships
- concept: threat-detection
  relationship: triggered_by
  description: "Incident response begins with detection — the quality of detection determines how early response starts."
- concept: kill-chain
  relationship: position_aware
  description: "Response actions depend on kill-chain position — early chain interruption differs from late-stage containment."
- concept: incomplete-evidence
  relationship: operates_under
  description: "Response operates under incomplete evidence — action on partial information is the norm, not the exception."
- concept: threat-actor
  relationship: responds_to
  description: "Response is directed against actor behaviour — actor understanding informs containment and eradication."
- concept: defense-in-depth
  relationship: final_layer
  description: "Response is the final depth layer — it bounds the damage when all prevention layers fail."
- concept: risk-acceptance
  relationship: informs
  description: "Incident outcomes inform risk acceptance — realised incidents validate or challenge accepted risks."

## Tradeoffs
- dimension: speed_vs_thoroughness
  options:
    containment_first:
      value: damage_limit
      rationale: "Contain first, investigate after — faster damage control but risk of incomplete eradication."
    investigate_first:
      value: completeness
      rationale: "Understand fully before acting — complete eradication but longer attacker dwell time."
  importance: high
- dimension: preservation_vs_recovery
  options:
    preserve_evidence:
      value: forensics
      rationale: "Preserve forensic integrity — enables attribution and learning but delays recovery."
    rapid_recovery:
      value: business_continuity
      rationale: "Restore service quickly — resumes business but may destroy evidence and skip root-cause learning."
  importance: high

## Failure Modes
- name: unprepared_response
  description: "No plan, no runbooks, no trained team — response is improvised under incident pressure."
  likelihood: high
  observable_evidence: "Ad-hoc response actions; unclear ownership; slow decisions; repeated mistakes across incidents"
  detection: "Preparedness audit; incident review identifying improvisation patterns"
  recovery: "Build IR plan and runbooks; train and exercise teams; appoint incident command roles"
  retryable: true
- name: containment_hesitation
  description: "Delay in containment while teams debate causes — attackers gain time and damage grows."
  likelihood: high
  observable_evidence: "Long dwell time post-detection; extended containment decisions; teams still investigating while attacker active"
  detection: "Dwell time metrics; response timeline review"
  recovery: "Pre-approve containment actions; practice containment-first drills; set decision time-boxes"
  retryable: true
- name: incomplete_eradication
  description: "Eradication misses persistence mechanisms — attackers return through hidden footholds."
  likelihood: high
  observable_evidence: "Re-infection after declared recovery; same actor returns via known footholds; repeated incident patterns"
  detection: "Recurrence tracking; persistence hunting after incidents"
  recovery: "Hunt for persistence before declaring recovery; assume partial eradication until validated"
  retryable: true

## Observations
- observation: "Preparedness predicts response quality better than team size — exercised teams respond measurably faster and more correctly."
  confidence: high
  source: Incident response research, tabletop exercise data
- observation: "Containment speed is the strongest controllable predictor of breach cost."
  confidence: high
  source: Breach cost research, incident statistics
- observation: "Blameless postmortems produce measurably better learning than blame-oriented reviews."
  confidence: high
  source: SRE literature, organisational learning research

## Constraints
- constraint: "Response decisions are made under incomplete evidence — waiting for complete understanding forfeits the time advantage."
  type: invariant
  scope: cross-domain
- constraint: "Eradication cannot be declared complete without persistence hunting — absence of observed footholds is not absence of footholds."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Contain first, investigate after — assume the attacker is active and stop them before understanding them."
  rationale: "Containment-first trades completeness for time, and time is the critical resource."
  evidence_level: high
- heuristic: "Exercise the response plan under realistic scenarios before incidents — tabletop exercises find plan gaps cheaply."
  rationale: "Untested plans fail under pressure; exercises convert plans into capability."
  evidence_level: high
- heuristic: "Run blameless post-incident reviews and track action items to closure."
  rationale: "Blameless review produces learning; untracked actions produce nothing."
  evidence_level: high

## Recommendations
- recommendation: "Pre-approve containment actions so responders do not wait for escalation during an active incident."
  context: incident_response
  certainty: strong
  rationale: "Pre-approval removes the most common source of containment delay."
- recommendation: "Hunt for persistence before declaring recovery — assume incomplete eradication until validated."
  context: incident_recovery
  certainty: strong
  rationale: "Recurring incidents trace to un-hunted persistence; validation prevents premature recovery declarations."
- recommendation: "Track dwell time as a core response metric and review trends quarterly."
  context: security_operations
  certainty: strong
  rationale: "Dwell time is the outcome metric that ties detection, response, and containment quality together."
