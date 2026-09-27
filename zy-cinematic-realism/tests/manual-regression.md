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

## Test 04 — Legacy GPT Image 2

**Setup:** Supply a completed model-neutral or other-model prompt.

**User:** `转成 GPT Image 2。`

**Expected:** Retains the explicit GPT Image 2 legacy target (also test `GPT-Image-2` and `gpt-image-2`). Scene facts do not change. Output uses a natural-language production brief with integrated constraints; it does not silently relabel the target as 2.5.

## Test 05 — Transcode Lock

**Setup:** Supply a Midjourney prompt with clear character, action, camera, light, visual center, time, and weather.

**User:** `转成 Seedream 5.0 Pro。`

**Expected:** Character, action, camera position, light sources, visual center, time, weather, aspect ratio, props, and restrictions remain identical. Only model-native expression changes.

## Test 06 — Multi-model Pack

**User:** `同一个画面分别输出 GPT Image 2.5、Midjourney、Seedream 5.0 Pro、Nano Banana Prompt。`

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

## GPT Image 2.5 Compatibility Regression

### Test 26 — GPT Image 2.5 default routing

**Setup:** Supply a locked scene, with no established legacy target. Run each alias in a fresh conversation.

**User:** `编译成 GPT Image。` Also test `OpenAI image`, `ChatGPT 生图`, `GPT Image 2.5`, and `Images 2.5`.

**Expected:** Uses the current ChatGPT Images 2.5-compatible adapter at the unchanged `models/gpt-image-2.md` path. Does not ask which OpenAI version, require special syntax, invent API fields, or claim installation selects the underlying model.

### Test 27 — Migration unchanged prompt

**Setup:** Supply the validated GPT Image 2 brief from Test 16 with the same reference images and 2:3 aspect-ratio intent.

**User:** `升级到 GPT Image 2.5，先比较效果。`

**Expected:** Tests the exact prompt unchanged first, with the same references, scene facts, aspect-ratio intent, and constraints where practical. No reordering, beautification, new story, or automatic rewrite for the version number. Evaluates specific failures before changing prose; does not claim generated-image evaluation occurred when no images were generated. For API comparison, preserves supported settings and considers quality levels before rewriting.

### Test 28 — Edit preserve/change

**Setup:** OpenAI 2.5 editing; provide a car image with accepted geometry, camera, environment, and light.

**User:** `只把汽车从黑色改成白色，其他不变。`

**Expected:** `CHANGE ONLY` identifies the black painted body panels and their new white paint state. `PRESERVE EXACTLY` protects car identity, geometry, glass, tires, trim, viewpoint, framing, lighting relationships, background, and unaffected objects. White paint responds to the existing light; no new light sources or composition changes. No pixel-identical guarantee.

### Test 29 — Multi-reference roles

**Setup:** Provide A (identity), B (wardrobe), C (location), D (composition), and E (material/light), with conflicting clothing visible in A and B.

**User:** `人物按 A，服装以 B 优先，地点按 C，构图按 D，材质和光线参考 E。`

**Expected:** Assigns each supplied image its declared role, respects B's wardrobe priority, and does not infer one image controls everything. Does not invent reference data or attachment parameters. If a required role is ambiguous, identifies the conflict rather than silently choosing.

### Test 30 — API routing

**User A:** `需要大量快速 API generation，画质要达到现有 GPT Image 2 水平。`

**Expected A:** Recommends evaluating GPT-Image-2.5 Flare first on the unchanged baseline.

**User B:** `API 用于高精度复杂 editing，允许更长生成时间。`

**Expected B:** Recommends evaluating GPT-Image-2.5 Sunburst for precision, explains the time tradeoff, and avoids a permanent ranking. Both routes verify current documentation before emitting requested API parameters.

**User C:** `ChatGPT 生图，只给我汽车改白色的 Prompt。`

**Expected C:** Only the edit prompt, without API model IDs, quality fields, pricing, endpoint syntax, or a claim that the Skill forces a model version.

### Test 31 — Multi-turn preservation and related changes

**Setup:** Continue Test 28 using its accepted output and continuity locks.

**User:** `现在只让驾驶员侧车窗降下一半。`

**Expected:** One meaningful variable per edit: window state changes; the white paint and all unaffected locks remain. Restates critical preserve rules and inspects the result. If the user instead requests two closely related window changes together, may perform both without inventing additional edits.

### Test 32 — Repair only the evaluated migration failure

**Setup:** After Test 27, the user reports composition drift but confirms identity, paint, materials, and source lights are correct.

