# Browser Profiles Concept

## Identity
- id: browser-profiles-concept
- type: concept
- title: Isolated Browser Profiles
- tags: [profiles, isolation, persistence, storage, fingerprint]
- entities: [profile, browser profile, user-data-dir, persistence]
- concepts: [browser-profile, browser-storage, memory-pressure]

## Metadata
- created: 2025-04-07
- updated: 2026-07-29
- domain: browser-automation
- version: 0.2.0
- research_cycle: 002

## Semantic Layer
- definition: A browser profile is an isolated storage directory containing all persistent browser state (cookies, localStorage, IndexedDB, caches, preferences) that outlives individual browser sessions.
- isolation: Profiles are fully isolated from each other; one profile cannot access another's data.
- persistence: Profile data survives browser restart unless the profile directory is deleted.
- components: cookies_db, local_storage, indexed_db, http_cache, service_worker_cache, preferences, extensions, tls_state, login_data, history

## Narrative Layer
Browser profiles are the primary mechanism for persistent state in automation. Every automation framework uses them, but with different defaults: Chrome for Testing creates temp profiles; Playwright creates isolated contexts within a profile; Selenium allows explicit profile specification. The choice between fresh and persistent profiles is the most consequential decision for cross-session behaviour.

## Compare Section
- dimension: detection_risk
- fresh_profile:
  - value: low
  - reason: No tracking cookies, no cached fingerprint, appears as new visitor to all tracking networks
- persistent_profile:
  - value: medium-to-high
  - reason: Accumulates tracking cookies, consistent fingerprint over time, session history visible

- dimension: auth_state
- fresh_profile:
  - value: none
  - reason: Must re-authenticate every session
- persistent_profile:
  - value: preserved
  - reason: Maintains login tokens, session cookies, OAuth state across sessions

- dimension: performance
- fresh_profile:
  - value: slower (first load)
  - reason: No cached resources, full download on first visit
- persistent_profile:
  - value: faster
  - reason: Cached resources, pre-warmed TLS, HSTS state

- dimension: reliability
- fresh_profile:
  - value: higher
  - reason: No accumulated corruption, no state bloat, deterministic starting state
- persistent_profile:
  - value: lower
  - reason: Profile corruption risk, cache bloat, state conflicts from previous sessions

- dimension: resource_usage
- fresh_profile:
  - value: minimal
  - reason: Small profile directory (KB), no history or accumulated data
- persistent_profile:
  - value: grows over time
  - reason: Accumulates history, cache, IndexedDB; 6-month profile can be 100x larger

- tradeoff_table:
  - criterion: detection_risk
  - winner: fresh_profile
  - importance: critical_for_evasion

  - criterion: auth_state
  - winner: persistent_profile
  - importance: operational_requirement

  - criterion: performance
  - winner: persistent_profile
  - importance: medium

  - criterion: reliability
  - winner: fresh_profile
  - importance: critical_for_production

  - criterion: resource_usage
  - winner: fresh_profile
  - importance: medium

- recommendation:
  - case: scraping_public_data
  - use: fresh_profile
  - reason: Low detection risk, no auth needed
  - case: authenticated_automation
  - use: persistent_profile (re-authenticate periodically)
  - reason: Maintains auth state, faster, but monitor for detection
  - case: production_at_scale
  - use: fresh_profile_per_session
  - reason: Isolation, reliability, no cross-session contamination

## Troubleshoot Section
- failure_modes:
  - name: profile_corruption
  - observable_evidence: Browser fails to start with profile, SQLite errors in logs
  - likelihood: low
  - detection: Browser launch failure, CDP connection timeout
  - recovery: Delete profile or use backup, start fresh
  - retryable: true

  - name: profile_locking
  - observable_evidence: Chrome/Browser process already using the profile
  - likelihood: medium
  - detection: Browser launch failure with "profile in use" error
  - recovery: Kill existing process, wait for lock release, or use different profile
  - retryable: true

  - name: profile_bloat
  - observable_evidence: Slow browser startup, large profile directory (>1GB), long page load times
  - likelihood: medium
  - detection: Directory size monitoring, slow launch timing
  - recovery: Clear cache, clear storage, or rotate to fresh profile
  - retryable: true

  - name: tracking_accumulation
  - observable_evidence: Increasing detection rate over time, CAPTCHA frequency rises
  - likelihood: medium
  - detection: Monitor block rate vs profile age
  - recovery: Switch to fresh profile
  - retryable: true (different profile)

  - name: version_incompatibility
  - observable_evidence: Profile created by older browser version, migration warning on launch
  - likelihood: low
  - detection: Browser log warnings
  - recovery: Delete profile, create new one for current browser version
  - retryable: true

