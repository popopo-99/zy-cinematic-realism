<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Camera and Light

## Capture Design Entry

For conversational camera selection, parameter dependencies, explicit locks, or a requested setup, read [capture-design.md](capture-design.md). Store the resolved setup once, inside Scene Master → Camera / Viewpoint, and coordinate it with Light / Value and Surface / Rendering. Complete unspecified choices directly when the user asks for a prompt. A separate approval round is optional.

Use [equipment-library.md](equipment-library.md) for relevant equipment cards and [cinema-shot-library.md](cinema-shot-library.md) for source-backed film and scene methods. Ordinary language and professional terminology enter the same workflow. A product specification or a proposed recreation does not identify equipment in an uncredited reference image.

## Camera Decision Order

Choose in this order:

1. Witness position: where can the camera physically stand?
2. Subject scale / framing: extreme wide, wide, medium, close, or detail. Resolve physical camera-to-subject distance separately when it affects perspective, subject scale, or focus requirements.
3. Height and angle: eye level, seated eye level, waist height, floor level, or elevated.
4. Boundary: doorframe, seat, glass, traffic, curtain, or no obstruction.
5. Focal behavior: spatially open, neutral, compressed, or intimate.
6. Movement: locked-off, restrained handheld, vehicle vibration, slow observational drift, or none.

## Practical Focal Guidance

The ranges below use full-frame / 35mm-still framing as a reference. Record the actual format when it matters. Perspective follows camera position and subject distance. At the same position, changing focal length changes field of view; moving to preserve subject size changes the spatial relationships.

| Range | Typical framing behavior | Useful for |
|---|---|---|
| 24-32mm | Wider view; a close camera can emphasize near/far relationships | confined interiors, architecture, environmental tension |
| 35-50mm | Natural observation with moderate context | street scenes, two-shots, everyday interiors |
| 65-85mm | Narrower view; greater distance for the same subject size | surveillance, private gestures, frames through layers |
| 100mm+ | Narrow view suited to distant observation | long-lens observation, crowds, inaccessible subjects |

Do not prescribe a focal length when the model or task will not benefit from it. Never use lens choice as a substitute for a camera position.

State focal-length equivalence only when the relevant formats are known. If one choice changes, adjust only OPEN dependent choices such as distance or framing. Preserve explicit locks and explain an actual conflict briefly when it cannot be resolved within them.

## Aspect Ratio

- Use 1.33:1 or 4:3 for archival, intimate, or period television framing when requested.
- Use 1.66:1 or 1.85:1 for balanced theatrical drama.
- Use 2.00:1, 2.35:1, or 2.39:1 when horizontal relationships or environmental negative space matter.
- Do not default every scene to anamorphic ultrawide. Honor the user's requested ratio.
- Output aspect ratio, sensor format, and lens design are separate choices. A 21:9 crop alone does not produce anamorphic bokeh or flare.

## Light Construction

Build a source map:

```text
Primary source: source, direction, hardness, color tendency
Secondary source: source, timing or intensity
Shadow zones: where light is naturally blocked
Highlight surfaces: skin, wet fabric, glass, metal, dust, or paint
Exposure behavior: normal, slightly under, or protected highlights
```

Examples of motivated combinations:

- old green fluorescent bus lights plus intermittent amber streetlights;
- overcast window light plus one low warm table lamp;
- blue pre-sunrise ambient light plus weak warm light on upper brickwork;
- sodium-vapor streetlight plus cool light leaking from a convenience store;
- practical desk lamp plus dim corridor spill.

## Capture Texture

Select at most a few compatible traits:

- natural or fine grain;
- subtle halation around real bright sources;
- soft highlight roll-off;
- slight lens falloff;
- minor focus imperfection;
- physically plausible motion blur;
- muted or aged color response;
- readable shadows without an HDR look.

Treat grain and halation as capture behavior, not a decorative overlay.

Separate optical lens behavior, diffusion filters, recording-medium response, weather, and post-processing. Digital capture does not automatically add grain. A vintage lens does not automatically add swirl, halation, or a color cast. Specify the visible shape, source, location, and strength of an effect when it matters, then preserve the user's exclusions.
