# Changelog

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
