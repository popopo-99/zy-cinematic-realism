<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Prompt Check

Inspect before rewriting. Never use numeric scores, a “cinematic index,” or praise-word counting as the diagnosis.

## Status Labels

- **PASS** — the element is clear, compatible, and physically usable.
- **WEAK** — present but underspecified or unlikely to control the result.
- **RISK** — likely to produce drift, artificial polish, or model failure.
- **CONFLICT** — two instructions, syntaxes, or constraints cannot both hold.

## Inspection Dimensions

Check Story Beat, Character Action, Blocking, Physical Space, Camera Witness Position, Composition, Lighting Source Logic, Color Logic, Material Realism, Capture Texture, Anti-AI Logic, Continuity, Model Compatibility, Reference Roles, Constraint Conflict, and Prompt Redundancy.

Default to the three to five findings with the greatest effect on the image. Separate:

- **structural scene failures** — missing or contradictory story, action, space, camera, composition, or light;
- **model expression failures** — mixed syntax, unsupported parameters, unsuitable density, or weak reference/edit wording;
- **cosmetic symptoms** — generic praise words, excessive texture labels, or polish that follows from the deeper problem.

Do not diagnose “too many keywords” when the real failure is that no physical camera, story beat, or light hierarchy exists.

## Rewrite Gate

- “只检查” / “check only” → findings only; no rewrite.
- “帮我修” / “rewrite” → full corrected prompt through the target adapter.
- “尽量少改” / “surgical” → change only the minimum clauses required; list what remains preserved when explanation is allowed.

If the target model is unknown, diagnose model-neutral structure and label model compatibility as unknown. Do not block a check merely to ask for a model.
