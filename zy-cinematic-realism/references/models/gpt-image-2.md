<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# GPT Image 2.5 Adapter

- **Current baseline:** ChatGPT Images 2.5 / GPT-Image-2.5 family
- **Current aliases:** GPT Image, OpenAI image, ChatGPT 生图, GPT Image 2.5, Images 2.5
- **Legacy compatibility:** GPT Image 2, GPT-Image-2, `gpt-image-2`; keep this file path stable for existing links and installations.
- **Verified date:** 2026-09-09
- **Official basis:** [Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/), [image prompting and migration](https://developers.openai.com/api/docs/guides/image-prompting), [image generation](https://developers.openai.com/api/docs/guides/image-generation), [Flare model](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare), [Sunburst model](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst), and [Images in ChatGPT](https://help.openai.com/en/articles/11084440-im).

## Product and API boundary

ChatGPT Images 2.5 is the product-facing baseline in ChatGPT / Codex. This Skill produces visual plans and prompts; installation does not select an underlying image model or call an API model ID.

For API requests only, consider **GPT-Image-2.5 Flare** for fast, high-quality everyday generation and editing: it accepts text and image inputs and is the official default choice for most applications, with higher quality than GPT-Image-2 at substantially lower latency. Consider **GPT-Image-2.5 Sunburst**, currently described by OpenAI as its most capable image generation/editing model, when editing precision matters most in premium or production work; generation takes longer than Flare. These are dated task heuristics, not a permanent ranking. Do not emit API model IDs, quality fields, pricing, or endpoint syntax unless the user asks for API usage; verify supported parameters then.

## Migration from GPT Image 2

Test existing validated GPT Image 2 prompts unchanged on GPT Image 2.5 first. Do not rewrite a working prompt merely because the model version changed. Preserve the prompt, reference images, scene facts, aspect-ratio intent, and constraints for the first comparison whenever practical. For API comparisons, also hold supported request settings, dimensions, and output format constant; evaluate quality settings before rewriting prose.

Only revise after evaluation identifies a specific failure: spatial misunderstanding, identity drift, unwanted beautification, incorrect edit scope, weak material response, constraint failure, or composition drift. Then repair only the failed variable, preserving successful facts. Inspect individual edits and the complete multi-turn sequence; improved preservation is not pixel-level determinism.

Do not rewrite for the sake of version numbers. The existing compiler contract still applies: `MODEL SYNTAX MAY CHANGE. SCENE LOGIC MAY NOT.`

## 2.5 capability update

OpenAI reports sharper details, more natural lighting, richer textures, improved reference-subject fidelity, more precise edits, and better preservation across editing turns. Image generation is faster, with latency reduced by **up to 50% compared with Images 2.0**. The percentage concerns latency, not image quality; inspect actual results for the current task.

## Best for

Structured natural-language production briefs, high-quality image generation, image-input workflows, and conversational generation or editing where explicit constraints must remain legible.

## Prompt density

Use complete, concrete sentences grouped by function. Keep one clear instruction per sentence or short paragraph. Dense visual clauses are acceptable only when their relationships remain explicit. No special 2.5 syntax is required: use readable natural language, concrete observable descriptions, explicit action, spatial relationships, camera position, source-based light, material response, and constraints. Sections may help complex tasks; JSON, tags, and fixed templates are optional. Do not introduce `masterpiece`, `8K`, `award-winning`, or `hyper detailed` as new quality rules.

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

Identify the source image and state `CHANGE ONLY` and `PRESERVE EXACTLY` in observable terms. Name the changed region and new physical state; preserve identity, geometry, requested composition, lighting relationships, and unaffected objects. Integrate the change with the existing light and perspective.

Use **one meaningful variable per edit** across turns and repeat the critical preserve rules, using the previous accepted output as the next input. Closely related changes explicitly requested together may share one edit; do not expand scope to demonstrate capability. Follow Prompt Doctor, One Variable Remix, and the Continuity Bible. Inspect each result; do not claim pixel-level determinism.

## Reference-image strategy

Assign each image an explicit role or a clearly scoped combination: identity, wardrobe, object, location, composition, material, or light. When several images are present, name their roles and resolve conflicts in favor of user-declared priority. For example: Image A → identity; Image B → wardrobe; Image C → location; Image D → composition; Image E → material / light. These are brief-level roles, not API attachment parameters. Do not assume the model can infer each image's responsibility, and do not invent API attachment fields in a prose prompt.

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
