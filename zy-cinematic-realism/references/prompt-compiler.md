<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Prompt Compiler

## Contract

`MODEL SYNTAX MAY CHANGE. SCENE LOGIC MAY NOT.`

The Scene Master is the source of truth for scene facts. It is an internal structure unless the user explicitly requests it. When Dream Decode is active, Decoded Visual Grammar is a separate compiler input; do not merge reference-derived style behavior into scene facts.

## Scene Master Schema

- **Fixed Facts:** user-supplied era, place, people, event, mood, time, weather, ratio, model, and restrictions.
- **Story:** Story Beat, Narrative Before, Current Action, Implied Next.
- **Characters:** Character Identity, Character Blocking, Object Interaction.
- **Space:** Environment, Foreground, Midground, Background, Visual Center.
- **Camera / Viewpoint:** Witness Position for photography or viewpoint, framing, spatial arrangement, and form logic for other media; distance, height, and focal behavior only when relevant.
- **Light / Value:** Source Light Map and exposure for photographic media, or value, pigment, shading, and graphic-light behavior for other media.
- **Surface / Rendering:** Material Behavior and medium-appropriate capture, mark-making, edge, paper, texture, or rendering behavior.
- **Delivery:** Aspect Ratio, Visible Text, Reference Roles, Must Preserve, Allowed Variation, Likely Failure Modes.

Do not force absent or irrelevant fields into the visible prompt. Resolve only what the scene needs.

For visual decisions, distinguish **USER-LOCKED** explicit user choices from **OPEN** unspecified or system-completed defaults. Resolve OPEN camera/viewpoint, composition, subject scale, light, framing, perspective, blocking, aspect ratio, and visual-center decisions against authorized reference Hybrid Decisions before final locking. `USER-LOCKED > reference-derived Hybrid Decision > system-generated default`. This does not create a second source of scene facts; the resolved Scene Master is canonical.

## Dream Decode Inputs

When visual references are used for analysis or transfer, compile from two coordinated structures:

```text
Scene Master
+ Decoded Visual Grammar
  - Reference Roles
  - Primary Medium + Medium Constraints / Avoid
  - Expression Mechanism (optional)
  - Core Visual Rules (full 5–8 archived; Active Core Rules 3–5 for final prompt)
  - Transfer Scope
  - Hybrid Decisions: Preserve / Adapt / Release
  - Anti-cliches
```

The Scene Master continues to own characters, event, action, environment, story, topology, camera requirements, light facts, props, time, weather, aspect ratio, and restrictions. Decoded Visual Grammar supplies reference-derived color, exposure, material, texture, medium, rendering/capture, composition tendencies, spatial rhythm, and other transferred behavior.

Do not add every decode field to the Scene Master schema. If the two structures conflict, explicit user intent and Scene Master fixed facts win.

## Compiler Priority Gate / 编译优先级闸门

Resolve in strict order, before target-model syntax:

1. **Scene Master USER-LOCKED Facts / Decisions** — explicit user choices for characters, action, setting, story, visual decisions, ratio, and restrictions.
2. **User Explicit Reference Roles** — assigned authority and exclusions; no inferred role may override them.
3. **Primary Medium / Medium Constraints** — the authorized style reference's medium controls image-making logic unless the user explicitly requests realistic / cinematic reinterpretation.
4. **Expression Mechanism (optional)** — preserve an observed subject–event relationship; skip this layer entirely when no distinct mechanism exists.
5. **Active Core Rules (3–5)** — select from the full five to eight Core Visual Rules for the current scene.
6. **Transfer Scope** — Strong / Conditional / Do Not Transfer, with Hybrid Decisions resolved against the new scene.
7. **Relevant supporting Visual Grammar** — only details needed to execute higher-priority decisions.
8. **Scene-specific Reject / Anti-clichés** — three to five high-value exclusions when useful, not a universal negative list.
9. **Target-model formatting** — native syntax and controls without changing upstream logic.

This is an authority order, not an instruction to place nine headings in the final prompt. Step 1 protects USER-LOCKED facts and decisions; OPEN visual decisions may be filled or adapted by authorized Hybrid Decisions ahead of system defaults. A reference's non-photographic medium is not silently converted to photography, live-action, glossy CG, or generic concept art by the Skill's cinematic realism defaults. A model's inability to follow a correct prompt is a target-model compliance problem, not proof of a bad decode.

## Decode Card Input Selection

Do not paste the full Dream Decode or Decode Card into a target prompt. Select compiler input in this order:

1. Scene Master USER-LOCKED facts and decisions, then explicit Reference Roles; resolve OPEN visual decisions against authorized Hybrid Decisions before applying system defaults.
2. One Primary Medium and identity-critical Medium Constraints; include one primary Expression Mechanism with at most two or three related execution points **only when observed**. Otherwise skip it without substitution.
3. Select **three to five Active Core Rules** from the full five to eight Core Visual Rules. Prefer rules that establish medium identity or an observed mechanism, matter directly to the new Scene Master, have high-weight Strong Transfer, or whose absence would visibly lose the reference. Deprioritize archival-only or irrelevant rules, Conditional Rules that conflict with USER-LOCKED intent, and duplicates already expressed by Medium Constraints. Preserve the full set in the Decode Card for continuity and repair. Resolve Transfer Scope against the new scene.
4. Only supporting Visual Grammar relevant to the new scene; three to five high-value scene-specific rejects when useful.

