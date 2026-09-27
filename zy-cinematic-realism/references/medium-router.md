<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Per-Reference Medium Router / 逐图媒介路由

Run this **after Reference Role Router and before Dream Decode**. Identify each image's making logic, not merely its subject or a generic style label. Analyze every reference separately, but only a reference assigned Visual Grammar, Rendering / Medium, or another explicit medium-authority role may control the final medium. A Character Identity or Composition reference does not silently become a medium reference.

## Per-reference record

- **Primary Medium:** the dominant image-making system, stated as an observable process, not a fixed category. Photography, ink on absorbent paper, painted cut-paper collage, stylized 3D, scanned print, and hybrids are examples, not a closed enum.
- **Secondary Influences (0–2):** only visible and causally relevant secondary processes. Do not list every resemblance.
- **Confidence:** high / medium / low, with a brief reason. At low confidence, describe the evidence and avoid fabricated production claims.
- **Medium Constraints:** actionable identity-critical marks of the medium—edges, layering, texture scale, light/shading logic, depth cues, surface response, or capture/print artifacts.
- **Medium Avoid:** likely substitutions that would erase the medium, such as photographic skin in a paper illustration or glossy game-render surfaces in a matte 3D reference.
- **Conflict Notes:** disagreement with other references, user roles, or the requested reinterpretation; `none` when absent.

Distinguish visual evidence from a claim about the actual production method. A digital imitation of watercolor can be routed by its visible watercolor-like behavior without asserting it was painted physically.

## Authority and mixed-media resolution

1. Respect explicit user-assigned roles and exclusions. An explicit realistic / cinematic reinterpretation may change the medium; record what remains of the reference rather than pretending the original medium was photographic.
2. Same or strongly aligned primary media: use the shared observable grammar; retain meaningful variation as conditional.
3. Compatible media: choose one primary medium according to explicit priority and use at most two compatible secondary influences with clear jobs. Mixed medium must have a legible construction rule, not an averaged label.
4. Incompatible media: resolve by role and user priority. If one is identity-only and one is medium-authoritative, the latter controls the medium. When the user explicitly requests cross-medium fusion, name a **Host Medium** that controls the final image surface and a **Secondary Construction Rule** specifying the other reference's limited contribution. For example, colored pencil on paper may host stylized-3D spatial geometry without importing glossy PBR, render polish, or volumetric cinematic lighting. This is an assigned construction, not automatic averaging. If two explicit medium-authoritative instructions remain incompatible without a host or priority and the difference materially changes the result, mark the conflict and ask one focused question; never average them.
5. If no image has medium authority, do not transfer medium from image appearance by accident. Use the Scene Master or ask only when the choice materially changes output.

For a style-reference Dream Decode, the authorized reference medium outranks the Skill's default cinematic realism. Do not translate a light paper illustration into a photograph or a stylized 3D scene into live-action / generic CG unless the user explicitly asks for that reinterpretation.

Pass the resolved **Primary Medium**, relevant Secondary Influences, Medium Constraints, Medium Avoid, and Conflict Notes to Dream Decode and the Prompt Compiler. Keep per-image evidence available for repair. Medium routing does not own people, events, objects, or scene facts.
