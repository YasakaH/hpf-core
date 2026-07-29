# Browser Readiness Model

## Identity
- id: browser-readiness-model
- type: concept
- title: Browser Readiness Model
- tags: [readiness, waiting, synchronization, readiness, timing]
- entities: [readiness, wait, timeout, DOM, network, load]
- concepts: [browser-readiness-model, navigation-lifecycle, browser-session-lifecycle]

## Metadata
- created: 2026-07-29
- domain: browser-automation
- version: 0.1.0
- research_cycle: 001

## Semantic Layer
Readiness defines when a browser context is ready for interaction. Multiple readiness levels exist: DOM ready, fully loaded, network idle, visual ready, element visible, and custom application signals. Each readiness model trades latency for reliability. Framework selection (Playwright, Selenium, Puppeteer, CDP) determines which readiness levels are available by default.

## Narrative Layer
The concept of "ready" is framework-dependent and context-dependent. Playwright's auto-waiting makes readiness implicit — elements are interacted with only when actionable (visible, enabled, stable). Selenium requires explicit waiting — the consumer decides when the page is ready. CDP gives full control but full responsibility. Understanding readiness models prevents the most common class of automation bugs: timing-dependent failures. The gap between different readiness definitions (DOMContentLoaded vs load vs networkIdle) widens with modern web complexity.

## Compare Section
### Playwright vs Selenium — Readiness Philosophy
| Criterion | Playwright | Selenium |
|---|---|---|
| Philosophy | Auto-wait: element is ready when actionable | Explicit wait: consumer defines readiness |
| Default navigation wait | `networkIdle` | `load` |
| Element wait | Automatic (actionable) | Explicit (ExpectedConditions) |
| Timeout granularity | Per-action timeout + global timeout | Implicit + explicit + page load timeout |
| Error on timeout | Detailed (pending operations, current state) | TimeoutException |
| SPA support | Built-in (network idle detection) | Manual (expected conditions for URL/element) |
| Race condition protection | Auto-wait on action | StaleElementReferenceException on interaction |

## Troubleshoot Section
### Likely Causes — Readiness Detection Failures
| Cause | Probability | Evidence | Diagnostic Steps | Fix |
|---|---|---|---|---|
| Framework readiness != actual readiness | High | Element exists but not interactive | Check if element is visible, enabled, not covered | Use explicit readiness check matching interaction type |
| SPA navigation not detected | Medium | URL changes but page unchanged | Check if `load` event fired (it won't) | Use URL change + element visibility, not `load` |
| Persistent network activity | Medium | Network idle never reached | Check for SSE, WebSocket, polling | Use fallback timeout, switch to element-based readiness |
| Frame navigation not awaited | Medium | Actions in iframe fail after iframe navigates | Check frame lifecycle events | Wait for frame `load` or `domcontentloaded` |
| Readiness flipped between check and action | Low-Medium | Race condition in dynamic page | Check if page modifies DOM after readiness signal | Re-check element state immediately before action |
| Custom readiness signal never fires | Low | Timeout waiting for application signal | Check application logic, JS errors | Add fallback timeout, log JS console errors |

## Design Section
### Approaches — Readiness Strategy Selection

**Approach 1: Single fixed readiness level**
Pick one readiness model and use it for all pages.
- Pros: Simple, predictable
- Cons: Suboptimal for heterogeneous pages
- Best for: Automation against a single known target

**Approach 2: Adaptive readiness**
Detect page type (traditional/SPA/SSR) and select readiness model accordingly.
- Pros: Optimal for each page type
- Cons: Page type detection is itself heuristic
- Best for: Automation against unknown or varied targets

**Approach 3: Minimum-guaranteed readiness**
Wait for lowest reliable readiness level, then verify element state.
- Pros: Fast, works across page types
- Cons: May interact before full readiness (race condition risk)
- Best for: Performance-critical automation

**Approach 4: Conservative readiness**
Always wait for `networkIdle` regardless of page type.
- Pros: Safest, lowest flake rate
- Cons: Slowest, may never resolve
- Best for: Reliability-critical automation

**Recommended**: Approach 2 for production systems. Approach 4 for maximum reliability. Approach 1 for known targets.

### Pitfalls
- Using `load` as readiness for SPA pages — never fires, navigation always times out
- Assuming DOMContentLoaded = interactive — not true for JS-rendered content
- Checking element existence when you need element visibility
- Not distinguishing between element present, visible, enabled, and stable
- Readiness check passes for the right element in the wrong frame

### Best Practices
- Use element-based readiness over page-level readiness for action-oriented automation
- Set explicit timeouts on all wait operations (no infinite waits)
- Implement readiness fallback chain: element visible > network idle > load > DOMContentLoaded
- For Playwright, prefer auto-waiting over manual readiness checks
- For Selenium, use FluentWait with polling interval for dynamic pages
- Always verify readiness state immediately before action, not before the async operation started
- Log readiness level used for each interaction — helps debug flaky test patterns
