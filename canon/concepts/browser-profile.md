# Browser Profile

**Domain**: Browser Memory

## Definition

A browser profile is an isolated storage directory containing all persistent browser state — cookies, localStorage, IndexedDB, caches, preferences, extensions, TLS state, and site data — that outlives individual browser sessions.

## Properties

- **Storage path**: Filesystem directory (`user-data-dir` in Chromium, profile directory in Firefox)
- **Isolation boundary**: Profiles are fully isolated — state from one profile is invisible to another
- **Persistence scope**: Cross-session (survives browser restart), cross-tab (shared within profile)
- **Lifetime**: Created once, persists until explicitly deleted
- **Components**: Cookies DB, Local Storage (LevelDB), IndexedDB (LevelDB), HTTP Cache (disk cache), Service Worker storage, Preferences (JSON), Extensions, TLS state, visited links DB, Top Sites, Shortcuts, Login Data, History, Bookmarks

## Profile Lifecycle

```
Create (mkdir user-data-dir)
  ↓
Load (browser reads profile on launch)
  ↓
Bind (automation attaches to profile via --user-data-dir)
  ↓
Use (tabs share cookies, localStorage, cache)
  ↓
Persist (writes happen continuously during use)
  ↓
Close (browser writes pending state on shutdown)
  ↓
Reuse (next launch reads persisted state)
  OR
Discard (delete profile directory)
```

## Relationships

| Concept | Relationship |
|---|---|
| Session Lifecycle | A session is one lifecycle instance within a profile. A profile may host many sessions. |
| Browser Storage | Storage mechanisms (cookies, localStorage, IndexedDB) are the content of a profile. |
| Memory Pressure | Profile size contributes to disk/memory pressure; large profiles slow browser startup. |
| Anti-Detection | Profile persistence is the primary mechanism for cross-session tracking and detection. |
| Automation Protocol | Protocol choice affects profile control: CDP provides profile-level control; WebDriver is session-level. |
| Navigation Lifecycle | Profile state (cookies, cache) affects page load behaviour across navigations. |

## Constraints

- Only one browser instance can use a profile at a time (file locking on SQLite databases)
- Profiles accumulate state over time — a 6-month-old profile may be 100x larger than a fresh one
- Profile corruption can render a profile unusable (corrupt Cookies or Local Storage files)
- Chrome for Testing uses a temp profile by default; persistent profiles require explicit `--user-data-dir`
- Incognito/guest mode creates an ephemeral in-memory profile (no disk writes)
- Profile migration between browser versions may fail (format changes)

---

*Canonical concept. Not tool-specific.*
