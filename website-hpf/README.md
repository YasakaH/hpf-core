# HPF Research Workbench (website-hpf)

**INTERNAL-ONLY SITE.** URL: `https://hpf.versatilesparks.qzz.io`

A private workbench over the HPF research corpus. The UI is a consumer of the
`knowledge-export-core-v1` export contract — it reads `data/export.json` and
its derived index `data/index.json`, and nothing else. It never reads
dossiers, programme state, or engine internals. If the workbench ever needs
HPF internals, that is contract pressure evidence, not permission to bypass
the contract.

## Orientation (2026-08-04, owner-directed)

The workbench faces the research workflow, not the engine's internals. Home is
a research prompt; the Research hub records intended investigations and shows
the pipeline the research orchestrator will execute (plan -> collect ->
extract -> cross-reference -> findings -> adjudicate -> corpus). The ontology,
schema, and exporter details live under Diagnostics, not the dashboard.
`config.json` holds hostnames and links so no code hardcodes a domain — during
the shared-root-domain migration only `config.json` changes.

## Data flow

```
Research Corpus  →  owner-driven release  →  exports/ (committed, versioned)
                                             2026-08-03.json
                                             2026-08-03.index.json
                                             latest.json
                                             latest.index.json
                        ↓ build.py (gate + sync)
             website-hpf/ static UI (read-only consumer)
```

- The corpus is the single source of truth; the export and index are derived
  projections of it.
- **Releases are committed and versioned.** `exports/YYYY-MM-DD.json` is an
  immutable release artifact. `latest.json` / `latest.index.json` point at the
  current release. The workbench always serves the committed release — the
  deployed dataset is reproducible from git alone.
- The UI is disposable and rebuildable from `scripts/build.py`.

### Making a release

```bash
python tools/hpf-engine/export.py --out exports/2026-08-03.json
python tools/hpf-engine/check_contract.py exports/2026-08-03.json   # must PASS
python tools/hpf-engine/index.py --export exports/2026-08-03.json --out exports/2026-08-03.index.json
copy exports\2026-08-03.json exports\latest.json        # (or cp)
copy exports\2026-08-03.index.json exports\latest.index.json
python website-hpf/scripts/build.py                      # local preview data
```

Commit `exports/` with the release, then deploy explicitly (below).

## Authentication (single boundary)

**Cloudflare Access is the only authentication boundary.** The application
itself has no login screen — anything shipped to the client is visible to an
authenticated user and adds no security. Anyone who reaches the app is
assumed authenticated by the edge.

- Cloudflare dashboard → Zero Trust → Access → Applications → Add
  application: type **Self-hosted**, domain `hpf.versatilesparks.qzz.io`
- Policy: allow your email (or "Everyone" with One-time PIN), prompt
  "Select an identity provider"
- Add **Login methods** (e.g. One-time PIN) so staff can sign in by email.

Do not share the `versatilesparks-hpf.pages.dev` URL; it is a deployment
endpoint, not a public address. The custom domain is the only entry point.

## Build locally

```bash
python website-hpf/scripts/build.py
# then serve the static site:
python -m http.server 8000 --directory website-hpf
# open http://localhost:8000
```

`build.py` gates the committed release (`check_contract.py`) and syncs
`exports/latest.*` into `website-hpf/data/`. If conformance fails, the build
exits non-zero and nothing is served.

## Deploy

Deployment is **explicit and manual only** — never triggered by a push.

- Repository: `YasakaH/hpf-core` (branch `main`) — engine, research,
  workbench, and releases live together
- Workflow: `.github/workflows/release-hpf.yml` — runs only via
  `workflow_dispatch` ("Release HPF Workbench"); it gates the committed
  release, verifies the committed index, and deploys those exact files. CI
  never regenerates the dataset.
- GitHub secrets required: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`
- Cloudflare Pages project: `versatilesparks-hpf`
- Custom domain: `hpf.versatilesparks.qzz.io` (Cloudflare Pages → project →
  Custom domains)

## Consumers (siblings of this workbench)

`tools/hpf-engine/consumers/` holds the other contract-only consumers:

- `render_markdown.py` — publishing adapter (Markdown report of all valid
  objects)
- `factsheet.py` — marketing adapter (one-line fact sheet)

Every consumer — the workbench, publishing, marketing — imports nothing but
the export contract.
