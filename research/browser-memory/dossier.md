# Research Dossier: Browser Memory

**Cycle**: Research Cycle 002
**Domain**: Browser Memory
**Date**: 2026-07-29
**Status**: Complete

---

## Abstract

Browser Memory encompasses persistent state management (profiles, storage, caches), runtime memory pressure (OOM, tab discard, garbage collection), and the fingerprinting surface exposed by persistent identifiers. It is the second foundational domain after Browser State — while State governs the lifecycle of a session, Memory governs what survives across sessions.

---

## Sources

| Type | Count | Key References |
|---|---|---|
| Official specifications | 4 | W3C Storage (cookies, localStorage, IndexedDB), W3C Service Worker (Cache API), W3C Resource Timing, Chrome Memory Saver |
| Vendor documentation | 6 | Chromium user-data-dir, CDP Storage/IndexedDB/CacheStorage domains, Playwright browser contexts, Puppeteer page context, Selenium profile management, Chrome --user-data-dir docs |
| Engineering blogs | 3 | Chrome DevTools (memory profiling), Chrome Speed (tab discarding), Airbnb (profile isolation patterns) |
| Academic papers | 2 | Browser fingerprinting surveys (Eckersley 2010, Laperdrix 2020) |
| Community evidence | 5 | GitHub issues (profile corruption, memory leaks, OOM in headless, cookie persistence failures) |

**Evidence quality**:
- Official specifications: ████████ (storage standards mature; memory pressure less specified)
- Vendor documentation: ████████ (profile docs good; OOM handling under-documented)
- Engineering blogs: ██████ (memory profiling well-covered; profile management patterns thin)
- Academic papers: ██████ (fingerprinting well-studied; automation-specific memory patterns not)
- Community evidence: ████████ (extensive OOM and memory leak reports)

---

## Domain Analysis

### 1. Browser Profiles

A browser profile is a directory on disk containing persistent state: cookies, localStorage, IndexedDB, service workers, cached resources, preferences, extensions, and TLS state.

**Profile components** (Chromium):

| Component | Location (within user-data-dir) | Persistence | Size |
|---|---|---|---|
| Cookies | `Default/Cookies` (SQLite) | Session + persistent | Small (KB-MB) |
| localStorage | `Default/Local Storage/` (LevelDB) | Persistent | Small (KB-MB) |
| sessionStorage | In-memory per tab | Session only | Small |
| IndexedDB | `Default/IndexedDB/` (LevelDB) | Persistent | Medium (MB-GB) |
| Cache (HTTP) | `Default/Cache/` (disk cache) | Time-bound | Large (MB-GB) |
| Service Workers | `Default/Service Worker/` | Persistent | Medium |
| Preferences | `Default/Preferences` (JSON) | Persistent | Small |
| Extensions | `Default/Extensions/` | Persistent | Variable |
| TLS state | Various | Session + persistent | Small |

**Profile lifecycle**:
```
Create → Load → Launch instance → Bind → Use → Close → Persist → Reuse
                                              ↓
                                        Discard (fresh next time)
```

**Key insight for automation**: Reusing a profile across sessions provides continuity (auth state, cached resources) but increases detection risk (consistent fingerprint) and can accumulate corrupted state. Fresh profiles provide isolation but incur the cost of re-authenticating and re-caching.

### 2. Storage Mechanisms

| Mechanism | Scope | Persistence | Capacity | Accessible via |
|---|---|---|---|---|
| Cookie | Domain + path | Session or expiry | 4KB per cookie, ~180 per domain | CDP `Network.getCookies`, WebDriver `getCookies` |
| localStorage | Origin | Until cleared | ~5-10MB per origin | CDP `Storage.getDOMStorageItems`, WebDriver `executeScript` |
| sessionStorage | Tab (session) | Until tab closes | ~5-10MB per origin | WebDriver `executeScript` |
| IndexedDB | Origin | Until cleared | Unlimited (device dependent) | CDP `IndexedDB.*`, limited WebDriver support |
| Cache API (SW) | Origin (SW scope) | Until cleared | Unlimited | CDP `CacheStorage.*` |
| HTTP Cache | Browser-wide | Time/TTL-bound | Disk-quota managed | CDP `Network.clearBrowserCache` |

