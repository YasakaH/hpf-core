# Session Lifecycle

**Domain**: Browser State

## Definition

The sequence of states a browser process transitions through from launch to termination, including attachment, navigation, resource loading, and detachment phases.

## Properties

- **Launch**: Process spawn, CDP/WebDriver attachment, initial page load
- **Ready**: DOM interactive, network quiet, event loop responsive
- **Navigation**: URL change, page unload, new page load, render complete
- **Degraded**: Resource constrained, memory pressure, connection issues
- **Terminated**: Process exit, crash, or explicit close
- **Detached**: Process alive but session connection lost

## Relationships

| Concept | Relationship |
|---|---|
| Browser Profile | A profile persists across sessions; a session is one lifecycle instance |
| Health Check | Health checks probe whether session is in Ready or Degraded state |
| Retry Strategy | Retry decisions depend on lifecycle state (retry during navigation? during degraded?) |
| Automation Protocol | Protocol choice affects which lifecycle states are observable |
| Anti-Detection | Detection signals may differ across lifecycle states |

## Constraints

- Only one navigation can be active per session (at protocol level)
- Session cannot be reused after termination
- Degraded state has a timeout before forced termination
- Detached sessions may leak OS resources if not explicitly cleaned

---

*Canonical concept. Not tool-specific.*
