<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Negative Prompt Selection

Select only likely failure modes for the current scene. Use approximately 10-20 concise terms.

## General synthetic look

`concept art`, `digital illustration`, `CGI appearance`, `3D render`, `game rendering`, `video game screenshot`, `plastic surfaces`, `clean digital image`, `oversharpening`, `HDR look`, `overprocessed colors`

## Portrait and posing failures

`hero pose`, `model-like expression`, `looking directly at camera`, `beauty retouching`, `plastic skin`, `perfect facial symmetry`, `perfectly styled clothing`, `promotional portrait`, `fashion editorial`

## Composition failures

`poster composition`, `perfectly centered subject`, `perfect symmetry`, `overly balanced composition`, `clean empty background`, `excessive subject separation`, `artificial shallow depth of field`, `trailer-style framing`

## Lighting failures

`unmotivated rim light`, `artificial cinematic lighting`, `decorative volumetric light`, `excessive lens flare`, `neon glow`, `crushed blacks`, `blown highlights`, `teal-and-orange grading`

## City and science-fiction failures

`generic cyberpunk neon`, `holographic interfaces`, `fantasy architecture`, `clean futuristic city`, `empty polished streets`, `luxury commercial cityscape`

## Anatomy and duplication failures

Use only when the target generator benefits from artifact negatives: `distorted hands`, `extra fingers`, `duplicated people`, `duplicated objects`, `unnatural posture`, `facial artifacts`.

## Selection Rules

1. Start with the three to five most probable category-level failures.
2. Add subject-specific failures such as posing or beauty treatment for character scenes.
3. Add setting-specific failures such as cyberpunk neon for a grounded future city.
4. Add technical artifacts only when relevant to the target model.
5. Remove contradictions. For example, do not ban all shallow depth of field when the requested frame is an intimate close-up.
6. Never paste the entire library by default.
