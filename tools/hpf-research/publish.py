"""Publishing Compiler: render an ADJUDICATED session into publish packs.

Core discipline (reviewer-mandated):
    Session -> Review -> Accepted Findings -> Compiler
    NEVER Draft Findings -> Compiler

The compiler refuses to run on a session with no review layer, and only
accepted findings (approve / revise / add) ever appear in output. Rejected
findings are counted in the pack metadata and never rendered.

Output (exports/publish/<session-id>/, immutable once written):
    publish-pack.json   machine-readable pack: metadata + accepted claims
    renders/            multiple renderings of the SAME accepted research:
                        comparison.md, article.md, linkedin.md,
                        x-thread.md, faq.md, documentation.md

Every rendered claim carries: status, confidence (null until validated),
sources (real URLs), evidence ids, and dates. The compiler assembles; it
never invents text beyond the claim strings themselves.

Usage:
    python tools/hpf-research/publish.py <session-dir> [--out exports/publish]
        [--title "Publication title (defaults to session topic)"]
"""
import argparse
import datetime
import json
import sys
from pathlib import Path


def accepted_findings(session: dict, adjudication: dict) -> list:
    """Only approve/revise/add decisions; revise uses the revised claim."""
    by_id = {f["id"]: f for f in session.get("findings", [])}
    out = []
    for d in adjudication.get("findings", []):
        dec = d.get("decision")
        if dec == "approve":
            f = by_id[d["id"]]
            out.append({**f, "review_decision": "approve", "review_note": d.get("note", "")})
        elif dec == "revise":
            f = by_id[d["id"]]
            out.append({**f, "claim": d["revised_claim"], "review_decision": "revise", "review_note": d.get("note", "")})
        elif dec == "add":
            out.append({
                "id": d["id"], "claim": d["claim"], "status": d.get("status", "needs_adjudication"),
                "confidence": None, "sources": d.get("sources", []), "evidence": [],
                "method": d.get("method", "adjudication-v0"), "review_decision": "add",
                "review_note": d.get("note", ""),
            })
    return out


def rejected_count(adjudication: dict) -> int:
    return sum(1 for d in adjudication.get("findings", []) if d.get("decision") == "reject")


def provenance(f: dict) -> str:
    lines = [f"  - status: {f.get('status')} · confidence: {f.get('confidence')} · method: {f.get('method')}"]
    if f.get("dates"):
        lines.append(f"  - dates: {', '.join(f['dates'])}")
    for s in f.get("sources", []):
        lines.append(f"  - source: {s}")
    if f.get("evidence"):
        lines.append(f"  - evidence: {', '.join(f['evidence'])}")
    if f.get("review_note"):
        lines.append(f"  - review note: {f['review_note']}")
    return "\n".join(lines)


def render_comparison(session, findings) -> str:
    lines = [f"# {session['topic']} — Comparison", ""]
    lines.append(f"Source: research session `{session['id']}` (adjudicated).")
    lines.append("")
    lines.append("## Accepted claims, side by side")
    for f in findings:
        lines.append(f"### {f['claim']}")
        lines.append("")
        lines.append(provenance(f))
        lines.append("")
    return "\n".join(lines)


def render_article(session, findings, adjudicated_at, publication_title=None) -> str:
    title = publication_title or session["topic"]
    lines = [f"# {title}", ""]
    if session.get("goal"):
        lines += [f"_{session['goal']}_", ""]
    lines.append(f"Status: draft article compiled from {len(findings)} accepted findings "
                 f"({session['id']}, research review {(adjudicated_at or '')[:10]}). "
                 "Claims are research findings, not validated facts; confidence is null until validated.")
    lines.append("")
    for i, f in enumerate(findings, 1):
        lines.append(f"## {i}. {f['claim']}")
        lines.append("")
        lines.append(provenance(f))
        lines.append("")
    lines.append("## Methodological note")
    lines.append("")
    lines.append("This article was compiled mechanically from an adjudicated research session. "
                 "Every claim is traceable to its sources and evidence. Nothing was rewritten "
                 "for style; rewriting belongs to the human publication step.")
    return "\n".join(lines)


def render_linkedin(session, findings) -> str:
    lines = [f"# LinkedIn draft — {session['topic']}", ""]
    lines.append("## Post body")
    lines.append("")
    lines.append(f"Research on: {session['topic']}.")
    for f in findings[:5]:
        lines.append(f"- {f['claim']}")
    lines.append("")
    lines.append("Claims are draft research findings (confidence null), not established facts.")
    lines.append("")
    lines.append(f"Source session: {session['id']}")
    return "\n".join(lines)


def render_x_thread(session, findings) -> str:
    lines = [f"# X thread draft — {session['topic']}", ""]
    lines.append("## Thread (one claim per post)")
    lines.append("")
    lines.append(f"1/{len(findings) + 1} Thread: {session['topic']}")
    for i, f in enumerate(findings, 2):
        claim = " ".join(f["claim"].split())[:250]
        lines.append(f"{i}/{len(findings) + 1} {claim}")
    lines.append(f"{len(findings) + 1}/{len(findings) + 1} Source session: {session['id']} — "
                 "draft findings, confidence null, not validated facts.")
    return "\n".join(lines)


