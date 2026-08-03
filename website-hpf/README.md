# HPF Research Workbench (website-hpf)

**INTERNAL-ONLY SITE.** URL: `https://hpf.versatilesparks.qzz.io`

A private, authenticated workbench over the HPF research corpus. The UI is a
consumer of the `knowledge-export-core-v1` export contract — it reads
`data/export.json` and its derived index `data/index.json`, and nothing else.
It never reads dossiers, programme state, or engine internals. If the
workbench ever needs HPF internals, that is contract pressure evidence, not
permission to bypass the contract.

## Data flow

```
Research Corpus  →  export.py  →  data/export.json  (contract, frozen)
                        ↓ check_contract.py (conformance gate, must PASS)
                  index.py → data/index.json (derived index)
                        ↓
             website-hpf/ static UI (read-only consumer)
```

The corpus is the single source of truth. The workbench is disposable and
rebuildable from `scripts/build.py`.

## Authentication (two layers)

1. **Cloudflare Access — the authoritative boundary.** The subdomain must be
   protected at the edge:
   - Cloudflare dashboard → Zero Trust → Access → Applications → Add
     application: type **Self-hosted**, domain `hpf.versatilesparks.qzz.io`
   - Policy: allow your email (or "Everyone" with One-time PIN), prompt
     "Select an identity provider"
   - Add **Login methods** (e.g. One-time PIN) so staff can sign in by email.
2. **In-app login gate** — a convenience layer, not a security boundary.
   Set a password hash in `config.js`:

   ```bash
   python website-hpf/scripts/hash_password.py 'your-password-here'
   ```

   Paste the SHA-256 hex into `config.js` → `auth.users`.

## Build locally

```bash
python website-hpf/scripts/build.py
# then serve the static site:
python -m http.server 8000 --directory website-hpf
# open http://localhost:8000
```

`build.py` runs export → conformance gate → index. If conformance fails the
build exits non-zero and nothing is served.

## Deploy

- Repository: `YasakaH/hpf-core` (branch `main`) — this repo contains both the
  engine and the workbench
- Workflow: `.github/workflows/hpf-deploy.yml` — auto-deploys on pushes
  touching `tools/hpf-engine/**`, `website-hpf/**`, or the workflow itself
  (manual `workflow_dispatch` also supported)
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
