<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Result Repair — Prompt Doctor

Use this mode when the user provides or describes a generated result. Diagnose the image-result gap, not only the wording of the original prompt.

## Dominant Failures

Choose at most three failures from:

`Story · Blocking · Space · Camera · Composition · Light · Exposure · Color · Material · Texture · Continuity · Rendering · Commercialization · CG · Medium Drift · Mechanism Drift · Reference Role Drift · Model Syntax`

Prefer causes over symptoms. “Commercial look” may come from posing, centered scale, equal highlight treatment, clean visibility, and a privileged camera position; do not treat it as a single negative keyword.

## Structural Decision

### A. Structural scene is sound

Use a Surgical Repair Prompt:

```text
CHANGE ONLY:
[the smallest observable changes]

PRESERVE EXACTLY:
[identity, wardrobe, scene, action, camera, light, topology, or other successful facts]

[Target Model] Repair Prompt:
[native edit instruction]
```

### B. Structural scene failed

When the story beat, visual center, blocking, topology, or camera position is wrong, rebuild from the Scene Master. Do not stack corrective adjectives onto a failed structure. State what is being rebuilt and what successful facts remain locked.

## Repeated photographic-effect failures

When the same photographic target remains unmet, use the current input and available result evidence to check the intended mechanism, preservation constraints that may suppress it, the scene conditions needed to reveal it, the suitability of the generation method for the change's scope, and model limitations actually observed in the results. Treat descriptions supplied by the user as reported feedback when images are unavailable.

Before proposing another repair after repeated failures, give a concise diagnosis of those factors and state what the available evidence can establish. Include any fidelity pressure or uncertainty about method limits, even when the user's decision requires continuing the same edit path. Then identify the specific new correction being tested, or explain why the available evidence supports only a limit or a request for the missing result.

Keep proposed next steps within the user-authorized workflow and available capabilities. An external preprocessing stage, crop or different execution method requires applicable authorization and a capability check. When the locked path has no supported new correction, explain the limitation or request the missing result evidence. A repair proposal itself leaves any needed release of constraints pending the user's decision.

Choose the next change from that diagnosis. Identify a concrete mechanism, region, condition or constraint to repair. If the evidence offers no new correction, explain the unmet target and the relevant strategy choice. Repeated intensifiers alone do not address the cause. Report unverified explanations as hypotheses and keep the model-specific conclusion within the observed cases.

For global projection changes, use [Capture Strategy Selection](capture-design.md#capture-strategy-selection) to distinguish preserved identity, topology and viewpoint from authorized image-point movement. Keep still-valid locks when rebuilding from the Scene Master. Continue within an explicitly locked image-edit path and state its observed limits. Releasing a lock or changing the generation method requires the user's applicable authorization. An already authorized compatible repair proceeds directly.

## OpenAI 2.5 edit scope

Use the existing Surgical Repair contract: name the changed region and new physical state in `CHANGE ONLY`; protect identity, geometry, requested composition, lighting relationships, and unaffected objects in `PRESERVE EXACTLY`. Prefer **one meaningful variable per edit**. Closely related changes requested together may share an edit, but do not proactively widen the scope.

Carry the previous accepted output into the next turn, restate the preserve rules, and inspect each result against the Continuity Bible / One Variable Remix locks. Improved multi-turn preservation does not guarantee unchanged pixels. During migration, test a validated GPT Image 2 prompt unchanged first and repair only an observed failure; see the [2.5 adapter and official basis](models/gpt-image-2.md).

## Adapter Rules

- GPT Image 2.5 (and GPT Image 2 legacy), Seedream, and Nano Banana repair instructions may emphasize explicit preserve/change boundaries when the active tool supports image editing.
- Midjourney V8.2 repair must first choose between prompt regeneration and the current Edit Model. Rebuild through an ordinary prompt when scene structure failed; use a supplied image/reference and, when relevant, an Editor selection for targeted inpainting, outpainting, perspective change, or recombination. Do not route the current default through legacy Omni Reference, Character Reference, or the separate Retexture workflow, and do not imply that prompt-only remix provides deterministic local preservation.
- For a series, load `continuity-cards.md` and protect the Continuity Bible before repairing a shot.

Compile every repair through the target adapter. Do not invent an editing control that the user's frontend has not established.

## Decode Repair

When the user supplies or compares both the original reference and a generated result, first compare the result with the accepted Reference Decode, Core Visual Rules, Transfer Scope, and Scene Master. Select at most three dominant drifts; do not re-run the entire creative process by default.

Before diagnosing failure, classify each difference:

- **Valid Adaptation:** a Conditional Transfer changed to satisfy the new Scene Intent, fixed facts, or physical logic. Preserve it. A requested close portrait is not Composition Drift merely because the reference subject was small in a wide frame.
- **Actual Drift:** the authorized Primary Medium or an actually observed Expression Mechanism, a Core Visual Rule, or Strong Transfer changed without justification; a Conditional Transfer moved farther than the new scene required; or Do Not Transfer source residue reappeared. An absent mechanism cannot create Mechanism Drift.

Inspect in this order, but select **at most three evidence-backed Actual Drifts**: (1) Valid Adaptation first; (2) Medium Drift—making logic changed, e.g. paper edges and flat pigment became photographic skin or glossy CG; (3) Mechanism Drift **only if a distinct mechanism was observed**—the abnormal event moved away from the subject or lost its emotional function; (4) broken Core Visual Rules; (5) lost Strong Transfer; (6) Source Residue leakage. A medium-compatible change explicitly required by the new Scene Master is Valid Adaptation, not Medium Drift. If the mechanism is preserved through different objects, do not repair it back into literal reference content.

Only Actual Drift enters `CHANGE ONLY`. Protect every Valid Adaptation, accepted Primary Medium, intact mechanism, and successful Scene Master facts in `PRESERVE EXACTLY`. Diagnose target-model noncompliance separately; a failed image does not by itself prove the decode or compiler was wrong.

If composition and scene facts are correct but light and material have drifted, `CHANGE ONLY` may contain only light and material corrections. `PRESERVE EXACTLY` must protect the successful Scene Master facts, composition, camera, blocking, color relationships, and every accepted rule outside the repair scope.

Use [dream-decode.md](dream-decode.md) for drift categories and [decode-card.md](decode-card.md) when a reusable card or series visual grammar exists. Reference Role Drift means content or authority came from the wrong reference; repair the role boundary before adding descriptive style language. Source Residue appearing in a style-only transfer is Actual Drift even when its rendering looks plausible.

## Style construction repair

For style drift, locate the changed construction in Form, Shading, Material, Color, Texture, View / Lens or Rendering rules and cite available result evidence. A plausible new interpretation remains Valid Adaptation within its accepted scope. Repair only actual failures of the authorized rules, such as lost value groups, photographic pores in simplified animation, flattened directional fur in realistic CG, or painted marks replaced by generic gloss.

Use the existing at-most-three-failure Surgical Repair. Protect identity, required facial and wardrobe features, composition, scene facts, successful rules and accepted partial transfers. A useful CG virtual lens remains valid within that medium. Keep Brief descriptions, image observations and proposed corrections distinguishable. If no result can be inspected, report supplied feedback as reported evidence. Repeated failures use the existing diagnostic branch and scoped authorization for any strategy change.
