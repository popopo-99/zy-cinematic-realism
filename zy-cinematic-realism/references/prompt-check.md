<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Prompt Check

Inspect before rewriting. Never use numeric scores, a “cinematic index,” or praise-word counting as the diagnosis.

## Status Labels

- **PASS** — the element is clear, compatible, and physically usable.
- **WEAK** — present but underspecified or unlikely to control the result.
- **RISK** — likely to produce drift, artificial polish, or model failure.
- **CONFLICT** — two instructions, syntaxes, or constraints cannot both hold.

## Inspection Dimensions

Check Story Beat, Character Action, Blocking, Physical Space, Camera Witness Position, Composition, Lighting Source Logic, Color Logic, Medium-appropriate Material Behavior, Capture / Rendering Texture, Anti-AI Logic, Continuity, Model Compatibility, Reference Roles, Constraint Conflict, and Prompt Redundancy.

Default to the three to five findings with the greatest effect on the image. Separate:

- **structural scene failures** — missing or contradictory story, action, space, camera, composition, or light;
- **model expression failures** — mixed syntax, unsupported parameters, unsuitable density, or weak reference/edit wording;
- **cosmetic symptoms** — generic praise words, excessive texture labels, or polish that follows from the deeper problem.

Check the structural cause behind an overloaded prompt, including missing viewpoint, action or value/light hierarchy where the chosen medium and requested scene need them.

## Camera Language Semantics

For ambiguous camera wording, use the [camera-language index](camera-language-dictionary.md). Inspect the actual camera, subject, projection and time interval before assigning CONFLICT.

- When a structural camera finding is needed, identify the missing witness position, height or viewing direction. Lens values and a centered composition supply only part of that decision.
- For a real CONFLICT, name the smallest requirement or overlapping interval that needs a decision. In check-only mode, identify that choice while retaining the findings-only output.
- Separate camera position, orientation, focal length and focus. “镜头不动，向右摇镜” can hold the support position while rotating right for Pan. A camera explicitly locked in both position and orientation conflicts with simultaneous Pan or Truck movement in that same interval.
- Compare overlapping intervals for the same camera. Locked-off during 0–5 seconds and Truck right during 0–5 seconds conflict. Locked-off during 0–2 seconds followed by Truck during 2–5 seconds form a valid ordered plan. A moving subject can coexist with a locked camera.
- Check the requested projection and the relevant lines. Standard fisheye projections curve general off-axis straight lines, while a line through the image center can remain straight. Rectilinear ultra-wide projection can retain straight lines and still show strong perspective convergence. Resolve an explicit fisheye requirement combined with all off-axis architectural lines perfectly straight through the existing conflict/question strategy and Rewrite Gate.
- Check the delivery's time scope. A still can show a focus state or framing reached during a camera move. A five-second completed Dolly In, Rack Focus or Dolly Zoom requires a temporal sequence. Preserve requested motion intent when diagnosing the mismatch and use the existing compiler boundary for the output.

## Rewrite Gate

- “只检查” / “check only” → findings only; no rewrite.
- “帮我修” / “rewrite” → full corrected prompt through the target adapter.
- “尽量少改” / “surgical” → change only the minimum clauses required; list what remains preserved when explanation is allowed.

If the target model is unknown, diagnose model-neutral structure and label model compatibility as unknown. Do not block a check merely to ask for a model.

## Style and medium checks

Interpret space, camera and material checks through the authorized medium. CG virtual cameras may be useful. Graphic or painted space can use deliberate flatness and designed lighting. Judge coherence within that construction and the user's locks.

Check source-status honesty, actual image access, unsupported production/device claims, Brief/image disagreements, and approximate versus sampled palette claims. Inspect capsule rules against the original reference roles and accepted partial transfer. Flag source character, wardrobe or location leakage and unsolicited ratio changes. Check for automatic pores, grain, photographic brands or unrelated optical effects that replace the selected animation or illustration grammar. Preserve the existing findings-only Rewrite Gate.
