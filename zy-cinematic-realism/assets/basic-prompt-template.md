<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Basic Cinematic Prompt Template

Replace every bracketed field and delete unused lines.

```text
A frame from a [era, place, and film genre], captured with restrained cinematic realism.

[Specific time, weather, and physical location.]

[Character identity and concrete action.]

This moment occurs after [immediate previous event] and before [implied next direction]. Emotion is expressed through [posture, distance, gaze, silence, or object handling], not a posed expression.

The location feels physically used: [two to four causal details tied to age, weather, occupation, or the recent event].

[When a director is named:]
Director and visual reference: [standard English director name], drawing strongly from the visual language associated with [representative film 1], [representative film 2], and [representative film 3].
Signature visual language: [scene-specific translation of the director's recognizable story beat, visual center, blocking, camera axis, lens behavior, movement, light, contrast, color, depth of field, and capture texture].

Foreground: [natural boundary, obstruction, reflection, or empty foreground].
Midground: [primary action and spatial relationship].
Background: [continuing activity, architecture, weather, or consequence].

The camera observes from [physical position] at [height and shot distance], using [focal behavior or focal length when useful]. [Movement behavior.] The composition places [subject relationship], with [negative space, asymmetry, or environmental scale] supporting the story.

[Aspect ratio when requested.]

Primary light source: [real source, direction, and quality].
Secondary light source: [real source and its limited effect].
[Shadow, highlight, and restrained color relationship.]

Natural exposure, [two to five compatible capture traits].

The frame feels like [narrative position and emotional aftertaste].
```

Return a separate `Avoid` list with 10-20 scene-specific terms.

When no director is named, delete the entire director block. When a director is named, do not delete it: fill both sentences with the director's name, two or three representative films, and a concrete scene-specific style translation. Never fill the block with a director name alone.
