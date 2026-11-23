<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Prompt Compiler

## Contract

`MODEL SYNTAX MAY CHANGE. SCENE LOGIC MAY NOT.`

The Scene Master is the source of truth for scene facts. It is an internal structure unless the user explicitly requests it. When Dream Decode is active, Decoded Visual Grammar is a separate compiler input; do not merge reference-derived style behavior into scene facts.

## Scene Master Schema

- **Fixed Facts:** user-supplied era, place, people, event, mood, time, weather, ratio, model, and restrictions.
- **Story:** Story Beat, Narrative Before, Current Action, Implied Next.
- **Characters:** Character Identity, Character Blocking, Object Interaction.
- **Space:** Environment, Foreground, Midground, Background, Visual Center.
- **Camera / Viewpoint:** Witness Position for photography or viewpoint, framing, spatial arrangement, and form logic for other media; distance, height, and focal behavior only when relevant. An optional Capture Design holds format/camera, lens/focal length, position/distance, aperture/focus, optical/filter behavior, and their source, lock, and scope. Coordinate recording texture with Surface / Rendering and exposure with Light / Value.
- **Light / Value:** Source Light Map and exposure for photographic media, or value, pigment, shading, and graphic-light behavior for other media.
- **Surface / Rendering:** Material Behavior and medium-appropriate capture, mark-making, edge, paper, texture, or rendering behavior.
- **Delivery:** Aspect Ratio, Visible Text, Reference Roles, Must Preserve, Allowed Variation, Likely Failure Modes.

Do not force absent or irrelevant fields into the visible prompt. Resolve only what the scene needs.

## Capture Design Input

Use [capture-design.md](capture-design.md) when photographic choices matter or the user requests equipment selection. Capture Design is part of Camera / Viewpoint in this Scene Master. Keep one resolved value for each decision. Library lookup supplies source-backed facts and possible creative choices. It does not override the scene or establish the historical equipment of an uncredited image.

Preserve explicit user equipment, focal length, focus, texture, and effect exclusions as USER-LOCKED with their current shot or project scope. A specifically adopted field becomes USER-LOCKED within its accepted scope. General image approval retains its stated visual scope and does not imply adoption of unshown parameters. Track source, lock and acceptance status separately. System candidates remain OPEN unless specifically chosen. Apply authorized reference Hybrid Decisions to OPEN fields during the requested design or redesign pass. A director reference may guide an open choice, while a documented film gear record retains its stated film/sequence/shot evidence scope.

Compile useful visible behavior alongside a requested model or lens name. Describe framing, subject distance, focus separation, and effect location concretely. Use numerical settings only when relevant and coherent with format, field of view, and focus needs. Do not paste equipment cards, citations, internal evidence tags, source notes, or unused parameters into the generation prompt. CG can retain useful virtual photographic references within its authorized medium. Drawn and painted media use medium-appropriate view, value and surface language, with photographic viewing analogies where useful. A change to photographic rendering requires the user's applicable authorization.

For visual decisions, distinguish **USER-LOCKED** explicit user choices from **OPEN** unspecified or system-completed defaults. Resolve OPEN camera/viewpoint, composition, subject scale, light, framing, perspective, blocking, aspect ratio, and visual-center decisions against authorized reference Hybrid Decisions before final locking. `USER-LOCKED > reference-derived Hybrid Decision > system-generated default`. This does not create a second source of scene facts; the resolved Scene Master is canonical.

## Capture Strategy Check