**Detection relevance**: Cookies and localStorage are the primary persistence vectors for tracking and authentication. IndexedDB is increasingly used for fingerprinting (canvas fingerprint caching, supercookies). Cache API can be used for covert storage.

### 3. Memory Pressure and Failure Modes

**Memory pressure signals**:

| Signal | Source | Threshold | Reliability |
|---|---|---|---|
| Tab discard | Chromium `about:discards` | Memory pressure + background | High (deterministic in Chrome) |
| Renderer OOM | OS signal, crash log | Process memory limit | High (post-facto) |
| Performance.memory | JS API | `jsHeapSizeLimit` approaching | Medium (page-dependent) |
| CDP Memory domain | `Memory.getDOMCounters` | Node count thresholds | Medium |
| System memory | OS metrics (OS-dependent) | Near-limit | High |
| GPU process crash | `Inspector.targetCrashed` | GPU memory exhaustion | High (but GPU-specific) |

**Failure mode taxonomy**:

| Mode | Observable Evidence | Likelihood | Detection | Recovery |
|---|---|---|---|---|
| Tab discard | Tab unresponsive, reload on focus | Medium (headless: lower) | Discard event (CDP: no direct event; infer from visibility change + reload) | Reload, check state |
| Renderer OOM | `Inspector.targetCrashed` with no crash dump | Medium (memory-intensive pages) | `Inspector.targetCrashed` | New session |
| Out-of-memory kill | Process exit, no crash dump | Low (depends on system) | Process exit code | New session, reduce load |
| Memory leak | Gradual performance degradation, increasing JS heap | High (long-running sessions) | CDP `Performance.getMetrics` (JSHeapUsedSize increasing) | Session rotation, GC hint |
| Cache bloat | Slow startup, large user-data-dir | Medium (long-lived profiles) | Directory size monitoring | Profile cleanup, fresh profile |
| Storage quota exceeded | `QuotaExceededError` in page | Low (except IndexedDB-heavy apps) | CDP `Storage.getUsageAndQuota` | Clear storage, increase quota |

**Key insight**: Memory pressure is often invisible until it causes a crash. The primary challenge is not recovery (crash → restart is simple) but detection of the pre-crash degraded state. CDP's `Performance.getMetrics` and `Memory.getDOMCounters` are the best early warning signals, but there is no single "memory health" event in any protocol.

### 4. Fingerprinting Persistence

**What persists across sessions with the same profile**:

| Identifier | Persistence | Evasion | Detection Use |
|---|---|---|---|
| Cookies (tracking) | Cross-session | Clear cookies | Session linking |
| localStorage | Cross-session | Clear storage | Session linking |
| IndexedDB (supercookies) | Cross-session | Clear IndexedDB | Resurrection tracking |
| Canvas fingerprint cache | Session (cleared on profile creation) | Fresh profile | Reduces per-session uniqueness |
| Font cache | Cross-session | Fresh profile | Reduces entropy |
| TLS session cache | Cross-session | Fresh profile | Performance, not fingerprint |
| HSTS/HPKP state | Cross-session | Fresh profile | Security, not fingerprint |

**Fresh vs persistent profile fingerprinting surface**:

| Fingerprint Dimension | Fresh Profile | Persistent Profile | Notes |
|---|---|---|---|
| Canvas fingerprint | New per profile | Same (cached) | Fresh = unique per creation |
| WebGL fingerprint | New per profile | Same | Hardware-constrained (same GPU) |
| Font enumeration | New per profile | Same | OS fonts + cached |
| Timezone | Dependent on OS | Same | |
| Screen resolution | Dependent on OS | Same | |
| Cookie-based tracking | Empty | Populated | Tracking networks link sessions |
| A/B test cohort | Not assigned | Assigned | Experiments see returning user |

**Key insight**: The primary detection advantage of fresh profiles is not fingerprint uniqueness (canvas/WebGL vary by hardware, not profile) but the absence of tracking cookies and state. A fresh profile appears as a new visitor to every tracking network. A persistent profile reveals the session history.

### 5. Memory Monitoring APIs