**User:** `只修构图漂移，其他已通过。`

**Expected:** Repairs the failed composition variable from the locked Scene Master, preserves the successful facts, and does not add quality buzzwords or redesign the scene. Without result evidence, reports evaluation as pending rather than claiming a model-quality improvement.

## Dream Decode Regression

### Test 33 — Style only

**Setup:** Supply a reference image showing a woman in a red dress beside a swimming pool and palm trees.

**User:** `只参考这张图的画风，生成一个月球基地里的宇航员。`

**Expected:** Routes the image to Visual Grammar. The new Scene Master contains the astronaut and lunar base but not the woman, red dress, pool, palm trees, or reference story event. Transfers only observed, relevant visual rules and keeps composition/camera conditional unless explicitly requested.

### Test 34 — Hybrid composition

**Setup:** Supply a reference dominated by architecture, with a very small person and extensive negative space.

**User:** `做人物近景肖像，但参考这个画风。`

**Expected:** Preserves the close-portrait intent. Releases the literal small-subject scale and adapts only compatible visual grammar; does not let distinctive reference composition override the new Scene Master.

### Test 35 — Multi-reference consensus

**Setup:** Supply three moodboard images. All use natural light, low saturation, partial foreground occlusion, and observed blocking, but their focal behavior differs.

**User:** `提取这几张图共同的感觉，做成同一套视觉语言。`

**Expected:** Uses Consensus Decode. Natural light, low saturation, occlusion, and observed blocking become Stable/Core Rules. Focal behavior is listed as a Variable Trait rather than averaged or locked.

### Test 36 — Role-based multi-reference

**Setup:** Supply four images.

**User:** `图一要颜色，图二要构图，图三要人物，图四要材质。`

**Expected:** Uses Role-Based Decode with explicit roles: A color, B composition, C identity, D material. Extracts only the assigned dimensions and does not search for a false consensus or let one image control the entire scene.

### Test 37 — Reference role conflict

**Setup:** Supply one image with distinctive lighting and composition.

**User:** `只参考图一灯光，不参考构图。`

**Expected:** Transfers observed light behavior only. Marks composition Do Not Transfer or Release; the reference composition does not contaminate the new Scene Master or final prompt.

### Test 38 — Analyze only

**Setup:** Supply one reference image.

**User:** `分析这张图为什么好看，不要给 Prompt。`

**Expected:** Outputs `画面理解`, `媒介判断`, useful `解梦分析`, and five to eight executable Core Visual Rules. Shows `表达机制` only when a distinct observable mechanism exists; an ordinary strong photograph or illustration may have none and must not invent an abnormal event. Does not output a prompt, target-model question, adapter settings, or hidden chain-of-thought.

### Test 39 — Dream Decode prompt only

**Setup:** Supply one usable style reference image.

**User:** `参考这个画风，给我 MJ Prompt，只要 Prompt。`

**Expected:** Returns only a Midjourney V8.2-native prompt. No analysis, routing table, menu, explanation, fabricated URL, style code, weight, or unsupported parameter.

### Test 40 — Decode Repair

**Setup:** Supply the original reference, accepted Scene Master, and generated result. Composition is correct; light and material have drifted.

**User:** `构图对了，但还是没有参考图的味道。只修真正漂掉的地方。`

**Expected:** Diagnoses Light Drift and Material Drift only. `CHANGE ONLY` repairs those variables; `PRESERVE EXACTLY` protects composition, camera, characters, action, space, and all other accepted facts. Does not redesign the whole scene.

### Test 41 — Decode Card

**Setup:** Complete a Dream Decode.

**User:** `把这个风格整理成以后可以复用的解梦卡。`

**Expected:** Produces a structured Decode Card with full Core Visual Rules, Medium in one dedicated location, Allowed Variation, Transfer Scope, Hybrid Decisions, Source Residue, and Drift Warnings. When a mechanism was observed, the card retains Abnormal Event, Subject–Event Coupling, Transferable Mechanism, and Surface Implementation; reusing the card alone without the original image preserves that relationship. Without a distinct mechanism, the entire section is absent. No permanent storage, memory, or database behavior is implied.

### Test 42 — Style Card conflict

**Setup:** Supply a reference image and request an existing Style Card whose behavior conflicts with part of the observed reference grammar.

**User:** `参考图里的真实视觉规律优先，同时用 Accidental Editorial 风格卡做辅助，冲突时以参考图为准。`

**Expected:** Uses the user's explicit reference-first priority. The predefined Style Card may supplement compatible dimensions but cannot silently override observed reference rules.

