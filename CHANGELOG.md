# Changelog

## [1.2.0] - Unreleased

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
