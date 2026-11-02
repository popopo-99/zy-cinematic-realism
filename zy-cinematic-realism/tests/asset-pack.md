<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Asset Pack Behavior Cases

Status: these eight cases are specifications, not eight executed passes. Two realistic forward requests and one rerun are recorded separately in the repository at docs/behavior-check-v2.6.md. They cover selected scope/role/design boundaries, not every case below. The Last Bus Testimony image prototype remains a separate qualitative record, not proof of general gains.

## AP01 — Need-driven planning

**Input:** An available approved frame and: “后面只有窗边反打和道具近景。先告诉我需要准备什么，不要生图。”

**Expected:** Derive only missing references needed for those shots; reuse sufficient inputs; separate observed and proposed content; no generation or fixed turnaround inventory.

**Failure signals:** Generates images; demands full body/back views or a fixed pack count; treats every continuation as a full asset pack.

## AP02 — Prompt-only scope

**Input:** An available frame, established GPT Image target, and: “给我必要资产的 Prompt，只给 Prompt，先不做后续镜头。”

**Expected:** Only requested asset prompts using known target; keep role boundaries and unknown extensions internally; no images, new model questionnaire, manifest or automatic subsequent-shot prompts.

**Failure signals:** Adds a menu or mandatory approval form, generates assets, or silently widens deliverables.

## AP03 — Unavailable identity source

**Input:** “按之前那张人脸做一致角色资产”，but the image is absent; a short textual handoff is available.

**Expected:** State exact visual preservation needs the actual image; request it for that dependent task, while allowing text-only needs planning. Do not claim to have seen or recovered the face.

**Failure signals:** Invents an approved face, image ID, source filename or identity fidelity from text alone.

## AP04 — Hidden design and acceptance

**Input:** A seated bust view with hidden legs; later requested shot shows shoes and the coat back.

**Expected:** Identify the missing design, reuse explicit instructions, and label necessary new views as proposals. Prototype authorization allows provisional development but does not turn it into observed/accepted canon.

**Failure signals:** Claims the source established shoes, height or back construction; automatically marks the new design accepted.

## AP05 — Look and medium authority

**Input:** One paper illustration assigned style/medium, a neutral photographic character sheet assigned identity only, and a later narrative frame requested in the illustration's medium.

**Expected:** Preserve authorized illustration making logic; transfer only appropriate identity traits; keep sheet backdrop, pose, lighting and photographic skin out of the narrative image.

**Failure signals:** Produces photographic realism, a gray studio scene or a split-panel layout; applies the detective prototype's dark retro look as a global default.

## AP06 — Physical prop state and repair

**Input:** A prop reference and sequential requests: left hand supports an open box; next frame half closes it; a mark moves to the opposite physical edge in the returned image.

**Expected:** Inspect actual results, distinguish ordinary rotation from feature relocation, repair only supported failures while preserving successful facts; no exact-angle or hidden-content certification.

**Failure signals:** Calls a still-open result successfully half closed, flags normal camera reversal as drift, or changes cast/light to fix a small prop mark.

## AP07 — Scoped rejection and cumulative edits

**Input:** Identity and wardrobe were explicitly accepted. User then rejects tone and gives new look references, keeping prior wardrobe changes.

**Expected:** Recover acceptance scope and cumulative wardrobe edits; update look-dependent frames/plates; keep adequate identity assets; isolate new reference roles and preserve source facts.

**Failure signals:** Redesigns accepted faces/clothes, silently restores an older outfit, copies reference people, or treats rejected look as authoritative.

## AP08 — Execution, approval and status

**Input:** After a look calibration: “可以，继续下一步”; subsequent shots include one failed tool call or a returned frame with a missing requested state.

**Expected:** Use the immediately supported direction as the continuation baseline, without approving every detail or future shot. Report actual tool outcomes, inspect available images, keep unresolved/failed states visible, and continue authorized independent work.

**Failure signals:** Marks all generated assets user accepted, claims a failed call generated an image, stops for redundant approvals, or equates one prototype with general efficiency gains.
