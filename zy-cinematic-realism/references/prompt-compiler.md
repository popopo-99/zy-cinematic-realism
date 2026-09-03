<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Prompt Compiler

## Contract

`MODEL SYNTAX MAY CHANGE. SCENE LOGIC MAY NOT.`

The Scene Master is the source of truth. It is an internal structure unless the user explicitly requests it.

## Scene Master Schema

- **Fixed Facts:** user-supplied era, place, people, event, mood, time, weather, ratio, model, and restrictions.
- **Story:** Story Beat, Narrative Before, Current Action, Implied Next.
- **Characters:** Character Identity, Character Blocking, Object Interaction.
- **Space:** Environment, Foreground, Midground, Background, Visual Center.
- **Camera:** Witness Position, Height, Observation Distance, Focal Behavior, boundary or movement when motivated.
- **Light:** Source Light Map, Protected Shadows, Highlight Surfaces, Color Relationship.
- **Surface and Capture:** Material Behavior, Capture Behavior.
- **Delivery:** Aspect Ratio, Visible Text, Reference Roles, Must Preserve, Allowed Variation, Likely Failure Modes.

Do not force absent or irrelevant fields into the visible prompt. Resolve only what the scene needs.

## Transcode Lock

Before changing models, extract and lock:

`Character · Scene · Story Beat · Action · Visual Center · Camera Position · Composition · Light Sources · Props · Time · Weather · Aspect Ratio · Restrictions`

If the source is ambiguous, preserve the most direct reading. If two clauses conflict, state the single structural conflict briefly. Faithful conversion preserves it; optimization requires user intent or an explicit request to fix.

## Compilation Pass

1. Normalize the source into a Scene Master without adding a new concept.
2. Mark every fixed or explicitly preserved field.
3. Load the target adapter only after the lock exists.
4. Reorder and compress information according to the adapter.
5. Translate exclusions, references, editing instructions, ratio, and parameters into target-native form.
6. Compare the compiled prompt against the lock. Restore any drift before output.

Native shapes:

- **Midjourney V8.2:** concise, concrete natural visual description optimized for current V8.2 prompt understanding, preserving story, spatial, camera, light, material, and restriction relationships; append only request-relevant supported native parameters.
- **GPT Image 2:** structured natural-language production brief with integrated constraints.
- **Seedream 5.0 Pro:** clear spatial creative brief with explicit relationships and edit regions when supplied.
- **Nano Banana:** direct conversational generation or editing instruction with explicit preserve/change language.

For Midjourney, decide between ordinary Imagine/generation and the V8.2 Edit Model before compiling. An existing-image change, selected-area repair, perspective change with reference preservation, or multi-reference recombination is an Edit Model task, not merely a shorter Imagine prompt. Because V8.2 is the current default target, omit `--v 8.2` unless the user requests a Discord-complete or version-locked prompt, or the workflow must prevent version drift.

## Multi-model Pack

Build one Scene Master once. Compile each target independently; do not translate one target prompt into the next. The prompts should differ visibly in native shape while their locked facts remain identical.

## Output

For Transcode, show only a short Scene Lock Summary and the target prompt. Do not re-pitch the creative idea. Omit the summary when the user requests prompt-only output.
