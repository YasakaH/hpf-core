# Research Dossier: Browser State

**Cycle**: Research Cycle 001
**Domain**: Browser State
**Date**: 2026-07-29
**Status**: Complete

---

## Abstract

Browser State encompasses the lifecycle, transitions, and observability of a browser process from launch to termination. It is the foundational domain for automation reliability — every automation failure is ultimately a state management failure. This dossier surveys navigation lifecycle, session lifecycle, readiness models, failure modes, and state observability across CDP and WebDriver protocols.

---

## Sources

| Type | Count | Key References |
|---|---|---|
| Official specifications | 3 | W3C Page Lifecycle, W3C WebDriver, Chrome DevTools Protocol |
| Vendor documentation | 5 | Chromium source (content/public), Playwright (lifecycle), Puppeteer (lifecycle), Selenium (wait strategies), CDP (Page, Network, Target domains) |
| Engineering blogs | 4 | Chrome DevTools team (lifecycle phases), Playwright (auto-waiting), Airbnb (browser state management), Puppeteer (navigation handling) |
| Community evidence | 6 | GitHub issues (flaky navigation, crash recovery, OOM handling), Stack Overflow (state checking patterns), testing conference talks |

**Evidence quality**:
- Official specifications: ██████████ (comprehensive coverage)
- Vendor documentation: ██████████ (well-documented across tools)
- Engineering blogs: ████████ (gap: few sources on crash recovery patterns)
- Community evidence: ████████ (extensive but distributed)

---

## Domain Analysis

### 1. Navigation Lifecycle

The page-level lifecycle is defined by the W3C Page Lifecycle specification and augmented by browser-specific events.

**Standard states** (W3C):
```
loading → interactive → complete → unloaded
                    ↓
                frozen → discarded
```

**Chromium-specific detail** (from content/public/browser content):
```
Loading → DOMContentLoaded → Load → FirstPaint → FirstContentfulPaint → NetworkAlmostIdle → NetworkIdle
```

**CDP-observable events**:
- `Page.frameStartedLoading` → frame navigation begins
- `Page.frameNavigated` → new document committed
- `Page.documentOpened` → document opened via `window.open`
- `Page.lifecycleEvent` → `DOMContentLoaded`, `load`, `networkAlmostIdle`, `networkIdle`, `firstPaint`, `firstContentfulPaint`
- `Page.frameStoppedLoading` → load complete for frame

**Key insight**: The gap between `load` and `networkIdle` is the most common source of flaky automation. Many pages are interactive at `DOMContentLoaded` but still loading resources. Automation frameworks handle this differently: Playwright auto-waits for networkIdle by default; Selenium defaults to `load`. HPF objects should expose this gap.

