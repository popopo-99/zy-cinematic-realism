#!/usr/bin/env python3
"""Validate the v2.3.0 Skill and its Dream Decode contracts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import validate_director_library as base


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "zy-cinematic-realism"
REF = SKILL / "references"
EXPECTED_ANCHORS = (
    "dream-decode", "core-workflows", "model-comparison", "model-router",
    "quick-start", "continuity", "prompt-doctor", "creative-grammar",
    "director-method", "input-card", "install-codex", "use-chatgpt",
    "repository-structure", "license",
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
        if ids.count(anchor) != 1 or links.count(anchor) != 1:
            errors.append(f"{path.name}: expected one explicit anchor and one TOC link for #{anchor}.")
    for link in links:
        if link not in ids:
            errors.append(f"{path.name}: TOC link #{link} has no explicit anchor.")


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
        for stale in ("v2.3.0-dev", "unreleased", "未发布", "local development", "本地开发版"):
            if stale in current:
                errors.append(f"{path.relative_to(ROOT)}: current release content contains '{stale}'.")
        if re.search(r"[A-Z]:\\Users\\", body):
            errors.append(f"{path.relative_to(ROOT)}: local Windows user path must not be published.")

    require(SKILL / "SKILL.md", ("name: zy-cinematic-realism", "v2.3.0", "medium-router.md", "dream-decode.md", "prompt-compiler.md", "USER-LOCKED", "OPEN", "optional `表达机制`"), errors)
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
    print(f"Skill validation passed: v2.3.0, {len(director_files)} directors, Dream Decode contracts, {len(cases)} image-level manual cases, README anchors, and local links.")
    print("Image generation and human scoring: NOT AUTOMATICALLY VERIFIED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
