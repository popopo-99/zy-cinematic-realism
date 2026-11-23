#!/usr/bin/env python3
"""Validate indexed camera-language cards and their existing-library links."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

import validate_director_library as base


ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "zy-cinematic-realism" / "references"
CATEGORIES = {
    "Optical Lens & Projection",
    "Framing & Shot Size",
    "Camera Position & Orientation",
    "Camera Movement",
    "Focus & Image Behavior",
    "Composition",
    "Editorial / Temporal Shot Grammar",
}
PRESENTATIONS = {
    "directly_visible_in_still",
    "inferred_or_suggested_in_still",
    "requires_temporal_sequence",
    "video_instruction",
}
FIELDS = (
    "分类",
    "常用别名",
    "通俗说法",
    "专业定义",
    "原理与条件",
    "可见结果",
    "典型场景",
    "常见误解",
    "呈现方式",
    "落入现有字段",
    "迁移方法",
    "related_equipment_ids",
    "related_film_card_ids",
)
TERM_ANCHOR = re.compile(r'<a id="(term-[^"]+)"></a>')
TERM_ID = re.compile(r"term-[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FIELD_LINE = re.compile(r"^- \*\*([^*]+)\*\*[ \t]*[:：]?[ \t]*(.*)$", re.MULTILINE)


def read_markdown(path: Path) -> str:
    return base.markdown_content(path.read_text(encoding="utf-8-sig"))


def discover_routes(index: Path, errors: list[str]) -> dict[str, Path]:
    """Use term links in the Markdown index as the only card registry."""
    routes: dict[str, Path] = {}
    for link in base.MARKDOWN_LINK_RE.findall(read_markdown(index)):
        value = link.strip().strip("<>")
        anchor = unquote(value.partition("#")[2])
        if not anchor.startswith("term-"):
            continue
        if not TERM_ID.fullmatch(anchor):
            errors.append(f"{index.name}: invalid stable term ID '{anchor}'.")
        try:
            parsed = urlsplit(value)
        except ValueError:
            errors.append(f"{index.name}: malformed term route '{link}'.")
            continue
        target = base.local_target(value, index)
        if parsed.scheme or parsed.netloc or parsed.query or target is None:
            errors.append(f"{index.name}: term route must be a local Markdown path: '{link}'.")
            continue
        if (
            not target.is_relative_to(index.parent.resolve())
            or target.suffix.lower() != ".md"
            or target == index.resolve()
        ):
            errors.append(f"{index.name}: term route escapes the references or targets a non-card resource: '{link}'.")
            continue
        if anchor in routes:
            errors.append(f"{index.name}: duplicate index route for '{anchor}'.")
        else:
            routes[anchor] = target
        if not target.is_file():
            errors.append(f"{index.name}: missing indexed card file '{link}'.")
    if not routes:
        errors.append(f"{index.name}: no indexed camera-language cards.")
    return routes


def string_array(term_id: str, field: str, value: str, errors: list[str]) -> list[str] | None:
    arrays = re.findall(r"`(\[[^\r\n]*?\])`", value)
    if len(arrays) != 1:
        errors.append(f"{term_id}: {field} must contain one backtick-delimited JSON array.")
        return None
    try:
        items = json.loads(arrays[0])
    except json.JSONDecodeError:
        errors.append(f"{term_id}: {field} contains invalid JSON.")
        return None
    if not isinstance(items, list) or any(
        not isinstance(item, str) or not item.strip() for item in items
    ):
        errors.append(f"{term_id}: {field} must be an array of nonempty string values.")
        return None
    if len(items) != len(set(items)):
        errors.append(f"{term_id}: {field} contains duplicate values.")
    return items


def validate_related_ids(
    term_id: str,
    field: str,
    value: str,
    source: Path,
    library: Path,
    available_ids: set[str],
    errors: list[str],
) -> int:
    """Validate each evidence edge, including its actual library destination."""
    ids = string_array(term_id, field, value, errors)
    if ids is None:
        return 0
    linked_ids: set[str] = set()
    for link in base.MARKDOWN_LINK_RE.findall(value):
        try:
            parsed = urlsplit(link.strip().strip("<>"))
        except ValueError:
            errors.append(f"{term_id}: {field} has a malformed library link: '{link}'.")
            continue
        if parsed.scheme or parsed.netloc or parsed.query:
            errors.append(f"{term_id}: {field} must use a local library link without a query: '{link}'.")
            continue
        target = base.local_target(link, source)
        anchor = unquote(link.strip().strip("<>").partition("#")[2])
        if target == library.resolve():
            linked_ids.add(anchor)
        else:
            errors.append(f"{term_id}: {field} has a link outside its existing library: '{link}'.")
    for related_id in ids:
        if related_id not in available_ids:
            errors.append(f"{term_id}: {field} references unknown ID '{related_id}'.")
        if related_id not in linked_ids:
            errors.append(f"{term_id}: {field} has no matching library link for '{related_id}'.")
    for undeclared in linked_ids - set(ids):
        errors.append(f"{term_id}: {field} links undeclared ID '{undeclared}'.")
    return len(ids)


def capture_fields(path: Path, errors: list[str]) -> set[str]:
    """Read the current Capture Design table instead of duplicating its schema."""
    match = re.search(
        r"^## 摄影记录\s*$\n(.*?)(?=^## |\Z)",
        read_markdown(path),
        re.MULTILINE | re.DOTALL,
    )
    fields = set()
    if match:
        for line in match.group(1).splitlines():
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if (
                line.startswith("|")
                and len(cells) == 2
                and cells[0] != "项目"
                and not re.fullmatch(r"[- :]+", cells[0])
            ):
                fields.add(cells[0])
    if not fields:
        errors.append(f"{path.name}: cannot read the existing 摄影记录 field table.")
    return fields


def validate_card(
    term_id: str,
    block: str,
    source: Path,
    reference_root: Path,
    equipment_ids: set[str],
    film_ids: set[str],
    known_fields: set[str],
    errors: list[str],
) -> tuple[int, int]:
    headings = re.findall(r"^###\s+(.+)$", block, re.MULTILINE)
    heading = headings[0] if len(headings) == 1 else ""
    chinese, separator, english = heading.partition(" / ")
    if not separator or not re.search(r"[\u4e00-\u9fff]", chinese) or not re.search(r"[A-Za-z]", english):
        errors.append(f"{term_id}: expected one Chinese / English card heading.")
    fields: dict[str, str] = {}
    for name, value in FIELD_LINE.findall(block):
        if name in fields:
            errors.append(f"{term_id}: duplicate field '{name}'.")
        fields[name] = value.strip()
    for name in FIELDS:
        if not fields.get(name):
            errors.append(f"{term_id}: missing or empty field '{name}'.")
    category_text = fields.get("分类", "").replace("`", "")
    categories = [item.strip() for item in re.split(r"[,，、]", category_text) if item.strip()]
    if (
        not categories
        or len(categories) != len(set(categories))
        or any(item not in CATEGORIES for item in categories)
    ):
        errors.append(f"{term_id}: 分类 must use unique values from the seven principle dimensions.")
    aliases = string_array(term_id, "常用别名", fields.get("常用别名", ""), errors)
    if aliases == []:
        errors.append(f"{term_id}: 常用别名 needs at least one common alias.")
    presentation_text = fields.get("呈现方式", "")
    presentations = re.findall(r"`([^`]+)`", presentation_text)
    remainder = re.sub(r"`[^`]+`", "", presentation_text).strip(" ,，、/|")
    if (
        not presentations
        or remainder
        or len(presentations) != len(set(presentations))
        or any(item not in PRESENTATIONS for item in presentations)
    ):
        errors.append(f"{term_id}: 呈现方式 must use unique values from the four presentation tags.")
    mapped_fields = set(re.findall(r"`([^`]+)`", fields.get("落入现有字段", "")))
    if not mapped_fields.intersection(known_fields):
        errors.append(f"{term_id}: 落入现有字段 must name an existing Capture Design table field in backticks.")
    equipment_edges = validate_related_ids(
        term_id, "related_equipment_ids", fields.get("related_equipment_ids", ""),
        source, reference_root / "equipment-library.md", equipment_ids, errors,
    )
    film_edges = validate_related_ids(
        term_id, "related_film_card_ids", fields.get("related_film_card_ids", ""),
        source, reference_root / "cinema-shot-library.md", film_ids, errors,
    )
    return equipment_edges, film_edges


def validate_legacy_routes(path: Path, routes: dict[str, Path], errors: list[str]) -> None:
    """Keep old stable anchors as data-driven redirects."""
    if not path.is_file():
        errors.append(f"Missing stable-ID compatibility page: {path.name}")
        return
    body = read_markdown(path)
    anchors = list(TERM_ANCHOR.finditer(body))
    if not anchors:
        errors.append(f"{path.name}: compatibility page has no stable term anchors.")
    counts = Counter(match.group(1) for match in anchors)
    for term_id, count in counts.items():
        if count != 1:
            errors.append(f"{path.name}: duplicate compatibility anchor '{term_id}'.")
    for number, match in enumerate(anchors):
        term_id = match.group(1)
        end = anchors[number + 1].start() if number + 1 < len(anchors) else len(body)
        block = body[match.end():end]
        matches = [
            link for link in base.MARKDOWN_LINK_RE.findall(block)
            if unquote(link.strip().strip("<>").partition("#")[2]) == term_id
            and base.local_target(link, path) == routes.get(term_id)
        ]
        if term_id not in routes or len(matches) != 1:
            errors.append(f"{path.name}: '{term_id}' must redirect once to the indexed card with the same stable ID.")


def validate_camera_language(errors: list[str], reference_root: Path | None = None) -> dict[str, int]:
    """Append errors for the main validator and return data-derived coverage.

    The optional root supports isolated fixture tests. The caller owns the
    repository-wide Markdown link check. This function does not run agents.
    """
    reference_root = (reference_root or REF).resolve()
    index = reference_root / "camera-language-dictionary.md"
    equipment = reference_root / "equipment-library.md"
    cinema = reference_root / "cinema-shot-library.md"
    capture = reference_root / "capture-design.md"
    stats = {"terms": 0, "files": 0, "equipment_edges": 0, "film_edges": 0}
    resources = (index, equipment, cinema, capture)
    for path in resources:
        if not path.is_file():
            errors.append(f"Missing camera-language resource: {path}")
    if any(not path.is_file() for path in resources):
        return stats
    routes = discover_routes(index, errors)
    equipment_anchors = Counter(re.findall(r'<a id="([^"]+)"></a>', read_markdown(equipment)))
    film_anchors = Counter(re.findall(r'<a id="((?:film|shot)-[^"]+)"></a>', read_markdown(cinema)))
    for library, anchors in ((equipment, equipment_anchors), (cinema, film_anchors)):
        for stable_id, count in anchors.items():
            if count > 1:
                errors.append(f"{library.name}: duplicate library stable ID '{stable_id}' ({count} anchors).")
    equipment_ids = set(equipment_anchors)
    film_ids = set(film_anchors)
    known_fields = capture_fields(capture, errors)
    indexed_files = set(routes.values())
    category_files = set((reference_root / "camera-language").rglob("*.md"))
    files = indexed_files | {path.resolve() for path in category_files}
    found: Counter[str] = Counter()
    for path in sorted(files):
        if not path.is_file():
            continue
        body = read_markdown(path)
        anchors = list(TERM_ANCHOR.finditer(body))
        if path in indexed_files and not anchors:
            errors.append(f"{path.name}: indexed file contains no explicit term anchors.")
        for number, match in enumerate(anchors):
            term_id = match.group(1)
            found[term_id] += 1
            if not TERM_ID.fullmatch(term_id):
                errors.append(f"{path.name}: invalid stable term ID '{term_id}'.")
            if routes.get(term_id) != path:
                errors.append(f"{path.name}: unindexed card or wrong file route for '{term_id}'.")
            end = anchors[number + 1].start() if number + 1 < len(anchors) else len(body)
            equipment_edges, film_edges = validate_card(
                term_id, body[match.end():end], path, reference_root,
                equipment_ids, film_ids, known_fields, errors,
            )
            stats["equipment_edges"] += equipment_edges
            stats["film_edges"] += film_edges
    for term_id in routes.keys() | found.keys():
        if found[term_id] != 1:
            errors.append(f"{term_id}: expected one explicit card anchor across indexed/category files, found {found[term_id]}.")
    validate_legacy_routes(reference_root / "camera-language-p0.md", routes, errors)
    stats.update(terms=len(routes), files=len(indexed_files))
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--allow-sparse",
        action="store_true",
        help="Accept omitted reference targets only when marked skip-worktree in the Git index.",
    )
    args = parser.parse_args()
    errors: list[str] = []
    stats = validate_camera_language(errors)
    base.validate_markdown_links(errors, allow_sparse=args.allow_sparse)
    if errors:
        print(f"Camera-language static validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Camera-language static validation passed: "
        f"{stats['terms']} indexed cards in {stats['files']} files, "
        f"{stats['equipment_edges']} equipment links, {stats['film_edges']} film/shot links, "
        "structure, compatibility routes, and local Markdown links."
    )
    print("Agent text behavior, image generation, and visual execution: NOT VERIFIED by this script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
