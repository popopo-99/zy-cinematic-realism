#!/usr/bin/env python3
"""Statically validate the v2.7.0 candidate, resource routes, and retained contracts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import validate_director_library as base
import validate_camera_language as language


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
    ids = re.findall(r'<a id="([a-z0-9-]+)"></a>', body)
    links = re.findall(r"\[[^\]]+\]\(#([a-z0-9-]+)\)", body)
    for anchor in EXPECTED_ANCHORS:
        if ids.count(anchor) != 1:
            errors.append(f"{path.name}: expected one explicit anchor for #{anchor}.")
    for link in links:
        if link not in ids:
            errors.append(f"{path.name}: local navigation #{link} has no explicit anchor.")
    for duplicate in {item for item in ids if ids.count(item) > 1}:
        errors.append(f"{path.name}: duplicate anchor #{duplicate}.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-sparse", action="store_true", help="Accept referenced files explicitly omitted by the Git sparse-checkout index.")
    args = parser.parse_args()
    errors: list[str] = []
    director_files = base.validate_directors(errors)
    base.validate_index(director_files, errors)
    base.validate_signature_and_versions(errors)
    base.validate_markdown_links(errors, allow_sparse=args.allow_sparse)
    base.validate_dream_decode_terminology(errors)
    language.validate_camera_language(errors)
    for name in ("README.md", "README_EN.md"):
        validate_readme_toc(ROOT / name, errors)
    for path in (ROOT / "README.md", ROOT / "README_EN.md", ROOT / "CHANGELOG.md", ROOT / "RELEASE_NOTES.md", SKILL / "SKILL.md"):
        body = path.read_text(encoding="utf-8")
        current = body.split("\n---\n", 1)[0] if path.name == "RELEASE_NOTES.md" else body
        # Release candidates may truthfully state that they are not published.
        # Reject stale development identities, not accurate publication status.
        for stale in ("v2.6.0-dev", "local development", "本地开发版"):
            if stale in current:
                errors.append(f"{path.relative_to(ROOT)}: current release content contains '{stale}'.")
        if re.search(r"[A-Z]:\\Users\\", body):
            errors.append(f"{path.relative_to(ROOT)}: local Windows user path must not be published.")

    require(SKILL / "SKILL.md", ("name: zy-cinematic-realism", "v2.7.0", "medium-router.md", "dream-decode.md", "prompt-compiler.md", "USER-LOCKED", "OPEN", "optional `表达机制`", "story-visual-development.md"), errors)
    story_path = REF / "story-visual-development.md"
    if not story_path.is_file():
        errors.append("Missing story visual development resource.")
    for path in (REF / "story-source-ledger.md", SKILL / "tests" / "story-to-frame.md", SKILL / "tests" / "story-art-development.md", ROOT / "docs" / "titanic-story-to-frame.md", ROOT / "docs" / "last-photo-art-development.md", ROOT / "docs" / "behavior-check-art-development-v2.5.md", ROOT / "docs" / "validation-v2.5.md"):
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
        require(path, ("v2.6.0", "CC BY-NC 4.0"), errors)
        if path.is_file() and re.search(r"\]\((?:\.\./)?(?:zy-cinematic-realism/)?references/", path.read_text(encoding="utf-8")):
            errors.append(f"{name}: basic chat rules depend on external reference files.")
    for path in (ROOT / "docs" / "getting-started.md", ROOT / "docs" / "getting-started_EN.md"):
        require(path, ('<a id="install-codex"></a>', '<a id="use-chatgpt"></a>', "v2.6.0"), errors)
    metadata = SKILL / "agents" / "openai.yaml"
    require(metadata, ("$zy-cinematic-realism", "model-native", "plain-text image prompt"), errors)
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

    # Asset resources are checked structurally here; model behavior is recorded separately.
    asset_reference = REF / "asset-pack.md"
    if not asset_reference.is_file() or "references/asset-pack.md" not in (SKILL / "SKILL.md").read_text(encoding="utf-8"):
        errors.append("Asset Pack reference must exist and be discoverable from the entry.")
    for resource in (SKILL / "tests" / "asset-pack.md", ROOT / "docs" / "validation-v2.6.md", ROOT / "docs" / "behavior-check-v2.6.md", ROOT / "docs" / "last-bus-testimony-asset-pack.md"):
        if not resource.is_file():
            errors.append(f"Missing Asset Pack resource: {resource.relative_to(ROOT)}")
    asset_tests = SKILL / "tests" / "asset-pack.md"
    if asset_tests.is_file():
        identifiers = re.findall(r"^## (AP\d{2}) —", asset_tests.read_text(encoding="utf-8"), re.MULTILINE)
        if identifiers != [f"AP{number:02d}" for number in range(1, 9)]:
            errors.append("Asset behavior specifications must retain AP01–AP08 in order.")

    # These checks establish resource presence and links, not runtime behavior.
    for name in ("capture-design.md", "equipment-library.md", "cinema-shot-library.md"):
        require(REF / name, ("Jury",), errors)
        require(SKILL / "SKILL.md", (f"references/{name}",), errors)
    require(REF / "models" / "seedream-5-5.md", ("Seedream 5.5", "2026-11-17", "seed.bytedance.com", "Scene Master"), errors)
    require(REF / "model-routing.md", ("models/seedream-5-5.md", "models/seedream-5-pro.md"), errors)
    require(REF / "capture-design.md", ("Camera / Viewpoint", "USER-LOCKED", "OPEN", "JSON"), errors)
    require(REF / "guided-capture-workflow.md", ("Scene Master", "Capture Design", "USER-LOCKED", "OPEN", "jury-json-brief.md"), errors)
    require(REF / "jury-json-brief.md", ("Jury", "jury-json-brief-still.schema.json", "60620023de0ebecc05478df21478675ef2019f7802a371f432eae7cf70a05832"), errors)
    require(SKILL / "SKILL.md", ("references/guided-capture-workflow.md", "references/jury-json-brief.md"), errors)
    schema_path = SKILL / "assets" / "jury-json-brief-still.schema.json"
    if schema_path.is_file():
        try:
            json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Jury still Schema contains invalid JSON: {exc}")
    else:
        errors.append("Missing Jury still Schema.")
    require(SKILL / "tests" / "guided-capture.md", ("**User**", "**Expected**", "**Failure**"), errors)
    for name in ("capture-design.md", "capture-design-credits.md"):
        require(ROOT / "docs" / name, ("v2.7.0",), errors)

    if errors:
        print(f"Skill validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Static Skill validation passed: v2.7.0 candidate, {len(director_files)} directors, retained Story/Asset/Dream Decode resources, Capture Design, dynamic camera-language contracts and guided Capture/Jury still resources, Seedream adapters, {len(cases)} preserved image-level manual specifications, README anchors, and local links.")
    if args.allow_sparse:
        print("Sparse checkout mode: absent reference targets are accepted only when marked skip-worktree in the Git index.")
    print("Image generation and human scoring: NOT AUTOMATICALLY VERIFIED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
