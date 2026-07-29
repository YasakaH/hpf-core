# Browser Readiness Model

**Domain**: Browser State

## Definition

A model that defines when a browser context is considered "ready" for automation interaction, incorporating page lifecycle state, network activity, rendering progress, and application-specific signals.

## Readiness Levels

| Level | Signal | Latency | Reliability | Best For |
|---|---|---|---|---|
| DOM ready | `DOMContentLoaded` | Lowest | High (deterministic) | Text extraction, attribute reading, structure analysis |
| Fully loaded | `load` event | Medium | High | Screenshots, full page capture, PDF generation |
| Network idle | 0 active connections for N ms | Highest | Medium (may never fire) | SPA interaction, lazy content, dynamic pages |
| Visual ready | First paint / FCP metrics | Low-Medium | Medium (paint =/= usable) | Visual comparison, user-facing automation |
| Element visible | Element visible + stable | Variable | High (context-specific) | Click, type, hover actions |
| Custom signal | Application-defined | Variable | Application-dependent | Domain-specific readiness |

## Framework Implementations

| Framework | Default Wait | Configurable Options | Edge Case Handling |
|---|---|---|---|
| Playwright | Actionable state + network idle | `load`, `domcontentloaded`, `commit`, `networkidle` | Timeout with detailed error, auto-retry on detached frame |
| Selenium | `load` | `load`, `interactive`, `none` | No auto-retry, `StaleElementReferenceException` common |
| Puppeteer | `load` | `load`, `domcontentloaded`, `networkidle0`, `networkidle2` | Timeout with basic error, manual retry needed |
| CDP raw | None (consumer-defined) | Any, via `Page.lifecycleEvent` | Full control, full responsibility |

## Readiness Detection Mechanisms

**CDP-based**:
- `Page.lifecycleEvent` — precise event for each milestone
- `Runtime.evaluate` — check `document.readyState`
- `Runtime.evaluate` — check `performance.timing` (deprecated) or `performance.getEntriesByType('navigation')`
- Custom CDP domain polling for specific elements

**WebDriver-based**:
- `executeScript` — check `document.readyState`
- `executeScript` — check element visibility/state
- Expected conditions APIs (visibility, clickability, staleness)

**Playwright-specific**:
- Internal DOM signal tracking (element handles emit "attached", "detached" internally)
- Network event monitoring for idle detection
- Frame lifecycle events (`frame.loaded`, `frame.domcontentloaded`)

## Relationships

| Concept | Relationship |
|---|---|
| Navigation Lifecycle | The readiness model defines which navigation milestone constitutes "ready" |
| Session Lifecycle | Readiness checks depend on the session being attached and not degraded |
| Health Check | A health check is a readiness probe for the session, not just a single page |
| Retry Strategy | Retry decisions depend on readiness — waiting longer may succeed; retrying in unload phase will not |
| Selector Strategy | Selector reliability depends on page readiness at query time |

## Constraints

- Readiness signals are per-frame, not per-page — iframes have independent lifecycles
- `networkIdle` and `load` diverge for pages with Server-Sent Events, WebSockets, or long-polling
- SPA navigations do not reset `document.readyState` — it stays `complete` throughout
- Performance APIs (`performance.timing`, `performance.getEntriesByType`) may be disabled or modified by page scripts
- Cross-origin iframes cannot be probed for readiness from the parent context
- Browser DevTools protocol disconnection invalidates all pending wait conditions

## Open Issues

- No cross-browser standard for "element ready" — each framework implements differently
- Auto-waiting frameworks (Playwright) trade predictability for ease of use — readiness is implicit
- CDP's `Page.lifecycleEvent` is Chromium-only; Firefox and WebKit equivalents diverge
- The gap between DOMContentLoaded and networkIdle increases with modern web complexity (lazy loading, micro-frontends, dynamic imports)

---

*Canonical concept. Not tool-specific.*
