---
name: zy-cinematic-realism
description: Turn brief scene ideas into production-ready English prompts for restrained, physically believable cinematic stills or video keyframes. This skill is publicly presented as 造梦师：AI时代电影视觉指南. Use when users ask for 电影感 or cinematic AIGC prompts, want to reduce the artificial AI look, need a story beat, camera position, composition, motivated lighting, film texture, and scene-specific negative prompts, or want an existing visual prompt diagnosed and rewritten as a believable movie frame.
---

<!--
Copyright (c) 2026 ZY / popopo-99
Project: 造梦师：AI时代电影视觉指南
SPDX-License-Identifier: CC-BY-NC-4.0
Source: https://github.com/popopo-99/zy-cinematic-realism
-->

# 造梦师 · ZY Cinematic Realism

Public edition: 《造梦师：AI时代电影视觉指南 v1.1》

Transform a simple idea into a frame that feels observed inside an ongoing story. Build narrative, physical space, camera logic, and motivated light before adding lens or film terminology.

## Workflow

1. Parse the user's fixed facts: era, place, characters, event, mood, time, weather, aspect ratio, model, and restrictions.
2. Preserve supplied facts. Infer ordinary production details when they are missing. Ask one concise question only when a missing choice would materially change the result; otherwise proceed with restrained defaults.
3. Identify the emotional subject beneath the literal subject. State what happened immediately before the frame and what may happen next.
4. Select a specific story beat. Prefer anticipation, waiting, aftermath, departure, private observation, or interrupted routine over a heroic climax unless the user requests one.
5. Give each character a small, concrete action. Express emotion through posture, distance, gaze, handling of objects, and silence. Do not direct characters to pose for the camera.
6. Build a usable physical location with foreground, midground, background, age, weather or air, wear, and two to four story-relevant traces of use.
7. Place the camera somewhere a real camera could be. Specify height, distance or shot size, focal length only when useful, and one justified obstruction, reflection, or spatial boundary when appropriate.
8. Compose observationally. Use off-center placement, negative space, partial occlusion, asymmetry, and environmental scale only when they support the story.
9. Motivate every important light source from the location. Describe primary source, secondary source, shadow placement, highlight placement, and a restrained color relationship.
10. Add capture texture last: natural exposure, soft highlight roll-off, believable grain, restrained halation, lens falloff, focus imperfection, or motion blur. Use only effects supported by the scene.
11. Select 10-20 scene-specific Avoid terms. Remove generic terms that do not address a likely failure mode.
12. Run the final quality check in [references/quality-checklist.md](references/quality-checklist.md). Rewrite any weak section before answering.

## Reference Routing

- Read [references/cinematic-principles.md](references/cinematic-principles.md) when building or diagnosing story, environment, and composition.
- Read [references/camera-and-light.md](references/camera-and-light.md) when selecting camera placement, focal behavior, aspect ratio, or motivated light.
- Read [references/negative-prompts.md](references/negative-prompts.md) before composing the Avoid section.
- Read [references/anti-ai-cleanup.md](references/anti-ai-cleanup.md) before finalizing every output. It is a global cleanup layer, not a substitute for director rules.
- Read [references/examples.md](references/examples.md) only when calibration through examples would improve the result.
- Read [references/director-routing.md](references/director-routing.md) only when the user explicitly names a director, requests a director method, asks to compare director directions, or asks for a director recommendation. Then use [references/directors/index.md](references/directors/index.md) to read the matching reference.
- For a single named director, read director-routing.md, the index, and exactly one matching director reference. For a requested comparison or recommendation, read only the two or three candidate references needed. For an explicit mix, read no more than the primary and secondary director references.
- Do not load the Director Lens Library when no director reference is requested. Use one director by default; use one primary and one secondary director only when the user explicitly asks to mix them.
- Use [assets/basic-prompt-template.md](assets/basic-prompt-template.md) as the output scaffold; replace every placeholder and remove unused lines.

## Director and Anti-AI Checks

When a director reference uses strength `strong` or `iconic`, its signature image grammar must visibly affect at least six of these nine dimensions: story beat, character blocking, camera height, camera distance or lens behavior, movement grammar, light and contrast, color behavior, depth-of-field strategy, and texture or capture character. If the result remains interchangeable with the baseline after removing the name, rebuild it.