| API | Protocol | Granularity | Overhead | Use Case |
|---|---|---|---|---|
| `Performance.getMetrics` | CDP | Per-snapshot | Low | JS heap trend, node count, event listener count |
| `Memory.getDOMCounters` | CDP | Per-snapshot | Low | DOM node leaks, detached DOM trees |
| `Memory.prepareForLeakDetection` | CDP | Trigger | Low | GC hint before snapshot |
| `Memory.getBrowserSamplingProfile` | CDP | Per-snapshot | Medium | V8 heap profiling |
| `performance.memory` | JS | Per-snapshot | Low | JS heap (Chromium-only) |
| `performance.measureUserAgentSpecificMemory` | JS | Per-snapshot | Low | Cross-origin memory (estimated) |
| `about:discards` | Chrome URL | Snapshot | Manual | Tab discard status |
| OS process metrics | OS APIs | Continuous | Low | Resident set size, CPU, file descriptors |

---

## Research Confidence

**Primary-source coverage**: 70% (storage specs are mature; memory pressure and OOM handling are less formally specified)

**Gaps**:
- No standardized memory pressure event across browser engines or protocols
- Tab discard behavior in headless mode is undocumented (Chrome Saver doesn't apply, but OS-level OOM still does)
- Supercookie persistence across profile resets is under-documented (IndexedDB-based tracking)
- The interaction between CDP Memory domain and incognito/headless mode is unclear
- Cross-browser profile format differences (Chromium vs Firefox vs WebKit) are poorly documented

---

## Implications for HPF

### Structure for Direct Mode Consumption

Each HPF object in this cycle must expose structured fields that reasoning modes can consume without inference.

**For Explain mode** — each concept must have:
- definition (semantic)
- properties (keyed list)
- mechanics (how it works)

**For Compare mode** — each concept must have:
- comparison_criteria (criterion, entity_a, entity_b, importance)
- tradeoff_tables (dimension, option_a, option_b, recommendation)

**For Troubleshoot mode** — each concept must have:
- failure_modes (name, observable_evidence, likelihood, detection, recovery, retryable)

**For Design mode** — each concept must have:
- approaches (name, pros, cons, best_for)
- pitfalls (name, description, mitigation)
- best_practices (practice, rationale)

**For Decide mode** — each concept must have:
- decision_factors (factor, supporting_evidence, contradictory_evidence, weight)

This is the new quality bar. Prose under headings is not sufficient.

### Specific Benchmark Impact

| QID | Mode | Question | Current Dependency | New Knowledge |
|---|---|---|---|---|
| D05 | decide | Should I use a fresh browser profile per session? | browser-profiles-concept (18 lines) | Profile lifecycle, fingerprint analysis, trade-offs |
| C06 | compare | Browser profile vs fresh session | browser-profiles-concept | Structured comparison with specific criteria |
| D03 | decide | Should I use data-testid selectors? | selector-strategy-pattern (indirect) | Memory/state persistence not directly relevant |
| D06 | decide | Should I use anti-detection techniques? | anti-detection-principle | Profile-based fingerprinting persistence |
| T01 | troubleshoot | Why do sessions expire unexpectedly? | session-lifecycle-concept | Cache/storage corruption as root cause |
| E05 | explain | Why do browser profiles matter? | browser-profiles-concept | Complete profile component breakdown |
| C05 | compare | Exponential backoff vs fixed backoff | retry-pattern (indirect) | Memory pressure influences retry strategy selection |

---

## Open Questions

1. Does Chrome Memory Saver (tab discarding) operate in headless mode? Current evidence suggests no, but undocumented.
2. What is the precise relationship between CDP `Memory` domain availability and incognito/guest mode?
3. How do different browser engines (Chromium, Firefox, WebKit) differ in profile structure and memory management? Current research is Chromium-dominant.
4. Can IndexedDB-based supercookies survive a "clear cookies and site data" operation, or is a new profile required for complete isolation?
5. What is the memory overhead per CDP connection? Does each attached target consume significant additional memory?
6. Is there a standardized way to detect impending OOM before the renderer crashes, or is post-crash detection the only reliable option?
7. How does service worker cache persistence interact with automation profile management? Can a service worker from a previous session interfere with a new session?

---

*Research Cycle 002 — 2026-07-29*
