<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Dream Decode / 解梦

Dream Decode explains why one or more reference images look the way they do, extracts the visual rules that can survive a change of subject or story, and connects those rules to the existing Scene Master and Model Compiler. It is not a generic image description, a keyword harvest, or a prompt-to-prompt rewrite.

Use Dream Decode only when the user wants visual analysis, visual-language transfer, multi-reference synthesis, or comparison between a reference and a generated result. An attached image alone does not activate this workflow. Ordinary removal, replacement, or local image editing may use the normal editing or Result Repair path.

Core contract:

`TRANSFER VISUAL LOGIC. PRESERVE NEW SCENE INTENT.`

Stable pipeline:

```text
User Intent + Reference Image(s)
→ Reference Role Router
→ Per-Reference Medium Analysis
→ Dream Decode
→ Scene Facts + Visual Grammar + Hybrid Decisions + optional Expression Mechanism
→ Core Visual Rules
→ Transfer Scope
→ Compiler Priority Gate
→ Scene Master + Decoded Visual Grammar
→ target-specific Model Compiler
→ Generated Result
→ Decode Repair (Medium / Mechanism / Visual drift)
```

Scene Master remains the source of truth for scene facts. Visual Grammar is the complete reference-derived archive. Core Visual Rules are its five-to-eight-rule high-impact archive; the final prompt selects three to five Active Core Rules. Transfer Scope decides which rules and supporting grammar enter the new scene.

Run [medium-router.md](medium-router.md) on each reference after its role is assigned. Its Primary Medium and Medium Constraints are independent of camera realism defaults. A style reference's authorized paper, print, illustration, collage, or stylized-3D medium must survive compilation unless the user explicitly requests a realistic / cinematic reinterpretation.

## Three-Layer Decode

Separate every observation into three layers before transferring anything.

### A. Scene Facts

Facts specific to the reference image: character identity, apparent age or gender, wardrobe, location, architecture, props, vehicles, animals, story event, visible text, logos, and brand elements.

These facts do not transfer from a style or visual-grammar reference unless the user explicitly assigns them a role. Never disguise reference content as style.

### B. Visual Grammar

Transferable relationships and behaviors: image medium, color relationships, contrast and exposure behavior, light behavior, material treatment, surface response, texture scale, edge behavior, detail density, capture or rendering character, editorial or observational tendencies, imperfection, and scene-specific anti-clichés.

Describe relationships rather than labels. Replace `moody`, `cinematic`, or `vintage` with observable rules about source light, shadow density, subject-environment scale, surface response, or capture behavior.

### C. Hybrid Decisions

Decisions that may serve both scene intent and visual grammar: composition, camera height and distance, subject scale, focal behavior, framing boundary, occlusion, foreground framing, negative space, spatial layering, symmetry, blocking relationships, and light direction.

Do not automatically lock or discard these decisions. Resolve each one against:

1. the user's new scene intent and fixed facts;
2. the assigned Reference Role;
3. the Transfer Scope;
4. physical and narrative requirements in the Scene Master.

Mark user-specified visual decisions **USER-LOCKED** and unspecified, system-completed decisions **OPEN** in the Scene Master. Priority: `USER-LOCKED > reference-derived Hybrid Decision > system-generated default`. Hybrid Decisions may Preserve, Adapt, Fill, or Release an OPEN decision before final compilation; they may not overwrite a USER-LOCKED one. For example, keep a user-requested close portrait despite a wide reference, but let a reference's viewpoint fill an OPEN camera choice when it fits the new scene. Scene Master remains canonical after resolution.

## Expression Mechanism / 表达机制

Expression Mechanism is **optional**. Extract one only when the reference has a distinct, observable, executable expressive event: a subject or spatial rule changes unusually; material, group, temporal, reflection, light, or body relationships perform a clear narrative or psychological function; or a visual event is central rather than decorative. If none is observed, record internally `Expression Mechanism: Not required` and omit the user-visible block. Attractive color, unusual composition, atmosphere, loneliness, prestige, cinematic quality, or dreaminess alone do not qualify. Never invent an abnormal event or relabel a Core Visual Rule as a mechanism. When present, record one primary mechanism with up to two or three related execution points. Core Visual Rules specify repeatable visual identity; the mechanism specifies the event–subject relationship behind expressive force.

- **Abnormal Event:** what departs from ordinary visual or narrative expectation.
- **Event Locus:** where that departure occurs—subject, body, object, environment, space, or the relationship between them.
- **Subject–Event Coupling:** whether the subject causes, undergoes, witnesses, or is structurally inseparable from the event.
- **Emotional Function:** the effect produced by that coupling, stated as a cause-and-effect relationship rather than `dreamy` or `surreal`.
- **Transferable Mechanism:** the abstract, executable relationship that can work with a new subject and scene.
- **Surface Implementation:** the reference's particular visual execution; transfer only if its role and scope permit.
- **Non-transferable Residue:** source-specific people, props, symbols, text, architecture, and events that must not leak into a new scene.