## Decide Section
- decision_factors:
  - factor: isolation_requirement
  - question: "Do I need cross-session isolation?"
  - supporting: Fresh profiles prevent cookie/storage leakage between sessions, prevent fingerprint linking, eliminate tracking accumulation
  - contradictory: Persistent profiles are simpler for authenticated flows (single login), but isolation can be achieved with per-session profiles
  - weight: high

  - factor: auth_persistence
  - question: "Does the automation need to maintain login state?"
  - supporting: Persistent profiles avoid re-authentication, maintain session cookies, preserve OAuth tokens
  - contradictory: Long-lived auth state increases detection risk; periodic re-auth may be safer
  - weight: high

  - factor: detection_sensitivity
  - question: "How important is avoiding detection?"
  - supporting: Fresh profiles minimize tracking surface, appear as new visitors, avoid cookie-based linking
  - contradictory: Detection based on behaviour (rate, pattern) is unaffected by profile freshness
  - weight: high

  - factor: performance_requirement
  - question: "Are sub-second session starts required?"
  - supporting: Persistent profiles skip resource downloads, have cached DNS/TLS, reduce cold-start overhead
  - contradictory: Fresh profile overhead (~2-5s for first page) is acceptable for most use cases
  - weight: medium

  - factor: operational_complexity
  - question: "Can the automation manage per-session profile creation/deletion?"
  - supporting: Modern frameworks (Playwright contexts) handle this automatically
  - contradictory: Custom profile management adds code, monitoring, and storage overhead
  - weight: medium

- recommendation:
  - scenario: web_scraping_public
  - use: fresh_profile
  - certainty: strong
  - scenario: authenticated_dashboard
  - use: persistent_profile
  - certainty: moderate
  - scenario: production_pipeline
  - use: fresh_profile
  - certainty: strong
  - scenario: testing_framework
  - use: fresh_profile
  - certainty: strong

## Design Section
- approaches:
  - name: fresh_profile_per_session
  - description: Create new profile directory for each session, delete after session ends
  - pros: Maximum isolation, no tracking accumulation, deterministic state, easy cleanup
  - cons: No auth persistence, cold cache, ~2-5s overhead on first page load
  - best_for: Web scraping, production pipelines, anti-detection automation
  - implementation: Use temp profile (Chrome for Testing default) or create new --user-data-dir per session

  - name: persistent_profile_pool
  - description: Maintain a pool of persistent profiles, rotate them across sessions
  - pros: Balanced isolation and performance, cached resources, can maintain auth per profile
  - cons: Profile management overhead, storage growth, periodic cleanup needed
  - best_for: Authenticated automation at scale, multi-account management
  - implementation: Pre-create N profiles, assign to sessions via pool, rotate periodically

  - name: single_persistent_profile
  - description: One profile used for all sessions, cleared periodically
  - pros: Simple implementation, fast startup, single auth point
  - cons: High detection risk, state bloat, corruption affects all automation
  - best_for: Development, testing against known targets, non-production use
  - implementation: Single --user-data-dir, periodic manual cleanup

### Pitfalls
- pitfall: profile_lock_conflicts
- description: Two browser instances cannot share the same profile simultaneously
- mitigation: Use unique profile paths per session, or use Playwright contexts (virtual per-session profiles)

- pitfall: profile_corruption_propagation
- description: A corrupted profile takes down all sessions using it
- mitigation: Fresh profiles per session limits blast radius to one session

- pitfall: undetected_bloat
- description: Profile grows to gigabytes over months, slowing everything
- mitigation: Monitor profile size, implement max-age rotation, use fresh profiles for production

### Best Practices
- practice: Use fresh profiles for public data scraping
- rationale: Eliminates tracking linking, prevents state accumulation, deterministic recovery

- practice: Use persistent profiles only when auth is required
- rationale: Reduces overhead of repeated authentication

- practice: Delete profiles after session completion
- rationale: Prevents disk bloat, profile locking, and stale state

- practice: Monitor profile age as a detection risk metric
- rationale: Older profiles accumulate more tracking surface, increasing block rate over time
