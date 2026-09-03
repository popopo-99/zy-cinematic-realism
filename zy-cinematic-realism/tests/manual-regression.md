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

**Expected:** Routes to the Midjourney V8.2 adapter. Uses a concise, natural, relational visual prompt; supported request-relevant parameters appear at the end. Does not emit V6/V7 legacy syntax, mechanically append `--v 8.2`, output GPT-style production-brief sections, or ask for the model again.

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

## Midjourney V8.2 Adapter Regression

### Test 15 — Default Version

**User:** `给 Midjourney。`

**Expected:** Routes to the Midjourney V8.2 adapter. Does not produce V6, V6.1, or V7 legacy syntax by default. Because V8.2 is the current default, does not require `--v 8.2` unless the delivery context needs an explicit version lock.

### Test 16 — GPT Image 2 to Midjourney V8.2 Transcode

**Setup:** Supply this GPT Image 2 production brief:

```text
Create a vertical 2:3 image set outside a convenience store just after rain at 3 a.m. A woman stands beside the glass entrance, head lowered as she lights a cigarette. The camera observes her candidly from behind a parked car at street level; the car occupies the lower foreground, she remains the midground visual center, and stocked shelves recede behind the glass. The store's white fluorescent ceiling lights are the only dominant source, spilling through the door onto wet pavement and catching small reflections on the car roof. Keep the street otherwise dim and ordinary. No neon, cyberpunk treatment, fantasy architecture, centered hero pose, or advertising polish.
```

**User:** `转成 Midjourney。`

**Expected:** Reconstructs a Scene Master and Transcode Lock, then compiles directly through the V8.2 adapter. Preserves the woman, 3 a.m., recent rain, convenience store, behind-car witness position, head-lowered cigarette-lighting action, white fluorescent source light, foreground car, background shelves, ordinary dark street, restrictions, and 2:3 ratio. Uses a concise natural visual description, removes GPT production headings, keeps parameters at the end, uses `--ar 2:3`, and adds no unsupported or irrelevant parameters.

### Test 17 — Raw Decision

**Setup:** Supply a locked cinematic scene and camera position.

**User:** `我要尽量严格执行这个电影机位，不要 Midjourney 自动美化太多。`

**Expected:** May add `--raw` at the parameter end because the request prioritizes adherence and reduced automatic styling. Does not claim Raw guarantees exact execution.

### Test 18 — No Automatic Raw

**Setup:** Supply the same locked scene.

**User:** `给我几个更有视觉惊喜的方向。`

**Expected:** Does not mechanically force `--raw`. Keeps locked scene facts while allowing broader V8.2 aesthetic interpretation; it does not silently redesign the scene.

### Test 19 — Edit Model Routing

**Setup:** User supplies an image containing the person to preserve.

**User:** `人物不变，只把背景改成凌晨便利店。`

**Expected:** Routes to the V8.2 Edit Model strategy with the supplied image/reference and explicit preserve/change boundaries. Does not pretend a normal Imagine prompt can perfectly preserve identity, and does not default to Omni Reference, Character Reference, or the separate Retexture workflow.

### Test 20 — Style Reference Role

**Setup:** User supplies a usable style reference image and a separate character reference for an Edit Model task.

**User:** `人物按角色参考，画面质感按风格参考。`

**Expected:** Uses the character image as an Edit Model Reference and the style image only as a Style Reference. Does not claim Style Reference locks the character, and does not invent reference weights or codes.

### Test 21 — No Fabricated Reference

**User:** `用参考图保持人物。`

**Expected:** When no usable image or URL is actually available, does not fabricate a URL, `--sref` code, image weight, style weight, seed, reference identifier, or personalization profile. Requests the missing image or gives a clearly limited text-only fallback.

### Test 22 — Seed Is Not Identity

**User:** `用同一个 seed 保持8张图的人物完全一致。`

**Expected:** Does not treat seed as a character ID or continuity lock. Uses a Continuity Bible plus Base Lock and Shot Delta, routes usable supplied images through the current reference/Edit Model workflow, and describes seed only as an optional experimental control.

### Test 23 — Aspect Ratio Lock and SD / HD

**Setup:** Source Scene Master ratio is `2:3`.

**User:** `转成 Midjourney。`

**Expected:** Outputs `--ar 2:3` at the end with no silent change to 9:16. If a locked extreme ratio conflicts with the selected SD or HD limit, reports the incompatibility instead of modifying the ratio.

### Test 24 — Visible Text

**User:** `凌晨便利店门牌上必须出现短字“OPEN”，构图不变，给 Midjourney。`

**Expected:** Keeps the composition and places the short visible text in double quotation marks. Does not promise exact complex typography and does not add unrelated text-generation parameters.

### Test 25 — Explicit Legacy Version

**User:** `按 Midjourney V7 输出。`

**Expected:** Treats V7 as an explicit legacy target, checks its compatible reference and parameter workflow, and does not silently relabel V8.2 Edit Model behavior as V7. An unqualified follow-up request returns to V8.2 only if the user changes or clears the established legacy target.
