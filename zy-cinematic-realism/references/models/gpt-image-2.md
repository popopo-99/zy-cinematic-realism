<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# GPT Image 2 Adapter

- **Model:** GPT Image 2
- **Aliases:** GPT-Image-2, `gpt-image-2`
- **Verified date:** 2026-08-29
- **Official basis:** [model page](https://developers.openai.com/api/docs/models/gpt-image-2) and [image generation guide](https://developers.openai.com/api/docs/guides/image-generation)

## Best for

Structured natural-language production briefs, high-quality image generation, image-input workflows, and conversational generation or editing where explicit constraints must remain legible.

## Prompt density

Use complete, concrete sentences grouped by function. Keep one clear instruction per sentence or short paragraph. Dense visual clauses are acceptable only when their relationships remain explicit.

## Prompt structure

1. Task and grounded scene facts.
2. Story beat and current action.
3. blocking, object interaction, and physical space.
4. camera witness position, distance, height, and composition.
5. source-light map, exposure, color, and material response.
6. capture behavior and aspect-ratio intent.
7. integrated constraints and preserve rules.

## Generation strategy

Write a production brief that explains spatial and causal relationships. Prefer “the camera stands behind the parked car, with its roof cutting across the lower foreground” over a disconnected list of camera adjectives.

## Editing strategy

Identify the source image and state `Change only` and `Preserve exactly` in observable terms. Make the changed region, new physical state, and required light/perspective integration explicit. Do not claim pixel-level determinism.

## Reference-image strategy

Assign each image one role: identity, wardrobe, object, location, composition, material, or light. When several images are present, name their roles and resolve conflicts in favor of user-declared priority. Do not invent API attachment fields in a prose prompt.

## Text strategy

Quote exact visible wording, specify location, hierarchy, orientation, and material. Keep text requirements separate from decorative scene prose and do not promise perfect spelling.

## Negative / exclusion strategy

Integrate exclusions as direct constraints near the relevant instruction: “keep the parking garage ordinary and contemporary; do not introduce cyberpunk lighting or fantasy architecture.” Do not assume a separate negative-prompt field.

## Aspect ratio strategy

Describe the intended ratio and why its space matters. If API or frontend settings are requested, use only values verified in the active interface; do not infer them from this card.

## Parameter strategy

Do not append Midjourney-style flags or invent API fields. Offer API parameters only when the user asks for API usage and current official documentation has been checked.

## Strong at

Natural-language structure, high-fidelity image inputs, generation/editing workflows, explicit relationships, and preserve/change instructions.

## Common failure modes

Overlong briefs with repeated constraints; beautifying every surface; interpreting abstract mood as decorative lighting; identity or layout drift when reference roles are not assigned.

## Compilation rules

Expand compressed source prompts into clear causal prose without adding new creative facts. Fold the Avoid list into relevant constraints. Keep the Scene Master hierarchy visible but omit internal labels unless they improve execution.

## Repair rules

For a sound structure, use a short edit brief with `CHANGE ONLY` and `PRESERVE EXACTLY`. For a failed camera, story beat, or visual center, rebuild from the locked Scene Master and say which successful facts remain fixed.
