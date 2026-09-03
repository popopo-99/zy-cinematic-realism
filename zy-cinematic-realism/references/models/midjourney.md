<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Midjourney V8.2 Adapter

- **Model:** Midjourney V8.2
- **Aliases:** Midjourney, MJ, Midjourney V8, Midjourney V8.2, MJ V8.2, V8.2
- **Default compilation target:** V8.2
- **Verified date:** 2026-09-03
- **Official basis:** [Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version), [Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics), [Parameter List](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List), [Raw](https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw), [Stylize](https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize), [Image Prompts](https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts), [Style Reference](https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference), [Edit Model](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model), [Text Generation](https://docs.midjourney.com/hc/en-us/articles/32502277092109-Text-Generation), [Seeds](https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds), and [Aspect Ratio](https://docs.midjourney.com/hc/en-us/articles/31894244298125-Aspect-Ratio)

## Version baseline

Unqualified `Midjourney`, `MJ`, or `编译成 Midjourney` means the current V8.2 adapter. Do not emit a V6, V6.1, or V7 prompt by default and do not silently fall back for compatibility.

V8.2 is the current official default, so adapter selection does not require `--v 8.2` in every prompt. Add an explicit version parameter only when the user requests a complete Discord-ready prompt, asks to lock V8.2, needs protection from version drift, or explicitly targets a historical version.

Treat explicit V6, V6.1, or V7 requests as legacy targets. Verify that version's documented parameter and reference compatibility instead of pretending the V8.2 adapter is equivalent.

## Best for

Prompt-led visual exploration, concise scene generation, native parameter control, role-specific image references, and V8.2 Edit Model generation or repair.

## Compilation contract

Preserve semantics before compression. The Midjourney-native rewrite must retain:

- subject identity, action, story moment, Narrative Before, and Implied Next;
- spatial relationships, foreground/midground/background, visual center, and witness position;
- camera height, observation distance, subject scale, focal behavior, and motivated movement;
- source light, exposure relationship, material response, weather, and environmental state;
- props, visible text, aspect ratio, and explicit restrictions.

Compress only after those facts are locked. High information density means few redundant words with clear relationships, not a comma-separated V6-era keyword chain.

## Native prompt shape

Write a concise, concrete, natural visual description in this order when useful:

1. visible subject, current action, place, and story moment;
2. the subject's relationship to foreground, midground, background, and visual center;
3. the camera's physically possible witness position, height, distance, subject scale, and observation behavior;
4. motivated source light, shadow/exposure relationship, material response, weather, and restrained aesthetic direction;
5. short visible text in double quotation marks when required;
6. only request-relevant supported native parameters, all at the end.

Do not convert the Scene Master into `cinematic, masterpiece, photorealistic, 8K, ultra detailed, award winning`. Remove quality adjectives that do not change visible content. Do not over-compress a complex scene until actions, depth relationships, camera observation, or light causality disappear.

## Imagine versus Edit Model

Use the ordinary Imagine/generation path for a new image or prompt-led variation where exact preservation is not required.

Use the V8.2 Edit Model path when the request is fundamentally about an existing image or supplied references, including:

- keeping a person or object while changing the setting;
- changing camera perspective while carrying referenced identity or design forward;
- combining up to four supplied reference images;
- changing a selected region through inpainting;
- extending the frame through outpainting;
- recombining referenced characters, objects, or scenes;
- changing the visual treatment of an existing image.

Do not force these requests into a normal Imagine prompt or promise deterministic preservation. V8.2 Edit Model replaces Omni Reference, Character Reference, and the separate Retexture workflow as the current default path. In the Editor, identify the intended selected area and state what changes; keep every unselected or locked fact explicit.

## Reference-image roles

Assign each supplied reference exactly one primary role before compiling. Combine roles only when the user intentionally supplies the same image for more than one purpose.

| Reference type | Primary role | Do not claim |
|---|---|---|
| Image Prompt | Influence content, composition, and color relationships in a new generation | Exact copying or deterministic preservation |
| Style Reference | Transfer visual style, palette, texture, medium, or aesthetic language | Character or object identity lock |
| Edit Model Reference | Integrate or edit supplied characters, objects, scenes, and multiple references | Pixel-exact preservation |
| Moodboard / Personalization | Apply a user-owned broader aesthetic profile | Scene facts, identity, or composition lock |

Use only references, URLs, style codes, weights, seeds, and personalization profiles that the user actually supplies or confirms are active. Never fabricate an image URL, `--sref` code, `--iw`, `--sw`, reference weight, seed, profile, or style code. If a required reference is absent, request it or provide a text-only fallback with the limitation stated.

## Raw strategy

`--raw` is a purposeful control, not a default cinematic suffix.

- Consider it when the user prioritizes prompt adherence, restrained photographic interpretation, precise cinematic control, or less automatic Midjourney styling.
- Omit it when the user wants open visual exploration, stronger default Midjourney interpretation, or aesthetic surprise.

Raw can improve control but does not guarantee perfect instruction following or identity preservation.

## Stylize strategy

Treat stylize as an adherence-versus-interpretation decision:

- **Low intent:** continuity, strict scene execution, production-design lock, or close adherence.
- **Medium intent:** cinematic interpretation, editorial/fashion exploration, or a balance of facts and aesthetic response.
- **High intent:** only when the user explicitly wants stronger Midjourney aesthetic interpretation and accepts more semantic drift.

Do not append a universal `--s` value. If no explicit stylize control is needed, omit it and let V8.2 use its default behavior. Preserve a user-supplied supported value; otherwise do not invent a number merely from the words “cinematic” or “beautiful.”

## Capability-driven parameters

Use native parameters only when they serve the current request. Relevant current controls may include `--ar`, `--raw`, `--stylize` / `--s`, `--weird` / `--w`, `--seed`, `--sref`, `--iw`, `--no`, `--profile` / `--p`, `--hd` / `--sd`, `--edit`, and `--version` / `--v`. This is a capability set, not a suffix template.

- Put every parameter after the text prompt with valid spacing.
- Do not add punctuation inside the parameter block.
- Do not invent a parameter, value, reference identifier, profile, default, or weight range.
- Do not use a legacy-only or incompatible parameter in V8.2.
- Do not use `--quality` / `--q`, `--draft`, `--turbo`, `--niji`, or `--oref` as V8.2 controls; the current official compatibility chart does not support them on V8.2.
- Keep user-supplied valid controls unless they conflict with V8.2; report a conflict instead of silently substituting.
- For a parameter outside the common set above, verify its current official V8.2 support before emitting it.

## Aspect ratio and SD / HD

Preserve the Scene Master ratio exactly. Translate `vertical 2:3 composition` to `--ar 2:3`, not 9:16. The current official V8.2 limits are up to 14:1 in SD and 4:1 in HD. If a locked ratio exceeds the selected mode's limit, disclose the incompatibility and change the mode or ask the user; never silently change the ratio.

The Edit Model tries to match the first supplied image's ratio unless `--ar` overrides it. Explicitly apply a locked target ratio when preservation matters.

## Exclusion strategy

Solve restrictions through positive scene design first. Use `--no` only for short, concrete objects or concepts that Midjourney can exclude cleanly. Do not convert a GPT-style negative paragraph into a large `--no` list, and avoid multiword negatives whose independently interpreted words create a contradiction. Preserve nuanced restrictions such as “no centered hero pose” through composition and camera language rather than a mechanical negative.

## Visible text

Put required short visible words or phrases in double quotation marks and describe where they appear. Do not use single quotes as a substitute. Treat exact spelling, complex typography, long copy, and layout as conditional; use Edit Model repair when appropriate, without changing the locked composition merely to accommodate text.

## Seed and continuity

`--seed` controls initial noise for tests and controlled experiments. It is not a character ID, style ID, continuity system, or identity lock, and it may not remain reliable across sessions or setting changes. Use the project's Continuity Bible, Base Lock, Shot Delta, and supplied references as the primary continuity structure.

## Transcode rules

For any source model:

1. parse the source into the shared Scene Master;
2. establish the Transcode Lock;
3. load this V8.2 adapter directly;
4. rewrite the scene into the native prompt shape above;
5. append only supported, request-relevant parameters;
6. compare every locked fact against the compiled result and restore drift.

Never chain GPT Image 2 → Midjourney → Seedream or any other prompt-to-prompt translation. Each target compiles independently from the same Scene Master.

## Repair rules

Choose between two different operations:

- **Prompt regeneration:** rewrite the V8.2 prompt when the whole result or scene structure failed; preservation is a goal, not a deterministic local edit.
- **Edit Model precision editing:** use a supplied image/reference and, when relevant, a selected region for a targeted change while explicitly locking successful areas.

Do not imply that prompt-only remix can preserve identity, framing, or untouched pixels like an Edit Model operation.

## Common failure modes

Legacy keyword soup; automatic `--raw`; arbitrary stylize values; mechanical `--v 8.2`; lost camera or light relationships; changed aspect ratio; Style Reference treated as identity; seed treated as continuity; fabricated reference data; Edit Model requests routed to Imagine; and V6/V7 reference syntax leaking into the V8.2 default path.
