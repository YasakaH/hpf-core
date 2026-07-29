# Automation Protocol

**Domain**: Browser Architecture

## Definition

The wire-level protocol that enables external control of a browser process, defining commands, events, data types, and session semantics.

## Properties

- **Transport**: WebSocket, HTTP, pipe, or custom socket
- **Command model**: Request-response, pub-sub, or bidirectional streaming
- **Session model**: Single-tab, multi-tab, or context-based
- **Event system**: Push-based (events emitted) or poll-based
- **Capability negotiation**: Feature detection on connect
- **Security model**: Authentication, origin restrictions, sandbox level

## Relationships

| Concept | Relationship |
|---|---|
| Session Lifecycle | Protocol defines what lifecycle states are visible and controllable |
| Anti-Detection | Protocol choice affects detectability (CDP vs WebDriver signals differ) |
| Blocking and Rate Limiting | Protocol overhead and connection patterns influence rate limit triggers |
| Selector Strategy | Protocols differ in DOM query capability and performance |

## Constraints

- One protocol connection per browser process (typically)
- Protocol version must match browser version within compatibility window
- Network-level protocol metadata (WebSocket upgrade headers) is observable by the page

## Known Instantiations

| Protocol | Transport | Session Model | Detectability |
|---|---|---|---|
| CDP | WebSocket | Multi-tab (targets) | High (via `navigator.webdriver`) |
| WebDriver Classic | HTTP | Single-tab via session ID | High (standard) |
| WebDriver BiDi | WebSocket | Multi-context | Medium (newer, less profiled) |
| Custom (Playwright CDP) | WebSocket | Context-based isolation | Tool-specific |

---

*Canonical concept. Not tool-specific.*