When strength is `strong` or `iconic`, do not preserve the baseline shot design by default. Preserve the user's fixed story facts, but allow the director method to reselect the exact temporal beat, visual center, information hierarchy, subject scale, and spatial relationship.

A director variation fails differentiation when it preserves the same dominant action, focal object relationship, camera axis, and lighting hierarchy as the baseline while changing only crop, focal depth, color, or descriptive language. For `iconic`, fundamentally reselect at least three of the following rather than lightly adjusting them: exact moment before, during, or after the stated action; dominant narrative subject; camera axis and physical witness position; subject scale and completeness; primary light hierarchy; information completeness; movement versus stillness; depth and focus behavior.

Fixed facts must remain present in the scene, but not every fixed fact must be fully visible, equally sharp, or placed at the compositional center.

Before answering, check that surfaces are not waxy or plastic, not every object is equally legible, shadows and falloff retain natural dead areas, and wear looks lived-in rather than designed. Keep the scene physically believable.

## Explicit Director Style Anchors

When the user names a director without a strength, default to `iconic`, publicly labeled `强烈`. Treat legacy `strong` input as `iconic`. Lower strength only when the user explicitly asks for a light reference, restraint, one borrowed method, no obvious director effect, a name-free prompt, or a platform that does not allow director names. When no director is named, keep the original cinematic realism workflow and do not add director or film anchors.

For `subtle`, the Final Prompt may include only the director name and no film anchors; translate only a few visual dimensions. For `clear`, include the standard English director name and optionally one or two representative films; the director must visibly affect story beat, camera, light, and composition. For `iconic` / `强烈`, include the standard English director name and two or three representative films; its image grammar must lead exact story beat, visual center, blocking, camera axis, focal behavior, movement grammar, light and contrast, color response, depth of field, and capture texture.

For every named-director request, names and film anchors are model-facing signals, not a replacement for scene-specific visual grammar. Put the anchor immediately after grounded scene facts and before detailed camera design; do not append it as an unrelated ending. Preserve the user's original characters, event, era, and location unless the user explicitly asks to recreate a particular film scene.

When a user explicitly requests a name-free prompt, says that their platform does not allow director names, or asks for a compatibility version, omit names and titles. Otherwise, output one anchored version rather than two competing variants.

## Output Contract

Default to the following order:

1. `画面理解` - a concise Chinese summary of the story beat and key production choices. Use the user's language instead when it is clearly preferred.
2. `Final Prompt` - one complete, fluent English prompt. Integrate concrete scene information instead of listing abstract praise words.
3. `Avoid` - a compact English, comma-separated negative prompt tailored to the scene.

Do not expose hidden reasoning. Do not leave placeholders. Do not repeat the user's brief verbatim as the entire result.

If the user requests only a prompt, omit the interpretation and return `Final Prompt` plus `Avoid`. If a target model is named, adapt syntax and length without changing the scene logic. If the user supplies an existing prompt, briefly identify its strongest failure modes, then provide a complete rewrite.

## Non-Negotiable Rules

- Make the frame work after removing words such as `cinematic`, `35mm`, `Kodak`, `ARRI`, `anamorphic`, and `film grain`.
- Do not use `photorealistic` as a default quality badge. Prefer an observed live-action frame, a grounded film frame, or a physically believable captured moment; retain `photorealistic` when the user explicitly requests it.
- Prefer specific nouns and observable actions over `masterpiece`, `epic`, `stunning`, `award-winning`, `8K`, or `highly detailed`.
- Keep period, weather, wardrobe, architecture, props, light, and capture medium internally consistent.
- Do not invent decorative rim lights, neon, fog, lens flare, or shallow depth of field without a physical reason.
- Do not force damage, dirt, occlusion, or imperfection into every frame. Use them only when the location and story support them.
- Avoid poster, fashion editorial, game render, concept-art, and commercial-advertising logic unless explicitly requested.
- Director references are optional and must not override the user's era, place, character, event, weather, or composition requirements.
- Translate a director method into observable story, action, camera, light, and spatial decisions; preserve physical plausibility and motivated light.
- Do not use `in the style of` or `directed by` as a substitute for a scene-specific director translation.
