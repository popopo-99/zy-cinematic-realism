<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Quality Checklist

Check every applicable item before responding. Rewrite any failed structural item before polishing syntax.

## Scene

- [ ] The frame occupies a specific story beat with a trace of before or after.
- [ ] Every visible character performs a natural action rather than posing.
- [ ] Environment details are few, causal, and story-relevant.
- [ ] Foreground, midground, background, and location topology are physically plausible.
- [ ] The visual center and information hierarchy are intentional.
- [ ] Period, wardrobe, props, signage, architecture, time, and weather agree.
- [ ] No user-fixed fact or restriction was silently changed.

## Camera and Light

- [ ] The witness position, distance, and height can be sketched inside the location.
- [ ] Obstruction or reflection, if present, follows from that position.
- [ ] Composition does not default to centered promotion or symmetry.
- [ ] Every important light has a source; protected shadows remain plausible.
- [ ] Color and material response follow sources, exposure, weather, and surface properties.
- [ ] Capture texture reinforces the scene instead of replacing it.

## Model

- [ ] Target model is known or explicitly model-neutral.
- [ ] The correct adapter was loaded.
- [ ] No syntax from another model leaked into the output.
- [ ] No unsupported parameter, limit, or model capability was invented.

## Scene Master and Modes

- [ ] Transcoding preserved every Scene Master invariant.
- [ ] Model syntax did not redesign story, blocking, camera, composition, or light.
- [ ] Prompt Check separates structural problems from model limitations.
- [ ] Remix changed only the requested variable axis.
- [ ] Continuity kept Base Lock stable and used Shot Delta only for current narrative change.
- [ ] Shuffle remains causally believable and uses at most one dominant unusual premise unless requested.
- [ ] A Style Card changes visual grammar rather than adding adjectives.
- [ ] A Cinematography Card changes witness role, camera, light, or spatial behavior.

## Director and Cleanup

- [ ] A supported named-director prompt follows the Four-Axis and nearest-neighbor rules in `director-routing.md`.
- [ ] Removing director names and film titles still leaves an executable visual method.
- [ ] Surfaces are not uniformly glossy, sharp, clean, or equally legible.
- [ ] The exclusion list is concise, scene-specific, model-compatible, and non-contradictory.
- [ ] The output contains no placeholders or hidden reasoning.

If the result reads like an advertisement, poster, fashion portrait, concept sheet, or game render, first revise action, subject scale, witness position, and source hierarchy. Do not repair structure with more style words.
