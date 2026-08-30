<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Model Capability Matrix

Verified: 2026-08-29. This is a routing heuristic based on current official product documentation, not a benchmark or permanent ranking. Frontend features may differ from underlying model capabilities.

| Task axis | GPT Image 2 | Midjourney | Seedream 5.0 Pro | Nano Banana family |
|---|---|---|---|---|
| Natural-language instruction following | Strong | Good | Strong | Strong |
| Cinematic single-image generation | Strong | Strong | Strong | Strong |
| Stylistic exploration | Good | Strong | Good | Good |
| Multi-reference handling | Good | Good | Strong / frontend-dependent | Model-dependent; Strong on current generalist/pro members |
| Character or object continuity | Good with explicit locks and references | Conditional; reference and frontend dependent | Good to Strong with references | Good to Strong; member and workflow dependent |
| Iterative conversational editing | Strong | Conditional; workflow dependent | Strong | Strong |
| Local or region-specific editing | Good when editing tools expose it | Frontend-dependent through Editor | Strong when spatial controls are exposed | Good to Strong; member and frontend dependent |
| Spatial relationship control | Strong with explicit production-brief structure | Good but compression-sensitive | Strong | Strong |
| Visible text and typography | Good | Conditional | Strong | Good to Strong; member dependent |
| Layout, poster, or graphic design | Good | Good for exploration | Strong | Good to Strong; member dependent |
| Prompt compression sensitivity | Low to moderate | High | Moderate | Low to moderate |
| Parameterized control | API/frontend dependent | Strong native parameter workflow | Frontend-dependent | API/frontend dependent |
| Fast exploration | Good | Strong | Good | Strong on speed-oriented members |
| Multi-turn workflow | Strong | Frontend-dependent | Good to Strong | Strong |

## Selection Rules

- Match the recommendation to the user's actual interface, references, editing needs, text needs, and iteration style.
- Give one primary choice and optionally one backup. Do not call any model universally best.
- Treat `Conditional` and `Frontend-dependent` as a prompt to verify the user's tool, not as a deficiency score.
- Do not infer exact reference counts, resolution limits, strength ranges, or parameters from this matrix.

## Official Basis

- OpenAI: [GPT Image 2 model page](https://developers.openai.com/api/docs/models/gpt-image-2) and [image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- Midjourney: [Prompt Basics](https://docs.midjourney.com/docs/prompts), [Parameter List](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List), [Image Prompts](https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts), and [Editor](https://docs.midjourney.com/hc/en-us/articles/32764383466893-Editor)
- ByteDance Seed: [Seedream 5.0 Pro](https://seed.bytedance.com/en/seedream5_0_pro) and [official launch article](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro)
- Google: [Nano Banana image generation](https://ai.google.dev/gemini-api/docs/image-generation)