### Test 43 — Dream Decode multi-model compilation

**Setup:** Complete one Dream Decode and a new locked Scene Master.

**User:** `同一个解梦结果，分别给 GPT Image 2.5 和 Midjourney V8.2。`

**Expected:** Uses the same Scene Master, full Core Visual Rules archive, three to five scene-selected Active Core Rules, and Transfer Scope for both outputs. Compiles each independently through its adapter; GPT and Midjourney prompt shapes differ, but visual grammar and scene facts remain aligned. Does not translate one target prompt into the other.

### Test 44 — Scene contamination

**Setup:** Supply a style reference containing a visible brand, readable slogan, distinctive building, specific vehicle, and named product.

**User:** `只参考画风，换成一个普通乡村诊所的候诊室。`

**Expected:** Classifies the brand, slogan, building, vehicle, product, and original event as Scene Facts and keeps them out of the new Scene Master and prompt. Transfers only relevant visual grammar; visible text and architecture do not leak through as style.

### Test 45 — Forbidden terminology in Decode Card

**Setup:** Complete a Dream Decode and request a reusable card.

**User:** `整理成一张可复用的解梦卡。`

**Expected:** Uses `视觉语法`, `核心梦律`, and `Core Visual Rules`. The generated card must not use `视觉 DNA`, `Style DNA`, `Visual DNA`, `视觉基因`, `风格基因`, `Genome`, or another heredity metaphor as product language.

### Test 46 — Core Visual Rules compression

**Setup:** Supply a visually complex reference with distinctive composition, light, exposure, color, materials, space, blocking, and capture behavior.

**User:** `完整分析这张图，再提炼最关键的规则。`

**Expected:** The full Visual Grammar may be detailed, but Core Visual Rules contain only five to eight high-impact executable rules. They describe relationships or behavior rather than labels, source content, or a twenty-item analysis checklist.

### Test 47 — Explicit Transfer Scope in Decode Card

**Setup:** Complete a Dream Decode.

**User:** `整理成解梦卡。`

**Expected:** The card explicitly contains Strong Transfer, Conditional Transfer, and Do Not Transfer, or clear Chinese equivalents. Conditional items state Preserve, Adapt, or Release conditions; the scope is specific enough for later Decode Transfer.

### Test 48 — Hybrid valid adaptation

**Setup:** The reference uses a very small subject and extensive negative space. The new locked Scene Master explicitly requires a chest-up close portrait, and the generated result follows that requirement while retaining accepted light, exposure, color, and material rules.

**User:** `对比参考图和结果，看看哪里漂了。`

**Expected:** Marks the explicit chest-up portrait USER-LOCKED. Classifies the close framing as Valid Adaptation, not Composition Drift or Camera Drift. Does not ask the repair prompt to make the subject small again. Only unrelated, evidence-backed Actual Drift may enter `CHANGE ONLY`.

### Test 49 — Source Residue protection

**Setup:** Supply a visual-grammar reference containing an animal, visible brand, distinctive building, readable text, specific prop, and incidental background objects.

**User:** `只要视觉语言，整理成解梦卡。`

**Expected:** Lists the animal, brand, building, text, prop, and incidental objects under Source Residue and/or Do Not Transfer. None appears in Core Visual Rules. Later reuse does not import them into the new Scene Master.

### Test 50 — Compile from Core Rules

**Setup:** Supply a complete Decode Card containing detailed archival Visual Grammar, eight Core Visual Rules, Transfer Scope, Source Residue, Drift Warnings, and a new Scene Master whose composition is OPEN because the user did not specify it.

**User:** `按这张解梦卡给我 GPT Image 2.5 Prompt。`

**Expected:** Keeps all eight Core Visual Rules in the card but selects only three to five Active Core Rules in the final prompt. An authorized reference-derived composition may Fill the OPEN Scene Master decision ahead of a system default; USER-LOCKED facts remain intact. Does not paste or paraphrase the complete card, Source Residue, archival explanation, optional naming, or unused fields into the final prompt.

## Image-level Dream Decode Regression / 图像级解梦回归（人工）

This is a **manual image-generation protocol, not an automated harness**. No score below is claimed as executed. For each case, run **at least three paired comparisons**. Within every pair, hold the same reference image(s), user intent, new Scene Master, target model/version, aspect ratio, and visible generation settings. Use the same seed or equivalent condition when available; otherwise run three independent pairs under the same visible conditions. The only main variable is the prompt: a fair baseline containing the user request and a reasonable basic prompt **without full Dream Decode**, versus a Dream Decode-enhanced prompt using Primary Medium, optional Expression Mechanism, three to five Active Core Rules, and Transfer Scope. Never deliberately weaken the baseline. Compare actual generated images blind where possible; save every prompt and output. Repeat on each relevant model separately; model noncompliance is not automatically a decode defect.

