<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Director Four-Axis Visual Fingerprint Library

## When to use

Use this library only when the user explicitly names a director, asks for a director's visual method, asks to compare directions, or asks for a suitable director recommendation.

## Mandatory Strong / Iconic Mode

- Whenever a director listed in [directors/index.md](directors/index.md) is named, execute the request as `iconic`, publicly labeled `强烈`.
- Normalize every supplied strength word to `iconic`: `subtle`, `clear`, `strong`, `iconic`, `轻微`, `明确`, and `强烈` are all the same mandatory strongest behavior.
- No named director means no director reference. Use one director by default.
- Read only the references needed for the task: exactly one matching reference for a single named director, two or three candidates for a comparison or recommendation, or no more than the primary and secondary references for an explicit mix.
- For each named director, read that director's `Default Iconic Anchor` and use its strongest recognizable image grammar as strongly as possible. Convert the method into visual decisions; never use a name as shorthand for those decisions.
- The director must lead the exact story beat, visual center, blocking, camera axis, focal behavior, movement grammar, light and contrast, color response, depth of field, texture or capture character, and environment participation; physical plausibility and user-fixed facts still prevail.
- `Iconic` is not a stronger version of the baseline composition. It must reinterpret the scene through a different visual priority.

Before generating, ask:

- Does the director version preserve the same central gesture as the baseline?
- Are the same two objects still perfectly aligned as the main visual event?
- Is the camera merely closer, lower, wider, or shallower without changing what the shot is actually about?
- Could the director version and baseline be used as adjacent coverage in the same conventional scene?

If any answer is yes, reselect the specific moment, visual center, or camera relationship before generating.

## Four-Axis Visual Fingerprint

For every supported named director, read and translate all four fingerprint sections in the selected director file:

1. `Light and Contrast Fingerprint`
2. `Color and Exposure Fingerprint`
3. `Lens and Camera Fingerprint`
4. `Composition and Spatial Fingerprint`

Missing any axis is a failed output. Apply structural change on at least three axes relative to an undirected baseline. A name, film title, focal-length number, shallow focus, warm/cool swap, grain, atmosphere adjective, or aspect-ratio change alone does not count.

Reselect at least three of these five viewing decisions:

- the moment before, during, or after the stated action;
- the primary visual center;
- the camera's physical witness position;
- the subject's scale and whether it remains fully visible;
- whether environment, person, or object controls the frame.

After drafting, mentally delete the director name and film titles. The four axes must still communicate a distinct method. Then read the selected file's `Nearest-Neighbor Contrast`; if the result could belong to that neighboring director, rebuild the ambiguous axes.

## Mixing

Allow at most one primary and one secondary director, and only on explicit request. The secondary director may control one stated dimension only, such as weather pressure, camera distance, character intimacy, spatial geometry, or movement rhythm.

Do not average two full fingerprints. State which single axis the secondary director controls, keep the primary director in control of the other three, and reject mixtures whose source hierarchy or camera logic contradicts.

## Recommendation Routing

For recommendations, read [directors/recommendation-matrix.md](directors/recommendation-matrix.md) first. Select two or three candidates by scene goal, explain their four-axis difference briefly, then load only those director files. Never load the full library into working context.

## Differentiation and Cleanup

Read [anti-ai-cleanup.md](anti-ai-cleanup.md) for every output. For every named supported director, rebuild if the result could be exchanged with the baseline after removing the director name. Do not use polished AI finish, decorative aging, uniform sharpness, or a new Avoid list as a substitute for changed image grammar.

## Output rule

For every named-director request, put the following uninterrupted block immediately after grounded scene facts and before detailed camera design:

```text
Director and visual reference: [standard English director name], drawing strongly from the visual language associated with [film 1], [film 2], and [film 3].

Lighting and contrast signature: [current-scene decision].

Color and exposure signature: [current-scene decision].

Lens and camera signature: [current-scene decision].

Composition and spatial signature: [current-scene decision].
```

Keep all five labels and translate the selected fingerprint into the current scene. Never rely on names or titles alone, and do not use `in the style of` or `directed by`.

Do not output an ordinary name-free version when a supported director is named, unless the user explicitly requests a name-free prompt or explicitly says that their platform does not allow director names. In either exception, omit names and titles but retain the four labeled signatures and the strongest internal director grammar. Preserve the user's original characters, event, era, and location unless the user explicitly asks to recreate a particular film scene. Keep light motivated and physical, and never copy a specific film scene.