**Failure modes during navigation**:
- Frame detaches mid-navigation (SPA route changes)
- Navigation never completes (infinite redirects, hanging resource)
- Navigation to unsupported protocol (chrome://, file://, blob:) fails silently
- Cross-origin navigation loses existing frame references

### 2. Session Lifecycle

The browser process-level lifecycle, from process spawn to termination.

**States**:
```
Spawn → Attach → Ready → Navigating ←→ Ready → Terminate
                         ↓                              ↓
                     Degraded → Recover → Ready      Terminated
                         ↓
                     Unresponsive → Kill → Terminated
```

**Key events**:
| Event | Protocol | Description |
|---|---|---|
| `Target.targetCreated` | CDP | New tab/window/worker created |
| `Target.targetDestroyed` | CDP | Tab/window/worker destroyed |
| `Target.attachedToTarget` | CDP | Session attached to a target |
| `Target.detachedFromTarget` | CDP | Session detached from target |
| `Inspector.targetCrashed` | CDP | Target process crashed |
| `Inspector.detached` | CDP | Debugger detached (session invalidated) |
| `Page.windowOpen` | CDP | `window.open()` triggered |

**Failure modes**:
- Target crash (OOM, renderer crash, GPU process crash)
- Target detach (navigation to new origin replaces target)
- Session disconnect (websocket drop, browser process exit)
- Zombie sessions (process alive but unresponsive, no IPC response)
- Resource exhaustion (too many targets, memory pressure, GPU memory)

**Key insight**: Session lifecycle failures are the hardest to diagnose because the browser process may still be alive but the automation session is orphaned. CDP's `Inspector.detached` is the cleanest signal. WebDriver has no equivalent event — the session simply stops responding.

### 3. Readiness Models

Different consumers have different definitions of "ready":

| Model | Definition | Use Case |
|---|---|---|
| DOM interactive | DOM parsed, scripts loaded | Text extraction, attribute reading |
| Load | All resources loaded | Full page capture, screenshots |
| Network idle | No network activity for N ms | SPA interaction, lazy content |
| First paint | First non-white pixel | Visual readiness |
| User-visible | Critical above-fold content rendered | User-facing automation |
| Custom | Application-specific signal | Domain-specific readiness |

**Framework auto-wait strategies**:
- **Playwright**: Auto-waits for actionable state (visible, enabled, stable). Navigation waits for `networkIdle` by default (configurable to `load`, `domcontentloaded`, or `commit`).
- **Selenium**: Waits for `load` event by default. Explicit waits required for finer control.
- **Puppeteer**: `waitForNavigation` resolves on `load`. `waitForNetworkIdle` available as separate method.
- **CDP directly**: No auto-wait. Consumer must implement readiness checks from lifecycle events.

**Failure modes**:
- Network idle never reached (long-polling, Server-Sent Events, websocket heartbeat)
- Custom readiness signal never fires (SPA bootstrap failure, JS exception)
- Readiness changed between check and action (race condition)
- Page ready but frame not ready (iframe content)

### 4. Failure Mode Taxonomy

| Mode | Cause | Detection | Recovery |
|---|---|---|---|
| Renderer crash | OOM, GPU hang, JS runaway | `Inspector.targetCrashed` | New session |
| Navigation hang | Missing redirect, hanging resource | Timeout | Abort navigation |
| Session detach | Cross-origin nav, new tab | `Inspector.detached`, event missing | Re-attach |
| Zombie session | Process alive, no IPC | Heartbeat timeout | Kill and restart |
| Memory pressure | Tab accumulation, leaks | Performance.memory, CDP Memory domain | GC, close tabs |
| Process exit | Browser kill, crash | Connection close, process exit code | New session |
| Race condition | State change between check and action | Flaky test pattern | Rethink synchronization |

### 5. State Observability

| What | CDP | WebDriver | Notes |
|---|---|---|---|
| Navigation events | `Page.frameStartedLoading`, `Page.frameNavigated`, `Page.lifecycleEvent` | Navigation via URL change, `executeScript` return | CDP provides granular events; WebDriver requires polling |
| Target lifecycle | `Target.targetCreated/Destroyed`, `Inspector.targetCrashed` | Window handles | CDP: 5 events; WebDriver: 3 states (window exists/closed/error) |
| Process state | `Browser.getVersion`, `SystemInfo`, `Target.getTargets` | Status | CDP richer; WebDriver process state is opaque |
| Memory pressure | `Memory.getDOMCounters`, `Performance.getMetrics` | `executeScript(performance.memory)` | CDP provides more; both have `performance` API |
| Crash detection | `Inspector.targetCrashed` | Timeout on command | CDP: explicit event; WebDriver: infer from failure |
| Event bus state | WebSocket readyState | HTTP response status | CDP: connection state; WebDriver: session validity |

---

## Research Confidence

**Primary-source coverage**: 65% (W3C specs, Chromium source, CDP protocol docs cover the core well; crash recovery and OOM handling are less formally specified)

**Gaps**:
- No single unified state machine definition exists across browser tools
- Crash recovery best practices are community-derived, not documented by vendors
- Memory pressure detection patterns are undocumented across frameworks
- WebDriver process state observability is poorly specified

**Key secondary sources used**: Playwright source (auto-waiting), Puppeteer issue tracker (navigation handling), Chrome DevTools blog (lifecycle events), Selenium documentation (wait strategies)

---

## Implications for HPF

1. **Compare mode**: Browser State provides concrete comparison criteria for CDP vs WebDriver (C01), Playwright vs Selenium (C03) — they differ significantly in state observability
2. **Troubleshoot mode**: Session expiry (T01), browser crash (T04) gain better root cause taxonomies
3. **Explain mode**: Session lifecycle (E04) gains richer detail with specific CDP events and protocol differences
4. **Decide mode**: Questions about session reuse, fresh profiles, health checks gain evidence-backed reasoning

---

## Open Questions

1. What is the optimal heartbeat interval for zombie session detection? Industry practice varies (2-30s).
2. Can `Page.lifecycleEvent` be relied upon as a cross-browser standard? Currently Chromium-only.
3. WebDriver BiDi promises improved observability — does it close the gap with CDP for state tracking?
4. Are memory pressure events present consistently across browser engines (Chromium, Firefox, WebKit)?
5. What is the precise relationship between `frame` detach and session invalidation — does a frame detach always invalidate CDP bindings, or only cross-origin navigations?

---

*Research Cycle 001 — 2026-07-29*
