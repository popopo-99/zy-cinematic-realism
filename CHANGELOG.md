# Changelog

## v2.4.0 — 2026-10-03

### Fixed

- Director strength now respects subtle / clear / strong requests; unspecified strength uses clear instead of coercing every request to iconic.
- User-locked action, viewpoint, framing, sources, and composition are excluded from differentiation quotas. Strong interpretation uses only available compatible open decisions.
- Four-axis director planning no longer forces a labeled five-line block into every native or prompt-only result; target adapters control final syntax.
- Installation docs no longer equate pasting SKILL.md with providing its complete reference library.

### Added

- Opt-in Project Handoff Card and restore workflow for cumulative accepted state, reference availability, image status, and the next permitted change.
- Chinese and English self-contained basic chat starters without external reference-file dependencies; their reduced scope is explicit.
- A reference-grounded Dream Decode text example with a complete portable card, new-scene prompt, and explicit not-generated status.
- Manual behavior cases 61–72 for strength, locks, native output, cumulative handoff, unavailable inputs, mood preservation, and accepted edits.
- Reproducible ZIP builder and lossless PNG-to-WebP presentation conversion with pixel equality checks.

### Improved

- Chinese and English README lead with first use and creator tasks, with long tutorials, authored galleries, credits, model comparisons, and unchanged licensing text linked from focused pages.
- Ordinary creation can expose a few concise visual decisions; prompt-only and analysis-only output remain scoped. Detailed plans and handoff are requested as needed.
- Cinematic defaults and cleanup preserve explicit joy, daylight, celebration, or climax instead of implying darkness or aftermath is mandatory.

### Validation and Compatibility

- Independent text behavior checks and static/package validation are recorded separately in docs/validation-v2.4.md. Image comparisons and human usability gains remain unvalidated.
- Technical name, invocation, 38 director files, four model adapters, legacy handling, original showcase images, attribution, and CC BY-NC 4.0 remain intact.
- Intentional behavior change: unspecified director strength is now clear. Use strong / iconic explicitly to request the previous strong interpretation, subject to user locks.

## v2.3.0 — 2026-09-27

### Added

- Medium-aware Dream Decode with per-reference role isolation and explicit `Host Medium + Secondary Construction Rule` for user-requested cross-medium work.
- Optional Expression Mechanism and reusable Decode Card fields that preserve the transferable relationship without copying source content.
- `USER-LOCKED` / `OPEN` Scene Master visual decisions and three-to-five Active Core Rules selected from the full five-to-eight-rule archive.
- Image-level manual regression protocol using at least three paired comparisons per case, plus a general Skill validator.

### Improved

- Compiler Priority Gate preserves reference medium and scene intent while selecting only relevant visual grammar for each native model prompt.
- Decode Repair distinguishes Valid Adaptation from Medium Drift and Mechanism Drift; GPT Image compilation protects non-photographic media from default camera/capture language.
- Kept the technical name, four independent model adapters, earlier workflows, and CC BY-NC 4.0 license unchanged.

## v2.2.0 — 2026-09-24

### Added

- Dream Decode / 解梦 for explaining why reference images look the way they do and extracting transferable visual rules.
- Reference Role Router with explicit user-role priority and conservative role inference.
- Separation of reference Scene Facts, transferable Visual Grammar, and context-dependent Hybrid Decisions.
- Five-to-eight executable Core Visual Rules as the main decoded input to transfer and compilation.
- Dynamic Transfer Scope with Strong Transfer, Conditional Transfer, and Do Not Transfer boundaries.
- Decode Transfer from reference-derived visual grammar into a new Scene Master without prompt-to-prompt noun replacement.
- Multi-Reference Consensus Decode for stable shared rules and Variable Traits.
- Role-Based Multi-Reference Decode for separately assigned color, composition, identity, material, and other responsibilities.
- Decode Card schema with Core Visual Rules / 核心梦律, explicit Transfer Scope, Allowed Variation, Source Residue, and Drift Warnings, without automatic persistence claims.
- Decode Repair classification for Valid Adaptation versus Actual Drift before surgical correction.
- Eighteen Dream Decode regression cases covering analysis, transfer, multi-reference routing, conflicts, cards, valid adaptation, terminology, compression, compilation, repair, and scene contamination.