Human reviewers score each output 1–5: **Medium Fidelity** (making logic), **Visual Grammar Fidelity** (core rules), **Expression Fidelity** (mechanism; **N/A** if none exists), **Scene Integrity** (fixed facts), **Content Leakage** (5 = no source residue, 1 = severe leakage), and **Creative Value (Human Review Only)**. Record evidence, not just numbers. For each case record Enhanced wins / Baseline wins / Ties across at least three pairs; a single better image is not a pass. Look for stable improvement in applicable Medium, Visual Grammar, and Expression Fidelity without meaningful damage to Scene Integrity, Content Leakage, or Creative Value. Attribute failures to **Decode Logic, Medium Routing, Reference Role, Expression Mechanism, Transfer Scope, Compiler, Target Model Compliance, or Unknown**. Human judgment is required.

Use three reference sets: **A — light paper illustration**, where the risk is photographic conversion, artificial depth, or lost pigment/paper edge behavior; **B — stylized 3D**, where the risk is live-action conversion, glossy generic game rendering, or lost shape/shading grammar; **C — Dream Eye**, where the subject itself carries the abnormal event, and the risk is moving the magic to the background or copying source objects. Secure suitable rights-cleared references and record their identity locally before execution.

### Case 51 — Paper Medium Override (A)

New scene: a woman waiting in a quiet station. Style-only A, compiled for GPT Image. Expected: paper/pigment edges, shallow layered depth, and scene facts; no photoreal skin, camera/capture structure, or cinematic lens look. If A has no distinct expressive event, Expression Mechanism is omitted and Expression Fidelity is N/A.

### Case 52 — Mixed Medium (A + compatible secondary)

New scene: a street food stall at dawn. Explicitly request A's colored-pencil paper surface combined with B's stylized-3D spatial geometry. Expected: Host Medium = paper-based colored pencil; Secondary Construction Rule = B's spatial geometry only, without glossy PBR or cinematic volumetric lighting. This explicit cross-medium fusion is not automatic averaging.

### Case 53 — Role vs Medium (A + identity image)

New scene: the identity reference's person reading indoors; A controls medium, second image identity only. Expected: identity transfers without the identity image's photographic medium taking control.

### Case 54 — Medium Conflict (A + B)

Both references explicitly assigned medium authority with no host, construction rule, or priority. Expected before generation: conflict noted and one focused question; no silently averaged paper/3D prompt. If priority or an explicit Host Medium + Secondary Construction Rule is then supplied, generate and score the resolved version.

### Case 55 — Dream Eye Mechanism (C)

New scene: a different subject in a different setting. Expected: abnormal transformation stays coupled to the subject's own eye/body; atmospheric background effects alone fail Expression Fidelity.

### Case 56 — Mechanism Transfer (C)

New scene: a musician undergoing a different subject-local transformation. Expected: transferable cause–subject relationship and emotional function survive without copying the source's exact eye form or props.

### Case 57 — Mechanism Drift Repair (C)

Start from a result with correct scene and medium but background-only magic. Expected: Actual Mechanism Drift; `CHANGE ONLY` restores subject–event coupling, while `PRESERVE EXACTLY` locks successful facts and medium.

### Case 58 — Medium Drift Repair (A)

Start from a result with correct scene but photoreal rendering. A has no distinct Expression Mechanism. Expected: Actual Medium Drift only; smallest correction restores paper edges, pigment, and layering without inventing or repairing a mechanism or rewriting the scene.

### Case 59 — Prompt Overload (A)

Use a verbose Decode Card with eight full Core Visual Rules and many archival notes; the new Scene Master leaves composition OPEN. Expected: the authorized reference composition can Fill OPEN ahead of a system default. The final prompt retains USER-LOCKED facts, primary medium, optional observed mechanism, only three to five Active Core Rules, scope, and relevant grammar; no full-card dump or low-value negative list.

### Case 60 — Cinematic Override (A and B separately)

Use a new scene with dramatic light but no request for photoreal reinterpretation; include GPT Image runs. Expected: A stays paper illustration with medium-appropriate viewpoint/value/mark language; B stays stylized 3D with form/surface/stylized-light language. Neither becomes photographic, glossy generic CG, or generic concept art merely because the Skill's broader domain is cinematic.
