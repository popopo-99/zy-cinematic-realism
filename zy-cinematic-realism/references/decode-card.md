<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Decode Card / 解梦卡

A Decode Card is a named, structured, reusable visual-grammar summary of one successful Dream Decode. It can support a new scene, series extension, or controlled variation. It is not the final generation prompt.

A Decode Card is not:

- a complete description of the source image;
- generic Image-to-Prompt output;
- an automatically saved database record;
- permission to copy every visible property from the reference.

Create one only when the user asks for a card, wants to reuse the decode, or needs shared visual grammar for a series. A user may choose an evocative title such as `解梦卡｜粉雾铬镜仪式`, but do not invent an exaggerated style name when neutral archival naming is more appropriate.

## Core Visual Rules / 核心梦律

Core Visual Rules are the **five to eight** highest-impact, most executable rules compressed from the full Dream Decode. Keep the full set in the card for continuity and repair; only three to five scene-relevant Active Core Rules enter a final generation prompt.

They are not:

- style labels or mood adjectives;
- keyword soup;
- a description of source-image people, places, props, animals, text, or brands;
- the complete Visual Grammar copied without selection.

Each rule must express an observable relationship or behavior involving composition, space, light, exposure, color, material, blocking, or capture/render behavior. Examples:

- The subject occupies a small part of the frame while the environment carries most of the visual weight.
- Key light comes only from explainable environmental sources; add no decorative rim light.
- Highlights approach pale clipping while retaining color, and shadows keep density without HDR-style global lifting.
- Characters remain inside an unfolding action rather than presenting a completed frontal pose.
- Real foreground occlusion establishes observation distance and spatial depth when the new scene allows it.

Do not use `cinematic`, `dreamy`, `elegant`, `surreal`, `high-end`, `vintage`, `beautiful`, or `film look` as Core Visual Rules.

## Visual Grammar and Compression

Visual Grammar is the fuller archive of observed composition, viewpoint, light/value, exposure/tonal behavior, color, material, spatial, blocking, capture/render/mark-making, and art-direction behavior. The card records medium once in its dedicated medium section. Core Visual Rules are its high-weight compression layer.

Use this order:

`Reference Roles → Per-Reference Medium Analysis → Full Dream Decode + optional Expression Mechanism → Visual Grammar → Core Visual Rules → Transfer Scope → Compiler Priority Gate → Compilation`

Do not send the complete Decode Card to the Prompt Compiler. Compile from three to five Active Core Rules, Transfer Scope, only the relevant supporting Visual Grammar, and the Scene Master.

## Transfer Scope / 迁移范围

Transfer Scope must be explicit enough for a later Decode Transfer to use directly. The following categories are defaults, not mechanical field assignments; the current reference, Reference Roles, and user intent decide the final scope.

### Strong Transfer / 强继承

Usually suitable when observed and relevant: Color Structure, Light Behavior, Exposure Behavior, Material Treatment, Texture / Capture Character, Medium, Rendering Character, and Detail Density.

### Conditional Transfer / 条件继承

Hybrid Decisions that must obey the new Scene Intent: Composition, Camera, Subject Scale, Negative Space, Occlusion, Spatial Layering, Blocking, Focal Behavior, Symmetry / Asymmetry, and Light Direction.

Record whether each conditional item should be **Preserve**, **Adapt**, or **Release**. A literal source value is not required when its underlying relationship can be adapted.

### Do Not Transfer / 默认不继承

Unless the user explicitly assigns the role: Character Identity, Exact Wardrobe, Exact Location, Specific Props, Visible Text, Brand Marks, Specific Architecture, Specific Story Event, Reference-only Objects, and incidental source residue.

`TRANSFER VISUAL LOGIC. PRESERVE NEW SCENE INTENT.`

## Final Schema

Use only sections supported by the reference and reuse goal. A compact card does not need every optional subsection.

