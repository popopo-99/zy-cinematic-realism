<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Result Repair — Prompt Doctor

Use this mode when the user provides or describes a generated result. Diagnose the image-result gap, not only the wording of the original prompt.

## Dominant Failures

Choose at most three failures from:

`Story · Blocking · Space · Camera · Composition · Light · Material · Continuity · Reference Drift · Model Syntax`

Prefer causes over symptoms. “Commercial look” may come from posing, centered scale, equal highlight treatment, clean visibility, and a privileged camera position; do not treat it as a single negative keyword.

## Structural Decision

### A. Structural scene is sound

Use a Surgical Repair Prompt:

```text
CHANGE ONLY:
[the smallest observable changes]

PRESERVE EXACTLY:
[identity, wardrobe, scene, action, camera, light, topology, or other successful facts]

[Target Model] Repair Prompt:
[native edit instruction]
```

### B. Structural scene failed

When the story beat, visual center, blocking, topology, or camera position is wrong, rebuild from the Scene Master. Do not stack corrective adjectives onto a failed structure. State what is being rebuilt and what successful facts remain locked.

## Adapter Rules

- GPT Image 2, Seedream, and Nano Banana repair instructions may emphasize explicit preserve/change boundaries when the active tool supports image editing.
- Midjourney V8.2 repair must first choose between prompt regeneration and the current Edit Model. Rebuild through an ordinary prompt when scene structure failed; use a supplied image/reference and, when relevant, an Editor selection for targeted inpainting, outpainting, perspective change, or recombination. Do not route the current default through legacy Omni Reference, Character Reference, or the separate Retexture workflow, and do not imply that prompt-only remix provides deterministic local preservation.
- For a series, load `continuity-cards.md` and protect the Continuity Bible before repairing a shot.

Compile every repair through the target adapter. Do not invent an editing control that the user's frontend has not established.
