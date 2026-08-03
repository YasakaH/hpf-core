# Session Lifecycle Concept

## Identity
- id: session-lifecycle-concept
- type: concept
- title: Browser Session Lifecycle
- tags: [session, lifecycle, browser, state, process]
- entities: [session, browser, lifecycle, process, target]
- concepts: [browser-session-lifecycle, navigation-lifecycle, browser-readiness-model]

## Metadata
- created: 2025-04-07
- updated: 2026-07-29
- domain: browser-automation
- version: 0.2.0
- research_cycle: 001

## Semantic Layer
A browser session progresses through: launch → attach → ready → navigate → interact → degrade/recover → terminate. Each stage has specific failure modes, observability signals, and recovery paths. The session lifecycle is the top-level state machine governing all browser automation.

## Narrative Layer
Session lifecycle management is critical for production automation. Proper session lifecycle management prevents resource leaks, enables reliable recovery from failures, and provides the foundation for all higher-level automation patterns. Key lifecycle events include process spawn, CDP/WebSocket attachment, target discovery, navigation, degradation (memory pressure, connection issues), and clean termination.

## Compare Section
### CDP vs WebDriver — Session Lifecycle Observability
| Criterion | CDP | WebDriver |
|---|---|---|
| Target lifecycle events | Explicit events: `Target.targetCreated/Destroyed`, `Inspector.targetCrashed` | Implicit via window handles; no crash event |
| Session detach detection | `Inspector.detached` event with reason | Inferred from command timeout |
| Process state visibility | Rich: `Browser.getVersion`, `SystemInfo`, `Target.getTargets` | Minimal: status endpoint only |
| Crash detection | `Inspector.targetCrashed` event (explicit) | Timeout (inferred) |
| Re-attach support | Yes — targets persist across detach | No — new session required |
| Memory monitoring | `Memory.getDOMCounters`, `Performance.getMetrics` | `executeScript(performance.memory)` only |

### Playwright vs Selenium — Lifecycle Management
| Criterion | Playwright | Selenium |
|---|---|---|
| Browser launch | Manages Chromium/Firefox/WebKit processes | Requires driver binary |
| Context isolation | Browser contexts separate sessions | One session per WebDriver instance |
| Default navigation wait | networkIdle | load |
| Target management | Automatic (new page = new context) | Manual (window handle switching) |
| Session recovery | Browser-level restart via fixtures | WebDriver-level restart |
| Resource cleanup | Automatic on context close | Manual quit required |

## Troubleshoot Section
### Likely Causes — Session Termination or Detachment
| Cause | Probability | Evidence | Diagnostic Steps | Fix |
|---|---|---|---|---|
| OOM / renderer crash | High | `Inspector.targetCrashed` event, no IPC response | Check `chrome://gpu`, `chrome://memory-internals` | Reduce tabs, increase memory limit, restart session |
| WebSocket disconnect | Medium | `Inspector.detached` with "Connection lost" | Check network stability, proxy health | Re-attach target, or restart session |
| Navigation to new origin | Medium | Frame references stale, `detachedFromTarget` | Check URL change pattern | Re-acquire frame references after navigation |
| Idle timeout / throttling | Low-Medium | Session stops responding after inactivity | Check browser args (`--disable-background-timer-throttling`) | Send periodic heartbeat, disable throttling |
| Browser process crash | Low | Process exit code, connection close | Check system logs | Restart process, consider container restart policy |

## Design Section
### Approaches — Managing Session Lifecycle

**Approach 1: Single persistent session**
Keep one session alive for the automation lifetime. Reuse tabs for navigations.
- Pros: Low overhead, fast, simple
- Cons: Accumulates memory, detection risk (long-lived fingerprint), single point of failure
- Best for: Short-lived automation (<1 hour), simple scraping

**Approach 2: Session per operation**
Spawn a new session for each discrete operation. Terminate after completion.
- Pros: Clean state, minimal detection, easy cleanup
- Cons: High overhead (browser launch is slow), no state persistence
- Best for: Low-volume automation, high-reliability requirements

**Approach 3: Session pool**
Maintain a pool of pre-warmed sessions. Draw from pool, return after use.
- Pros: Low latency, resource bounded, natural load distribution
- Cons: Complex implementation, session health management required
- Best for: Production automation at scale

**Recommended**: Approach 3 (session pool) for production. Approach 1 for development and testing.

### Pitfalls
- Not cleaning up detached sessions causes zombie processes (OS resource exhaustion)
- Reusing a terminated session (no is_alive check) causes confusing errors
- Long-running sessions accumulate browser memory (Chromium memory leak per tab)
- Session health checks that are too aggressive kill healthy sessions; too lenient waste time on dead sessions
- Chrome for Testing terminates on session disconnect; full Chrome persists — know which you're using

### Best Practices
- Implement heartbeat monitoring (check `Target.getTargets` every 5-10s)
- Always explicitly close sessions (`browser.close()` or driver.quit())
- Use process-level health checks (OS signal, PID exists?) in addition to protocol-level checks
- Set up `Inspector.detached` listener in CDP-based automation
- Implement session recovery with exponential backoff (see Retry Strategy)
- Monitor memory pressure via CDP `Memory` domain or `performance.memory` (WebDriver)
- Fresh browser profile per session for isolation; persistent profile for stateful automation
