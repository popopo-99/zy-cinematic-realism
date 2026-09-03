[中文](README.md) | **English**

# Dream Director

## A Cinematic Visual Guide for the AI Era · v2.1.0

**DREAM DIRECTOR v2.1 — Midjourney V8.2 Adapter Migration**

> Build one stable visual plan first. Then translate it into the language each model understands best.

![Two detectives sitting apart in silence on a night bus after a failed interrogation](docs/images/hero-night-bus.png)

<p align="center">
  <strong>From one prompt to a complete visual plan.</strong>
</p>

<p align="center">
  <strong>One Scene Master. Different models. Native prompts.</strong>
</p>

Dream Director is not a new image model or a bag of universal “cinematic” keywords. It is a cinematic visual workflow for ChatGPT and Codex. It first locks the character, story moment, action, setting, camera, composition, light, props, time, weather, and constraints, then compiles that plan into a native prompt for the target model.

`Scene Master → Creative Grammar → Model Compiler → Result Repair`

The public brand is **造梦师 / DREAM DIRECTOR**. To preserve installation paths, automatic triggering, and explicit invocation, the technical name remains `zy-cinematic-realism`, and the invocation remains `$zy-cinematic-realism`.

**[Download the latest release](https://github.com/popopo-99/zy-cinematic-realism/releases/latest)**

### v2.1.0 — Midjourney V8.2 Adapter Migration

Midjourney compilation now uses V8.2 as its capability baseline, with updated prompt compilation, Edit Model routing, reference-image strategy, parameter handling, and Transcode behavior.

## v2.0.0: From Final Prompt to Model Compiler

The old workflow was:

`Idea → Skill → Final Prompt`

In v2.0.0 it becomes:

`Idea → Scene Master → Creative Grammar → Model Compiler → GPT Image 2 / Midjourney / Seedream 5.0 Pro / Nano Banana`

The `Scene Master` is the single source of truth. It locks the visual design first. `Creative Grammar` then decides style, cinematography, and blocking, and the appropriate `Model Compiler` translates the result. Transcoding may change syntax, information density, parameter placement, and editing language, but it must not silently change the character, action, location, light, or narrative relationship.

```text
MODEL SYNTAX MAY CHANGE.
SCENE LOGIC MAY NOT.
```

**Model language may change. The visual design may not change behind your back.**

## Ten Core Capabilities

- **Create** — Build a Scene Master from one idea and compile it into a native prompt for the target model. Example: `A woman holds a hot coffee outside a convenience store on a rainy night, looking away from camera.`
- **Model Router** — Recommend a suitable adapter path for the task. Example: `I need a character look first, then several prop edits. Which model workflow should I use?`
- **Model Compiler** — Translate one visual plan into an expression a specific model can execute more naturally. Example: `Compile this Scene Master for Midjourney.`
- **Transcode** — Change model language while preserving scene facts. Example: `Convert this GPT Image 2 prompt to Seedream 5.0 Pro.`
- **Multi-model Pack** — Produce native versions for multiple models in one pass. Example: `Give me four model-native versions of the same scene.`
- **Continuity Bible** — Lock characters, wardrobe, props, locations, and light across shots. Example: `Build an eight-shot sequence of an urban knight leaving work.`
- **Prompt Check** — Find conflicts, vague language, and physically impossible instructions before generation. Example: `Check why this prompt may turn into a poster.`
- **Prompt Doctor** — Repair only the variables that caused a failed result. Example: `The character looks like an ad; only fix camera position, posing, and light hierarchy.`
- **One Variable Remix** — Lock every core fact and change one variable only. Example: `Move the witness position from the front to outside the doorway, and change nothing else.`
- **Creative Shuffle** — Recombine style, cinematography, and blocking within controlled boundaries. Example: `Give me three restrained, production-ready directions.`

## One Scene Master, Four Model Interpretations

The four results below share the same core visual constraints: a black horse, a person in silver armor, a coast, breaking waves, and a cool, realistic environment. Only the model adapter and the model's own interpretation differ. These are not the same image, and the workflow does not promise pixel-level consistency.

<table>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/v2/model-compiler-gpt-image-2.webp" alt="GPT Image 2 interpretation of a Scene Master with a black horse, silver-armored figure, and coast" width="100%">
      <br><strong>GPT Image 2</strong>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/v2/model-compiler-midjourney.webp" alt="Midjourney interpretation of a Scene Master with a black horse, silver-armored figure, and coast" width="100%">
      <br><strong>Midjourney</strong>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/v2/model-compiler-seedream-5-pro.webp" alt="Seedream 5.0 Pro interpretation of a Scene Master with a black horse, silver-armored figure, and coast" width="100%">
      <br><strong>Seedream 5.0 Pro</strong>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/v2/model-compiler-nano-banana.webp" alt="Nano Banana interpretation of a Scene Master with a black horse, silver-armored figure, and coast" width="100%">
      <br><strong>Nano Banana</strong>
    </td>
  </tr>
</table>

```text
Same Scene Master.
Different native prompts.
Different model interpretations.
```

## Model Router and Four Native Adapters

| Target model | Compilation focus |
|---|---|
| GPT Image 2 | Structured natural-language visual and editing instructions |
| Midjourney V8.2 | Concise, natural visual relationships with request-relevant parameters at the end |
| Seedream 5.0 Pro | Explicit spatial and subject relationships presented as a visual brief |
| Nano Banana | Direct, task-oriented language suited to iterative editing |

The Router is a task heuristic, not a permanent ranking, and it does not claim that one model is “best.” Model capabilities and interfaces change; the Scene Master remains responsible for scene logic.

The Midjourney adapter now targets the current V8.2 by default, preserves natural visual relationships, distinguishes Imagine from the Edit Model, and selects parameters by need instead of applying a legacy suffix template.

## Get Started in 60 Seconds

### 1. Create from one sentence and choose a model

```text
Use $zy-cinematic-realism:
A woman who has just finished work holds a hot coffee with both hands
inside a convenience store on a rainy night. She is not looking at camera.
Recommend a suitable model path, then compile a native Midjourney prompt.
Avoid advertising poses, direct eye contact, and unmotivated rim light.
```

The Skill first organizes a Scene Master, then produces a Midjourney-native expression. You do not need to know photographic terminology. At minimum, provide:

```text
who + where + what just happened + the small action now + what you do not want
```

### 2. Transcode, compile a pack, repair, or remix

```text
Transcode: Keep the woman, convenience store, rainy night, hot coffee,
and lack of eye contact unchanged. Convert it to GPT Image 2.

Multi-model Pack: Compile the same Scene Master into native prompts for all four models.

Prompt Doctor: The result looks like a coffee commercial. Only repair the camera position,
character pose, and light hierarchy. Preserve identity, wardrobe, coffee, and location.

One Variable Remix: Move the camera from a frontal interior view to a position outside
the awning, looking through glass. Lock everything else.
```

## Continuity: Base Lock + Shot Delta

For an eight-shot sequence about an urban woman knight leaving work, start with a `Continuity Bible` that locks her face, silver commuter armor, worn canvas bag, folding spear, station, and cool/warm practical light sources. Every shot combines the same `Base Lock` with one limited `Shot Delta` describing only the new action, camera, or time change.

This reduces drift in faces, clothing, props, locations, and lighting. It does not promise identical model outputs; it makes every change traceable.

## Prompt Doctor: Repair, Do Not Rewrite

When a result looks like a commercial, the problem is usually not a lack of “cinematic” words. The camera may be too frontal, the character may be posing, or the key and supporting light may have no hierarchy. Prompt Doctor diagnoses the result before producing a scoped repair instruction:

```text
CHANGE ONLY: camera position, posing, and light hierarchy.
PRESERVE EXACTLY: identity, wardrobe, car, and location.
```

Repair is not a new creative pass. Character identity, wardrobe, vehicle, and location remain anchored to the original Scene Master. Only named variables may change.

## Creative Grammar: Executable Decisions, Not Filters

v2.0.0 preserves the Four-Axis Visual Fingerprints for 38 directors and adds 16 style cards plus 8 cinematography cards. These cards alter light, exposure, camera, space, blocking, and visual center instead of appending a style label.

- Style cards provide controlled directions such as austere realism, wet noir, quiet everyday life, or institutional pressure.
- Cinematography cards provide witness positions such as outside a doorway, close but obstructed, distant negative space, or a procedural locked-off camera.
- Director references continue to shape contrast, color and exposure, camera position, and composition without copying any specific film shot.

Technical camera details come last. They strengthen a story moment that already works; they do not replace the story.

## Choose a Different Moment from the Same Story

The Skill does more than apply filters to one composition. It helps decide which moment in the story deserves to be seen.

### The interrogation is slipping out of control

![An interrogation slipping out of control, observed through one-way glass](docs/images/scene-interrogation.png)

The camera is not seated at the negotiation table. It watches through one-way glass. Reflections, monitoring equipment, and large dark areas make the audience feel like an observer who should not be there.

### The case follows him home

![A detective reading files alone in his apartment late at night](docs/images/scene-private-aftermath.png)

The character does not need to cry or shout. A letter on the desk, unfinished coffee, a doorway obstruction, and one table lamp are enough to show that he still cannot let go.

### Silence after the truth

![Two detectives standing small inside the negative space of a riverfront](docs/images/scene-river-silence.png)

The characters become small and move away from center while the city and river occupy most of the frame. The environment no longer serves as background; it speaks for them.

### The protagonist leaves; the city continues

![A police car receding along a city street at dawn](docs/images/scene-city-finale.png)

An ending does not require a close-up of the protagonist. Seen through scratched glass, the police car disappears as ordinary people begin a new day. The story is over, but the city has not stopped.

## The Method Works Across Genres

![A boxer caught at the instant of impact through the ring ropes](docs/images/scene-boxer-corner.png)

Action does not require a clean, complete heroic composition. Foreground ropes and an opponent's body obstruct the view; slight motion blur preserves the speed of impact; the subject may not even be perfectly focused. It feels like a frame the camera managed to catch during the fight, not a sports advertisement.

The same method works for crime, boxing, family drama, science fiction, historical stories, and urban shorts. The principle remains:

> **Do not stop at “two boxers fighting intensely.” Specify the round, the fraction of a second before or after impact, what the camera sees through, and how much motion blur should remain.**

## Reobserve the Same Story Through a Director's Method

### Director Four-Axis Visual Fingerprint System

The director library is no longer a list of names, representative films, and a style sentence appended to the end of a prompt. When a supported director is selected, the Final Prompt generates four consecutive, scene-specific decisions after the grounded facts and before detailed camera design:

1. `Lighting and contrast signature`
2. `Color and exposure signature`
3. `Lens and camera signature`
4. `Composition and spatial signature`

Every line must describe a concrete decision for the current scene. Compared with the no-director baseline, at least three axes must change structurally, and at least three of the following must be reselected: story moment, visual center, camera position, subject scale, or whether environment, character, or object dominates. If the director's name and film titles are removed, the four-axis result should still be recognizable.

The same story therefore changes in light, color, camera, and composition while preserving the user's period, location, characters, event, physical space, and motivated light. Representative works are model-recognition anchors only; the system does not copy any specific scene.

| Region | Selected directors | Most visible four-axis direction |
|---|---|---|
| Chinese-language cinema | Zhang Yimou, Jia Zhangke, Wong Kar-wai, Hou Hsiao-hsien, Edward Yang, Diao Yinan | From ritual color order to social transition, subjective cities, and layered everyday life |
| Japanese cinema | Akira Kurosawa, Yasujirō Ozu, Shunji Iwai, Hirokazu Kore-eda, Kiyoshi Kurosawa | From weather-driven action axes to domestic space, seasonal memory, and unseen threat |
| Korea and Southeast Asia | Bong Joon-ho, Park Chan-wook, Lee Chang-dong, Apichatpong Weerasethakul | From class space and object desire to moral observation and tropical time |
| European auteurs | Andrei Tarkovsky, Stanley Kubrick, Alfred Hitchcock, Ingmar Bergman | From elemental memory and institutional geometry to gaze-based suspense and facial relationships |
| American genre and auteur cinema | David Fincher, David Lynch, Martin Scorsese, Francis Ford Coppola, Michael Mann | From procedural information and psychological disturbance to street systems, family power, and nocturnal professional networks |
| Contemporary international cinema | Christopher Nolan, Denis Villeneuve, Terrence Malick, Alfonso Cuarón, Chloé Zhao | From physical mechanisms and environmental scale to bodily tactility, continuous social space, and working landscapes |

[Browse the full index of 38 directors, aliases, and four-axis summaries](zy-cinematic-realism/references/directors/index.md) · [Choose directors by scene goal with the recommendation matrix](zy-cinematic-realism/references/directors/recommendation-matrix.md)

```text
Use $zy-cinematic-realism:

Late 1990s, a small city in southern China. A young police officer searches
a video rental shop during a blackout for a tape left by a missing person.

Director reference: Diao Yinan
Style strength: strong

Make the director's light and contrast, color and exposure, camera distance,
and spatial composition distinct, explicit, and non-interchangeable.
Do not copy any specific film scene.
```

> For supported directors, `轻微 / 明确 / 强烈 / subtle / clear / strong / iconic` all resolve to the mandatory strong mode.

### Four directors, one fixed scene

The story fact remains “searching for a tape inside a video store during a blackout”:

| Director | Light | Color and exposure | Camera | Composition and space |
|---|---|---|---|---|
| Diao Yinan | Green emergency lamps and a red exit sign form isolated hard pools of light | Tired skin, dense blacks, practical sources cutting through the frame | A slightly delayed observational medium-wide shot, panning only after the action | Departing customers and seats fragment the officer; danger remains inside public order |
| David Fincher | Low illumination preserves legibility on the tape, hand, and logbook | Neutral-cool response, controlled paper white, precise falloff in secondary zones | An exact medium shot from the doorway with minimal movement; focus connects information nodes | Tape, record, and gesture form a traceable evidence chain |
| Wong Kar-wai | Fluorescent light, exit light, and rain-soaked exterior light contaminate one another | Mixed color casts, local underexposure, slight drift around practical highlights | Compressed or mildly distorted close observation through glass or seating | Reflection and obstruction turn the search into a private missed encounter |
| Edward Yang | The store, corridor, and street retain ordinary practical light | Honest fluorescent and urban material colors without an emotional filter | A clear medium-long view from the adjacent room or ticket counter, retaining context | Architecture separates officer, clerk, and departing customers; social relationships outweigh the tape |

## What Would Different Directors See in the Same Story?

This stress test locks the same story, characters, period, location, and evidence, changing only the director reference. v2.0.0 preserves those structural differences and forces every direction into four consecutive signatures—contrast, color and exposure, camera position, and composition—so models are less likely to collapse the result into one generic style sentence.

The difference is not a filter on the same image. Each director makes a new decision about what the shot is actually watching.

Fixed scene: mid-1980s Manhattan, late at night in a police evidence room. A tired detective compares a city garage employee card with a black-and-white surveillance projection on the wall.

<table>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/baseline.webp" alt="No-director baseline in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>No-director baseline</strong>
      <br>
      <sub>Grounded investigative action, plausible camera, practical light</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/wong-kar-wai.webp" alt="Strong Wong Kar-wai mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>Wong Kar-wai</strong>
      <br>
      <sub>Subjective time, obstructed reflections, unfinished nocturnal relationships</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/stanley-kubrick.webp" alt="Strong Stanley Kubrick mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>Stanley Kubrick</strong>
      <br>
      <sub>Institutional geometry, cool distance, unease inside order</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/denis-villeneuve.webp" alt="Strong Denis Villeneuve mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>Denis Villeneuve</strong>
      <br>
      <sub>Spatial pressure, negative space, small figures inside environment</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/david-fincher.webp" alt="Strong David Fincher mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>David Fincher</strong>
      <br>
      <sub>Procedural information, exact camera position, controlled evidence hierarchy</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/terrence-malick.webp" alt="Strong Terrence Malick mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>Terrence Malick</strong>
      <br>
      <sub>Bodily pauses, tactile interruption, incomplete projected moments</sub>
    </td>
  </tr>
</table>

| Version | What the shot primarily watches |
|---|---|
| No-director baseline | How the detective compares the employee card with the surveillance projection |
| Wong Kar-wai | Late-night isolation, reflection, obstruction, and an incomplete psychological relationship |
| Stanley Kubrick | How the individual is controlled by institutional space and geometric order |
| Denis Villeneuve | How a small detective faces an evidence system heavier than himself |
| David Fincher | How cards, projection, photographs, and text form a precise information chain |
| Terrence Malick | How a tired body, paper edges, sleeves, and projection light interrupt procedural action |

> Every version preserves the same story facts. The differences come from reselecting the moment, visual center, camera, blocking, light, depth of field, and texture.

[View all six invocation examples, Final Prompts, and Avoid blocks](docs/director-style-comparison.md)

## Complete Input Card

Copy this card when you first use the Skill. It is fine to leave fields blank:

```text
Use $zy-cinematic-realism:

Story genre:
Time and place:
Characters:
What just happened:
Small action in this moment:
Emotion:
Preferred witness position:
What you most want to avoid:
Target model (leave blank if unsure):

Output:
1. Scene Master
2. Target-model-native prompt
3. Scene-specific constraints and Avoid block
```

## Install in Codex

According to the current OpenAI documentation, Codex discovers Skills in the user-level `$HOME/.agents/skills` and project-level `.agents/skills` directories. You can also ask the built-in `$skill-installer` to install from another GitHub repository. See [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills).

### Method 1: Ask Codex to install from GitHub

Enter this in Codex:

```text
Use $skill-installer to install zy-cinematic-realism from this GitHub repository:
https://github.com/popopo-99/zy-cinematic-realism
```

If your Codex interface offers a Skills installation or local import entry point, you can also choose the ZIP from the latest Release or the extracted `zy-cinematic-realism` folder. Entry points vary by product interface.

### Method 2: Install manually

Download and extract the latest package from [Releases](https://github.com/popopo-99/zy-cinematic-realism/releases/latest), then copy the complete `zy-cinematic-realism` folder into your user-level Skills directory.

**Windows**

```text
%USERPROFILE%\.agents\skills\zy-cinematic-realism
```

**macOS / Linux**

```text
$HOME/.agents/skills/zy-cinematic-realism
```

You can also install it for one project only:

```text
your-project/.agents/skills/zy-cinematic-realism
```

Codex normally discovers the change automatically. Restart Codex if the Skill does not appear. After installation, enter:

```text
Use $zy-cinematic-realism to turn “two detectives riding a night bus back to the station
after a failed interrogation” into a grounded cinematic still prompt.
```

## Use in ChatGPT

### If your account has a Skills installation entry point

According to the current OpenAI documentation, Personal Skills are generally available to ChatGPT Business, Enterprise, Healthcare, and Edu users, subject to workspace settings and permissions. Do not assume the feature is enabled for every ChatGPT account. See [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066).

If Skills are available in your account or workspace:

1. Open **Plugins** in the sidebar.
2. Open **Skills** in the Plugin Directory.
3. Choose **Create**, then **Upload from your computer**.
4. Upload `zy-cinematic-realism-v2.1.0.zip` from the latest Release.
5. After scanning and installation finish, enter `$zy-cinematic-realism` or describe a cinematic prompt task directly.

Personal Skills currently need to be added separately in desktop and web/mobile interfaces; they do not automatically synchronize across those interfaces.

### If your account does not have a Skills entry point

You can still use the workflow directly:

1. Open [`zy-cinematic-realism/SKILL.md`](zy-cinematic-realism/SKILL.md).
2. Copy its contents into a new AI conversation.
3. Add your scene idea below it.
4. Ask the AI to follow the workflow and output a target-model-native prompt plus scene-specific constraints.

This does not require Codex or plugin installation, but you may need to provide the rules again in each conversation.

## Repository and Package Structure

The repository root contains the brand guide, tutorials, license, and release history. The installable Skill itself is the `zy-cinematic-realism/` folder.

```text
zy-cinematic-realism/                 # GitHub repository root
├── README.md                          # Default Chinese guide and showcase
├── README_EN.md                       # English guide and showcase
├── CHANGELOG.md                       # Version history
├── LICENSE                            # CC BY-NC 4.0
├── RELEASE_NOTES.md                   # v2.1.0 release notes
├── docs/
│   └── images/                        # Visual examples
├── scripts/
│   └── validate_director_library.py   # Director-library and Markdown-link validation
└── zy-cinematic-realism/              # Installable Skill
    ├── SKILL.md
    ├── LICENSE
    ├── NOTICE.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   └── basic-prompt-template.md
    ├── references/
        ├── camera-and-light.md
        ├── cinematic-principles.md
        ├── model-routing.md
        ├── model-capability-matrix.md
        ├── prompt-compiler.md
        ├── prompt-check.md
        ├── result-repair.md
        ├── continuity-cards.md
        ├── style-cards.md
        ├── cinematography-cards.md
        ├── examples.md
        ├── director-routing.md
        ├── directors/
        │   ├── index.md
        │   └── recommendation-matrix.md
        ├── negative-prompts.md
        ├── models/
        │   ├── gpt-image-2.md
        │   ├── midjourney.md
        │   ├── seedream-5-pro.md
        │   └── nano-banana.md
        └── quality-checklist.md
    └── tests/
        └── manual-regression.md
```

The v2.1.0 Release package has exactly one top-level Skill folder:

```text
zy-cinematic-realism-v2.1.0.zip
└── zy-cinematic-realism/
    ├── SKILL.md
    ├── LICENSE
    ├── NOTICE.md
    ├── agents/
    ├── assets/
    ├── references/
    └── tests/
```

## Copyright and License

The Skill source files include copyright notices. The distributable Skill package contains its own license file.

Copyright:

ZY / popopo-99

License:

CC BY-NC 4.0

## Use and Licensing

*Dream Director: A Cinematic Visual Guide for the AI Era v2.1.0* is licensed under [Creative Commons Attribution-NonCommercial 4.0 International](LICENSE) (CC BY-NC 4.0).

You may:

- Use it for personal study and non-commercial creation.
- Adapt the workflow for your own projects.
- Share adaptations while preserving attribution, the license, and the source.

You may not:

- Repackage and sell this Skill or a lightly modified version.
- Remove the author and source information and present it as your original work.
- Include it in paid courses, membership resources, prompt collections, or commercial products without permission.

For redistribution, include:

```text
Author: ZY / popopo-99
Project: Dream Director — A Cinematic Visual Guide for the AI Era
Repository: https://github.com/popopo-99/zy-cinematic-realism
License: CC BY-NC 4.0
```

For commercial collaboration or licensing:

- Douyin: 2053586074
- Email: zhang.yanpo@foxmail.com

Specific prompts generated by the Skill and works created by users from those prompts do not automatically belong to the project author. Users remain responsible for following the rules of their AI platforms and applicable law.

## One Last Principle

> **Make the image a real moment from the middle of a story before deciding which lens and film stock it uses. Have fun.**

The example images were created by the author using AIGC to demonstrate the narrative and cinematographic direction of this workflow.
