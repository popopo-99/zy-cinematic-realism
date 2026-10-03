<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Continuity Bible

For a series, establish one Base Lock and express each image as a Shot Delta. Do not redesign the cast, wardrobe, location, or visual grammar from scratch for every shot.

When a series uses Dream Decode, keep the Continuity Bible and Decode Card as coordinated but non-competing structures. The Bible owns scene and story continuity; the Decode Card owns shared visual grammar. The current Scene Master remains the canonical source of facts for each shot.

## Bible Schema

### Project

Define title or identifier, image count, narrative span, aspect ratio, target model, delivery order, and user restrictions.

For story-backed projects, associate the Bible with the actual source version, verified read scope, and stable internal scene IDs using [story-source-ledger.md](story-source-ledger.md) when needed. Keep source facts, interpretations, and visual proposals distinct; only user-accepted proposals become accepted project locks. A proposed Bible may support candidate development when requested, but must retain that provisional status.

### Narrative Invariants

Lock the premise, event boundaries, emotional trajectory, chronology, and facts that cannot change across the series.

### Knowledge and Reveals

When relevant, track what each character knows, believes, or has not learned, and what the audience has been shown at each moment. Distinguish story chronology from scene presentation order. Do not import a later reveal from film memory or turn an unresolved belief into truth.

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

For story-backed frames, include the relevant knowledge/reveal state and source scene/beat. Track clothing, damage, wetness, and prop ownership/hand occupancy across actual time progression; they cannot reset merely because the source changes scenes.

### Allowed Delta

List changes the series may introduce: current action, expression, camera position within the Bible, prop state, weather progression, or time progression.

### Forbidden Drift

List identity mutation, wardrobe redesign, topology changes, prop duplication, light-source relocation, style switching, camera heroization, and any project-specific failure.

### Reference Image Roles

Assign each reference one role such as facial identity, wardrobe construction, prop identity, location topology, material, composition, or light. Do not treat every reference as authority over every field.

### Shared Visual Grammar

When the project uses Dream Decode, link or restate only the Decode Card's Core Visual Rules, Allowed Variation, Transfer Scope, and Drift Warnings. Keep color/exposure behavior, material language, texture/capture character, composition tendencies, spatial rhythm, and anti-cliches here only as visual-grammar constraints. Do not copy Source Residue—characters, wardrobe, props, location, or story facts—out of the Decode Card.

Story-developed art-direction rules may be recorded here once accepted. Keep them distinct from reference-observed grammar, and keep unaccepted alternatives out of the accepted Base Lock. A proposed screenplay expression is not an observed image mechanism.

### Target Model

Name the adapter and frontend context. Record only verified controls actually available in that workflow.

## Shot Construction

For each shot:

1. Copy the current **BASE LOCK** from the Bible.
2. Write a **SHOT DELTA** containing only what changes from the immediately previous narrative state.
3. Update dependent physical consequences: hand occupancy, wetness, damage, shadow direction, visibility, or object location.
4. Compile `Base Lock + Shot Delta + optional Decoded Visual Grammar` through the target adapter.
5. Compare the prompt against Forbidden Drift before output.

Do not let a Shot Delta restate or silently revise the Bible. When a new user instruction conflicts with the Bible, identify the conflict and ask only if it cannot be resolved as an allowed state change.

For source revisions, inspect affected scene and downstream state dependencies through [story-source-ledger.md](story-source-ledger.md). Mark which outputs still apply or need review/recompilation; preserve unrelated accepted changes and do not silently regenerate or discard a whole series.

## Project Handoff

When the user asks to resume later or move to another conversation, use [project-handoff.md](project-handoff.md). Record the latest accepted narrative state and necessary locks, not merely the initial Bible. No automatic storage or identity-reference recovery is implied.

## Output

Return the Continuity Bible, concise Shot List, one Shot Delta per image, and model-native prompts. For long series, define the full Bible and shot list first; generate prompts in manageable batches only when requested or when output length would otherwise reduce quality.
