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

## OpenAI 2.5 edit scope

Use the existing Surgical Repair contract: name the changed region and new physical state in `CHANGE ONLY`; protect identity, geometry, requested composition, lighting relationships, and unaffected objects in `PRESERVE EXACTLY`. Prefer **one meaningful variable per edit**. Closely related changes requested together may share an edit, but do not proactively widen the scope.

Carry the previous accepted output into the next turn, restate the preserve rules, and inspect each result against the Continuity Bible / One Variable Remix locks. Improved multi-turn preservation does not guarantee unchanged pixels. During migration, test a validated GPT Image 2 prompt unchanged first and repair only an observed failure; see the [2.5 adapter and official basis](models/gpt-image-2.md).

## Adapter Rules

- GPT Image 2.5 (and GPT Image 2 legacy), Seedream, and Nano Banana repair instructions may emphasize explicit preserve/change boundaries when the active tool supports image editing.
- Midjourney V8.2 repair must first choose between prompt regeneration and the current Edit Model. Rebuild through an ordinary prompt when scene structure failed; use a supplied image/reference and, when relevant, an Editor selection for targeted inpainting, outpainting, perspective change, or recombination. Do not route the current default through legacy Omni Reference, Character Reference, or the separate Retexture workflow, and do not imply that prompt-only remix provides deterministic local preservation.
- For a series, load `continuity-cards.md` and protect the Continuity Bible before repairing a shot.

Compile every repair through the target adapter. Do not invent an editing control that the user's frontend has not established.
