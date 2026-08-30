<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Midjourney Adapter

- **Model:** Midjourney
- **Aliases:** MJ
- **Verified date:** 2026-08-29
- **Official basis:** [Prompt Basics](https://docs.midjourney.com/docs/prompts), [Parameter List](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List), [Image Prompts](https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts), and [Editor](https://docs.midjourney.com/hc/en-us/articles/32764383466893-Editor)

## Best for

Prompt-led visual exploration, rapid aesthetic iteration, image-reference workflows, and native parameter control.

## Prompt density

Compress the Scene Master into a coherent sequence of concrete visual clauses. Remove explanatory prose, internal headings, and repeated preserve statements while retaining story, spatial, camera, and light facts.

## Prompt structure

1. Subject, action, place, and story moment.
2. foreground/midground/background and visual center.
3. physical witness position, subject scale, focal behavior, and movement implication.
4. motivated light, exposure, color, material response, and restrained capture behavior.
5. exclusions and supported parameters at the end.

## Generation strategy

Describe what should be visible rather than giving conversational meta-instructions. Use precise nouns and visual relationships. Keep all native parameters after the text prompt with correct spacing and no punctuation inside the parameter block.

## Editing strategy

Ordinary prompt variation is not deterministic local editing. When the user is in Midjourney Editor, write instructions suited to the selected region, Pan, Zoom Out, Vary Region, or Retexture workflow. Otherwise describe a new variation and disclose that preservation is conditional.

## Reference-image strategy

Use image prompts or the current reference tools only when the user has supplied usable inputs and the active frontend supports them. Assign content, composition, style, or identity roles explicitly. Do not fabricate URLs, weights, or reference modes.

## Text strategy

Keep exact visible text short and plainly quoted. Treat precise typography as conditional and suggest an editing workflow when exactness is critical.

## Negative / exclusion strategy

Use concise `--no` concepts only when supported and non-contradictory. Do not paste a paragraph of GPT-style “do not” sentences after the parameter block.

## Aspect ratio strategy

Use a supported aspect-ratio parameter at the end when the user specifies one or composition requires it. Do not change the locked ratio during transcode.

## Parameter strategy

Only use current documented parameters that serve the request. Parameters always go at the end. Do not invent model-version flags, stylization values, chaos values, reference weights, or defaults.

## Strong at

Visual exploration, concise visual prompting, prompt/image reference combinations, and parameterized iteration.

## Common failure modes

Keyword soup, loss of causal story during compression, decorative style overwhelming action, unintended hero framing, mixed GPT edit language, and parameters inserted before prompt text.

## Compilation rules

Convert natural-language production briefs into dense visual clauses while retaining every Transcode Lock field. Exclusions become a short supported `--no` list or are expressed positively in the visual clauses. Keep parameters last.

## Repair rules

Match the repair to the user's actual Midjourney tool. For prompt-only remix, state that preservation is a target rather than an exact local edit. For Editor workflows, describe only the selected change and keep unselected image regions intact; do not promise capabilities beyond the current interface.
