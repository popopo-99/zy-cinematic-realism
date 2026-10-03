#!/usr/bin/env python3
"""Validate the v2.5.0 Skill, resource routes, and existing contracts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import validate_director_library as base


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "zy-cinematic-realism"
REF = SKILL / "references"
EXPECTED_ANCHORS = (
    "quick-start", "use-cases", "showcase", "install",
    "advanced", "validation", "community", "license",
)


def require(path: Path, terms: tuple[str, ...], errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return
    body = path.read_text(encoding="utf-8")
    for term in terms:
        if term not in body:
            errors.append(f"{path.relative_to(ROOT)}: missing '{term}'")


def validate_readme_toc(path: Path, errors: list[str]) -> None:
    body = path.read_text(encoding="utf-8")
    ids = re.findall(r'<a id="([^\"]+)"></a>', body)
    links = re.findall(r"\[[^\]]+\]\(#([^\s)]+)\)", body)
    # README navigation may use GitHub's plain-heading anchors. Keep explicit
    # aliases for existing inbound links, but do not require them for new links.
    heading_ids = set()
    counts: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6} (.+)$", body, re.MULTILINE):
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        heading_ids.add(f"{slug}-{count}" if count else slug)
        counts[slug] = count + 1
    for anchor in EXPECTED_ANCHORS:
        if ids.count(anchor) != 1:
            errors.append(f"{path.name}: expected one explicit anchor for #{anchor}.")
    for link in links:
        target = link.removeprefix("user-content-")
        if target not in ids and target not in heading_ids:
            errors.append(f"{path.name}: local navigation #{link} has no explicit or heading anchor.")
    for duplicate in {item for item in ids if ids.count(item) > 1}:
        errors.append(f"{path.name}: duplicate anchor #{duplicate}.")


def main() -> int:
    errors: list[str] = []
    director_files = base.validate_directors(errors)
    base.validate_index(director_files, errors)
    base.validate_signature_and_versions(errors)
    base.validate_markdown_links(errors)
    base.validate_dream_decode_terminology(errors)
    for name in ("README.md", "README_EN.md"):
        validate_readme_toc(ROOT / name, errors)
    for path in (ROOT / "README.md", ROOT / "README_EN.md", ROOT / "CHANGELOG.md", ROOT / "RELEASE_NOTES.md", SKILL / "SKILL.md"):
        body = path.read_text(encoding="utf-8")
        current = body.split("\n---\n", 1)[0] if path.name == "RELEASE_NOTES.md" else body
        # Release candidates may truthfully state that they are not published.
        # Reject stale development identities, not accurate publication status.
        for stale in ("v2.5.0-dev", "local development", "本地开发版"):
            if stale in current:
                errors.append(f"{path.relative_to(ROOT)}: current release content contains '{stale}'.")
        if re.search(r"[A-Z]:\\Users\\", body):
            errors.append(f"{path.relative_to(ROOT)}: local Windows user path must not be published.")

    require(SKILL / "SKILL.md", ("name: zy-cinematic-realism", "v2.5.0", "medium-router.md", "dream-decode.md", "prompt-compiler.md", "USER-LOCKED", "OPEN", "optional `表达机制`", "story-visual-development.md"), errors)
    story_path = REF / "story-visual-development.md"
    if not story_path.is_file():
        errors.append("Missing story visual development resource.")
    for path in (REF / "story-source-ledger.md", SKILL / "tests" / "story-to-frame.md", ROOT / "docs" / "titanic-story-to-frame.md", ROOT / "docs" / "validation-v2.5.md"):
        if not path.is_file():
            errors.append(f"Missing Story to Frame resource: {path.relative_to(ROOT)}")
    # These are resource/contract checks; actual responses are reviewed separately.
    require(story_path, ("Source Facts /", "Interpretations /", "Visual Proposals /", "Task and Reading Scope", "cinematic-principles.md", "camera-and-light.md", "prompt-compiler.md", "continuity-cards.md", "Dream Decode"), errors)
    require(REF / "story-source-ledger.md", ("Read coverage", "Frame dependencies", "Result status", "Recompile only the requested affected outputs"), errors)
    require(REF / "prompt-compiler.md", ("Story Visual Development Inputs", "Freezing a candidate for compilation does not mark it user accepted or USER-LOCKED"), errors)
    require(REF / "quality-checklist.md", ("Story Visual Development (when active)",), errors)
    story_tests = SKILL / "tests" / "story-to-frame.md"
    if story_tests.is_file():
        case_ids = re.findall(r"^## (S\d{2}) —", story_tests.read_text(encoding="utf-8"), re.MULTILINE)
        if case_ids != [f"S{number:02d}" for number in range(1, 10)]:
            errors.append("Story regression document must retain S01–S09 in order.")
    if not (ROOT / "docs" / "behavior-check-v2.5.md").is_file():
        errors.append("Missing v2.5 text behavior record.")
    require(REF / "medium-router.md", ("Primary Medium", "Secondary Influences (0–2)", "Confidence", "Medium Constraints", "Medium Avoid", "Conflict Notes", "never average", "Host Medium", "Secondary Construction Rule"), errors)
    require(REF / "dream-decode.md", ("Expression Mechanism is **optional**", "Expression Mechanism: Not required", "Abnormal Event", "Event Locus", "Subject–Event Coupling", "Emotional Function", "Transferable Mechanism", "Surface Implementation", "Non-transferable Residue", "Core Visual Rules", "five to eight", "Strong Transfer", "Conditional Transfer", "Do Not Transfer", "USER-LOCKED", "OPEN"), errors)
    require(REF / "prompt-compiler.md", ("Compiler Priority Gate", "USER-LOCKED", "OPEN", "User Explicit Reference Roles", "Primary Medium / Medium Constraints", "Expression Mechanism (optional)", "Active Core Rules (3–5)", "Transfer Scope", "Medium Drift Risk", "Mechanism Drift Risk", "Prompt Overload", "three to five Active Core Rules", "full five to eight Core Visual Rules"), errors)
    require(REF / "result-repair.md", ("Valid Adaptation", "Actual Drift", "Medium Drift", "Mechanism Drift", "CHANGE ONLY", "PRESERVE EXACTLY"), errors)
    require(REF / "decode-card.md", ("Primary Medium", "Secondary Influences", "Medium Constraints", "Expression Mechanism", "Abnormal Event", "Subject–Event Coupling", "Transferable Mechanism", "Surface Implementation", "five to eight", "three to five Active Core Rules"), errors)
    card = REF / "decode-card.md"
    if card.is_file():
        card_body = card.read_text(encoding="utf-8")
        schema = card_body.split("## Final Schema", 1)[-1].split("```markdown", 1)[-1].split("```", 1)[0]
        if len(re.findall(r"^- Primary Medium:", schema, re.MULTILINE)) != 1 or re.search(r"^- Medium:", schema, re.MULTILINE):
            errors.append("Decode Card schema must have exactly one Primary Medium field and no duplicate Visual Grammar Medium field.")
        if "[omit this entire section if no distinct mechanism is observed]" not in schema:
            errors.append("Decode Card mechanism section must be optional.")
    gpt = REF / "models" / "gpt-image-2.md"
    require(gpt, ("For non-photo media", "when the Primary Medium is photographic", "three to five Active Core Rules", "an Expression Mechanism only if observed"), errors)
    require(REF / "director-routing.md", ("Never normalize a subtle request to strong", "USER-LOCKED", "only when that many are available", "selected model adapter", "Prompt-only"), errors)
    director = (REF / "director-routing.md").read_text(encoding="utf-8")
    if "Normalize every supplied strength" in director or "Mandatory Strong / Iconic Mode" in director:
        errors.append("Director routing still coerces strength to iconic.")
    require(REF / "project-handoff.md", ("accepted", "cumulative", "automatic storage", "Result status", "unavailable image", "Newer explicit user instructions"), errors)
    for name in ("chat-starter-zh.md", "chat-starter-en.md"):
        path = ROOT / "docs" / name
        require(path, ("v2.5.0", "CC BY-NC 4.0"), errors)
        if path.is_file() and re.search(r"\]\((?:\.\./)?(?:zy-cinematic-realism/)?references/", path.read_text(encoding="utf-8")):
            errors.append(f"{name}: basic chat rules depend on external reference files.")
    for path in (ROOT / "docs" / "getting-started.md", ROOT / "docs" / "getting-started_EN.md"):
        require(path, ('<a id="install-codex"></a>', '<a id="use-chatgpt"></a>', "v2.5.0"), errors)
    metadata = SKILL / "agents" / "openai.yaml"
    require(metadata, ("$zy-cinematic-realism", "model-native image prompt"), errors)
    if metadata.is_file() and "model-native cinematic image prompt" in metadata.read_text(encoding="utf-8"):
        errors.append("openai.yaml default prompt must not force a cinematic image prompt.")
    tests = SKILL / "tests" / "manual-regression.md"
    require(tests, ("Image-level Dream Decode Regression", "at least three paired comparisons", "three independent pairs", "reasonable basic prompt", "Enhanced wins / Baseline wins / Ties", "Expression Fidelity", "N/A", "Medium Fidelity", "Visual Grammar Fidelity", "Scene Integrity", "Content Leakage", "Creative Value (Human Review Only)", "Target Model Compliance", "A — light paper illustration", "B — stylized 3D", "C — Dream Eye"), errors)
    if tests.is_file():
        body = tests.read_text(encoding="utf-8")
        cases = re.findall(r"^### Case (\d+) —", body, flags=re.MULTILINE)
        if len(cases) < 10:
            errors.append(f"Image-level regression requires >=10 cases; found {len(cases)}")
        required_cases = ("Paper Medium Override", "Mixed Medium", "Role vs Medium", "Medium Conflict", "Dream Eye Mechanism", "Mechanism Transfer", "Mechanism Drift Repair", "Medium Drift Repair", "Prompt Overload", "Cinematic Override")
        for case in required_cases:
            if case not in body:
                errors.append(f"Image-level regression missing case: {case}")

    if errors:
        print(f"Skill validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Skill validation passed: v2.5.0, {len(director_files)} directors, Story to Frame route, Dream Decode contracts, {len(cases)} image-level manual cases, README anchors, and local links.")
    print("Image generation and human scoring: NOT AUTOMATICALLY VERIFIED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
