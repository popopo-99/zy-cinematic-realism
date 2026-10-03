# v2.4.0 验证记录 / Validation Record

Date: 2026-10-03 (Asia/Shanghai).

不同证据分别记录；文字或静态通过不等于图像增益。 / Static or text checks do not establish image-quality or usability gains.

| Check | Status | Evidence / boundary |
| --- | --- | --- |
| Static director, version, local-link checks | Passed locally | `scripts/validate_director_library.py`; checks content organization, not director recognizability |
| Static Skill and README contracts | Passed locally | `scripts/validate_skill.py`; manual-case presence is not execution |
| Skill frontmatter / scaffold validation | Passed locally | skill-creator quick validator; no behavioral gain claim |
| Independent text behavior | Executed, 6 cases | [Full inputs, responses, references, and observations](behavior-check-v2.4.md); no image generation |
| ZIP packaging | Built and verified: 73 files, 193,725 bytes | `scripts/build_release.py`; checks single root, file set, bytes, licensing files, integrity, and SHA256 |
| Lossless presentation encoding | Executed, 7 images | 14,585,369 PNG bytes → 10,948,374 WebP bytes (24.9% smaller). Pixel equality checked; original PNGs retained. No artwork changes |
| GitHub README desktop/mobile rendering | Visually inspected | Chinese and English pages at desktop and 390px widths; first-use anchors navigate correctly, four showcase images per page load, task entries remain readable. First-use code lines shortened for narrow screens |
| GitHub Actions static/package checks | Passed | PR #4 runs the two repository validators and release builder; this verifies repository/package contracts, not image quality |
| Image-level comparison | Not executed | Existing 10-case protocol remains; no new-versus-old image-quality winner selected |
| Human first-use / interaction comparison | Not executed | Layout and output-depth changes are implemented design candidates, not proven usability gains |

## Independent Text Checks

Six requests cover subtle/strong director interpretation with daylight joy and locked framing; a locked procedural gesture and sole source in MJ output; cumulative car edits in a handoff; a missing card/identity image; and check-only prompt diagnosis.

Observed text retained the principal locks, respected prompt-only/check-only scope, retained cumulative white paint and half-lowered driver window, and did not invent memory or generated-image acceptance. Strong director recognizability under extensive locks remains unknown. The handoff honestly records absent full prior prompt and unresolved passenger-window state; these cannot be recovered from missing material.

This is one independent agent execution of each request, not a statistical reliability estimate, an online model compatibility check, or execution of every manual case.

## Further Evaluation

- Repeat meaningful behavior cases in real user sessions when expanding scope or changing rules.
- Compare new and old output approaches on three tasks: first-use from one sentence, non-photographic reference transfer, and three successive edits plus restoration.
- Use the [paired image protocol](../zy-cinematic-realism/tests/manual-regression.md): preserve reference, scene facts, model/version, ratio, and visible settings; at least three independent pairs per relevant case. Do not weaken the baseline.
- Record source-content leakage, scene integrity, medium and grammar fidelity, and human creative judgment. Director recognizability and human interaction gains require their own evidence.

No image-generation result, acceptance rate, latency improvement, or human usability score is claimed for v2.4.0.

Package SHA256: `1a8e5fa45a523f2ea396153e1938f16a3153b9b4a31dcded600f63de80cdfd98`.
