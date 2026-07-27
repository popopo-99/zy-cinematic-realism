<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Director Lens Library

## When to use

Use this library only when the user explicitly names a director, asks for a director's visual method, asks to compare directions, or asks for a suitable director recommendation.

## Default behavior

- Default director strength: `iconic` (public label: `强烈`). Treat legacy `strong` input as `iconic`.
- No named director means no director reference.
- Use one director by default.
- Read only the references needed for the task: exactly one matching reference for a single named director, two or three candidates for a comparison or recommendation, or no more than the primary and secondary references for an explicit mix.
- Convert the method into visual decisions; never use a name as shorthand for those decisions.
- Lower the default only when the user explicitly asks for a light reference, restraint, one borrowed method, no obvious director effect, a name-free prompt, or a platform that does not allow director names.

## Style strength

### Subtle

Influence only a few choices in story beat, composition, or light. The Final Prompt may include only the director name, and does not add film titles by default.

### Clear

Clearly influence story beat, character action, camera position, spatial relationship, and light. Include the standard English director name once in the Final Prompt, immediately followed by the current scene's concrete visual translation; one or two representative films may be included.

### Strong (legacy alias)

Treat `strong` as `iconic`.

### Iconic

Include the standard English director name and two or three representative films as broad reference points. Use the director's most recognizable overall image grammar as strongly as possible. It must lead exact story beat, visual center, blocking, camera axis, focal behavior, movement grammar, light and contrast, color response, depth of field, texture or capture character, and environment participation; physical plausibility and user-fixed facts still prevail.

`Iconic` is not a stronger version of the baseline composition. It must reinterpret the scene through a different visual priority.

Before generating, ask:

- Does the director version preserve the same central gesture as the baseline?
- Are the same two objects still perfectly aligned as the main visual event?
- Is the camera merely closer, lower, wider, or shallower without changing what the shot is actually about?
- Could the director version and baseline be used as adjacent coverage in the same conventional scene?

If any answer is yes, reselect the specific moment, visual center, or camera relationship before generating.

## Mixing

Allow at most one primary and one secondary director, and only on explicit request. The secondary director may control one stated dimension only, such as weather pressure, camera distance, character intimacy, spatial geometry, or movement rhythm.

## Differentiation and Cleanup

Read [anti-ai-cleanup.md](anti-ai-cleanup.md) for every output. Under `strong` or `iconic`, rebuild if the result could be exchanged with the baseline after removing the director name. Do not use polished AI finish, decorative aging, uniform sharpness, or a new Avoid list as a substitute for changed image grammar.

## Output rule

For named-director requests, explicit director names are model-facing style anchors. Under `iconic`, include two or three representative films. Never rely on names or titles alone; immediately translate them into scene-specific visual grammar. Put the anchor after grounded scene facts and before detailed camera design, not as an unrelated ending.

If the user explicitly requests a name-free prompt, says that their platform does not allow director names, or asks for a compatibility version, omit names and titles. Do not use `in the style of` or `directed by`. Preserve the user's original characters, event, era, and location unless the user explicitly asks to recreate a particular film scene. Keep light motivated and physical.
