<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Continuity Bible

For a series, establish one Base Lock and express each image as a Shot Delta. Do not redesign the cast, wardrobe, location, or visual grammar from scratch for every shot.

## Bible Schema

### Project

Define title or identifier, image count, narrative span, aspect ratio, target model, delivery order, and user restrictions.

### Narrative Invariants

Lock the premise, event boundaries, emotional trajectory, chronology, and facts that cannot change across the series.

### Character Lock

Record facial identity, apparent age, body proportions, hair, makeup, defining features, handedness when relevant, and stable relationship to other characters. Separate identity from temporary expression or pose.

### Wardrobe Lock

Record base outfit, construction, layers, materials, fit, fasteners, footwear, and accessories. Track state changes such as wetness, dirt, damage, removal, or repair chronologically.

### Prop Lock

Record object identity, dimensions when visually important, hand relationship, orientation, placement, damage, contents, and state. A prop cannot jump hands or reset without a Shot Delta.

### Location Topology

Map entrances, exits, columns, windows, stairs, roads, room geometry, parking bays, furniture, recurring landmarks, and camera-accessible positions. Preserve left/right and near/far relationships unless the camera crosses a clearly described axis.

### Lighting Bible

Lock fixed sources, time progression, color contamination, exposure logic, source failures or switching events, protected shadows, and weather effects. Do not relight each frame for beauty.

### Camera Bible

Define preferred witness positions, subject-scale range, focal behavior, movement, obstruction logic, axis rules, and forbidden hero framing. Individual shots vary within this grammar unless a deliberate transition is listed.

### Material Bible

Record recurring materials, roughness, reflectivity, wetness, wear, dirt transfer, damage, and how each changes over time.

### Narrative State

Track the current location, time, character positions, wardrobe/prop states, weather, and unresolved action after each shot.

### Allowed Delta

List changes the series may introduce: current action, expression, camera position within the Bible, prop state, weather progression, or time progression.

### Forbidden Drift

List identity mutation, wardrobe redesign, topology changes, prop duplication, light-source relocation, style switching, camera heroization, and any project-specific failure.

### Reference Image Roles

Assign each reference one role such as facial identity, wardrobe construction, prop identity, location topology, material, composition, or light. Do not treat every reference as authority over every field.

### Target Model

Name the adapter and frontend context. Record only verified controls actually available in that workflow.

## Shot Construction

For each shot:

1. Copy the current **BASE LOCK** from the Bible.
2. Write a **SHOT DELTA** containing only what changes from the immediately previous narrative state.
3. Update dependent physical consequences: hand occupancy, wetness, damage, shadow direction, visibility, or object location.
4. Compile `Base Lock + Shot Delta` through the target adapter.
5. Compare the prompt against Forbidden Drift before output.

Do not let a Shot Delta restate or silently revise the Bible. When a new user instruction conflicts with the Bible, identify the conflict and ask only if it cannot be resolved as an allowed state change.

## Output

Return the Continuity Bible, concise Shot List, one Shot Delta per image, and model-native prompts. For long series, define the full Bible and shot list first; generate prompts in manageable batches only when requested or when output length would otherwise reduce quality.