### Changed

- Scene Master can now receive visual grammar extracted from reference images without treating reference content as scene facts.
- Prompt Compiler prioritizes Scene Master, five-to-eight Core Visual Rules, Transfer Scope, and only relevant supporting Visual Grammar instead of copying the complete Decode Card.
- Reference handling now resolves explicit roles before analysis, transfer, or adapter mapping.
- GPT Image 2.5, Midjourney V8.2, Seedream 5.0 Pro, and Nano Banana adapters can compile the same `Scene Master + Decoded Visual Grammar` through their own native prompt shapes.
- Result Repair can compare an accepted Reference Decode with a generated result and preserve successful variables.
- Continuity can use a Decode Card for shared visual grammar while the Continuity Bible remains responsible for series facts and state.
- Chinese and English README files now introduce Dream Decode through “understand, learn, use” rather than a feature dump.

### Preserved

- Scene Master remains the canonical source of scene facts.
- Model Compiler architecture and independent target-specific compilation remain unchanged.
- Existing Director, Style, Cinematography, Prompt Check, Transcode, Remix, Creative Shuffle, Result Repair, and Continuity systems remain compatible.
- GPT Image 2.5, Midjourney V8.2, Seedream 5.0 Pro, Nano Banana, and legacy target handling remain supported.
- Technical skill name `zy-cinematic-realism`, folder name, and `$zy-cinematic-realism` invocation remain unchanged.
- License remains CC BY-NC 4.0 and is unchanged.

## v2.1.1 — 2026-09-09

### GPT Image 2.5 Compatibility Update

- Migrated the OpenAI image adapter baseline to ChatGPT Images 2.5 while preserving GPT Image 2 legacy prompt compatibility and the existing adapter path.
- Added unchanged-prompt-first migration evaluation; repair only specific observed failures.
- Strengthened editing scope and preserve/change guidance, including multi-turn preservation.
- Updated multi-reference role assignment and user-priority handling.
- Documented GPT-Image-2.5 Flare / Sunburst API routing without exposing API details to ordinary ChatGPT / Codex prompt requests.
- Refreshed the OpenAI Model Capability Matrix against official sources verified on 2026-09-09.
- Updated regression coverage, current documentation, validation, and the v2.1.1 Skill package.
- No Scene Master architecture changes; director, style, cinematography, other model adapters, and license remain unchanged.

## v2.1.0

### Midjourney V8.2 Adapter Migration

- Updated the default Midjourney compilation target to V8.2.
- Reworked Midjourney prompt compilation for current V8.2 prompt understanding.
- Added V8.2-native Imagine / Edit Model routing.
- Updated Image Prompt, Style Reference, Edit Model Reference, Moodboard, and Personalization strategies.
- Added need-driven Raw, Stylize, version, seed, text, and aspect-ratio handling.
- Removed legacy V6/V7 assumptions from the default Midjourney path.
- Improved Midjourney Transcode so source prompts rebuild through Scene Master before V8.2 compilation.
- Added dedicated Midjourney V8.2 regression tests.

## [2.0.0] - 2026-08-30

### Added

- Scene Master canonical representation for locking character, story moment, action, scene, camera, composition, light, props, time, weather, and constraints.
- Model Router for task-aware adapter recommendations.
- Model Capability Matrix for comparing model-facing compilation needs without permanent rankings.
- Model Compiler architecture.
- Four native adapters: GPT Image 2, Midjourney, Seedream 5.0 Pro, and Nano Banana.
- Transcode Lock for changing model syntax without changing scene logic.
- Multi-model Pack for compiling one Scene Master into several native prompts.
- Prompt Check for pre-generation conflict, vagueness, and physical-plausibility checks.
- Prompt Doctor / Result Repair for diagnosis-first, variable-scoped corrections.
- Continuity Bible for locking identity, wardrobe, props, locations, and light across a sequence.
- Shot Delta for expressing only the controlled change from the continuity base.
- One Variable Remix for changing one declared decision while preserving all other locks.
- Creative Shuffle for bounded creative alternatives.
- 16 style cards and 8 cinematography cards that alter executable visual decisions.
- A 14-case manual regression suite covering routing, compilation, continuity, repair, remix, and creative grammar.

