# Navigation Lifecycle

**Domain**: Browser State

## Definition

The sequence of states a page/document transitions through from initial navigation to unload, including resource loading, parsing, rendering, and network activity phases.

## Properties

- **Loading**: URL request initiated, response headers received, document parser active
- **Interactive**: DOM parsed, deferred scripts executed, DOMContentLoaded fired
- **Complete**: All resources loaded, `load` event fired, rendering complete
- **Unloaded**: Page unload initiated, `beforeunload`/`unload` fired, document detached
- **Frozen**: Page frozen for backgrounding/memory pressure (W3C Lifecycle)
- **Discarded**: Page resources released, cannot be unfrozen

## Cycle Types

| Cycle | Trigger | Events | Observable Via |
|---|---|---|---|
| Full navigation | New URL, browser refresh | loading → interactive → complete → idle | CDP `Page.lifecycleEvent`, WebDriver navigation |
| SPA navigation | History API, pushState | interactive → (virtual navigation) → interactive | CDP `Page.frameNavigated`, custom events |
| Client redirect | `window.location`, meta refresh | loading → (existing) → loading | CDP `Page.frameScheduledNavigation` |
| Server redirect | HTTP 301/302/307/308 | loading → (new URL) → loading | CDP `Network.requestRedirected` |
| iframe navigation | iframe src change | Parallel lifecycle in sub-frame | CDP `Page.frameStartedLoading` (sub-frame) |
| Form submission | POST/GET via form | loading → interactive → complete | CDP `Page.frameScheduledNavigation` |

## Important Milestones (CDP `Page.lifecycleEvent`)

| Event | Timing | Meaning |
|---|---|---|
| `DOMContentLoaded` | After HTML parsed, deferred scripts done | DOM queryable, page not fully loaded |
| `load` | After all resources loaded | Page visually complete, network may still be active |
| `networkAlmostIdle` | 2+ connections active, no new for 500ms | Most resources loaded, lazy loads may still fire |
| `networkIdle` | 0 connections for 500ms | Network fully idle |
| `firstPaint` | First non-white pixel rendered | First visual content |
| `firstContentfulPaint` | First text/image/ SVG painted | First meaningful visual |

## Relationships

| Concept | Relationship |
|---|---|
| Session Lifecycle | Navigation lifecycle is a phase within session lifecycle. A session spans many navigations. |
| Readiness Model | The readiness model defines which navigation milestone to wait for before interaction. |
| Retry Strategy | Retry depends on navigation phase (never retry during unload; acceptable during loading). |
| Automation Protocol | Protocol choice determines which lifecycle events are observable. |

## Constraints

- Only one navigation can be in-flight per frame at a time
- Navigation to a new origin invalidates existing CDP bindings for that frame
- SPA navigations don't trigger `load` — readiness must be determined differently
- `networkIdle` may never fire for pages with persistent connections (WebSocket, SSE)
- Form submission navigation may include `beforeunload` dialog that blocks navigation
- Navigation to unsupported protocols (chrome://, file://, blob:, data:) completes differently or fails

---

*Canonical concept. Not tool-specific.*
