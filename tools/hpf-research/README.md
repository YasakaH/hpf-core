# HPF Research Orchestrator (tools/hpf-research)

Evidence-collection pipeline v0. Turns a research request into a session
artifact (plan -> collect -> extract -> draft findings). Sessions are
operational evidence records — never corpus knowledge. Nothing here touches
the corpus; corpus admission happens later through the authoring/validation
pipeline if the owner decides.

Scope is deliberately mechanical: no LLM. HTML -> text, paragraph chunking,
keyword-density ranking. Findings are DRAFT candidate findings that require
adjudication.

## Usage

```bash
python research.py --topic "Microsoft Fara vs nodriver" \
  --goal "Does Microsoft Fara make nodriver obsolete?" \
  --audience Blog --depth standard \
  --import-md evidence-1.md --source-url https://github.com/microsoft/fara \
  --import-md evidence-2.md \
  --sync-web ../../website-hpf/sessions
```

- `--url URL` fetches a page (stdlib only); `--import-md` imports a text/markdown
  file with a declared `--source-url`.
- `--sync-web <dir>` copies the session into the workbench's `sessions/` dir and
  writes `index.json` so the workbench can render it.

## Session shape

`sessions/<id>/session.json`:
`{ schema, id, topic, goal, audience, depth, created, started, finished,
   activity[{ts,msg}], status, stages[], sources[], evidence[], findings[],
   notes }`

`activity` is the real per-step execution log with UTC timestamps, recorded
during the run (no fabricated progress). `started`/`finished` bound the run;
the workbench renders elapsed time from them. Sessions created before this
field existed simply omit it.

## Boundaries

- Consumers of the workbench are read-only with respect to the corpus.
- Findings carry `status: needs_adjudication` and `confidence: null` until the
  owner adjudicates them. A draft finding never implies corpus admission.
- `website-hpf/sessions/` is git-ignored; sessions are dev/local artifacts.