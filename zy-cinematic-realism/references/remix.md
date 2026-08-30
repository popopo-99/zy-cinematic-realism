<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# One Variable Remix

Change one major axis per remix. Do not regenerate unrelated details.

## Internal Lock

Create two internal fields before writing:

- **PRESERVE LOCK** — every Scene Master field that must remain unchanged.
- **VARIABLE AXIS** — exactly one of Camera, Moment, Light, Blocking, Spatial, Style, Material, or Weather.

Do not display the internal lock unless requested.

## Axes

- **Camera:** may change witness position, height, distance, obstruction, movement, or focal behavior. Preserve people, wardrobe, scene, event, action, time, weather, and source-light logic.
- **Moment:** move only between a plausible before, during, or after beat. Update the minimum action state and object state required by time.
- **Light:** change time or source state only when physically possible; update shadows, highlights, exposure, and color consequences together.
- **Blocking:** change body placement, gaze, spacing, and object handling while keeping event, camera, scene, and identities fixed.
- **Spatial:** change foreground/midground/background emphasis or a plausible witness boundary without changing location identity or topology.
- **Style:** apply one Style Card's grammar while preserving story, blocking, camera facts, and source logic unless that card explicitly controls one of them and the user permits it.
- **Material:** alter one material relationship or surface state with causal light response; do not restyle the whole world.
- **Weather:** change one weather state and only its necessary ground, air, wardrobe, visibility, and light consequences.

If the requested variant does not name an axis, infer the narrowest one from context. Ask only when two axes would produce materially different results and neither is implied.

## Validation and Output

Compare the new Scene Master against the original field by field. Revert any drift outside the selected axis and its unavoidable physical consequences.

When explanation is allowed, output `Preserved`, `Changed axis`, and `New Prompt`. For prompt-only requests, output only the compiled prompt.