If the prompt is overloaded, remove low-impact supporting grammar, redundant adjectives, and low-value rejects first. Do not sacrifice USER-LOCKED facts, medium identity, an observed mechanism, or the selected Active Core Rules to keep ornamental detail.

Source Residue, archival explanation, optional naming, Drift Warnings, and unused Visual Grammar fields are not prompt payload. They remain available for contamination checks, continuity, and repair.

## Transcode Lock

Before changing models, extract and lock:

`Character · Scene · Story Beat · Action · Visual Center · Camera Position · Composition · Light Sources · Props · Time · Weather · Aspect Ratio · Restrictions`

If the source is ambiguous, preserve the most direct reading. If two clauses conflict, state the single structural conflict briefly. Faithful conversion preserves it; optimization requires user intent or an explicit request to fix.

For GPT Image 2 → GPT Image 2.5 migration, apply the [unchanged-prompt-first rule](models/gpt-image-2.md) before any reordering or expansion. Keep the validated prompt and references for the first comparison; use the compilation or repair pass only when requested or when evaluation identifies a specific failure. Scene Master facts stay locked.

## Compilation Pass

1. Normalize the source into a Scene Master without adding a new concept.
2. Mark explicit user visual decisions USER-LOCKED and unspecified system defaults OPEN; allow authorized Hybrid Decisions to fill or adapt OPEN fields before the final lock.
3. When Dream Decode is active, run the Compiler Priority Gate after Reference Roles, per-reference medium analysis, optional Expression Mechanism, and Hybrid Decisions are resolved; select three to five Active Core Rules.
4. Load the target adapter only after the lock exists.
5. Reorder and compress information according to the adapter.
6. Translate exclusions, references, editing instructions, ratio, and parameters into target-native form.
7. Compare the compiled prompt against both the lock and Transfer Scope. Restore any drift before output.

Dream Decode preflight:

1. **Medium Drift Risk:** did the prompt replace the authorized Primary Medium with photography, generic CG, or a different making logic?
2. **Mechanism Drift Risk:** only if a distinct mechanism was observed, is the Abnormal Event still coupled to the intended subject or relationship?
3. **Source Residue Leak:** did a person, wardrobe, object, location, brand, text, architecture, or event leak from a visual-grammar reference?
4. **Reference Role Conflict:** does every image obey its explicit or conservatively inferred authority, including medium authority?
5. **Conditional Transfer Misuse:** were Hybrid Decisions adapted or released where literal inheritance would break the new scene?
6. **Scene Intent Damage:** are USER-LOCKED facts, action, space, and requested composition intact, while reference logic had a chance to fill OPEN decisions?
7. **Generic Cinematic Override:** did realism defaults erase a non-photo medium?
8. **Generic Concept Art Override:** did an undifferentiated concept-art / game-render look erase specific medium constraints?
9. **Prompt Overload:** did compilation paste the full Decode Card or too much low-value grammar? Remove low-priority material first.

Native shapes:

- **Midjourney V8.2:** concise, concrete natural visual description optimized for current V8.2 prompt understanding, preserving story, spatial, camera, light, material, and restriction relationships; append only request-relevant supported native parameters.
- **ChatGPT Images 2.5 / GPT Image 2.5:** structured natural-language production brief with integrated constraints; explicit GPT Image 2 targets retain legacy compatibility.
- **Seedream 5.0 Pro:** clear spatial creative brief with explicit relationships and edit regions when supplied.
- **Nano Banana:** direct conversational generation or editing instruction with explicit preserve/change language.

For Midjourney, decide between ordinary Imagine/generation and the V8.2 Edit Model before compiling. An existing-image change, selected-area repair, perspective change with reference preservation, or multi-reference recombination is an Edit Model task, not merely a shorter Imagine prompt. Because V8.2 is the current default target, omit `--v 8.2` unless the user requests a Discord-complete or version-locked prompt, or the workflow must prevent version drift.

## Multi-model Pack

Build one Scene Master once. When present, reuse the same Primary Medium, optional Expression Mechanism, full Core Visual Rules, scene-selected Active Core Rules, Transfer Scope, and Decoded Visual Grammar. Compile each target independently; do not translate one target prompt into the next. The prompts should differ visibly in native shape while their locked facts and visual rules remain identical. Always use `Scene Master + optional Decoded Visual Grammar → target-specific adapter`; never chain `GPT Image → Midjourney → Seedream` or any prompt-to-prompt translation. An unchanged OpenAI migration baseline does not require cosmetic differences.

## Output

For Transcode, show only a short Scene Lock Summary and the target prompt. Do not re-pitch the creative idea. Omit the summary when the user requests prompt-only output.
