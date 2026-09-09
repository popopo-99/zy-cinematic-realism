<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Model Routing

## Principle

Use one locked Scene Master and compile it into native model language. Model selection changes expression and workflow, not the creative facts of the image.

`One Scene Master, multiple native model prompts.`

## Resolve the Target

1. If the user names a supported model or alias, load its adapter and do not ask again.
2. If the conversation already establishes the model, keep using it unless the user changes it.
3. If the user wants a generation-ready prompt and model choice materially affects structure, ask once which model they will use.
4. If the user declines questions or asks to proceed immediately, compile a model-neutral Scene Master prompt.
5. If the user asks which model to choose, read [model-capability-matrix.md](model-capability-matrix.md). Give one main recommendation and, when useful, one alternative. Explain only the task-relevant difference.

Supported adapters:

- `GPT Image`, `OpenAI image`, `ChatGPT 生图`, `ChatGPT Images 2.5`, `GPT Image 2.5`, `Images 2.5` → current [ChatGPT Images 2.5-compatible adapter](models/gpt-image-2.md)
- Explicit `GPT Image 2`, `GPT-Image-2`, `gpt-image-2` → [the same adapter](models/gpt-image-2.md), retaining the requested legacy target or legacy-prompt compatibility task
- `Midjourney`, `MJ`, `Midjourney V8`, `Midjourney V8.2`, `MJ V8.2` → [models/midjourney.md](models/midjourney.md), using V8.2 as the default target
- `Seedream 5.0 Pro`, `Seedream`, `即梦` when the context clearly means this model → [models/seedream-5-pro.md](models/seedream-5-pro.md)
- `Nano Banana`, `Nano Banana family`, or a named Gemini image member → [models/nano-banana.md](models/nano-banana.md)

For any other model, stay model-neutral unless reliable current documentation is available. Do not borrow syntax from a supported adapter merely because the model is similar.

## Routing Heuristics

- Prefer **ChatGPT Images 2.5 / GPT Image 2.5** for a structured production brief, high-fidelity image input, or conversational generation/editing in an OpenAI workflow.
- Prefer **Midjourney V8.2** for prompt-led visual exploration, native parameterized iteration, role-specific reference workflows, and current Edit Model generation or repair.
- Prefer **Seedream 5.0 Pro** for spatially explicit creative briefs, multilingual or text-rich production, annotated/local editing, and multi-source composition when the available frontend exposes those controls.
- Choose the **Nano Banana family** member according to the actual frontend/model: fast iteration, general multi-reference work, or precision production. Never treat all family members as identical.

These are heuristics, not a permanent ranking. Capabilities and frontends change. Use `Strong`, `Good`, `Conditional`, `Limited`, or `Frontend-dependent`; never invent numerical scores.

## OpenAI product / API routing

Verified: 2026-09-09. Ordinary ChatGPT / Codex image prompts use the 2.5-compatible adapter without API details. The Skill does not force the underlying product model version.

Only for API usage, recommend **GPT-Image-2.5 Flare** for fast, high-quality generation at volume, and consider **GPT-Image-2.5 Sunburst** when complex editing precision is the priority and longer generation time is acceptable. Start a validated GPT Image 2 migration unchanged on Flare; if quality is already insufficient for a complex task, evaluate Sunburst first. These recommendations require workflow evaluation, not a permanent model ranking. See the [adapter's official sources and migration rule](models/gpt-image-2.md).

Do not add model IDs, quality fields, unsupported parameters, pricing, or endpoint syntax to an ordinary ChatGPT prompt. An explicit legacy OpenAI target remains legacy until the user changes it; a fresh generic OpenAI request defaults to 2.5 compatibility.

## Adapter Boundary

An adapter may alter prompt order, clause density, exclusions, edit wording, reference-role syntax, and supported parameters. It must not alter character identity, scene, story beat, action, camera witness position, visual center, spatial layers, source lights, props, time, weather, aspect ratio, or explicit restrictions.

For Transcode, first apply the lock in [prompt-compiler.md](prompt-compiler.md). If the source prompt contains a structural conflict, warn briefly that faithful transcoding will retain it. Preserve it by default; fix it only when the user asks for optimization.

An explicit `V6`, `V6.1`, or `V7` request is a legacy Midjourney target. Route it deliberately, verify that version's documented feature and parameter compatibility, and do not present the current V8.2 Edit Model or reference workflow as equivalent. An unqualified Midjourney request must never fall back to a legacy target.