Before compilation, apply [Capture Strategy Selection](capture-design.md#capture-strategy-selection) to the current Scene Master and reference roles. Compile an original scene as a new-image payload and an accepted image modification as an edit payload. Keep explicitly supplied professional terms and parameters.

For a global projection change, distinguish identity, scene topology, observation position and image-point coordinates. Describe the authorized projection movement in Allowed Variation while protecting the other relevant locks. A generic preserve-position phrase must be interpreted against the requested projection and actual accepted scope.

For an image-preserving global projection request, briefly explain the edit path's continuity advantage, its possible geometric limits and the preserved versus movable content. This explanation can accompany immediate compilation. When there is an actual unresolved tradeoff, offer concrete choices within the user's scope. Changing generation method or releasing a lock requires existing authorization or an actual user decision. An explicit compatible path proceeds directly. An explicit compatible prompt-only request expresses the preservation and projection boundaries in the payload, with the existing essential-conflict exception for unresolved choices.

## Guided Plan and Structured Output

A requested Plan-first workflow uses [guided-capture-workflow.md](guided-capture-workflow.md) to present this same Scene Master for review. Continue compilation after the requested confirmation, modification plus direct-output authorization, or explicit bypass. A direct prompt or JSON request compiles immediately. Acceptance applies to the visible, identifiable choices in its stated scope, while undisclosed OPEN values retain their status.

Select the requested output structure after resolving the same scene and target-model expression. Preserve a supplied schema's hierarchy and value types. An explicit Jury JSON Brief request uses [the verified still profile](jury-json-brief.md); its required fields and palette constraints apply within that profile. A faithful format conversion carries current values, including OPEN candidates, without reselecting them. Map reference roles, preserve/change instructions and target constraints into relevant image fields. Keep research and acceptance records in their existing planning or handoff context.

## Still and Temporal Camera Language

When a camera term, projection or time-dependent instruction needs interpretation, use the [camera-language index](camera-language-dictionary.md). During a new design or requested repair, normalize its meaning into the existing Camera / Viewpoint and Capture Design. A faithful Transcode carries the current resolved meaning, values, locks and OPEN candidates forward.

Compile a still-image target as one coherent moment. Dolly In, Pan, Zoom and Rack Focus can supply a selected viewpoint, framing, focus state or a suggested action trace. Their progress, duration and changing relationships require a temporal sequence. Express a requested still as the relevant state and explain the time boundary briefly when explanation is requested or needed to resolve an actual conflict. Prompt-only output retains its existing contract.

For an explicit continuous-camera request, retain the user's duration, direction, start/end intent and locked parameters as a model-neutral camera plan or pass the transferable Camera / Viewpoint information to an available independent Motion workflow. Target-specific video compilation and execution checks belong to that workflow. The dictionary's `video_instruction` label identifies temporal instruction material and carries no model-execution guarantee.

For an authorized illustration or other non-photographic Primary Medium, apply requested projection, framing or viewpoint behavior through that medium's existing geometry, marks and rendering constraints. The Compiler Priority Gate continues to govern medium authority.

## Story Visual Development Inputs

For [story visual development](story-visual-development.md), build the current Scene Master from the source-backed moment, relevant Continuity Bible state, and resolved visual proposal. Preserve explicit source actions and visual directions for faithful development; only a user-requested adaptation may change them. Keep interpretations separate from source facts and complete unspecified visual decisions as OPEN candidate choices. Freezing a candidate for compilation does not mark it user accepted or USER-LOCKED.

Retain source version, scene/beat locator, character/audience knowledge, and revision dependencies in the [story source ledger](story-source-ledger.md) when needed, not as compulsory prompt headings. Do not paste the ledger or import unprovided later plot, actors, or original-film framing. Prompts must show one coherent current moment and only the information intended to be visible then. Story-derived art direction remains distinct from visual grammar actually observed in references; a proposed narrative device is not an observed Dream Decode Expression Mechanism.

## Dream Decode Inputs

When visual references are used for analysis or transfer, compile from two coordinated structures:

```text
Scene Master
+ Decoded Visual Grammar
  - Reference Roles
  - Primary Medium + Medium Constraints / Avoid
  - Expression Mechanism (optional)
  - Core Visual Rules (full 5–8 archived; Active Core Rules 3–5 for final prompt)
  - Transfer Scope
  - Hybrid Decisions: Preserve / Adapt / Release
  - Anti-cliches
```

The Scene Master continues to own characters, event, action, environment, story, topology, camera requirements, light facts, props, time, weather, aspect ratio, and restrictions. Decoded Visual Grammar supplies reference-derived color, exposure, material, texture, medium, rendering/capture, composition tendencies, spatial rhythm, and other transferred behavior.

Do not add every decode field to the Scene Master schema. If the two structures conflict, explicit user intent and Scene Master fixed facts win.

## Compiler Priority Gate / 编译优先级闸门

Resolve in strict order, before target-model syntax:

1. **Scene Master USER-LOCKED Facts / Decisions** — explicit user choices for characters, action, setting, story, visual decisions, ratio, and restrictions.
2. **User Explicit Reference Roles** — assigned authority and exclusions; no inferred role may override them.
3. **Primary Medium / Medium Constraints** — the authorized style reference's medium controls image-making logic unless the user explicitly requests realistic / cinematic reinterpretation.
4. **Expression Mechanism (optional)** — preserve an observed subject–event relationship; skip this layer entirely when no distinct mechanism exists.
5. **Active Core Rules (3–5)** — select from the full five to eight Core Visual Rules for the current scene.
6. **Transfer Scope** — Strong / Conditional / Do Not Transfer, with Hybrid Decisions resolved against the new scene.
7. **Relevant supporting Visual Grammar** — only details needed to execute higher-priority decisions.
8. **Scene-specific Reject / Anti-clichés** — three to five high-value exclusions when useful, not a universal negative list.
9. **Target-model formatting** — native syntax and controls without changing upstream logic.

This is an authority order, not an instruction to place nine headings in the final prompt. Step 1 protects USER-LOCKED facts and decisions; OPEN visual decisions may be filled or adapted by authorized Hybrid Decisions ahead of system defaults. A reference's non-photographic medium is not silently converted to photography, live-action, glossy CG, or generic concept art by the Skill's cinematic realism defaults. A model's inability to follow a correct prompt is a target-model compliance problem, not proof of a bad decode.

## Decode Card Input Selection

Do not paste the full Dream Decode or Decode Card into a target prompt. Select compiler input in this order:

1. Scene Master USER-LOCKED facts and decisions, then explicit Reference Roles; resolve OPEN visual decisions against authorized Hybrid Decisions before applying system defaults.
2. One Primary Medium and identity-critical Medium Constraints; include one primary Expression Mechanism with at most two or three related execution points **only when observed**. Otherwise skip it without substitution.
3. Select **three to five Active Core Rules** from the full five to eight Core Visual Rules. Prefer rules that establish medium identity or an observed mechanism, matter directly to the new Scene Master, have high-weight Strong Transfer, or whose absence would visibly lose the reference. Deprioritize archival-only or irrelevant rules, Conditional Rules that conflict with USER-LOCKED intent, and duplicates already expressed by Medium Constraints. Preserve the full set in the Decode Card for continuity and repair. Resolve Transfer Scope against the new scene.
4. Only supporting Visual Grammar relevant to the new scene; three to five high-value scene-specific rejects when useful.

If the prompt is overloaded, remove low-impact supporting grammar, redundant adjectives, and low-value rejects first. Do not sacrifice USER-LOCKED facts, medium identity, an observed mechanism, or the selected Active Core Rules to keep ornamental detail.

Source Residue, archival explanation, optional naming, Drift Warnings, and unused Visual Grammar fields are not prompt payload. They remain available for contamination checks, continuity, and repair.

## Transcode Lock

Before changing models, extract and lock:

`Character · Scene · Story Beat · Action · Visual Center · Camera Position · Composition · current resolved Capture Design and its source/lock/acceptance/scope · Light Sources · Props · Time · Weather · Aspect Ratio · Restrictions`

Keep the currently used OPEN candidate values as well as USER-LOCKED choices during a faithful conversion. This conversion lock preserves the current design without promoting candidates to accepted project decisions. A model change alone does not authorize reselecting equipment or reapplying references to redesign OPEN fields.

If the source is ambiguous, preserve the most direct reading. If two clauses conflict, state the single structural conflict briefly. Faithful conversion preserves it; optimization requires user intent or an explicit request to fix.

For GPT Image 2 → GPT Image 2.5 migration, apply the [unchanged-prompt-first rule](models/gpt-image-2.md) before any reordering or expansion. Keep the validated prompt and references for the first comparison; use the compilation or repair pass only when requested or when evaluation identifies a specific failure. Scene Master facts stay locked.

## Compilation Pass

1. Normalize the source into a Scene Master without adding a new concept.
2. Mark explicit user visual decisions USER-LOCKED and unspecified system defaults OPEN; allow authorized Hybrid Decisions to fill or adapt OPEN fields before the final lock.
3. When Dream Decode is active, run the Compiler Priority Gate after Reference Roles, per-reference medium analysis, optional Expression Mechanism, and Hybrid Decisions are resolved; select three to five Active Core Rules.
4. Resolve any relevant Capture Design inside Camera / Viewpoint, coordinate light and surface decisions, and preserve the resulting lock and scope. Load the target adapter after this shared input exists.
5. Reorder and compress information according to the adapter.
6. Translate exclusions, references, editing instructions, ratio, and parameters into target-native form.
7. Compare the compiled prompt against both the lock and Transfer Scope. Restore any drift before output.

Dream Decode preflight:

1. **Medium Drift Risk:** did the prompt replace the authorized Primary Medium with photography, generic CG, or a different making logic?
2. **Mechanism Drift Risk:** only if a distinct mechanism was observed, is the Abnormal Event still coupled to the intended subject or relationship?
3. **Source Residue Leak:** did a person, wardrobe, object, location, brand, text, architecture, or event leak from a visual-grammar reference?
4. **Reference Role Conflict:** does every image obey its explicit or conservatively inferred authority, including medium authority?
5. **Conditional Transfer Misuse:** were Hybrid Decisions adapted or released where literal inheritance would break the new scene?
6. **Scene Intent Damage:** are USER-LOCKED facts, action, space, and requested composition intact, while reference logic had a chance to fill OPEN decisions?
7. **Generic Cinematic Override:** did realism defaults erase a non-photo medium?
8. **Generic Concept Art Override:** did an undifferentiated concept-art / game-render look erase specific medium constraints?
9. **Prompt Overload:** did compilation paste the full Decode Card or too much low-value grammar? Remove low-priority material first.

Native shapes:

- **Midjourney V8.2:** concise, concrete natural visual description optimized for current V8.2 prompt understanding, preserving story, spatial, camera, light, material, and restriction relationships; append only request-relevant supported native parameters.
- **ChatGPT Images 2.5 / GPT Image 2.5:** structured natural-language production brief with integrated constraints; explicit GPT Image 2 targets retain legacy compatibility.
- **Seedream 5.0 Pro:** clear spatial creative brief with explicit relationships and edit regions when supplied.
- **Seedream 5.5:** clear natural-language scene or edit brief with explicit reference roles, preserve/change boundaries, spatial relationships, and the resolved capture behavior.
- **Nano Banana:** direct conversational generation or editing instruction with explicit preserve/change language.

For Midjourney, decide between ordinary Imagine/generation and the V8.2 Edit Model before compiling. An existing-image change, selected-area repair, perspective change with reference preservation, or multi-reference recombination is an Edit Model task, not merely a shorter Imagine prompt. Because V8.2 is the current default target, omit `--v 8.2` unless the user requests a Discord-complete or version-locked prompt, or the workflow must prevent version drift.

## Multi-model Pack

Build one Scene Master once. Reuse its current resolved Capture Design, including OPEN candidate values, with the same source, lock, acceptance status and scope. When present, reuse the same Primary Medium, optional Expression Mechanism, full Core Visual Rules, scene-selected Active Core Rules, Transfer Scope, and Decoded Visual Grammar. Compile each target independently from that shared input. Each prompt follows its adapter while preserving the same scene and visual rules. Natural-language adapters may share wording. Always use `Scene Master + optional Decoded Visual Grammar → target-specific adapter`; never chain `GPT Image → Midjourney → Seedream` or any prompt-to-prompt translation. An unchanged OpenAI migration baseline does not require cosmetic differences.

## Output

For Transcode, show only a short Scene Lock Summary and the target prompt. Do not re-pitch the creative idea. Omit the summary when the user requests prompt-only output.

Ordinary Create and Capture Design requests return a copyable plain-text prompt by default. A requested setup may add a concise rationale, while an explicit Plan-first request stops at its review stage. Library questions return the requested cards and sources without forcing prompt generation. Output JSON only when explicitly requested, using the selected structure in [capture-design.md](capture-design.md). Source citations and setup explanations stay outside the prompt block.

## Style Capsule input and media adaptation

Consume the [Style Capsule](dream-decode.md#style-capsule--风格胶囊) as the compact view of existing Decoded Visual Grammar. Reuse its full Core Visual Rules and select three to five Active Core Rules through the same Compiler Priority Gate. Keep source-status records, confidence and capsule field names outside a prompt-only payload. Relevant preservation and reference-role boundaries belong in the actual prompt.

For photography, use coherent capture choices. For realistic or stylized CG, retain useful virtual viewpoint, lens/focal reference, focus and light logic without claiming verified real equipment or exact simulation. For 3D-to-2D animation, prioritize designed form, grouped shading, simplified response and selective marks. For drawing, painting, graphic illustration or comics, express space, contours, value groups, brushwork and edges through that medium. Use supplied professional terminology directly and explain plain-language choices only when helpful.

Brief-to-prompt faithful conversion preserves current aspect ratio, virtual-camera intent, scene and exclusions. Style-only transfer replaces source-specific content with the new Scene Master and honors assigned roles. Full Jury JSON uses the existing field mapping and Schema. A request for a concise prompt receives only the executable prompt, with no compulsory capsule, analysis or Plan turn.
