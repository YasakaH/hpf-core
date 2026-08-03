# HPF Knowledge Object Schema

Each knowledge object is a markdown file with identity metadata followed by atomic evidence blocks. Blocks are mode-agnostic. Reasoning modes compose from the atoms they need.

## Identity Block (Required)

```yaml
- id: object-id
- type: concept
- title: Human Readable Title
- tags: [tag1, tag2, tag3]
- entities: [entity1, entity2]
- concepts: [canonical-concept-ref1, canonical-concept-ref2]
```

## Atomic Evidence Blocks

### Claims

Factual statements about the concept. Each claim is independently verifiable.

```
## Claims
- claim: "A browser profile is an isolated storage directory."
  certainty: high
  evidence: Chromium source, W3C spec reference
  scope: cross-browser
- claim: "IndexedDB supercookies can survive cookie clear operations."
  certainty: medium
  evidence: Community testing, vendor documentation gaps
  scope: Chromium-specific
```

Used by: Explain, Compare, Decide

### Relationships

Links to other concepts with typed relationship and direction.

```
## Relationships
- concept: session-lifecycle
  relationship: contains
  description: A session is one lifecycle instance within a profile.
- concept: anti-detection
  relationship: influences
  description: Profile persistence is the primary mechanism for cross-session tracking.
```

Used by: Explain, Compare

### Tradeoffs

Comparisons between options with per-dimension analysis.

```
## Tradeoffs
- dimension: detection_risk
  options:
    fresh_profile:
      value: low
      rationale: No tracking cookies, appears as new visitor
    persistent_profile:
      value: medium-to-high
      rationale: Accumulates tracking cookies and cached fingerprint
  importance: critical
- dimension: auth_state
  options:
    fresh_profile:
      value: none
      rationale: Must re-authenticate every session
    persistent_profile:
      value: preserved
      rationale: Maintains login tokens across sessions
  importance: operational
```

Used by: Compare, Decide, Design

### Failure Modes

Typed failure description with detection and recovery.

```
## Failure Modes
- name: profile_corruption
  description: Browser fails to start because profile SQLite databases are corrupt.
  likelihood: low
  observable_evidence: Browser launch failure, SQLite errors in logs
  detection: CDP connection timeout, process exit code
  recovery: Delete profile directory, restore from backup, or start fresh
  prevention: Graceful shutdown, filesystem integrity monitoring
  retryable: true
  affects_modes: [troubleshoot, decide]
```

Used by: Troubleshoot, Explain, Design, Decide

### Decision Factors

Structured inputs for should-I-do-X reasoning.

```
## Decision Factors
- factor: isolation_requirement
  question: "Does the automation require cross-session isolation?"
  supporting: "Fresh profiles prevent cookie/storage leakage between sessions."
  contradictory: "Persistent profiles are simpler for authenticated flows (single login)."
  weight: high
  scenario_mapping:
    web_scraping_public: use_fresh
    authenticated_dashboard: use_persistent
    production_pipeline: use_fresh
```

Used by: Decide, Design

### Observations

Empirical observations about behaviour that may not be formally specified.

```
## Observations
- observation: "Chrome Memory Saver tab discarding does not appear to operate in headless mode."
  confidence: medium
  source: Community testing, undocumented
  protocol: cdp
  implication: "Tab discard is not a failure mode for headless automation."
- observation: "Profile size can grow 100x over 6 months of regular use."
  confidence: high
  source: Measured data
  implication: "Production systems should implement profile age-based rotation."
```

Used by: Explain, Troubleshoot, Design

### Constraints

Invariants that the concept guarantees or requires.

```
## Constraints
- constraint: "Only one browser instance can use a profile at a time."
  type: invariant
  scope: cross-browser
  violation_consequence: File locking errors, database corruption
- constraint: "Session cannot be reused after termination."
  type: invariant
  scope: cross-protocol
  violation_consequence: Connection errors, unexpected behaviour
```

Used by: Explain, Design, Troubleshoot

### Heuristics

Rules of thumb derived from experience, not formal specification.

```
## Heuristics
- heuristic: "Rotate sessions when JS heap exceeds 2x baseline."
  rationale: "Consistent doubling indicates a leak rather than normal allocation."
  applicability: Long-running sessions with CDP access
  evidence_level: moderate
- heuristic: "Use fresh profiles for public scraping; persistent for authenticated."
  rationale: "Fresh profiles eliminate detection surface; persistent profiles reduce auth overhead."
  applicability: All automation
  evidence_level: high
```

Used by: Design, Decide

### Recommendations

Actionable guidance with context.

```
## Recommendations
- recommendation: "Use fresh profiles per session for production automation."
  context: production_pipeline
  certainty: strong
  rationale: "Isolation, reliability, no cross-session contamination."
- recommendation: "Use persistent profiles when authentication is required."
  context: authenticated_automation
  certainty: moderate
  rationale: "Avoids repeated auth, but monitor for detection risk increase over time."
```

Used by: Decide, Design

## Schema Validation Rules

### Required per object
- Identity block with id, title, tags, entities
- At least one atomic evidence block

### Structural rules
- Each claim must have: claim, certainty (high/medium/low), evidence, scope
- Each relationship must have: concept, relationship, description
- Each tradeoff must have: dimension, options (2+), importance (critical/high/medium/low)
- Each failure mode must have: name, description, likelihood, observable_evidence, detection, recovery, retryable
- Each decision factor must have: factor, question, supporting, contradictory, weight
- Each observation must have: observation, confidence, source
- Each constraint must have: constraint, type, scope
- Each heuristic must have: heuristic, rationale, evidence_level
- Each recommendation must have: recommendation, context, certainty

### Referential rules
- relationship.concept values should resolve to existing concept IDs
- entities in identity should be a superset of entity references in evidence blocks
- concepts in identity should reference valid canonical concept paths

---

*Schema version 0.1.0 — 2026-07-29*
