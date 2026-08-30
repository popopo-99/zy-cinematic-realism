<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Nano Banana Family Adapter

- **Model:** Nano Banana family
- **Aliases:** Nano Banana, Nano Banana 2, Nano Banana 2 Lite, Nano Banana Pro, named Gemini image model IDs
- **Verified date:** 2026-08-29
- **Official basis:** [Google image generation guide](https://ai.google.dev/gemini-api/docs/image-generation)

## Best for

Conversational image generation and editing, rapid iteration, multimodal reference workflows, and—depending on the selected family member—multi-reference consistency, text rendering, or higher-precision production.

## Family routing

Do not treat the family as one fixed capability set. Use the exact member named by the user or exposed by the frontend. Current official guidance distinguishes speed-oriented Lite, generalist Nano Banana 2, precision-oriented Pro, and the legacy Nano Banana model. Verify current names and availability before giving API-specific advice.

## Prompt density

Use direct natural-language instructions. State the desired result first, then the scene relationships, then preserve/change and exclusions. Avoid both telegraphic keyword chains and long repeated briefs.

## Prompt structure

1. Generate or edit task.
2. grounded scene, story beat, and action.
3. character blocking and reference roles.
4. physical space, camera witness position, and visual center.
5. source light, color, materials, and capture behavior.
6. exact text or layout when needed.
7. preserve/change constraints.

## Generation strategy

Use conversational but observable instructions. Explain where subjects and objects are relative to one another and how the camera shares the space. Select the family member based on the real task, not on a universal quality ranking.

## Editing strategy

State `Change only` and `Keep unchanged` in concrete visual terms. Mention the supplied base image and any reference-role images. Require new content to inherit the base perspective, source light, grain/noise character, and material response where appropriate.

## Reference-image strategy

Assign one role per image and specify priority when roles overlap. Multi-reference capability varies by family member; do not assume the fastest member is optimized for complex reference sets or long sequential editing.

## Text strategy

Quote exact wording and define placement, hierarchy, language, orientation, and material. Choose a member suited to text or production precision when the user has access to it; do not promise perfect rendering.

## Negative / exclusion strategy

Use direct constraints within the instruction. Avoid unsupported negative-prompt syntax and do not append Midjourney flags.

## Aspect ratio strategy

Describe the intended frame and use only ratio controls confirmed in the active frontend or current API documentation.

## Parameter strategy

Do not invent model IDs, API fields, reference counts, output resolutions, or limits. When API syntax is requested, verify the selected family member against current official documentation.

## Strong at

Conversational multimodal iteration; generation and editing; model-dependent multi-reference, text, and consistency workflows.

## Common failure modes

Treating all family members as equivalent; vague preserve requests; long sequential edits that accumulate drift; unassigned reference roles; using a speed model for a complex production task without checking fit.

## Compilation rules

Turn the Scene Master into a direct instruction. Keep the base scene intact and describe relationships explicitly. Use the selected member's documented name only when known; otherwise label the prompt for the Nano Banana family without inventing an ID.

## Repair rules

Prefer a concise preserve/change edit instruction. For series work, restate only the relevant Continuity Bible locks and current Shot Delta. If the structure failed, regenerate from the Scene Master rather than layering additional adjectives.