### Changed

- Replaced the single Final Prompt pipeline with `Scene Master → Creative Grammar → Model Compiler → Result Repair`.
- Reorganized the README around v2 product capabilities while retaining the established cinematic methodology and examples.
- Expanded output contracts to support model-neutral planning, native model prompts, continuity packs, checks, and repairs.
- Made scene invariants explicit during transcoding and multi-model compilation.

### Preserved

- The 38-director library and Director Four-Axis Visual Fingerprint System.
- Story-first cinema principles, physically plausible camera placement, motivated light, and anti-AI cleanup.
- Technical skill name `zy-cinematic-realism`, folder name, and `$zy-cinematic-realism` invocation.

### Fixed

- Reduced scene drift when moving one visual direction between models.
- Reduced full-prompt rewrites when only camera, blocking, light, or another local variable needs repair.
- Reduced continuity drift caused by repeating complete prompts without a shared base lock.
- Clarified the difference between model-native syntax changes and protected scene logic.

## [1.2.0] - Unreleased

Development work folded into v2.0.0; not released separately.

### Added

- Director Four-Axis Visual Fingerprint System.
- Expanded Chinese, Asian, European, and American director library from 12 to 38 directors.
- Director recommendation matrix for selective two-to-three-candidate routing.
- Nearest-neighbor director contrast rules.
- Stronger Chinese, English, surname, abbreviation, and alternate-spelling aliases.
- Lightweight director-library and Markdown-link validation.

### Changed

- Named-director prompts now require explicit lighting, color/exposure, lens/camera, and composition/spatial signatures.
- Director differentiation validation now checks structural changes instead of descriptive wording.
- Director index reorganized by region for faster selective loading.
- Named-director outputs must reselect at least three viewing decisions and pass name-removal and nearest-neighbor checks.

### Fixed

- Reduced director outputs that differed only through color grading, lens labels, film grain, crop, or atmosphere words.
- Prevented the Director Signature Block from being moved to the prompt ending as decorative style text.

## [1.1.2] - 2026-07-27

### Changed

- All supported named-director requests now use mandatory strong / iconic behavior.
- Removed lower-strength behavior for supported director names.
- Every named-director Final Prompt now explicitly includes the director's English name, representative films, and corresponding signature visual language.
- Updated the base prompt template and README examples to reflect mandatory strong director behavior.

## [1.1.1] - 2026-07-27

### Added

- Added file-level copyright notices and SPDX identifiers.
- Added LICENSE and NOTICE.md to the distributable Skill package.
- Added canonical source attribution to SKILL.md.
- Added copyright notices to core reference and template files.

### Preserved

- No changes to the cinematic workflow, output contract, director behavior, installation path, or skill name.

## [1.1.0] - 2026-07-26

### Added

- Added the Director Lens Library with twelve director references and director routing.
- Added explicit director-name and two-to-three representative-film anchors for strong director recognition.
- Added Anti-AI Cleanup, selective legibility guidance, and director signature overrides.
- Added six evidence-room comparison images and a complete comparison case page.
- Added name-free compatibility behavior when a platform or user requires it.

### Changed

- Director requests now default to the strongest `iconic` behavior, publicly labeled `强烈`.
- Director names are preserved by default; iconic prompts include two or three representative films and scene-specific visual grammar.
- Removed default `photorealistic` quality-badge wording and strengthened material realism, uneven exposure, and selective readability.
- Strengthened director differentiation, visual-center reselection, and model-facing anchors.

### Preserved

- Existing cinematic realism workflow and output contract.
- Existing installation paths, technical skill name, folder name, and `$zy-cinematic-realism` invocation.

## v1.0.0 — Public Edition

《造梦师：AI时代电影视觉指南》首次公开版本。

### 包含

- 电影感的核心生成原则
- 故事瞬间选择工作流
- 人物动作与关系设计
- 真实空间与环境痕迹
- 摄影机位置和观察式构图
- 有物理来源的光线系统
- 克制的胶片与镜头质感
- 场景专属 Avoid 负面提示词
- 质量检查清单
- 完整生成案例
- Codex / ChatGPT 使用说明