For a Dream Eye image, the subject's own eye/body may carry the impossible change; background magic alone loses Subject–Event Coupling. For `粉雾铬镜仪式`, a singular human presence set against impersonal mirrored order may be the mechanism; copying its exact person, set, or props is not required. If evidence is weak, do not extract a mechanism. When present, evaluate it separately from Medium Fidelity and Core Visual Rules.

## Single Reference Decode

Analyze the reference selectively. Use only dimensions that explain its identity; do not fill a template for its own sake.

- **Medium / Image Nature:** photography, illustration, painting, CGI, collage, print, low-poly, analog capture, editorial image, game capture, or mixed medium.
- **Composition:** subject placement and scale, negative space, symmetry, visual center, depth layers, edge tension, crop, and occlusion.
- **Camera / Viewpoint:** camera witness position and focal behavior for photographic media; viewpoint, framing boundary, spatial arrangement, and depth logic for other media.
- **Light / Value:** source direction, contrast, and exposure for photography; value structure, pigment/shading behavior, or graphic light logic for non-photo media.
- **Color:** dominant relationships, saturation structure, warm/cool balance, accent behavior, local color, shadow/highlight color, and color contamination.
- **Exposure:** highlight rolloff, shadow density, midtones, HDR or non-HDR character, and under- or overexposure tendency.
- **Material:** roughness, gloss, translucency, wear, texture scale, surface response, and material contrast.
- **Spatial Grammar:** layering, depth, architecture relationship, environmental dominance, thresholds, frames within frames, and subject-environment scale.
- **Character / Blocking:** posed versus observed, eye line, body direction, gesture, object interaction, and environmental relationship.
- **Capture / Rendering / Mark-making Character:** photographic capture behavior when relevant; otherwise edges, marks, paper/print surface, rendering limits, texture, motion, and intentional imperfection.
- **Art Direction:** editorial, documentary, observational, graphic, fashion, surreal, minimal, dense, decorative, brutalist, nostalgic, or another supported tendency.
- **Anti-clichés:** the specific visual shortcuts the reference avoids, such as universal rim light, hero posing, decorative fog, excessive HDR, generic teal-orange, over-sharpening, or luxury-commercial polish.

Anti-clichés must come from the current reference and requested transfer. Do not paste a universal negative list.

## Core Visual Rules

After the full decode, reduce it to **five to eight** high-impact, executable rules. These rules—not the complete analysis—are the main visual input to transfer and compilation.

Each rule should:

- describe a visible relationship or behavior;
- materially affect composition, light, color, material, space, blocking, or capture;
- remain useful after the subject or story changes;
- avoid vague praise and medium-neutral adjectives;
- identify when a rule is conditional rather than absolute.

Examples of valid rule shapes:

- The environment carries more visual weight than the person; keep the person subordinate unless the new request explicitly requires a portrait.
- Use only motivated daylight or practical architectural openings; do not add decorative rim light.
- Let highlights approach pale clipping while preserving dense shadows instead of lifting the whole frame into HDR clarity.
- Create editorial tension through spatial relationships and incidental action, not frontal posing.
- Use real foreground architecture or objects for partial occlusion when the new scene allows it.

Do not output `cinematic`, `beautiful`, `moody`, `dreamy`, `high-end`, `film look`, or similar labels as Core Visual Rules.

Do not treat the full Visual Grammar or complete Decode Card as final-prompt payload. Preserve all five to eight Core Visual Rules for the Decode Card, continuity, and repair; compilation selects three to five Active Core Rules relevant to the new Scene Master, plus Transfer Scope and only necessary supporting Visual Grammar.

## Transfer Scope

Transfer Scope is dynamic. Classify decoded observations according to the user's requested relationship between the reference and the new image.

### Strong Transfer

Usually suitable for strong inheritance when observed and relevant: color structure, material treatment, medium, light behavior, exposure behavior, texture, capture/render character, and detail density.

### Conditional Transfer

Resolve against the new Scene Master: camera, composition, subject scale, occlusion, spatial layering, negative space, blocking, focal behavior, and light direction.

### Do Not Transfer

Unless explicitly assigned: character identity, specific wardrobe, exact location, props, brand marks, visible text, specific architecture, story event, or object identity.

These lists are defaults, not a fixed template. “Keep the whole feeling but replace only the person” may widen the scope. “Only use the style” must narrow it. User-declared roles and exclusions always override inferred scope.

## Analyze Workflow

