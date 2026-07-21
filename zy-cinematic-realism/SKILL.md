---
name: zy-cinematic-realism
description: Turn brief scene ideas into production-ready English prompts for restrained, physically believable cinematic stills or video keyframes. This skill is publicly presented as 造梦师：AI时代电影视觉指南. Use when users ask for 电影感 or cinematic AIGC prompts, want to reduce the artificial AI look, need a story beat, camera position, composition, motivated lighting, film texture, and scene-specific negative prompts, or want an existing visual prompt diagnosed and rewritten as a believable movie frame.
---

# 造梦师 · ZY Cinematic Realism

Public edition: 《造梦师：AI时代电影视觉指南 v1.0》

Transform a simple idea into a frame that feels observed inside an ongoing story. Build narrative, physical space, camera logic, and motivated light before adding lens or film terminology.

## Workflow

1. Parse the user's fixed facts: era, place, characters, event, mood, time, weather, aspect ratio, model, and restrictions.
2. Preserve supplied facts. Infer ordinary production details when they are missing. Ask one concise question only when a missing choice would materially change the result; otherwise proceed with restrained defaults.
3. Identify the emotional subject beneath the literal subject. State what happened immediately before the frame and what may happen next.
4. Select a specific story beat. Prefer anticipation, waiting, aftermath, departure, private observation, or interrupted routine over a heroic climax unless the user requests one.
5. Give each character a small, concrete action. Express emotion through posture, distance, gaze, handling of objects, and silence. Do not direct characters to pose for the camera.
6. Build a usable physical location with foreground, midground, background, age, weather or air, wear, and two to four story-relevant traces of use.
7. Place the camera somewhere a real camera could be. Specify height, distance or shot size, focal length only when useful, and one justified obstruction, reflection, or spatial boundary when appropriate.
8. Compose observationally. Use off-center placement, negative space, partial occlusion, asymmetry, and environmental scale only when they support the story.
9. Motivate every important light source from the location. Describe primary source, secondary source, shadow placement, highlight placement, and a restrained color relationship.
10. Add capture texture last: natural exposure, soft highlight roll-off, believable grain, restrained halation, lens falloff, focus imperfection, or motion blur. Use only effects supported by the scene.
11. Select 10-20 scene-specific Avoid terms. Remove generic terms that do not address a likely failure mode.
12. Run the final quality check in [references/quality-checklist.md](references/quality-checklist.md). Rewrite any weak section before answering.

## Reference Routing

- Read [references/cinematic-principles.md](references/cinematic-principles.md) when building or diagnosing story, environment, and composition.
- Read [references/camera-and-light.md](references/camera-and-light.md) when selecting camera placement, focal behavior, aspect ratio, or motivated light.
- Read [references/negative-prompts.md](references/negative-prompts.md) before composing the Avoid section.
- Read [references/examples.md](references/examples.md) only when calibration through examples would improve the result.
- Use [assets/basic-prompt-template.md](assets/basic-prompt-template.md) as the output scaffold; replace every placeholder and remove unused lines.

## Output Contract

Default to the following order:

1. `画面理解` - a concise Chinese summary of the story beat and key production choices. Use the user's language instead when it is clearly preferred.
2. `Final Prompt` - one complete, fluent English prompt. Integrate concrete scene information instead of listing abstract praise words.
3. `Avoid` - a compact English, comma-separated negative prompt tailored to the scene.

Do not expose hidden reasoning. Do not leave placeholders. Do not repeat the user's brief verbatim as the entire result.

If the user requests only a prompt, omit the interpretation and return `Final Prompt` plus `Avoid`. If a target model is named, adapt syntax and length without changing the scene logic. If the user supplies an existing prompt, briefly identify its strongest failure modes, then provide a complete rewrite.

## Non-Negotiable Rules

- Make the frame work after removing words such as `cinematic`, `35mm`, `Kodak`, `ARRI`, `anamorphic`, and `film grain`.
- Prefer specific nouns and observable actions over `masterpiece`, `epic`, `stunning`, `award-winning`, `8K`, or `highly detailed`.
- Keep period, weather, wardrobe, architecture, props, light, and capture medium internally consistent.
- Do not invent decorative rim lights, neon, fog, lens flare, or shallow depth of field without a physical reason.
- Do not force damage, dirt, occlusion, or imperfection into every frame. Use them only when the location and story support them.
- Avoid poster, fashion editorial, game render, concept-art, and commercial-advertising logic unless explicitly requested.
