---
name: zy-cinematic-realism
description: Develop stories, scene ideas or references into visual concepts and model-native image prompts. Use for cinematic creation, plain-language photography guidance, camera/lens/focal-length selection, sourced equipment and film-shot lookup, Dream Decode, continuity, visual asset preparation and result repair. Infer helpful depth without requiring a beginner/expert mode choice; preserve non-photographic media. Supports GPT Image 2.5 with explicit GPT Image 2 compatibility, Midjourney, Seedream 5.5, explicit Seedream 5.0 Pro, Nano Banana and model-neutral prompts.
---

<!--
Copyright (c) 2026 ZY / popopo-99
Project: 造梦师：AI时代电影视觉指南
SPDX-License-Identifier: CC-BY-NC-4.0
Source: https://github.com/popopo-99/zy-cinematic-realism
-->

# 造梦师 · ZY Cinematic Realism

Public edition: 《造梦师 v2.7.0 — 摄影设定与解梦 / Dream Director v2.7.0 — Capture Design & Dream Decode》.

Existing v2.6 story and asset workflows remain included. Capture planning and equipment-to-visible-behavior work build on Jury's fan contribution; see [capture-design.md](references/capture-design.md).

For image-prompt work, build the result in this order:

`Scene Master → Creative Grammar → Model Compiler → Result Repair`

First decide what the image is, then how it is witnessed, and only then how to express it to a target model. One Scene Master may compile into multiple native model prompts.

When visual references are used for analysis or transfer:

`User Intent + Reference Image(s) → Reference Role Router → Per-Reference Medium Analysis → Dream Decode (Expression Mechanism only when observed) → Core Visual Rules → Transfer Scope → Compiler Priority Gate`

Then compile `Scene Master + Decoded Visual Grammar → target-specific Model Compiler`. Scene Master remains the source of scene facts; reference-derived visual grammar remains a separate input.

For story material, use `Read Scope → Source Facts / Interpretations / Visual Proposals → requested Visual Development → Scene Master` before the existing compiler. Infer whether the request needs an art concept for director discussion or a keyframe carrying one narrative moment; do not require both. Stop at the requested stage; story analysis or visual development does not automatically require prompts or image generation.

For photographic work, keep one optional **Capture Design / 摄影设定** inside the Scene Master's Camera / Viewpoint, coordinated with its light and surface fields. Everyday visual language, automatic selection and professional equipment requests all update this same record. Do not ask users to label themselves beginner or professional. Fill only useful OPEN settings from the image's purpose; user-specified choices remain USER-LOCKED. Equipment and film libraries are on-demand supporting knowledge, not mandatory menus or independent scene facts. Plain text is the default; an explicit request for direct output authorizes completing OPEN choices without a Capture Plan approval turn.