1. Read the user's question and route each image through `reference-role-router.md`.
2. Analyze each authorized medium through `medium-router.md`; resolve conflicts without averaging.
3. Separate Scene Facts, Visual Grammar, and Hybrid Decisions; identify an Expression Mechanism only when the evidence meets the optional extraction condition.
4. Analyze only dimensions that explain the visual effect and distill five to eight Core Visual Rules.
5. Define Transfer Scope only if the user wants reuse or transfer.
6. If the request is analysis-only, stop without generating a prompt.

Default visible output:

`画面理解` → `媒介判断` → `表达机制` (only when observed) → `解梦分析` → `核心梦律`

Keep the analysis useful and observable. Do not expose hidden chain-of-thought or internal scoring.

## Decode Transfer Workflow

Do not write a reference-image prompt and replace a few nouns. Rebuild from two independent inputs:

`New User Intent → Scene Master`

`Reference Image(s) → Reference Role Router → Per-Reference Medium Analysis → Decoded Visual Grammar + optional Expression Mechanism + Core Visual Rules + Transfer Scope`

Then compile:

`Scene Master + Decoded Visual Grammar → Compiler Priority Gate → target-specific Model Compiler`

Before compilation, check:

1. no Scene Fact from the reference has contaminated the new scene;
2. every transferred observation fits an assigned Reference Role;
3. Strong, Conditional, and Do Not Transfer boundaries are respected;
4. Hybrid Decisions do not break the new story, action, spatial logic, or requested composition;
5. the adapter uses supplied image references only through controls actually available to the user.

Default visible output:

`解梦摘要` → `核心视觉规则` → `[Target Model] Prompt`

For prompt-only requests, return only the final prompt.

## Multi-Reference Decode

Route first; do not average all images.

### Consensus Decode

Use when the user wants the shared feeling of a moodboard or several references. Separate:

- **Shared Visual Grammar:** recurring relationships supported across the set.
- **Stable Rules:** repeated high-impact rules suitable for transfer.
- **Variable Traits:** differences that should remain flexible rather than being averaged or locked.
- **Core Visual Rules:** five to eight rules synthesized from the stable evidence.

If several images share low saturation, natural light, foreground occlusion, and observed blocking but use different focal behavior, preserve the shared rules and list focal behavior as variable.

### Role-Based Decode

Use when each image has an assigned responsibility. Decode only the relevant dimensions from each source, resolve conflicts according to user priority, and combine the results without searching for a false intersection.

Example: A → color/exposure; B → composition/camera; C → character identity; D → material/texture.

## Decode Repair / 解梦校正

Use when the user supplies or clearly compares an original reference with a generated result and says the result lacks the intended feeling. Compare the accepted Scene Master and Reference Decode against the result. Choose no more than three dominant drifts:

`Medium Drift · Mechanism Drift · Composition Drift · Camera Drift · Light Drift · Exposure Drift · Color Drift · Material Drift · Texture Drift · Spatial Drift · Blocking Drift · Rendering Drift · Commercialization Drift · CG Drift · Reference Role Drift`

Before naming a drift, distinguish:

- **Valid Adaptation:** a Conditional Transfer changed because the new Scene Intent, fixed facts, or physical logic required it. This is not a failure. A close portrait requested by the user is not Composition Drift merely because the reference used a tiny person and extensive negative space.
- **Actual Drift:** Primary Medium, an observed Expression Mechanism, a Core Visual Rule, or Strong Transfer was lost without justification; a Conditional Transfer changed beyond what the new scene required; or Do Not Transfer source content leaked back into the result. An absent mechanism cannot cause Mechanism Drift.

Only Actual Drift is handed to `result-repair.md`. If scene structure is already correct, use the existing surgical contract:

```text
Dominant Drift:
[at most three causes]

CHANGE ONLY:
[the smallest observable corrections]

PRESERVE EXACTLY:
[all successful scene facts and decoded rules]

[Target Model] Repair Prompt:
[native edit instruction]
```

Do not re-decode and rewrite the entire prompt when only light and material drifted. Rebuild from the Scene Master only when the structural scene itself failed.

## Relationship to Existing Systems

- **Scene Master:** remains the canonical source of scene facts and generation intent.
- **Decoded Visual Grammar:** supplies reference-derived visual behavior; it is not merged into scene facts.
- **Style Cards:** are predefined Creative Grammar. Dream Decode derives custom visual grammar from the user's references. A Style Card may help compare or supplement only when the user wants it; it never overrides observed rules.
- **Model Compiler:** independently compiles the same `Scene Master + Decoded Visual Grammar` for each target.
- **Result Repair:** performs the smallest correction after drift diagnosis.
- **Continuity Bible:** owns character, wardrobe, props, location, geography, story state, and stable light facts across a series. A Decode Card may supply shared visual grammar without becoming a second source of scene facts.
