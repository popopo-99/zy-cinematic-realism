<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Seedream 5.0 Pro Adapter

- **Model:** Seedream 5.0 Pro
- **Aliases:** Seedream 5 Pro, Seedream; 即梦 only when context identifies this model
- **Verified date:** 2026-08-29
- **Official basis:** [product page](https://seed.bytedance.com/en/seedream5_0_pro) and [official launch article](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro)

## Best for

Spatially explicit creative briefs, realistic image generation, multilingual and text-rich layouts, multi-source composition, and interactive editing when the frontend exposes annotations or regional controls.

## Prompt density

Use a clear creative brief with explicit subject positions, visual hierarchy, source relationships, and material behavior. Moderate detail works better than either keyword fragments or repetitive prose.

## Prompt structure

1. Intended image and fixed facts.
2. story beat, characters, action, and blocking.
3. spatial layout and visual center using concrete relative positions.
4. camera witness position and compositional hierarchy.
5. source light, exposure, color, and physical material response.
6. visible text or reference roles when applicable.
7. explicit exclusions and preserve/change rules.

## Generation strategy

Write a spatial production brief. Express relative positions, occlusions, scale, and foreground/midground/background directly. Keep the cinematic premise grounded before adding capture texture.

## Editing strategy

When the active interface provides points, boxes, masks, sketches, or annotations, tie each edit to the supplied region. State what changes, what remains untouched, and how new material/light must integrate. Without such controls, use a general edit instruction and avoid claims of pixel-level precision.

## Reference-image strategy

Assign roles to the base image and each auxiliary image. Identify which input controls layout, identity, wardrobe, object, material, or lighting. For fusion, state the target position and integration requirements. Do not invent reference-count limits.

## Text strategy

Quote exact wording and describe language, hierarchy, placement, orientation, and layout direction. Keep narrative imagery and dense information-layout requests structurally separate.

## Negative / exclusion strategy

Use direct exclusions after positive spatial instructions. Prefer specific failure prevention such as “keep every parking level ordinary; no cyberpunk conversion” over generic quality negatives.

## Aspect ratio strategy

State the desired ratio and map composition to it. Use interface parameters only when the user identifies the interface and the setting is verified.

## Parameter strategy

Do not invent API fields, coordinate syntax, annotation formats, strengths, reference limits, or resolution values. Use the controls visibly supplied by the user's frontend.

## Strong at

Spatial reasoning, annotated/local editing, multi-image fusion, text-rich layout, multilingual input/output, and physically descriptive image briefs.

## Common failure modes

Confusing a prose request with an unavailable regional tool; overloading one prompt with cinematic scene and infographic demands; reference-role conflict; unnecessary commercial polish.

## Compilation rules

Translate the Scene Master into a concise spatial brief. Keep positions, visual center, topology, source map, and material response explicit. Do not import Midjourney parameter syntax or GPT API language.

## Repair rules

For a localized issue, reference the supplied annotation or region and use preserve/change boundaries. For structural failure, rebuild the spatial brief from the Scene Master. Preserve identity, successful materials, and topology unless they are the diagnosed failure.