```markdown
# 解梦卡｜[Name]

类型：解梦卡 / Dream Decode Card

用途：为新场景、系列延展和受控变体保留同一套视觉语法；本卡不是最终生成 Prompt。

## 一句话视觉定义 / One-line Visual Definition
[one compact relationship-based definition]

## 情绪 / 视觉张力
[optional; include only when it changes visual decisions]

## 媒介 / Medium
- Primary Medium: [only when supported by reference evidence]
- Secondary Influences (0–2): [optional]
- Medium Constraints: [identity-critical, observable]
- Medium Avoid: [optional, only likely substitutions]

## 表达机制 / Expression Mechanism
[omit this entire section if no distinct mechanism is observed]
- Abnormal Event:
- Subject–Event Coupling:
- Transferable Mechanism:
- Surface Implementation:
- Emotional Function: [optional]

## 核心梦律 / Core Visual Rules
1. [five to eight high-impact executable rules]

## 视觉语法 / Visual Grammar
[include only relevant observed dimensions]
- Composition:
- Camera / Viewpoint:
- Light / Value:
- Exposure / Tonal Behavior:
- Color:
- Material:
- Spatial Grammar:
- Character / Blocking:
- Capture / Rendering / Mark-making:
- Art Direction:

## Transfer Scope / 迁移范围
### Strong Transfer / 强继承
- [...]
### Conditional Transfer / 条件继承
- [item → Preserve / Adapt / Release condition]
### Do Not Transfer / 默认不继承
- [...]

## 可替换槽位 / Allowed Variation
- [what may change and the condition that keeps the visual grammar intact]

## 来源残留 / Source Residue
- [specific people, wardrobe, locations, architecture, props, animals, text, brands, events, or incidental objects that do not belong to the visual grammar]

## 失效警报 / Drift Warnings
- [the most likely composition, light, exposure, color, material, capture, commercialization, or source-contamination failures]

## 单轴复用原则
[optional; include only for a series or remix that must vary one axis at a time]

## 复用前检查
- [only checks that materially protect this card]

## 最短记忆公式
[optional user-facing summary; never a substitute for Core Visual Rules]
```

Use `Not observed` or omit unsupported fields instead of inventing certainty. Omit the entire Expression Mechanism section when absent; do not print empty mechanism fields. Do not force optional tension, single-axis, checklist, or summary sections into an ordinary compact card.

## Reuse

When the user supplies an existing Decode Card:

1. Treat it as Decoded Visual Grammar, not as Scene Master facts.
2. Read Primary Medium, optional Expression Mechanism (including its four key fields), the full Core Visual Rules, Transfer Scope, Allowed Variation, Source Residue, and Drift Warnings first when present. A card without the original image must still preserve the mechanism's transferable relationship when one was observed.
3. Reconcile every Conditional Transfer item against the new Scene Master.
4. Respect newer explicit user instructions.
5. Compile `Scene Master + Primary Medium + optional Expression Mechanism + 3–5 Active Core Rules + Transfer Scope + relevant Visual Grammar` through the Compiler Priority Gate and selected target adapter. Omitted optional fields are not a license to invent them.

In a new conversation the user must supply the complete card again. A title alone does not recover an unavailable card. Reattach accessible images when visual identity or fresh image comparison requires them; a text card is not an image reference. Do not claim persistent memory.

Do not mechanically match the card to the nearest predefined Style Card. A Style Card may supplement it only when the user asks to combine them.

## Series Continuity

For a series, keep responsibilities separate:

- **Continuity Bible:** character, wardrobe, props, location, geography, story chronology, current state, and stable light facts.
- **Decode Card:** shared Primary Medium and Expression Mechanism when supported, Core Visual Rules, Transfer Scope, color and exposure behavior, material language, texture/capture character, composition tendencies, spatial rhythm, and anti-clichés.
- **Scene Master:** the canonical facts and intent for the current shot.

If the Decode Card conflicts with an explicit scene fact or Continuity Bible lock, the scene fact or continuity lock wins. Adapt or release the conflicting visual tendency; do not create a second source of truth.

## Drift Check

After each generated result, first decide whether a difference is a **Valid Adaptation** required by the new Scene Intent or an **Actual Drift** that breaks Core Visual Rules, Strong Transfer, or Reference Roles. Only Actual Drift enters Decode Repair and the existing `CHANGE ONLY` / `PRESERVE EXACTLY` contract.
