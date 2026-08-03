"""
HPF Knowledge Object Parser

Parses Markdown knowledge objects into typed KnowledgeObject instances.
This is the single entry point for all Markdown → domain model conversion.
No validation, no defaults, no repair, no analysis — just parsing.

Usage:
    obj = parse("knowledge/browser-profiles-concept.md")
    obj = parse_text(markdown_string)
"""

import re
from pathlib import Path

from models import BLOCK_TO_FIELD, Identity, KnowledgeObject


BLOCK_HEADER_RE = re.compile(
    r"^## (Claims|Relationships|Tradeoffs|Failure Modes|"
    r"Decision Factors|Observations|Constraints|Heuristics|Recommendations)\s*$"
)


def parse(path: Path | str) -> KnowledgeObject:
    """Read a Markdown file and return a typed KnowledgeObject."""
    p = Path(path)
    return parse_text(p.read_text(encoding="utf-8"))


def parse_text(text: str) -> KnowledgeObject:
    """Parse Markdown text into a typed KnowledgeObject."""
    lines = text.split("\n")
    identity = _parse_identity(lines)
    blocks = _find_blocks(lines)
    kwargs = {"identity": identity}

    kwargs["_section_names"] = set(blocks.keys())

    for section_name, section_lines in blocks.items():
        field = BLOCK_TO_FIELD.get(section_name)
        if field:
            kwargs[field] = _parse_block_items(section_lines)

    return KnowledgeObject(**kwargs)


def _parse_identity(lines: list[str]) -> Identity:
    """Extract Identity from the ## Identity section."""
    raw = {}
    in_identity = False
    identity_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped == "## Identity":
            in_identity = True
            continue
        if in_identity:
            if stripped.startswith("## "):
                break
            if stripped:
                identity_lines.append(stripped)

    for item in identity_lines:
        m = re.match(r"^- (\w+):\s*(.+)$", item)
        if m:
            key = m.group(1)
            value = m.group(2).strip()
            if key in ("tags", "entities", "concepts"):
                value = [v.strip().strip("[]").strip('"') for v in value.split(",")]
            raw[key] = value

    return Identity(
        id=raw.get("id"),
        type=raw.get("type"),
        title=raw.get("title"),
        tags=raw.get("tags", []),
        entities=raw.get("entities", []),
        concepts=raw.get("concepts", []),
        domain=raw.get("domain"),
        version=raw.get("version"),
        research_cycle=raw.get("research_cycle"),
    )


def _find_blocks(lines: list[str]) -> dict[str, list[str]]:
    """Split lines into sections by ## block headers."""
    blocks = {}
    current_block = None
    current_lines = []

    for line in lines:
        m = BLOCK_HEADER_RE.match(line)
        if m:
            if current_block:
                blocks[current_block] = current_lines
            current_block = m.group(1)
            current_lines = []
        elif current_block is not None:
            current_lines.append(line)

    if current_block:
        blocks[current_block] = current_lines

    return blocks


def _parse_block_items(lines: list[str]) -> list[dict]:
    """Parse a block's YAML-like list items into dicts."""
    items = []
    current_item = {}
    in_item = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        has_indent = re.match(r"^(\s+)", line)
        indent = len(has_indent.group(1)) if has_indent else 0

        is_item_start = re.match(r"^-\s+(\w[\w_]*):\s*(.*)$", stripped)
        is_sub_field = re.match(r"^(\w[\w_]*):\s*(.*)$", stripped)
        is_array_item = re.match(r"^-\s+(.+)$", stripped)

        if is_item_start and indent < 2:
            if in_item and current_item:
                items.append(current_item)
            current_item = {is_item_start.group(1): is_item_start.group(2).strip()}
            in_item = True
        elif is_sub_field and in_item and indent >= 2:
            key = is_sub_field.group(1)
            val = is_sub_field.group(2).strip()
            if key in current_item:
                if not isinstance(current_item[key], list):
                    current_item[key] = [current_item[key]]
                current_item[key].append(val)
            else:
                current_item[key] = val
        elif is_array_item and in_item and indent >= 4:
            current_item.setdefault("options", []).append(is_array_item.group(1).strip())

    if in_item and current_item:
        items.append(current_item)

    return items
