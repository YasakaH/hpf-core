# Navigation Lifecycle

## Identity
- id: navigation-lifecycle
- type: concept
- title: Page Navigation Lifecycle
- tags: [navigation, page, lifecycle, state, DOM, load, readiness]
- entities: [navigation, page, frame, load, DOM, resource]
- concepts: [navigation-lifecycle, browser-readiness-model, browser-session-lifecycle]

## Metadata
- created: 2026-07-29
- domain: browser-automation
- version: 0.1.0
- research_cycle: 001

## Semantic Layer
Page navigation progresses through: loading → interactive → complete → unloaded, with intermediate milestones (DOMContentLoaded, load, networkAlmostIdle, networkIdle). SPA navigations differ fundamentally — they don't reset readyState or trigger load events. Navigation behaviour varies across navigation types (full, SPA, redirect, iframe).

## Narrative Layer
Navigation lifecycle is the most common source of flaky automation. The gap between DOMContentLoaded (page queryable) and networkIdle (page fully loaded) is where most timing-dependent failures occur. Modern web patterns (SPA, lazy loading, micro-frontends, dynamic imports) widen this gap. Automation frameworks handle this gap differently — Playwright auto-waits for networkIdle by default, Selenium waits for load, CDP requires explicit lifecycle event handling. Understanding navigation lifecycle is essential for building reliable automation.

## Compare Section
### Full Navigation vs SPA Navigation — Lifecycle Behaviour
| Criterion | Full Navigation | SPA Navigation |
|---|---|---|
| Ready state | Resets through loading → complete | Stays complete (no reset) |
| Load events | `DOMContentLoaded`, `load` fire | Neither fires |
| CDP events | Full `Page.lifecycleEvent` sequence | `Page.frameNavigated` only (sometimes) |
| Frame references | Invalidated for new origin | Usually preserved |
| Resource loading | Full reload | Lazy chunks only |
| Network usage | Full page download | API calls + lazy bundles |

### Playwright vs Selenium — Navigation Wait Strategies
| Criterion | Playwright | Selenium |
|---|---|---|
| Default wait | `networkIdle` (configurable: load, domcontentloaded, commit) | `load` |
| SPA support | Auto-waits for network idle after action | No SPA detection; explicit wait needed |
| Timeout behavior | Detailed error with pending operations | TimeoutException with URL |
| Frame handling | Automatic (waits for frame lifecycle) | Manual (switchTo().frame()) |
| Navigation timeout | Separate from action timeout | Same as implicit/explicit wait |
| Recovery | Retries on detached frame | StaleElementReferenceException |

## Troubleshoot Section
### Likely Causes — Navigation Failures
| Cause | Probability | Evidence | Diagnostic Steps | Fix |
|---|---|---|---|---|
| Network timeout | High | Navigation never completes, resource hangs | Check network tab, `Network.requestWillBeSent` | Reduce timeout, implement retry |
| Infinite redirect | Medium | URL keeps changing, never settles | Check `Network.requestWillBeSent` chain | Implement redirect limit, detect loop |
| Cross-origin frame detach | Medium | Frame references stale after navigation | Check frame URL origin change | Re-acquire frame references |
| SPA route change not detected | Medium | Navigation resolves immediately, page unchanged | Check URL change, no `load` event | Use custom URL detection, wait for element |
| SSL / certificate error | Low | Navigation fails with `ERR_CERT_*` | Check `Security.securityStateChanged` | Handle certificate errors, use --ignore-certificate-errors |
| Unsupported protocol | Low | Navigation to `chrome://`, `file://`, `blob:` | Check URL scheme | Validate URL before navigation |
| beforeunload dialog | Low | Navigation blocked by user confirmation | Check `Page.javascriptDialogOpening` | Handle dialog, or use `Page.handleJavaScriptDialog` |

## Design Section
### Approaches — Reliable Navigation Handling

**Approach 1: Wait-for-load (Selenium default)**
Wait for `load` event before interaction.
- Pros: Simple, standard, cross-browser
- Cons: SPA pages never fire load; slow for resource-heavy pages
- Best for: Traditional multi-page apps, simple scraping

**Approach 2: Wait-for-network-idle (Playwright default)**
Wait for network activity to cease for N ms.
- Pros: Works for SPAs, ensures full page load
- Cons: May never resolve (SSE, websocket); slower
- Best for: SPA-heavy pages, production automation

**Approach 3: Custom readiness signal**
Define application-specific readiness (element visible, API response, DOM mutation).
- Pros: Fastest, most reliable for known apps
- Cons: Requires application knowledge, not generalizable
- Best for: Known target applications, test automation

**Approach 4: Smart readiness detection**
Monitor multiple signals, use first that fires within constraints.
- Pros: Adaptive, handles different page types
- Cons: Complex implementation, over-engineered for simple cases
- Best for: Automation against heterogeneous targets

**Recommended**: Approach 2 (network idle) for general automation. Approach 3 for known targets. Approach 4 for heterogeneous environments.

### Pitfalls
- Waiting for `load` on SPA pages never resolves — navigation will time out
- `networkIdle` may never fire for pages with persistent connections — implement fallback timeout
- Racing `waitForNavigation` and action triggers causes missed events — set up wait first, then trigger
- Cross-origin iframe navigation invalidates references silently — always verify frame context after navigation
- Navigation error handling differs by framework — CDP requires explicit error event listeners

### Best Practices
- Use `Promise.all` pattern: start waiting for navigation, then trigger navigation action
- Always set explicit navigation timeouts (defaults vary: Playwright 30s, Selenium infinite)
- Verify navigation outcome by checking URL, title, or expected element, not just wait resolution
- For SPAs, use element visibility or network idle, not `load` event
- After navigation to new origin, re-acquire all frame/document references
- Implement redirect chain limit to detect infinite redirect loops
- Use CDP `Network.requestWillBeSent` + `Network.loadingFailed` for detailed navigation diagnostics
