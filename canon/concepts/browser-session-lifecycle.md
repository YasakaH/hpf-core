# Session Lifecycle

**Domain**: Browser State

## Definition

The sequence of states a browser process transitions through from launch to termination, including process spawn, protocol attachment, navigation, resource loading, degradation, recovery, and termination phases.

## Properties

- **Spawn**: Process creation, Chrome for Testing / headless / full browser launch, user-data-dir initialization
- **Attach**: CDP WebSocket connection or WebDriver session creation, capability negotiation, target discovery
- **Ready**: DOM interactive, network quiet, event loop responsive, attached to at least one target
- **Navigation**: URL change, page unload, new page load, render complete (see Navigation Lifecycle for phases)
- **Degraded**: Resource constrained, memory pressure, connection issues, performance degraded but not failed
- **Unresponsive**: Process alive but IPC not responding, heartbeat timeout exceeded
- **Recover**: Re-attempt connection, re-attach target, resume from known state
- **Terminated**: Process exit, crash, or explicit close, all resources released
- **Detached**: Process alive but session connection lost (WebSocket drop, DevTools disconnect, network interruption)

## State Transitions

```
Spawn → Attach → Ready → Navigation ←→ Ready → Terminate
                    ↑        ↓                       ↓
                    |    Degraded → Recover → Ready  Terminated
                    |        ↓
                    |   Unresponsive → Kill
                    |        ↓
                    +--- Detached → Re-attach → Ready
```

## Key Observability Signals

| State | CDP Signal | WebDriver Signal | Timing |
|---|---|---|---|
| Spawn | Process handle, stdout/stderr | Process handle | Instant |
| Attach | WebSocket open, `Target.attachedToTarget` | Session created | <1s |
| Ready | `Page.lifecycleEvent(networkIdle)` | `executeScript` returns | Variable |
| Navigation | `Page.frameStartedLoading`, `Page.frameNavigated` | Navigate command, URL change | Variable |
| Degraded | `Performance.getMetrics` delta, memory pressure | `executeScript(performance.memory)` | Gradual |
| Unresponsive | No event received within heartbeat timeout | Command timeout | >N seconds configurable |
| Terminated | WebSocket close, process exit code | Session deleted | Instant |
| Detached | WebSocket close (unexpected), `Inspector.detached` | Command failure | Instant |
| Recover | New WebSocket open, re-attach | New session creation | Configurable |

## Relationships

| Concept | Relationship |
|---|---|
| Navigation Lifecycle | Session lifecycle contains many navigation lifecycles. Each navigation is a phase within the session. |
| Browser Readiness Model | Readiness model determines when within the session lifecycle interaction is safe. |
| Browser Profile | A profile persists across sessions; a session is one lifecycle instance of a profile. |
| Health Check | A health check probes whether the session is in Ready or Degraded state. |
| Retry Strategy | Retry decisions depend on session lifecycle state (retry during navigation? during degraded?). |
| Automation Protocol | Protocol choice affects which lifecycle states are observable and which transitions are detectable. |
| Anti-Detection | Detection signals may differ across lifecycle states (new session = clean fingerprint, aged session = more detectable). |

## Constraints

- Session cannot be reused after termination — must spawn new process
- Only one navigation per frame can be active at a time at the protocol level
- Degraded state has an implicit timeout before forced termination (browser-dependent, ~30s for OOM)
- Detached sessions may leak OS resources (zombie processes) if not explicitly cleaned
- Re-attach to a detached session is protocol-dependent — CDP supports re-attach to targets; WebDriver requires new session
- Heartbeat interval is application-defined; no protocol standard exists for zombie detection
- Chrome for Testing terminates when all sessions disconnect; full Chrome persists
- Some CDP events are only emitted for the first N seconds after attach (domain-specific throttling)

---

*Canonical concept. Not tool-specific.*
