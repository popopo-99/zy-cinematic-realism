#!/usr/bin/env python3
"""Validate the v1.2 director library and local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "zy-cinematic-realism"
DIRECTOR_ROOT = SKILL_ROOT / "references" / "directors"
INDEX_PATH = DIRECTOR_ROOT / "index.md"
EXPECTED_VERSION = "1.2.0"

REQUIRED_SECTIONS = (
    "Identity",
    "Core Dramatic Logic",
    "Light and Contrast Fingerprint",
    "Color and Exposure Fingerprint",
    "Lens and Camera Fingerprint",
    "Composition and Spatial Fingerprint",
    "Blocking and Story Translation",
    "Capture Texture",
    "Common Misreadings",
    "Nearest-Neighbor Contrast",
    "Model-Facing Style Anchor",
    "Default Iconic Anchor",
    "Scene Translation",
)

IDENTITY_FIELDS = (
    "Chinese name",
    "Region",
    "Representative works",
    "Best suited for",
)

SIGNATURE_FIELDS = (
    "Director and visual reference:",
    "Lighting and contrast signature:",
    "Color and exposure signature:",
    "Lens and camera signature:",
    "Composition and spatial signature:",
)

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"""(?:src|href)=["']([^"']+)["']""", re.IGNORECASE)


def section_body(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def validate_directors(errors: list[str]) -> list[Path]:
    director_files = sorted(
        path
        for path in DIRECTOR_ROOT.glob("*.md")
        if path.name not in {"index.md", "recommendation-matrix.md"}
    )
    if not 32 <= len(director_files) <= 40:
        errors.append(
            f"Director count must be between 32 and 40; found {len(director_files)}."
        )

    for path in director_files:
        text = path.read_text(encoding="utf-8")
        for heading in REQUIRED_SECTIONS:
            if not re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE):
                errors.append(f"{path.relative_to(REPO_ROOT)}: missing section '{heading}'.")

        identity = section_body(text, "Identity")
        for field in IDENTITY_FIELDS:
            if not re.search(rf"^- {re.escape(field)}:\s*\S", identity, re.MULTILINE):
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}: missing Identity field '{field}'."
                )

        works_match = re.search(
            r"^- Representative works:\s*(.+)$", identity, re.MULTILINE
        )
        if works_match:
            works_text = works_match.group(1)
            works = re.findall(r"\*[^*]+\*", works_text)
            if not works:
                works = [
                    item.strip() for item in works_text.split(",") if item.strip()
                ]
            if not 1 <= len(works) <= 3:
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}: Representative works must contain 1-3 titles; found {len(works)}."
                )

        misreadings = section_body(text, "Common Misreadings")
        bullet_count = len(re.findall(r"^- \S", misreadings, re.MULTILINE))
        if bullet_count < 5:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: Common Misreadings needs at least 5 bullets; found {bullet_count}."
            )

        if not section_body(text, "Nearest-Neighbor Contrast"):
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: Nearest-Neighbor Contrast is empty."
            )

    return director_files


def validate_index(director_files: list[Path], errors: list[str]) -> None:
    text = INDEX_PATH.read_text(encoding="utf-8")
    linked_names = {
        Path(target).name
        for target in re.findall(r"\[[^\]]+]\(([^)#?]+\.md)\)", text)
        if Path(target).name not in {"recommendation-matrix.md", "index.md"}
    }
    expected_names = {path.name for path in director_files}

    for missing in sorted(expected_names - linked_names):
        errors.append(f"Director index does not link {missing}.")
    for extra in sorted(linked_names - expected_names):
        errors.append(f"Director index links unknown director file {extra}.")

    lines = text.splitlines()
    for number, line in enumerate(lines):
        match = re.search(r"→ \[[^\]]+]\(([^)]+\.md)\)", line)
        if not match or Path(match.group(1)).name == "recommendation-matrix.md":
            continue
        alias_line = lines[number - 1].strip() if number else ""
        summary_line = lines[number + 1].strip() if number + 1 < len(lines) else ""
        best_line = lines[number + 2].strip() if number + 2 < len(lines) else ""
        if alias_line.count("/") < 2:
            errors.append(
                f"{INDEX_PATH.relative_to(REPO_ROOT)}:{number + 1}: director entry needs Chinese, English, and alias forms."
            )
        if not summary_line.startswith("— "):
            errors.append(
                f"{INDEX_PATH.relative_to(REPO_ROOT)}:{number + 2}: missing four-axis summary."
            )
        if not best_line.startswith("— Best for:"):
            errors.append(
                f"{INDEX_PATH.relative_to(REPO_ROOT)}:{number + 3}: missing Best for line."
            )


def validate_signature_and_versions(errors: list[str]) -> None:
    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    routing_text = (SKILL_ROOT / "references" / "director-routing.md").read_text(
        encoding="utf-8"
    )
    template_text = (SKILL_ROOT / "assets" / "basic-prompt-template.md").read_text(
        encoding="utf-8"
    )

    for field in SIGNATURE_FIELDS:
        for path, text in (
            (SKILL_ROOT / "SKILL.md", skill_text),
            (SKILL_ROOT / "references" / "director-routing.md", routing_text),
            (SKILL_ROOT / "assets" / "basic-prompt-template.md", template_text),
        ):
            if field not in text:
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}: missing Director Signature Block field '{field}'."
                )

    version_checks = (
        (REPO_ROOT / "README.md", f"v{EXPECTED_VERSION}"),
        (REPO_ROOT / "CHANGELOG.md", f"[{EXPECTED_VERSION}]"),
        (SKILL_ROOT / "SKILL.md", f"v{EXPECTED_VERSION}"),
    )
    for path, token in version_checks:
        if token not in path.read_text(encoding="utf-8"):
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: expected version token '{token}'."
            )


def local_target(link: str, source: Path) -> Path | None:
    value = link.strip().strip("<>")
    if not value or value.startswith(("#", "http://", "https://", "mailto:", "data:")):
        return None
    value = value.split("#", 1)[0].split("?", 1)[0].strip()
    if not value:
        return None
    return (source.parent / unquote(value)).resolve()


def validate_markdown_links(errors: list[str]) -> None:
    markdown_files = sorted(
        path
        for path in REPO_ROOT.rglob("*.md")
        if ".git" not in path.parts and "dist" not in path.parts
    )
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        links = MARKDOWN_LINK_RE.findall(text) + HTML_LINK_RE.findall(text)
        for link in links:
            target = local_target(link, path)
            if target is not None and not target.exists():
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}: broken local link '{link}'."
                )


def main() -> int:
    errors: list[str] = []
    director_files = validate_directors(errors)
    validate_index(director_files, errors)
    validate_signature_and_versions(errors)
    validate_markdown_links(errors)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Validation passed: "
        f"{len(director_files)} directors, required sections, index routing, "
        "Director Signature Block fields, version tokens, and local Markdown links."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
