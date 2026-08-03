# Browser Storage

## Identity
- id: browser-storage
- type: concept
- title: Browser Storage Mechanisms
- tags: [storage, cookies, localStorage, IndexedDB, cache, persistence]
- entities: [storage, cookie, localStorage, IndexedDB, cache, sessionStorage]
- concepts: [browser-storage, browser-profile, memory-pressure]

## Metadata
- created: 2026-07-29
- domain: browser-automation
- version: 0.1.0
- research_cycle: 002

## Semantic Layer
- definition: Browser storage encompasses all client-side data persistence mechanisms available to web pages, including cookies, Web Storage (localStorage/sessionStorage), IndexedDB, Cache API, and HTTP cache.
- key_property: Storage is origin-scoped — data from one origin is inaccessible to another.
- key_property: Storage mechanisms are independent — clearing cookies does not clear localStorage or IndexedDB.
- key_property: Storage survives browser restart (except sessionStorage) unless explicitly cleared or in incognito mode.

## Narrative Layer
Browser storage is the primary mechanism for state persistence across navigations and sessions. It enables authentication (session cookies), application data (IndexedDB for offline apps), and tracking (third-party cookies, localStorage fingerprinting). For automation, the key challenge is storage control: knowing what state exists, clearing it when needed, and understanding what persists across sessions. Each storage mechanism has different protocol-level accessibility (CDP gives direct access to most; WebDriver requires JavaScript execution for non-cookie storage).

## Compare Section
- dimension: protocol_access
- cookies:
  - cdp: direct (Network.getCookies, Network.deleteCookies)
  - webdriver: direct (getCookies, addCookie, deleteCookie)
- localStorage:
  - cdp: direct (Storage.getDOMStorageItems, Storage.setDOMStorageItem)
  - webdriver: via executeScript (localStorage.getItem/setItem)
- sessionStorage:
  - cdp: direct (Storage.getDOMStorageItems)
  - webdriver: via executeScript (sessionStorage.getItem/setItem)
- IndexedDB:
  - cdp: direct (IndexedDB.requestData, IndexedDB.deleteDatabase)
  - webdriver: via executeScript (JS IDB API)
- Cache API:
  - cdp: direct (CacheStorage.requestEntries, CacheStorage.deleteCache)
  - webdriver: via executeScript (caches.open/delete)
- HTTP Cache:
  - cdp: direct (Network.clearBrowserCache)
  - webdriver: no direct access

- dimension: clearance_precision
- cdp:
  - granularity: Per-origin, per-storage-type, per-key
  - capability: Clear single cookie, clear all cookies for domain, clear all storage for origin
- webdriver:
  - granularity: Per-cookie only
  - capability: Clear individual or all cookies; cannot clear localStorage, IndexedDB, or cache without JS

- tradeoff_table:
  - criterion: storage_control
  - winner: cdp
  - importance: critical
  - criterion: simplicity
  - winner: webdriver
  - importance: moderate
  - criterion: cross_browser_support
  - winner: webdriver
  - importance: high

- recommendation:
  - case: full_storage_control
  - use: cdp
  - reason: Direct access to all storage mechanisms
  - case: cross_browser_automation
  - use: webdriver
  - reason: Standardized API, but accept limited IndexedDB and cache control

## Troubleshoot Section
- failure_modes:
  - name: stale_cookies
  - observable_evidence: Authentication fails despite valid credentials, session expired errors
  - likelihood: high
  - detection: Compare cookie expiry against current time, check for missing session cookies
  - recovery: Refresh cookies, re-authenticate, clear stale cookies
  - retryable: true

  - name: quota_exceeded
  - observable_evidence: IndexedDB write failures, QuotaExceededError in console
  - likelihood: low
  - detection: CDP Storage.getUsageAndQuota shows quota exceeded
  - recovery: Clear storage for origin, or increase quota in browser flags
  - retryable: true

  - name: cross_origin_storage_conflict
  - observable_evidence: Unexpected state from different origin affecting automation (e.g., iframe storage)
  - likelihood: medium
  - detection: Trace storage access patterns across origins
  - recovery: Clear all storage for conflicting origin, or isolate via fresh profile
  - retryable: true

  - name: persistent_tracking_resurrection
  - observable_evidence: After cookie clear, tracking resumes from IndexedDB or Cache API
  - likelihood: medium
  - detection: Check IndexedDB for supercookie patterns, check Cache API for stored identifiers
  - recovery: Clear all storage types (not just cookies), or use fresh profile
  - retryable: true

  - name: storage_not_cleared_between_sessions
  - observable_evidence: State from previous session visible in new session, cross-session contamination
  - likelihood: high
  - detection: Verify expected storage state is empty at session start
  - recovery: Explicitly clear all storage on session start, or use fresh profile
  - retryable: true

