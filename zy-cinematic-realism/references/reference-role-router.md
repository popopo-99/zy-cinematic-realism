<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Reference Role Router

Use this router before Dream Decode or any multi-reference compilation. Its job is to decide what authority each supplied image has—not what the image contains.

After role assignment, run [medium-router.md](medium-router.md) for each image. Medium analysis observes every image, but only a Visual Grammar / Style, Rendering / Medium, or explicitly medium-authoritative role may set the final Primary Medium. Character, object, or composition roles do not gain medium authority by accident.

## Priority

1. A user-declared Reference Role has highest priority.
2. Explicit exclusions narrow that role: “lighting only, not composition” transfers light and rejects composition authority.
3. The user's new Scene Master facts outrank inferred reference content.
4. Existing adapter-specific reference categories determine how a role can be expressed in the target model; they do not redefine the user's intent.
5. Only when no role is declared may the Skill infer the narrowest reasonable role from the request.

Never treat every uploaded image as a style reference, and never let the presence of an image overwrite explicit scene facts.

## Role Vocabulary

Assign one primary role per image when possible. Combine roles only when the user clearly asks one image to control more than one dimension.

- **Visual Grammar / Style:** transferable medium, color, exposure, light, material, texture, rendering, capture, detail, and art-direction behavior.
- **Rendering / Medium:** the image-making system and identity-critical rendering behavior, without automatic authority over subject, composition, or story.
- **Character Identity:** facial and bodily identity, not wardrobe or pose unless included.
- **Wardrobe:** garment construction, layers, fit, materials, and accessories.
- **Object:** a specific prop, vehicle, product, or artifact.
- **Location:** place identity, environmental topology, or specific architecture.
- **Composition:** visual center, subject scale, negative space, layering, crop, and balance.
- **Camera:** witness position, height, distance, focal behavior, perspective, and framing boundary.
- **Lighting:** source direction and type, contrast, falloff, highlight and shadow behavior.
- **Color:** palette relationships, saturation structure, contamination, and accent behavior.
- **Material:** roughness, gloss, translucency, wear, texture scale, and surface response.
- **Texture / Capture:** grain, blur, bloom, compression, sharpness, motion, and rendering cleanliness.
- **Spatial Structure:** topology, thresholds, foreground/midground/background relationship, and environmental dominance.
- **Mood / Atmosphere:** only the observable conditions that produce the mood; do not transfer a vague adjective alone.

## Single-Reference Routing

When the user says “only use the style,” route the image to Visual Grammar and set character, wardrobe, location, objects, visible text, brand elements, and story event to Do Not Transfer. Composition, camera, subject scale, occlusion, and light direction remain Hybrid Decisions unless separately assigned.

When the user says “keep everything except the person,” assign the image a broader combined role and record the person as the explicit replacement boundary. Do not silently preserve or replace additional facts.

When the user merely asks to remove or replace an object in an image, use the ordinary edit or Result Repair path unless visual analysis or visual transfer is also requested.

## Multi-Reference Routing

First choose one of two modes.

### Consensus Decode

Use when the request asks for a shared feeling, common visual language, or moodboard synthesis without assigning separate responsibilities.

1. Decode each image independently into Scene Facts, Visual Grammar, and Hybrid Decisions.
2. Identify rules that recur as relationships, not just repeated labels.
3. Separate Stable Rules from Variable Traits.
4. Do not average contradictions. Mark them variable, conditional, or unresolved.
5. Build five to eight Core Visual Rules from the stable evidence.

### Role-Based Decode

Use when the user assigns responsibilities, such as “image one for color, image two for composition, image three for the character, image four for material.”

1. Record each assignment before analyzing the image.
2. Extract only the dimensions relevant to that assignment.
3. Preserve user-declared priority when two images affect the same field.
4. Keep identity, wardrobe, object, and location roles separate from Visual Grammar.
5. Combine assigned outputs with the new Scene Master; do not search for a shared style unless requested.

## Conflict Resolution

Resolve conflicts in this order:

1. explicit new-scene fixed fact;
2. explicit user role and priority;
3. explicit transfer exclusion;
4. established Continuity Bible fact for a series;
5. explicit Style Card instruction when the user asks to combine it;
6. inferred role or visual observation.

If two explicit user instructions remain irreconcilable and the difference would materially change the result, state the conflict briefly and ask one question. An explicit request to fuse different media is not automatically irreconcilable: use the [medium router's](medium-router.md) Host Medium and Secondary Construction Rule. Otherwise choose the narrowest interpretation that preserves the new scene.

## Hybrid Decision Gate

For composition, camera, subject scale, focal behavior, occlusion, negative space, layering, blocking, and light direction, record one of:

- **Preserve:** the user explicitly assigned it and it fits the new scene.
- **Adapt:** preserve the visual relationship while changing its literal value to fit the new scene.
- **Fill:** use an authorized reference decision where the Scene Master field is OPEN and the user did not specify a value.
- **Release:** the new scene intent or physical logic requires a different decision.

For an **OPEN** Scene Master visual decision, a system-generated default has lower priority than an authorized reference-derived Hybrid Decision; an explicit **USER-LOCKED** choice always wins.

Example: a reference uses a tiny person inside dominant architecture, while the new request requires a close portrait. Release the literal subject scale; preserve compatible light, exposure, material, edge, and capture rules. Composition does not win merely because it was visually distinctive.

## Adapter Mapping

After roles are resolved, map them to the selected adapter without inventing controls:

- **GPT Image 2.5:** describe each supplied image's brief-level responsibility; do not invent attachment fields or strengths.
- **Midjourney V8.2:** choose among Image Prompt, Style Reference, Edit Model Reference, or an established Moodboard/Personalization profile according to actual user inputs. Do not fabricate URLs, codes, weights, or profiles.
- **Seedream 5.0 Pro:** name base and auxiliary image roles and use regional controls only when the active interface exposes them.
- **Nano Banana:** assign one role per image and verify the selected family member before making multi-reference or API-specific claims.

Adapter categories express resolved roles. They do not replace Dream Decode or authorize reference content to leak into the Scene Master.

## Visible Output

For ordinary single-reference work, do not print a routing table unless it helps prevent confusion. For multi-reference work, use a compact form:

```text
Reference Roles
- A: Color + Exposure
- B: Composition + Camera
- C: Character Identity
- D: Material + Texture
```

Then continue with Shared or Assigned Visual Grammar, Core Visual Rules, and the requested prompt. Omit all explanation for prompt-only requests.
