# Why Clearing Cookies Isn't Enough

You clear cookies between automation sessions.

You think the state is clean.

It isn't.

## The Five Storage Systems

A browser has five independent storage systems:

| System | Cleared by "Clear Cookies"? | What it contains |
|---|---|---|
| Cookies | Yes | Session tokens, tracking IDs |
| localStorage | No | App data, tracking IDs |
| IndexedDB | No | Databases, offline data, supercookies |
| Cache API | No | SW-managed caches, identifiers |
| HTTP Cache | No | Cached resources |

Clearing cookies only touches the first row.

## Why This Matters for Automation

If you're using persistent profiles and only clearing cookies between sessions:

- Tracking networks can resurrect cookies from IndexedDB (supercookie pattern)
- localStorage-based sessions persist across cookie clears
- Service worker caches can re-populate tracking state
- The profile accumulates state over time, increasing the detection surface

A fresh profile is the only complete reset.

## What To Do

| Approach | What it clears | Effort |
|---|---|---|
| Clear cookies | Cookies only | Low |
| Clear all storage (CDP) | Cookies + localStorage + IndexedDB + Cache API | Medium |
| Fresh profile | Everything (new user-data-dir) | High (but most thorough) |
| Playwright context isolation | Everything (virtual profile per context) | Low (automatic) |

If you're using Playwright, browser contexts handle this automatically — each context gets an isolated storage environment.

If you're using Selenium or CDP directly, you need to manage this yourself. CDP provides individual commands for each storage system (`Network.clearBrowserCookies`, `Storage.clearDataForOrigin`, `IndexedDB.deleteDatabase`, `CacheStorage.deleteCache`).

---

*Derived from Research Cycle 002 — Browser Memory. Original dossier at research/browser-memory/dossier.md.*