## Decide Section
- decision_factors:
  - factor: storage_isolation_need
  - question: "Does the automation need clean storage state per operation?"
  - supporting: Fresh profiles provide complete isolation; clearing cookies alone is insufficient because localStorage and IndexedDB persist independently
  - contradictory: Clearing all storage types via CDP is possible without profile restart, but requires protocol-level access
  - weight: high

  - factor: auth_state_longevity
  - question: "How long should authentication state persist?"
  - supporting: Persistent storage maintains login across sessions; session-only storage (no persistence) requires re-auth on every start
  - contradictory: Long-lived auth increases detection risk; periodic re-auth is safer but slower
  - weight: high

  - factor: detection_evasion
  - question: "Can storage-based tracking be avoided?"
  - supporting: Fresh profiles eliminate all storage-based tracking; clearing cookies alone leaves IndexedDB supercookies and Cache API identifiers intact
  - contradictory: Behavioural detection (rate, patterns, browser fingerprint) is unaffected by storage state
  - weight: high

- recommendation:
  - scenario: anti_detection
  - use: fresh_profile
  - certainty: strong
  - scenario: authenticated_automation
  - use: persistent_profile + periodic storage audit
  - certainty: moderate

## Design Section
- approaches:
  - name: full_storage_clear_on_session_start
  - description: At session start, clear all storage types (cookies, localStorage, IndexedDB, Cache API, HTTP cache) via CDP or JS execution
  - pros: Clean state without profile restart, preserves profile auth if needed selectively
  - cons: Only possible with CDP; WebDriver cannot clear non-cookie storage without JS execution
  - best_for: CDP-based automation requiring fresh state within a persistent profile

  - name: storage_audit_before_action
  - description: Before each critical action, verify expected storage state and clear if contaminated
  - pros: Targeted, minimal performance impact, catches unexpected state changes
  - cons: Complex implementation, requires defining expected state per action
  - best_for: Production automation with strict state requirements

  - name: periodic_profile_rotation
  - description: Rotate profiles on a schedule (e.g., every 100 sessions, every week) regardless of observed state
  - pros: Simple, prevents long-term tracking accumulation without per-session analysis
  - cons: Loses cached resources and auth state on rotation
  - best_for: Long-running automation where detection risk increases with profile age

### Pitfalls
- pitfall: incomplete_clear
- description: Clearing cookies alone does not clear localStorage, IndexedDB, or Cache API
- mitigation: Use CDP to clear all storage types, or use fresh profile

- pitfall: supercookie_resurrection
- description: Some trackers use IndexedDB or Cache API to regenerate cookies after cookie clear
- mitigation: Clear all storage types, not just cookies; fresh profiles are the only complete solution

- pitfall: cross_profile_leakage
- description: Extensions and system-level state may persist across profiles
- mitigation: Fresh OS user account or container for maximum isolation

### Best Practices
- practice: Clear all storage types when resetting state
- rationale: Cookie-only clear leaves localStorage, IndexedDB, and Cache API data intact

- practice: Use CDP for storage operations when full control is needed
- rationale: CDP provides direct access to all storage mechanisms without JS execution overhead

- practice: Monitor storage growth for anomaly detection
- rationale: Sudden IndexedDB growth may indicate tracking scripts or fingerprinting

- practice: Verify storage state at session start
- rationale: Prevents cross-session contamination and unexpected auth state
