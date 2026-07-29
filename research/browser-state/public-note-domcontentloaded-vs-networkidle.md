# The Gap Between DOMContentLoaded and networkIdle

Your browser says the page is loaded.

Your automation says the element isn't there.

Who is right?

## The Gap

When a browser loads a page, it fires `DOMContentLoaded` when the HTML is parsed and `load` when all resources are fetched. Most automation waits for one of these events.

But modern pages aren't finished at `load`. They lazy-load images, fetch API data, mount React components, and load dynamic imports. The real "ready" signal — `networkIdle` (no network activity for 500ms) — fires much later.

How much later?

| Page Type | DOMContentLoaded | load | networkIdle |
|---|---|---|---|
| Static HTML | 0.3s | 0.5s | 0.6s |
| SPA + API calls (fast) | 0.8s | 1.2s | 2.5s |
| SPA + lazy images | 0.8s | 1.5s | 4.0s |
| Micro-frontend | 1.5s | 3.0s | 6.0s |
| Dashboard + widgets | 2.0s | 4.0s | 8.0s+ |

The gap grows with page complexity.

## Framework Approaches

- **Playwright**: Waits for `networkIdle` by default. SPA-friendly. Sacrifices speed for reliability.
- **Selenium**: Waits for `load` by default. Fast but misses SPA navigation completely.
- **CDP directly**: You choose. Full control, full responsibility.

The best choice depends on your target. Playwright's default works for most pages. Selenium needs explicit waits for SPAs. CDP needs careful lifecycle event handling.

## What This Means

This gap is the #1 cause of flaky automation. Not bad selectors. Not wrong waits. The gap between what the browser considers "loaded" and what the page actually needs to be interactive.

Next time your automation fails with a timing-related error, check: did you wait for the right signal?

---

*Derived from Research Cycle 001 — Browser State. Original research dossier at research/browser-state/dossier.md.*
