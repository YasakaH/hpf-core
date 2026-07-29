# Book Outline Notes — Browser State

These are notes, not prose. Each entry records what this research domain contributes to each book perspective.

---

## Perspective A — Browser Automation Engineering

### Where Browser State fits
Part of the Foundations section. After explaining what browsers are and how protocols work, the reader needs to understand what "state" means in a browser context.

### Key concepts to include
- Session vs page vs frame — three nested state machines
- The launch → attach → ready → navigate → terminate sequence
- Why readiness is framework-dependent (Playwright auto-wait vs Selenium explicit)
- The gap between DOMContentLoaded and networkIdle (grows with web complexity)

### Notes for chapters
- **Session lifecycle** belongs in "How Browsers Work" or similar architectural chapter
- **Navigation lifecycle** belongs in "Page Interaction" — explains why interactions fail
- **Readiness model** belongs in "Reliability Patterns" — foundational for wait strategies
- Use the state machine diagram from the dossier

### Open questions
- How deep should the CDP events go? Engineers need enough to debug, not a protocol reference

---

## Perspective B — Production Browser Agent Infrastructure

### Where Browser State fits
Part of the "Session Management" and "Reliability" sections. This is operational knowledge — how to keep sessions alive, detect failures, and recover.

### Key concepts to include
- Session pool architecture (pre-warm, health-check, return)
- Zombie session detection (heartbeat interval, process-level checks)
- Crash recovery (Inspector.targetCrashed handling, re-attach)
- Memory pressure monitoring and proactive session rotation
- The degraded → unresponsive → kill chain

### Notes for chapters
- **Session lifecycle** is the core of "Session Management Architecture" chapter
- **Failure modes** table belongs in "Handling Failure" chapter
- **Heartbeat and health checks** — operational patterns chapter
- Include decision tree: recover vs restart vs ignore
- Compare session-per-operation vs session-pool vs persistent approaches

### Open questions
- What is the optimal pool size for browser sessions? (depends on work, memory, site detection)
- Should production systems use Chrome for Testing or full Chrome?

---

## Perspective C — Browser UX Engineering / Agent-Ready Web

### Where Browser State fits
Part of the "How Agents See the Web" section. The concept of state is invisible to human users but critical for agents — making state explicit and predictable is a UX design concern.

### Key concepts to include
- The readiness gap — humans tolerate partial loading; agents need defined milestones
- Design implication: pages should emit explicit lifecycle signals for agents
- SPA state management — agents need non-visual signals for route changes
- The case for declarative readiness (e.g., data attributes, lifecycle events, `document.readyState`-like APIs for agent readiness)
- Contrast: human UX (loading spinner) vs agent UX (lifecycle event)

### Notes for chapters
- **State observability** — "What Agents Need That Humans Don't" chapter
- **Navigation lifecycle** — "Why SPA Patterns Break Agents" chapter
- **Readiness model** — "Designing for Agent Readiness" chapter
- Propose `document.agentState` or similar API concept as a design pattern
- The gap between DOMContentLoaded and networkIdle is an opportunity for better agent UX

### Open questions
- Is a W3C-style "Agent Readiness" specification viable?
- Should pages expose navigation type (full/SPA/redirect) in a standard way?

---

*Research Cycle 001 — 2026-07-29. Notes, not polished prose.*
