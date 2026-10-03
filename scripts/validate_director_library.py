#!/usr/bin/env python3
"""Validate the current director library and local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "zy-cinematic-realism"
DIRECTOR_ROOT = SKILL_ROOT / "references" / "directors"
INDEX_PATH = DIRECTOR_ROOT / "index.md"
EXPECTED_VERSION = "2.5.0"

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

DREAM_DECODE_PRODUCTION_PATHS = (
    REPO_ROOT / "README.md",
    REPO_ROOT / "README_EN.md",
    REPO_ROOT / "RELEASE_NOTES.md",
    REPO_ROOT / "CHANGELOG.md",
    SKILL_ROOT / "SKILL.md",
    SKILL_ROOT / "agents" / "openai.yaml",
    SKILL_ROOT / "references" / "dream-decode.md",
    SKILL_ROOT / "references" / "decode-card.md",
    SKILL_ROOT / "references" / "reference-role-router.md",
    SKILL_ROOT / "references" / "medium-router.md",
    SKILL_ROOT / "references" / "prompt-compiler.md",
    SKILL_ROOT / "references" / "result-repair.md",
    SKILL_ROOT / "references" / "continuity-cards.md",
    SKILL_ROOT / "references" / "models" / "gpt-image-2.md",
    SKILL_ROOT / "references" / "models" / "midjourney.md",
    SKILL_ROOT / "references" / "models" / "seedream-5-pro.md",
    SKILL_ROOT / "references" / "models" / "nano-banana.md",
)

FORBIDDEN_DREAM_DECODE_TERMS = (
    re.compile(r"\bDNA\b", re.IGNORECASE),
    re.compile(r"\bGenome\b", re.IGNORECASE),
    re.compile(r"\bgenetic\b", re.IGNORECASE),
    re.compile(r"\bgenes?\b", re.IGNORECASE),
    re.compile(r"基因"),
)


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

    routing_path = SKILL_ROOT / "references" / "director-routing.md"
    for field in SIGNATURE_FIELDS:
        if field not in routing_text:
            errors.append(
                f"{routing_path.relative_to(REPO_ROOT)}: missing Director Signature Block field '{field}'."
            )

    for path, text in (
        (SKILL_ROOT / "SKILL.md", skill_text),
        (SKILL_ROOT / "assets" / "basic-prompt-template.md", template_text),
    ):
        if "Director Four-Axis" not in text:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: missing Director Four-Axis routing reference."
            )

    version_checks = (
        (REPO_ROOT / "README.md", f"v{EXPECTED_VERSION}"),
        (REPO_ROOT / "README_EN.md", f"v{EXPECTED_VERSION}"),
        (REPO_ROOT / "RELEASE_NOTES.md", f"v{EXPECTED_VERSION}"),
        (REPO_ROOT / "CHANGELOG.md", f"v{EXPECTED_VERSION}"),
        (SKILL_ROOT / "SKILL.md", f"v{EXPECTED_VERSION}"),
    )
    for path, token in version_checks:
        text = path.read_text(encoding="utf-8")
        current_version = re.search(r"\bv\d+\.\d+\.\d+(?:-dev)?\b", text)
        if current_version is None or current_version.group() != token:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: expected current version '{token}'."
            )

    expected_zip = f"zy-cinematic-realism-v{EXPECTED_VERSION}.zip"
    for name in ("README.md", "README_EN.md", "RELEASE_NOTES.md"):
        text = (REPO_ROOT / name).read_text(encoding="utf-8")
        if name == "RELEASE_NOTES.md":
            text = text.split("\n---\n", 1)[0]
        packages = re.findall(r"zy-cinematic-realism-v\d+\.\d+\.\d+\.zip", text)
        if not packages or set(packages) != {expected_zip}:
            errors.append(f"{name}: current package must be '{expected_zip}'.")


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


def validate_dream_decode_terminology(errors: list[str]) -> None:
    """Reject heredity metaphors in current Dream Decode production content.

    Manual regression fixtures are intentionally outside this production-path list
    because they contain the forbidden literals as negative test data.
    """
    for path in DREAM_DECODE_PRODUCTION_PATHS:
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for pattern in FORBIDDEN_DREAM_DECODE_TERMS:
                match = pattern.search(line)
                if match:
                    errors.append(
                        f"{path.relative_to(REPO_ROOT)}:{line_number}: "
                        f"forbidden Dream Decode term '{match.group()}'."
                    )


def main() -> int:
    errors: list[str] = []
    director_files = validate_directors(errors)
    validate_index(director_files, errors)
    validate_signature_and_versions(errors)
    validate_markdown_links(errors)
    validate_dream_decode_terminology(errors)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Validation passed: "
        f"{len(director_files)} directors, required sections, index routing, "
        "Director Signature Block fields, version tokens, local Markdown links, "
        "and Dream Decode terminology."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
