<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Model-Neutral Scene Master Scaffold

Use this only as a drafting order. Replace each instruction with scene-specific prose, omit irrelevant lines, and compile the result through the selected model adapter. Never expose the scaffold labels unless they improve the requested output.

```text
Grounded scene: establish era, place, time, weather, and the fixed event.

Story beat: identify what just happened, the concrete current action, and the implied next event.

Character identity and blocking: describe who is present, where each person is, what each person is physically doing, and how objects occupy their hands or attention.

Environment and topology: establish usable entrances, exits, surfaces, routes, causal traces of use, and the relationship between foreground, midground, and background.

Visual center: state what the eye discovers first and what remains secondary, hidden, or unresolved.

Camera witness position: place a real camera at a specific location and height; define observation distance, subject scale, focal behavior, boundary or obstruction, and movement only when motivated.

Source light map: name the primary source, limited secondary sources, protected shadow zones, highlight surfaces, exposure behavior, and resulting color relationship.

Material behavior: describe how the important surfaces respond to weight, moisture, age, movement, contact, and the mapped sources.

Capture behavior: add only a few compatible traits such as natural exposure, soft highlight roll-off, plausible motion blur, focus imperfection, restrained grain, or source-bound halation.

Delivery: preserve the requested aspect ratio, visible text, reference-image roles, restrictions, and likely scene-specific failure modes.
```

For a named supported director, apply the Director Four-Axis block from `references/director-routing.md` after the grounded facts and before detailed camera design. For a model-neutral result, keep exclusions as direct visual constraints. For a target model, let its adapter determine whether exclusions are integrated, separated, or expressed through native syntax.
