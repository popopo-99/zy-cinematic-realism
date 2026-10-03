<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Director Four-Axis Visual Fingerprint Library

## When to use

Use only when the user names a director, requests a director's visual method or comparison, or asks for a recommendation. No named or requested director means no automatic director reference.

## Strength and User Control

Honor the user's requested strength. Never normalize a subtle request to strong.

| Request | Interpretation | Apply within open decisions |
| --- | --- | --- |
| 轻微 / 一点 / subtle / a touch | Subtle | Select one or two compatible signature traits. Keep the current moment and viewing logic unless the user asks to change them. |
| 明确 / clear | Clear | Make the method recognizable through relevant light, color/exposure, camera, and space decisions without requiring a new story moment. |
| 强烈 / 标志性 / strong / iconic | Strong | Use the Default Iconic Anchor as a strong interpretation. Seek structural distinction in open axes and viewing decisions. |

When strength is unspecified, use clear without asking another question. More specific user wording wins over these aliases. Disabling or reducing a director on a later turn is a valid change; preserve unrelated accepted facts. These are qualitative creative instructions, not native numerical reference weights or measured model guarantees.

Use one director by default. Load [directors/index.md](directors/index.md) and exactly one matching director file, two or three candidates for recommendations, or at most a primary and a secondary for an explicit mix. The `Default Iconic Anchor` is a strong-mode resource, not a command to maximize every request.

## Lock Before Differentiation

Mark explicit facts and visual decisions USER-LOCKED before applying the director. User-locked identity, event, action, moment, camera, framing, subject scale, composition, light sources, ratio, and restrictions remain unchanged. A locked gesture never has to change merely because it matches an undirected baseline.

For strong mode, aim for structural distinction across at least three open axes and three open viewing decisions **only when that many are available and compatible**. Exclude locked dimensions from the comparison. If fewer are open, use the available ones and retain the locks; do not fabricate a new source, relocate a prop, or change the action to meet a quota. Mention the limitation briefly only if it materially affects the requested result and explanation is allowed.

Possible viewing decisions are the precise moment, visual center, physical witness position, subject scale/visibility, and whether environment, person, or object leads. Reselect them only when OPEN. Matching the original gesture or camera is not a failure by itself. Differentiate through the unlocked dimensions rather than automatic re-composition.

## Four-Axis Visual Fingerprint

Read all four fingerprint sections in the selected file:

1. Light and Contrast Fingerprint.
2. Color and Exposure Fingerprint.
3. Lens and Camera Fingerprint.
4. Composition and Spatial Fingerprint.

Resolve each axis against the current scene, requested strength, medium, and locks. An axis can deliberately remain unchanged. In subtle mode only the selected traits are active; do not manufacture changes on the other axes. A name, film title, focal-length badge, warm/cool swap, grain, or atmosphere adjective alone is not an executable method.

Mentally remove names and titles: the active decisions must still describe what the image should do. Use `Nearest-Neighbor Contrast` to sharpen ambiguous active traits without escalating strength or breaking locks. Keep light motivated; never copy a specific film shot.

## Mixing

Only on explicit request, use one primary and one secondary director. The secondary controls one stated axis such as camera intimacy, weather pressure, or spatial geometry. Do not average two complete methods. Respect declared strength and locks for both; resolve an incompatible source hierarchy or camera instruction before compilation.

## Recommendation Routing

Read [directors/recommendation-matrix.md](directors/recommendation-matrix.md), select two or three candidates by the scene goal, briefly explain their relevant differences, and load only those files. Never load the entire library.

## Output and Native Compilation

The four axes are a planning and checking structure, not mandatory labels in every final prompt. The selected model adapter controls native ordering, density, parameters, and editing language. Prompt-only output contains only the compiled prompt; never prepend a director analysis or strength explanation.

When the user requests a breakdown, explain the applicable decisions with these labels, marking a locked axis preserved where useful:

```text
Lighting and contrast signature:
Color and exposure signature:
Lens and camera signature:
Composition and spatial signature:
```

When names help and the user permits them, include the director's standard English name and relevant film anchors at the requested strength. `Director and visual reference:` is an optional presentation label, not a mandatory five-line payload. For name-free output, omit names and titles while retaining the same applicable visual decisions. Do not use `in the style of` or `directed by` as substitutes for those decisions. Do not force film anchors into a concise prompt when they add no task-relevant information.

Read [anti-ai-cleanup.md](anti-ai-cleanup.md) when photographic realism is relevant. A non-photographic reference medium retains its own making logic. Cleanup cannot override the requested mood, medium, strength, or locks.
