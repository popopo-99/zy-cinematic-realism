<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Story Visual Development / 剧本到画面

Use supplied screenplay passages, short stories, synopses, or oral accounts to develop the requested scene understanding, visual world, art direction, keyframes, or image prompts. Reuse the existing Scene Master and compiler; do not create a second image-fact structure.

## Task and Reading Scope

- Follow the requested deliverable. `只分析人物关系` means that analysis only, with no automatic keyframes, model question, or prompt. `只看这一场` limits the source scope; `不要 Prompt` excludes prompts while allowing the visual development actually requested. Neither phrase cancels an otherwise explicit keyframe request. Visual-development planning does not require a generation model.
- Read the material actually available. Record its supplied title/version and the verified scene, page, paragraph, or transcript range when useful. Distinguish a PDF file page from a printed screenplay page. Do not invent a draft date, original scene number, or precise timestamp.
- A synopsis is its own source, not proof that the full screenplay was read. A spoken or typed account is the user's account; use an accessible recording or verified transcript before claiming to have heard audio. Mark unread, missing, or unclear material accurately.
- For a named film, use the supplied passage as evidence. Do not import actors' faces, remembered shots, production design, later plot, or a film's whole visual style. A title alone cannot establish a faithful script reading; request the relevant text when that is required. Open brainstorming may proceed as a new proposal with no claimed script evidence.
- One short passage usually needs no ledger. For multiple scenes, nonlinear chronology, or revisions, read [story-source-ledger.md](story-source-ledger.md) and work from the verified scope rather than claiming whole-story coverage.

## Facts, Interpretations, and Proposals

Keep three kinds of information distinct:

| Kind | Authority and use |
| --- | --- |
| **Source Facts / 来源事实** | Explicit actions, dialogue, setting, time, relationships, and visual directions in the available material. Preserve them for faithful development; associate important facts with a usable source locator. |
| **Interpretations / 叙事解释** | A reading of motivation, conflict, subtext, or a relationship change. State the supporting behavior and keep a material ambiguity open; an interpretation is not an additional plot fact. |
| **Visual Proposals / 视觉提案** | New choices of moment, viewpoint, blocking within unspecified space, light, materials, or recurring visual rules. Explain their story purpose when useful; do not present them as authored script directions or accepted project locks. |

Newer explicit user instructions outrank earlier source preferences. If the user requests an adaptation, identify the changed source fact rather than silently rewriting the source record. Complete OPEN visual decisions for the requested candidate without adding unrequested plot, identities, or major world premises. A candidate can be frozen for compilation without becoming user accepted or USER-LOCKED. Promote a proposal to an accepted Scene Master/Bible rule only when the user accepts it; prompt completion or image generation alone does not count as acceptance.

## From Story to Visual Decisions

1. **Locate the change.** Identify what each relevant character is trying to do, the concrete obstacle, and how action changes their relationship or situation. Track what characters and the audience know at this moment. Do not resolve a mystery using a remembered ending.
2. **Find observable evidence.** Connect emotion or subtext to supported action, distance, gaze, object handling, access to space, or traces of an event. When the text leaves the expression open, propose a specific visible behavior rather than claiming it happened. A still frame cannot literally show all dialogue, off-screen sound, or consecutive actions at once.
3. **Develop a visual world when requested.** Choose the few relationships that give this story its own spatial, material, light, color/value, and viewing logic. Explain how they serve conflict or change across scenes. Avoid a fixed emotion-to-color formula, a director chosen without request, or a generic list of cinematic badges. A joyful social scene may use crowded space and shared light; the actual story and physical sources determine the choices.
4. **Select keyframes for a reason.** Choose moments that reveal a decision, altered relationship, discovery, spatial rule, or necessary art-direction test. Give each proposed frame a current action, visual center, and reason for selection. Do not turn every scene into one frame, require three frames/directions, or replace a requested climax with waiting or aftermath. Keyframes are selected development images, not a claim to have completed a full storyboard.
5. **Resolve each frame.** Reuse [cinematic-principles.md](cinematic-principles.md), [camera-and-light.md](camera-and-light.md), and the existing Scene Master schema in [prompt-compiler.md](prompt-compiler.md). For a series, use [continuity-cards.md](continuity-cards.md) to protect identities, geography, chronology, wardrobe/prop states, and the accepted visual strategy. Keep tentative alternatives outside accepted locks.

Do not infer arbitrary architecture or light merely from an abstract mood. Add only the OPEN physical decisions needed to make the proposed image usable, and keep uncertainty that would materially alter the scene visible. Ask one focused question only when a missing source fact or unresolved conflict blocks the requested work; otherwise continue within the available scope.

## Visual References and Compilation

Story material supplies narrative facts and proposed expression. An actual supplied image separately supplies observed visual grammar through Reference Roles and Dream Decode. A proposed metaphor or unusual event in a screenplay is not a Dream Decode **observed Expression Mechanism**; that claim requires visible image evidence. Do not manufacture a Decode Card from a film title or imaginary reference.

For each requested prompt, compile:

`Source-backed Story Moment + resolved Visual Proposal + relevant Bible state → Scene Master`

Then use `Scene Master + optional Decoded Visual Grammar → selected model adapter`. Explicit scene facts and user decisions outrank visual proposals and transferred grammar. A non-photographic reference retains its authorized making logic. Preserve existing director-strength, model-routing, prompt-only, and repair rules; do not add a script-specific adapter or paste the source ledger into the prompt.

## Output and Continuation

- **Analysis only:** the requested understanding of the supplied scope, including consequential ambiguity; no extra art direction or prompt.
- **Visual development:** a brief source-scope note when needed, scene/relationship understanding, a concrete visual strategy, and the requested keyframe proposals with reasons. Distinguish facts from interpretation and invention without exposing hidden reasoning or a compulsory form.
- **Prompts requested:** compile the requested frames through the established target. Apply the existing Target Model Gate only when a generation-ready prompt needs it; if the user says to proceed, use the model-neutral route.
- **Prompt-only:** keep the source distinctions and checks internal and return only the requested prompts.

On revisions, update affected source facts and dependent frames using [story-source-ledger.md](story-source-ledger.md) when needed. Retain unrelated accepted changes. Report whether prompts are ready, images were generated/inspected, or the user accepted them. Use [project-handoff.md](project-handoff.md) only on request; a text summary does not recover an unavailable script or identity image.
