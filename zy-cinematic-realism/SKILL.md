---
name: zy-cinematic-realism
description: Compile scene ideas or existing visual prompts into restrained, physically believable cinematic image prompts for GPT Image 2, Midjourney, Seedream 5.0 Pro, Nano Banana, or a model-neutral workflow. Use for cinematic AIGC creation, model routing or transcoding, continuity packs, prompt diagnosis, result repair, director/style/cinematography methods, one-variable remixes, and grounded creative shuffles.
---

<!--
Copyright (c) 2026 ZY / popopo-99
Project: 造梦师：AI时代电影视觉指南
SPDX-License-Identifier: CC-BY-NC-4.0
Source: https://github.com/popopo-99/zy-cinematic-realism
-->

# 造梦师 · ZY Cinematic Realism

Public edition: 《造梦师：AI时代电影视觉指南 v2.1.0》.

Build every result in this order:

`Scene Master → Creative Grammar → Model Compiler → Result Repair`

First decide what the image is, then how it is witnessed, and only then how to express it to a target model. One Scene Master may compile into multiple native model prompts.

## Mode Selection

Infer the mode from the request. Do not print a menu.

- **Create** — build a new cinematic scene and compile it for one target model.
- **Model Router** — recommend a model when the user is unsure.
- **Transcode** — preserve an existing scene while changing model-native expression.
- **Multi-model Pack** — compile one locked Scene Master for several models.
- **Continuity** — create a Continuity Bible, shot list, and controlled Shot Deltas.
- **Repair** — diagnose a generated result and produce a model-native repair instruction.
- **Prompt Check** — inspect an existing prompt without rewriting unless requested.
- **Director / Style / Cinematography** — apply a selected visual grammar.
- **Remix** — change one major variable while preserving every other invariant.
- **Creative Shuffle** — combine one causal story card, camera card, and style card.

## Target Model Gate

When the user wants a prompt ready for generation and the target model is unknown, ask only:

> 你准备在哪个模型里生成：GPT Image 2、Midjourney、Seedream 5.0 Pro、Nano Banana，还是其他？

Ask once only when the choice materially changes prompt structure. Do not ask when the user already named a model or the active conversation establishes it. If the user says to proceed, skip questions, use a model-neutral Scene Master prompt, and mention model-specific transcoding only when extra explanation is allowed.

If the user requests prompt-only output, return only the prompt requested: no interpretation, menu, follow-up, or unrelated adapter question.

Unqualified `Midjourney` or `MJ` routes to the current Midjourney V8.2 adapter. Treat an explicitly requested V6, V6.1, or V7 target as legacy and verify its compatibility rather than silently applying V8.2 behavior.

## Scene Master Invariants

Build or recover the Scene Master before applying style or model syntax. Preserve all user-fixed facts. A model adapter may change structure, order, density, native syntax, exclusions, reference-image wording, parameter form, or edit-instruction form. It may not silently change:

- character identity, scene, time, weather, story beat, or current action;
- visual center, camera witness position, spatial layers, or composition logic;
- primary light sources, core props, aspect ratio, or explicit restrictions.

For Transcode and Multi-model Pack, apply a Transcode Lock before writing any target prompt. `MODEL SYNTAX MAY CHANGE. SCENE LOGIC MAY NOT.`

## Core Create Workflow

1. Parse fixed facts: era, place, characters, event, mood, time, weather, aspect ratio, target model, references, and restrictions.
2. Choose a specific story beat with a narrative before, concrete current action, and implied next event. Prefer observed transition, waiting, aftermath, departure, private observation, or interrupted routine unless the user requests a climax.
3. Give each character physical blocking and a small action. Express emotion through posture, distance, gaze, silence, and object handling, not posing.
4. Construct foreground, midground, background, usable topology, causal traces of use, and materially consistent surfaces.
5. Place the camera at a physically possible witness position. Choose distance, height, focal behavior, boundary, and movement only as the story requires.
6. Map motivated sources, protected shadows, highlight surfaces, exposure behavior, and restrained color relationships.
7. Apply only the requested creative grammar. Do not let a card or director overwrite fixed facts.
8. Compile through the selected model adapter. Select scene-specific exclusions rather than pasting a generic negative list.
9. Apply anti-AI cleanup and run the quality checklist before answering.

## Reference Routing

Load only the branch required for the active mode.