def render_faq(session, findings) -> str:
    lines = [f"# FAQ draft — {session['topic']}", ""]
    for i, f in enumerate(findings, 1):
        q = " ".join(f["claim"].split())[:140]
        if not q.endswith("?"):
            q += "?"
        lines.append(f"## Q{i}. {q}")
        lines.append("")
        lines.append(f"A{i}. {f['claim']}")
        lines.append("")
        lines.append(provenance(f))
        lines.append("")
    return "\n".join(lines)


def render_documentation(session, findings) -> str:
    lines = [f"# Documentation update draft — {session['topic']}", ""]
    lines.append("Reference-style material compiled from accepted findings. "
                 "Nothing here is corpus knowledge until it passes validation.")
    lines.append("")
    for f in findings:
        lines.append(f"### {f['claim']}")
        lines.append("")
        lines.append(f"- Sources: {', '.join(f.get('sources', []) or ['(none)'])}")
        if f.get("dates"):
            lines.append(f"- Dates: {', '.join(f['dates'])}")
        lines.append(f"- Evidence: {', '.join(f.get('evidence', []) or ['(none)'])}")
        lines.append(f"- Status: {f.get('status')} · Confidence: {f.get('confidence')}")
        lines.append("")
    return "\n".join(lines)


RENDERS = {
    "comparison.md": render_comparison,
    "article.md": render_article,
    "linkedin.md": render_linkedin,
    "x-thread.md": render_x_thread,
    "faq.md": render_faq,
    "documentation.md": render_documentation,
}

def main():
    ap = argparse.ArgumentParser(description="HPF Publishing Compiler")
    ap.add_argument("session_dir")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent.parent / "exports" / "publish"))
    ap.add_argument("--title", default="", help="publication title; defaults to the session topic")
    args = ap.parse_args()

    sdir = Path(args.session_dir)
    sf = sdir / "session.json"
    if not sf.exists():
        print(f"! session not found: {sdir}")
        return 2
    session = json.loads(sf.read_text(encoding="utf-8"))
    adjf = sdir / "adjudication.json"
    if not adjf.exists():
        print(f"! refused: {sdir.name} has no review layer — publish only compiles adjudicated sessions")
        return 2
    adjudication = json.loads(adjf.read_text(encoding="utf-8"))

    findings = accepted_findings(session, adjudication)
    rejected = rejected_count(adjudication)
    if not findings:
        print(f"! refused: no accepted findings after review — nothing to publish")
        return 2

    out_root = Path(args.out)
    pack_dir = out_root / session["id"]
    if pack_dir.exists():
        print(f"! refused: {session['id']} already has a publish pack (immutable)")
        return 3
    pack_dir.mkdir(parents=True, exist_ok=True)
    renders_dir = pack_dir / "renders"
    renders_dir.mkdir(parents=True, exist_ok=True)

    pack = {
        "schema": "hpf-publish-pack-v0",
        "session_id": session["id"],
        "topic": session["topic"],
        "publication_title": args.title.strip() or session["topic"],
        "goal": session.get("goal", ""),
        "audience": session.get("audience"),
        "compiled_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "adjudication_ref": adjf.name,
        "adjudicated_at": adjudication.get("adjudicated_at"),
        "adjudicator": adjudication.get("adjudicator"),
        "accepted": len(findings),
        "rejected": rejected,
        "status": "draft",  # published claims are drafts until validated
        "claims": [{
            "id": f.get("id"), "claim": f.get("claim"), "status": f.get("status"),
            "confidence": f.get("confidence"), "sources": f.get("sources", []),
            "evidence": f.get("evidence", []), "method": f.get("method"),
            "review_decision": f.get("review_decision"),
        } for f in findings],
    }
    (pack_dir / "publish-pack.json").write_text(json.dumps(pack, indent=2), encoding="utf-8")

    for name, fn in RENDERS.items():
        if name == "article.md":
            text = fn(session, findings, adjudication.get("adjudicated_at"), args.title.strip() or None)
        else:
            text = fn(session, findings)
        (renders_dir / name).write_text(text, encoding="utf-8")
    # manifest
    entries = []
    for d in sorted(out_root.iterdir()):
        if not d.is_dir():
            continue
        pf = d / "publish-pack.json"
        if not pf.exists():
            continue
        try:
            p = json.loads(pf.read_text(encoding="utf-8"))
            entries.append({
                "session_id": p.get("session_id"), "topic": p.get("topic"),
                "compiled_at": p.get("compiled_at"), "accepted": p.get("accepted"),
                "rejected": p.get("rejected"), "status": p.get("status"),
            })
        except (json.JSONDecodeError, OSError):
            continue
    entries.sort(key=lambda e: e.get("compiled_at") or "", reverse=True)
    (out_root / "index.json").write_text(
        json.dumps({"schema": "hpf-publish-manifest-v0", "packs": entries}, indent=2),
        encoding="utf-8")

    print(f"Compiled publish pack for {session['id']}:")
    print(f"  accepted findings: {len(findings)} (rejected excluded: {rejected})")
    print(f"  renders: {', '.join(sorted(RENDERS))}")
    print(f"  {pack_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
