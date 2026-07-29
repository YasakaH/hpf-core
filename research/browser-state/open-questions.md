# Open Questions — Browser State

Questions discovered during research that are unresolved. These seed future research cycles.

## Technical Questions

1. **Heartbeat interval** — What is the optimal interval for zombie session detection? Industry practice varies from 2s to 30s. No formal guidance exists. Relevant to T01, T04.

2. **CDP lifecycle event cross-browser support** — Can `Page.lifecycleEvent` be relied upon as a cross-browser standard? Currently Chromium-only in practice (CDP is Chromium-native). Firefox CDP support diverges. WebDriver BiDi may unify. Relevant to C01, C03.

3. **Frame detach → session invalidation mapping** — Does a frame detach always invalidate CDP bindings, or only cross-origin navigations? Current understanding: same-origin preserves bindings; cross-origin invalidates. But this is nuanced (iframes, nested frames, about:blank). Relevant to T04, DS03.

4. **Memory pressure event consistency** — Are memory pressure signals consistent across browser engines (Chromium, Firefox, WebKit)? CDP exposes Memory domain; others vary. Relevant to D04, T01.

5. **WebDriver BiDi state observability** — Does WebDriver BiDi close the observability gap with CDP for state tracking? BiDi is actively evolving. Relevant to C01, DS04.

## Architectural Questions

6. **State machine formalization** — Should the unified state machine definition be formalized as a standard (or at least a reference model)? No single source of truth currently exists across browser tools.

7. **Readiness taxonomy** — The 6-level readiness taxonomy (DOM ready, loaded, network idle, visual, element visible, custom) is a proposed framework. Does it generalize across automation frameworks, or does each framework need its own taxonomy?

8. **Agent Readiness API** — Could a standard browser API (e.g., `document.agentState`) expose readiness for automation agents? This is a potential W3C contribution. Relevant to Perspective C.

## Research Methodology Questions

9. **Primary source gaps** — Crash recovery and OOM handling are poorly documented in official sources. How should we fill these gaps? (Instrumented testing? Community surveys? Vendor outreach?)

10. **Version sensitivity** — Browser state behaviour changes across Chromium versions. How should knowledge objects track version-specific behaviour? (Version-ranged sections? Separate profiles?)

---

*Research Cycle 001 — 2026-07-29*