- **Create:** [cinematic-principles.md](references/cinematic-principles.md), [camera-and-light.md](references/camera-and-light.md), [anti-ai-cleanup.md](references/anti-ai-cleanup.md), [model-routing.md](references/model-routing.md), the selected adapter, and [quality-checklist.md](references/quality-checklist.md). Read [negative-prompts.md](references/negative-prompts.md) when exclusions are needed.
- **Model Router:** [model-routing.md](references/model-routing.md) and [model-capability-matrix.md](references/model-capability-matrix.md).
- **Transcode / Multi-model Pack:** [prompt-compiler.md](references/prompt-compiler.md), [model-routing.md](references/model-routing.md), and only the source and target adapters needed.
- **Prompt Check:** [prompt-check.md](references/prompt-check.md), the target adapter when known, and [anti-ai-cleanup.md](references/anti-ai-cleanup.md) when cinematic realism is relevant.
- **Continuity:** [continuity-cards.md](references/continuity-cards.md), [prompt-compiler.md](references/prompt-compiler.md), and the target adapter.
- **Repair:** [result-repair.md](references/result-repair.md), the target adapter, and [continuity-cards.md](references/continuity-cards.md) for a series.
- **Director:** [director-routing.md](references/director-routing.md), [directors/index.md](references/directors/index.md), and one matching director file. For recommendations, also read [directors/recommendation-matrix.md](references/directors/recommendation-matrix.md) and load only two or three candidates.
- **Style:** [creative-cards.md](references/creative-cards.md) and [style-cards.md](references/style-cards.md).
- **Cinematography:** [cinematography-cards.md](references/cinematography-cards.md).
- **Remix:** [remix.md](references/remix.md), [prompt-compiler.md](references/prompt-compiler.md), and the target adapter.
- **Creative Shuffle:** [creative-shuffle.md](references/creative-shuffle.md), [style-cards.md](references/style-cards.md), and [cinematography-cards.md](references/cinematography-cards.md) when useful.
- **Examples:** read [examples.md](references/examples.md) only when calibration is genuinely useful.
- **Scaffold:** use [basic-prompt-template.md](assets/basic-prompt-template.md) only when a compact model-neutral Scene Master writing order is useful; the selected adapter still controls final syntax.

Model adapters:

- [GPT Image 2](references/models/gpt-image-2.md)
- [Midjourney V8.2](references/models/midjourney.md)
- [Seedream 5.0 Pro](references/models/seedream-5-pro.md)
- [Nano Banana family](references/models/nano-banana.md)

## Director Compatibility

Preserve the existing Director Four-Axis system. Use it only when the user names a director, requests a director method or comparison, or asks for a recommendation. Supported named directors remain mandatory strong/iconic mode. Follow `director-routing.md`, translate all four axes into scene-specific decisions, and never substitute a name or film title for camera, light, color/exposure, composition, space, and blocking. Do not copy a specific film shot.

## Output Contracts

- **Create:** `画面理解` → `[Target Model] Prompt` → target-native constraints or settings only when useful.
- **Transcode:** short `Scene Lock Summary` → `[Target Model] Prompt`; do not re-explain the concept.
- **Multi-model Pack:** one short Scene Lock → clearly different native prompts sharing the same invariants.
- **Prompt Check:** three to five high-impact `PASS / WEAK / RISK / CONFLICT` findings → Rewrite, Surgical Fix, or No Rewrite as requested.
- **Repair:** dominant failures → `CHANGE ONLY` → `PRESERVE EXACTLY` → target-native repair prompt.
- **Continuity:** Continuity Bible → Shot List → Shot Deltas → model-native prompts.
- **Remix:** Preserved → Changed axis → New Prompt.
- **Shuffle:** Combination → Story Card → Camera Card → Style Card → Final Prompt.

Do not expose hidden reasoning or internal locks unless the user requests them. Do not leave placeholders.

## Non-Negotiable Rules

- The frame must still work after removing `cinematic`, camera brands, film stock, focal-length badges, resolution claims, and grain.
- Prefer specific nouns, physical actions, causal traces, and source-based light over `masterpiece`, `epic`, `stunning`, `award-winning`, `8K`, or `highly detailed`.
- Do not invent decorative rim light, neon, fog, flare, shallow focus, damage, dirt, obstruction, or imperfection without a physical or narrative cause.
- Avoid poster, fashion-campaign, game-render, concept-art, and advertising logic unless requested.
- Do not invent model versions, API fields, parameter values, reference counts, strength ranges, or resolution limits. Frontend behavior may differ from the underlying model.
- Respect the user's requested language, format, model, aspect ratio, and output brevity.