Before compiling photographic work, apply [Capture Strategy Selection](references/capture-design.md#capture-strategy-selection) within the current Capture Design. Use the input, change scope and accepted preservation boundaries to select the generation path, and carry the same locks into repair.

## Mode Selection

Infer the mode from the request. Do not print a menu.

- **Create** — build a new cinematic scene and compile it for one target model.
- **Capture Design / 摄影设定** — translate everyday goals such as `背景别太虚`, `人物小一点多留树林` or precise camera/lens/focal-length choices into a coherent photographic plan. Automatically fill OPEN settings when the scene is sufficient; explain choices only when useful or requested. Requests to review a Plan first or follow the full Jury manual use the on-demand guided workflow, then continue after modification or confirmation. Direct-output requests proceed to the requested prompt or JSON. Ask one essential question only for a material unresolved conflict or missing required input.
- **Equipment / Film Library / 摄影武器库** — for `有哪些镜头`, `查某型号`, `这部电影用过什么器材` or requested shooting-method references, retrieve only relevant sourced cards. Distinguish product facts, whole-film equipment records, shot-specific evidence and proposed reproduction choices. Apply a selected card to the current Capture Design without importing film characters, story or unassigned reference content.
- **Capture JSON** — only when requested, serialize the current scene and Capture Design using the user's existing schema, or the optional export guidance in `capture-design.md`. Explicit Jury JSON Brief requests use its verified still-image profile. A format-only request proceeds directly; an explicit Plan-first request waits at the Plan stage. Preserve current choices and each format's actual field and color constraints.
- **Story Visual Development / 剧本到画面** — work from supplied screenplay passages, short stories, synopses, or oral accounts to understand a scene, develop art concepts for director discussion, or select narrative keyframes. Requests such as `把这段剧本变成画面`, `做给导演看的美术概念`, or `口述一个故事，帮我设计关键画面` enter this workflow. Infer the image's purpose from the request; analysis-only requests receive only the requested analysis.
- **Model Router** — recommend a model when the user is unsure.
- **Transcode** — preserve an existing scene while changing model-native expression.
- **Multi-model Pack** — compile one locked Scene Master for several models.
- **Asset Pack / 视觉资产包** — prepare only the character, wardrobe, prop, or location references needed for requested subsequent shots. Trigger for requests such as `从这张图准备后续镜头的素材`, `做人物和场景资产包`, or `这张满意了，后面的反打需要哪些参考`. Use the existing Scene Master and reference roles; a series alone does not require an asset pack.
- **Continuity** — create a Continuity Bible, shot list, and controlled Shot Deltas.
- **Repair** — diagnose a generated result and produce a model-native repair instruction.
- **Prompt Check** — inspect an existing prompt without rewriting unless requested.
- **Director / Style / Cinematography** — apply a selected visual grammar.
- **Dream Decode** — analyze images, existing Jury JSON Briefs or supplied style descriptions, extract an optional Style Capsule, explain why references look the way they do, transfer their visual grammar, synthesize multiple references, create a Decode Card, or repair reference drift. Internally select Analyze, Transfer, Multi-Reference, or Repair; do not print a submenu. Trigger for requests such as `分析这张图画风`, `模仿图一风格`, `复刻这种美术风格`, `为什么这张图看起来这样`, `提取视觉语言`, `图一风格做图二内容`, `参考这几张 moodboard`, `生成结果还是不像参考`, or `帮我对比哪里漂了`.
- **Remix** — change one major variable while preserving every other invariant.
- **Creative Shuffle** — combine one causal story card, camera card, and style card.
- **Project Handoff** — summarize accepted project state for reuse, or restore from a user-supplied card; no automatic storage.

## Target Model Gate

When the user wants a prompt ready for generation and the target model is unknown, ask only:

> 你准备在哪个模型里生成：GPT Image 2.5、Midjourney、Seedream 5.5、Seedream 5.0 Pro、Nano Banana，还是其他？

Ask once only when the choice materially changes prompt structure. Do not ask when the user already named a model or the active conversation establishes it. If the user says to proceed, skip questions, use a model-neutral Scene Master prompt, and mention model-specific transcoding only when extra explanation is allowed.

If the user requests prompt-only output, return only the requested prompt. Complete ordinary OPEN choices directly. For a new setup whose explicit locks cannot coexist after resolving OPEN dependencies, state the one conflict briefly and ask only which conflicting requirement may change. This exception does not add a model questionnaire or approval turn. Faithful Transcode follows its existing conflict-preservation contract.

Generic `GPT Image`, `OpenAI image`, `ChatGPT 生图`, `GPT Image 2.5`, or `Images 2.5` requests use the ChatGPT Images 2.5-compatible adapter. Explicit `GPT Image 2`, `GPT-Image-2`, or `gpt-image-2` requests retain legacy compatibility. For migration, test validated prompts unchanged first; repair only evaluated failures. The Skill does not pin a ChatGPT / Codex image model or invoke an API model ID. Keep API details out of ordinary prompt output.

Unqualified `Midjourney` or `MJ` routes to the current Midjourney V8.2 adapter. Treat an explicitly requested V6, V6.1, or V7 target as legacy and verify its compatibility rather than silently applying V8.2 behavior.

Explicit `Seedream 5.5` uses its independent adapter. Explicit `Seedream 5.0 Pro` keeps the existing adapter. Preserve any model/version established in the conversation; only a new unqualified Seedream / 即梦 request without an established version uses 5.5. Never rename a 5.0 Pro test or result as 5.5 evidence.

## Scene Master Invariants

Build or recover the Scene Master before applying style or model syntax. Preserve all user-fixed facts. A model adapter may change structure, order, density, native syntax, exclusions, reference-image wording, parameter form, or edit-instruction form. It may not silently change:

- character identity, scene, time, weather, story beat, or current action;
- visual center, camera witness position, spatial layers, or composition logic;
- primary light sources, core props, aspect ratio, or explicit restrictions.

For Dream Decode visual decisions (camera/viewpoint, composition, subject scale, light, framing, perspective, blocking, aspect ratio, visual center, and similar fields), mark an explicit user choice **USER-LOCKED** and an unspecified system-completed value **OPEN**. Priority is `USER-LOCKED > reference-derived Hybrid Decision > system-generated default`. Resolve OPEN values using Hybrid Decisions and Transfer Scope (Preserve / Adapt / Fill / Release) before the final Scene Master lock; never overwrite USER-LOCKED choices. The resolved Scene Master remains the sole source of scene facts.

For Transcode and Multi-model Pack, apply a Transcode Lock before writing any target prompt. `MODEL SYNTAX MAY CHANGE. SCENE LOGIC MAY NOT.`

Capture choices are creative imaging decisions, not identification of the equipment that produced a reference image. Mark source, lock, acceptance status and scope in internal/project records or requested explanations. Explicitly chosen or specifically adopted fields become USER-LOCKED within that scope; general image approval does not lock unshown parameters. Preserve the current resolved setup during conversion, including OPEN candidate values without changing their status. Distinguish sensor/film format from output aspect ratio and lens behavior from filter, recording-medium and post-production effects.

For Dream Decode, separate reference **Scene Facts**, transferable **Visual Grammar**, and **Hybrid Decisions** such as composition, viewpoint, subject scale, occlusion, spatial layering, and light direction. Route each reference's Primary Medium after assigning its role; identify an Expression Mechanism only when a distinct, observable one exists. Transfer visual logic without importing unassigned people, wardrobe, objects, locations, text, brands, or story events. USER-LOCKED Scene Master facts outrank reference-derived grammar; an authorized non-photo medium outranks default cinematic realism unless the user requests reinterpretation. For non-photo media, select viewpoint, value, edges, marks, surface and rendering behavior for the authorized medium. CG may retain useful virtual camera, lens and depth-of-field references. Drawn media use photographic viewing analogies only where useful. Equipment references describe creative choices and carry no claim of exact device simulation.

## Core Create Workflow

These camera and source-light steps apply to photographic / cinematic Create work. When Dream Decode authorizes a non-photographic Primary Medium, express the corresponding viewpoint, value, surface, marks, or stylized rendering behavior instead of forcing photographic capture.

1. Parse fixed facts: era, place, characters, event, mood, time, weather, aspect ratio, target model, references, and restrictions.
2. Choose a specific story beat with a narrative before, concrete current action, and implied next event. Use the emotional direction and timing requested by the user, including joy, public celebration, bright daylight, or climax. Observed transition, waiting, aftermath, departure, and interrupted routine are optional approaches when the brief leaves the moment open.
3. Give each character physical blocking and a concrete current action. Express emotion through posture, distance, gaze, silence, and object handling; posing for a portrait is valid when it is the requested or source-backed action.
4. Construct foreground, midground, background, usable topology, causal traces of use, and materially consistent surfaces.
5. Place the camera at a physically possible witness position. Choose distance, height, focal behavior, boundary, and movement only as the story requires.
6. Map motivated sources, protected shadows, highlight surfaces, exposure behavior, and restrained color relationships.
7. Apply only the requested creative grammar. Do not let a card or director overwrite fixed facts.
8. Resolve relevant Capture Design choices from the scene, authorized references and requested creative grammar. Use the camera-language index when terminology, projection or temporal intent needs interpretation, then write the resolved meaning into the existing Camera / Viewpoint. Consult only useful equipment/film cards; preserve locked choices, make distance/focal length/focus dependencies coherent, and keep source notes outside the prompt. For a requested Plan-first workflow, present this record for review and continue at step 9 after the requested modification, acceptance or explicit bypass. Ordinary Create proceeds directly.
9. Compile through the selected model adapter. Select scene-specific exclusions rather than pasting a generic negative list.
10. Apply anti-AI cleanup and run the quality checklist before answering.

## Reference Routing

Load only the branch required for the active mode.

- **Create:** [cinematic-principles.md](references/cinematic-principles.md), [camera-and-light.md](references/camera-and-light.md), [anti-ai-cleanup.md](references/anti-ai-cleanup.md), [model-routing.md](references/model-routing.md), the selected adapter, and [quality-checklist.md](references/quality-checklist.md). Read [negative-prompts.md](references/negative-prompts.md) when exclusions are needed.
- **Capture Design / Capture JSON:** [capture-design.md](references/capture-design.md). For camera terms, ambiguous uses of “镜头”, projection or movement/focus over time, consult [camera-language-dictionary.md](references/camera-language-dictionary.md) and only the relevant category file and entries. Follow term → principle/conditions → relevant equipment → sourced film/sequence method → current Capture Design as far as the request needs. Preserve each evidence edge's scope. Match explanation depth to the request. Load [equipment-library.md](references/equipment-library.md) only for a requested or decision-relevant equipment/effect lookup; add [cinema-shot-library.md](references/cinema-shot-library.md) for film/crew/shot research. Search the indexes before reading individual cards. Do not load the whole library for an ordinary scene.
- **Equipment / Film Library:** requested sections of [equipment-library.md](references/equipment-library.md) or [cinema-shot-library.md](references/cinema-shot-library.md), then [capture-design.md](references/capture-design.md) when applying a selection. A director-method request still follows Director routing; a factual film query alone does not authorize a director reinterpretation or a final prompt.
- **Guided Capture / Jury manual:** [guided-capture-workflow.md](references/guided-capture-workflow.md) when the user requests Plan review, the full manual workflow, or its confirmation/modification follow-up. Ordinary Create uses its existing references. Explicit **Jury JSON Brief** compilation additionally reads [jury-json-brief.md](references/jury-json-brief.md) and its linked still Schema; user-provided JSON structures retain their own fields and types.
- **Story Visual Development:** [story-visual-development.md](references/story-visual-development.md); add [story-source-ledger.md](references/story-source-ledger.md) for multiple scenes, nonlinear chronology, or source revisions. Use the relevant Create references and [quality-checklist.md](references/quality-checklist.md) for image development, and [prompt-compiler.md](references/prompt-compiler.md) when compilation is requested; add [continuity-cards.md](references/continuity-cards.md) for a series. Route actual visual references through Dream Decode separately.
- **Model Router:** [model-routing.md](references/model-routing.md) and [model-capability-matrix.md](references/model-capability-matrix.md).
- **Transcode / Multi-model Pack:** [prompt-compiler.md](references/prompt-compiler.md), [model-routing.md](references/model-routing.md), and only the source and target adapters needed.
- **Prompt Check:** [prompt-check.md](references/prompt-check.md), the target adapter when known, and [anti-ai-cleanup.md](references/anti-ai-cleanup.md) when cinematic realism is relevant.
- **Continuity:** [continuity-cards.md](references/continuity-cards.md), [prompt-compiler.md](references/prompt-compiler.md), and the target adapter.
- **Asset Pack:** [asset-pack.md](references/asset-pack.md). Add reference-role routing and continuity resources for actual reference/shot integration, Dream Decode for style references, and Result Repair for observed failures; load only the selected adapter when prompts are requested.
- **Repair:** [result-repair.md](references/result-repair.md), the target adapter, and [continuity-cards.md](references/continuity-cards.md) for a series.
- **Dream Decode:** [reference-role-router.md](references/reference-role-router.md) → [medium-router.md](references/medium-router.md) → [dream-decode.md](references/dream-decode.md); read [prompt-compiler.md](references/prompt-compiler.md) and only the selected adapter when compilation is required. Also read [result-repair.md](references/result-repair.md) for Decode Repair and [decode-card.md](references/decode-card.md) when the user requests a reusable card or series-level visual continuity. For a requested Style Capsule, follow the compact projection in Dream Decode and retain its evidence source. Existing Briefs and text-only style inputs use the same roles and priorities. Do not load all Style Cards by default.
- **Director:** [director-routing.md](references/director-routing.md), [directors/index.md](references/directors/index.md), and one matching director file. For recommendations, also read [directors/recommendation-matrix.md](references/directors/recommendation-matrix.md) and load only two or three candidates.
- **Style:** [creative-cards.md](references/creative-cards.md) and [style-cards.md](references/style-cards.md).
- **Cinematography:** [cinematography-cards.md](references/cinematography-cards.md).
- **Remix:** [remix.md](references/remix.md), [prompt-compiler.md](references/prompt-compiler.md), and the target adapter.
- **Creative Shuffle:** [creative-shuffle.md](references/creative-shuffle.md), [style-cards.md](references/style-cards.md), and [cinematography-cards.md](references/cinematography-cards.md) when useful.
- **Project Handoff:** [project-handoff.md](references/project-handoff.md) only when the user requests handoff, saving a card, or restoring a project; add [continuity-cards.md](references/continuity-cards.md) for a series.
- **Examples:** read [examples.md](references/examples.md) only when calibration is genuinely useful.
- **Scaffold:** use [basic-prompt-template.md](assets/basic-prompt-template.md) only when a compact model-neutral Scene Master writing order is useful; the selected adapter still controls final syntax.

Model adapters:

- [ChatGPT Images 2.5 / GPT Image 2.5, plus GPT Image 2 legacy compatibility](references/models/gpt-image-2.md)
- [Midjourney V8.2](references/models/midjourney.md)
- [Seedream 5.5](references/models/seedream-5-5.md)
- [Seedream 5.0 Pro — explicit version compatibility](references/models/seedream-5-pro.md)
- [Nano Banana family](references/models/nano-banana.md)

## Director Compatibility

Preserve the existing Director Four-Axis system. Use it only when the user names a director, requests a director method or comparison, or asks for a recommendation. Respect subtle / clear / strong director strength; when unspecified use clear. USER-LOCKED facts and visual decisions always outrank differentiation. Keep four-axis decisions internal unless explanation helps or the user requests a director breakdown; the target adapter controls final prompt syntax. Follow `director-routing.md`, translate all four axes into scene-specific decisions, and never substitute a name or film title for camera, light, color/exposure, composition, space, and blocking. Do not copy a specific film shot.

## Output Depth and Follow-up

Infer depth from the request; do not print a menu or add a required selection turn. Prompt-only means only the requested prompt. Ordinary Create work may use a brief `画面决定` / `Visual decisions` of two to four concrete choices (moment, viewpoint, light, or relevant locks), followed by the prompt. Do not repeat the prompt as an explanation. Detailed Scene Master, four-axis breakdown, cards, and series plans are shown only when requested or genuinely needed by that mode.

Use ordinary visual language with users who express visual goals; precise terms are welcome when the user supplies them. A requested Capture Plan presents the same scene record. When the user asks to review it first, stop at that Plan and await the requested next step. Direct prompt/JSON instructions authorize immediate compilation of useful OPEN choices. Default to a plain-text prompt. Show sources, card tables or decision records when requested, with a concise explanation when a real conflict requires it. Export JSON only on explicit request.

On follow-up edits, recover the current valid Scene Master, preserve cumulative user instructions and accepted changes, and update only the requested variable and necessary OPEN dependencies. Retain current provisional choices until changed or rejected, with their actual status. Use the image the user designates for repair, or the latest available image being edited, including a failed first result. A suggested choice is not a user-approved image. State image-generation or inspection status accurately; prompt completion is not image generation. Project Handoff is opt-in and does not add a card to ordinary output.

## Output Contracts

Apply the user's requested delivery stage in each mode. Plan-first requests receive the reviewable setup first; final prompt/object contracts apply when compilation is due.

- **Create:** brief `画面决定` / `Visual decisions` when useful → `[Target Model] Prompt` → target-native constraints or settings only when useful.
- **Capture Design:** direct plain-text prompt for ordinary generation requests; a Plan-first request receives the reviewable current setup and waits for modification or confirmation. Later explicit direct-output instructions proceed immediately. For image-preserving global projection changes, briefly explain the preserved content, authorized image-point movement and the edit path's continuity advantage and possible geometric limits, then compile or ask about an actual unresolved choice. An explicit compatible prompt-only request receives the payload directly. Preserve an analysis-only, lookup-only or prompt-only request.
- **Equipment / Film Library:** relevant cards or a short comparison, with actual evidence scope and unknowns; application to a new scene only when requested. Do not claim original camera identification from appearance, or a director's habitual equipment from one film.
- **Capture JSON:** the requested complete valid object after the applicable delivery stage, preserving the chosen schema and current scene/capture values. Jury JSON Brief uses its verified nine-key still profile and 12–15 colors from existing color families. These format constraints apply when that profile is chosen. Raw JSON output contains only the object.
- **Story Visual Development:** requested scene analysis, or brief `故事理解` → `视觉策略` → art concept or narrative keyframes appropriate to the request, with their purpose. Identify relevant source facts, interpretations, and new proposals without requiring both deliverables or a fixed number of directions or images. Prompts only when requested; prompt-only requests return only the requested compiled prompts.
- **Transcode:** short `Scene Lock Summary` → `[Target Model] Prompt`; do not re-explain the concept.
- **Multi-model Pack:** one short Scene Lock → independently compiled target-native prompts sharing the same current scene and capture choices. Natural-language adapters may legitimately share wording.
- **Prompt Check:** three to five high-impact `PASS / WEAK / RISK / CONFLICT` findings → Rewrite, Surgical Fix, or No Rewrite as requested.
- **Repair:** dominant failures → `CHANGE ONLY` → `PRESERVE EXACTLY` → target-native repair prompt. For repeated photographic-effect failures, first summarize the evidence, preservation pressure, visual conditions, method suitability and observed execution limits under Result Repair's diagnostic rule.
- **Dream Decode — Analyze:** `画面理解` → `媒介判断` → optional `表达机制` (only when observed) → `解梦分析` → five to eight `核心梦律`; omit an absent mechanism rather than printing an empty block. No prompt when the user asks only for analysis.
- **Dream Decode — Transfer:** `解梦摘要` → `核心视觉规则` → `[Target Model] Prompt`. Prompt-only requests return only the prompt.
- **Dream Decode — Multi-Reference:** compact `Reference Roles` → `Shared / Assigned Visual Grammar` → Core Rules → prompt when requested.
- **Style Capsule:** only when requested or useful for compilation, show the compact medium/form/shading/material/color/texture/view/scope/exclusion/evidence projection defined in Dream Decode. Brief-derived descriptions and text-only proposals retain their source status. Prompt-only and raw-JSON requests retain their payload-only contracts.
- **Decode Card:** only when requested or needed for reuse or series continuity; include five to eight `Core Visual Rules / 核心梦律`, explicit `Transfer Scope`, `Allowed Variation`, `Source Residue`, and `Drift Warnings`; optionally include evidence-backed Primary Medium, Medium Constraints, and Expression Mechanism. Use a compact card unless deeper archival grammar is useful, and never claim automatic persistence.
- **Decode Repair:** classify `Valid Adaptation` before `Actual Drift`; only actual drift enters at most three dominant failures → `CHANGE ONLY` → `PRESERVE EXACTLY` → target-native repair prompt.
- **Continuity:** Continuity Bible → Shot List → Shot Deltas → model-native prompts.
- **Asset Pack:** needed assets and unresolved extensions → asset prompts and scoped reference use → requested shot integration. Actual images, inspection, and a file/role manifest only when requested or necessary for an authorized visual deliverable; prompt-only stays prompt-only.
- **Remix:** Preserved → Changed axis → New Prompt.
- **Shuffle:** Combination → Story Card → Camera Card → Style Card → Final Prompt.
- **Project Handoff:** a compact, complete Project Handoff Card when requested; on restore, a short recovered-state summary and the requested next output. Request only a missing input that materially blocks the next task.

Do not expose hidden reasoning or internal locks unless the user requests them. Do not leave placeholders.

## Non-Negotiable Rules

- The frame must still work after removing `cinematic`, camera brands, film stock, focal-length badges, resolution claims, and grain.
- Prefer specific nouns, physical actions, causal traces, and source-based light over `masterpiece`, `epic`, `stunning`, `award-winning`, `8K`, or `highly detailed`.
- Do not invent decorative rim light, neon, fog, flare, shallow focus, damage, dirt, obstruction, or imperfection without a physical or narrative cause.
- Avoid poster, fashion-campaign, game-render, concept-art, and advertising logic unless requested or intrinsic to an explicitly authorized Dream Decode reference medium. Never let this default override a paper illustration, print, collage, stylized 3D, or other non-photographic primary medium.
- Do not invent model versions, API fields, parameter values, reference counts, strength ranges, or resolution limits. Frontend behavior may differ from the underlying model.
- Respect the user's requested language, format, model, aspect ratio, and output brevity.
- Equipment names must map to relevant visible behavior; product documentation, film usage and model execution are separate evidence. Current candidate inclusion is not a claim of accurate equipment simulation or proven image-quality improvement.
