<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Manual Regression Tests

Run each test in a fresh conversation unless the setup says otherwise. Confirm routing, invariant preservation, output contract, and target-native shape; exact wording is not a pass criterion.

## Test 01 — Unknown Target Model

**User:** `一个女人凌晨站在便利店外，刚下过雨，帮我写电影感提示词。`

**Expected:** With no model context, asks one question only: which target model. Does not ask for camera, mood, or other details in the same turn.

## Test 02 — Explicit Midjourney

**Setup:** Continue Test 01.

**User:** `给 Midjourney。`

**Expected:** Uses a compact Midjourney-native visual prompt. Any supported parameters appear at the end. Does not output GPT-style production-brief sections or ask for the model again.

## Test 03 — Quick Model-Neutral

**Setup:** Start with Test 01's initial request.

**User:** `别问了，直接给。`

**Expected:** Produces a model-neutral Scene Master prompt without blocking. It may briefly mention later transcoding only if prompt-only output was not requested.

## Test 04 — GPT Image 2

**Setup:** Supply a completed model-neutral or other-model prompt.

**User:** `转成 GPT Image 2。`

**Expected:** Scene facts do not change. Output becomes a structured natural-language production brief with constraints integrated into the prompt.

## Test 05 — Transcode Lock

**Setup:** Supply a Midjourney prompt with clear character, action, camera, light, visual center, time, and weather.

**User:** `转成 Seedream 5.0 Pro。`

**Expected:** Character, action, camera position, light sources, visual center, time, weather, aspect ratio, props, and restrictions remain identical. Only model-native expression changes.

## Test 06 — Multi-model Pack

**User:** `同一个画面分别输出 GPT Image 2、Midjourney、Seedream 5.0 Pro、Nano Banana Prompt。`

**Expected:** Four prompts have visibly different native structures but share one Scene Master and identical invariants. No adapter syntax leaks into another prompt.

## Test 07 — Prompt Check

**User:** `帮我检查：cinematic, 8K, masterpiece, neon, dramatic rim light, centered portrait, 35mm, Kodak。`

**Expected:** Uses `PASS / WEAK / RISK / CONFLICT`, no numeric score. Identifies structural absence of story, action, camera witness position, and source-light logic rather than merely saying there are too many keywords. Does not rewrite unless requested.

## Test 08 — Surgical Repair

**Setup:** Provide a generated image or prompt where character and wardrobe are correct but the result looks like an advertisement.

**User:** `人物和服装没问题，但太像商业广告。`

**Expected:** Preserves identity and wardrobe. Diagnoses at most three dominant causes and changes camera witness position, posing/action, light hierarchy, subject scale, or advertising polish as necessary. Uses `CHANGE ONLY` and `PRESERVE EXACTLY` in a target-native repair.

## Test 09 — Continuity

**User:** `我要做8张都市女骑士在地下车库下班的连续组图。`

**Expected:** Builds a Continuity Bible before prompts. Defines character, silver armor, wardrobe state, props, garage topology, light, camera grammar, material state, and forbidden drift once. Every shot uses Base Lock plus Shot Delta rather than redesigning the knight or garage.

## Test 10 — One Variable Remix

**Setup:** Supply an accepted image design with known time, character, wardrobe, action, scene, weather, and light.

**User:** `这张不变，只换机位。`

**Expected:** Changes only the Camera axis: witness position, height, distance, obstruction, movement, or focal behavior. Time, character, action, source-light logic, weather, scene, and wardrobe remain locked.

## Test 11 — Shuffle

**User:** `没灵感了，给我一个意外方向。`

**Expected:** Selects one Story Card, one Camera Card, and one Style Card; the combination is causal and physically possible. It does not return a random adjective list or random director name.

## Test 12 — Urban Intrusion

**User:** `现代停车场里的银甲女骑士。`

**Expected:** Only the knight is unusual. The garage, people, vehicles, light sources, and materials remain contemporary and physically ordinary. No automatic cyberpunk city, fantasy-world conversion, or theatrical crowd reaction.

## Test 13 — Cinematography Card

**User:** `给我一个更像从车后偷拍到的现场感。`

**Expected:** Routes to Peripheral Witness or a compatible cinematography method and changes the actual witness position to behind a vehicle with plausible obstruction and exposure behavior. Does not solve the request with grain, focal length, or “documentary” adjectives alone.

## Test 14 — Prompt-Only

**User:** `只给我 Seedream Prompt。`

**Expected:** Returns only a Seedream-native prompt. No interpretation, menu, follow-up, or target-model question.
