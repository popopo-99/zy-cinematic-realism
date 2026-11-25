[中文](README.md) | **English**

# Dream Director · 造梦师

**Turn an idea into a visual plan you can generate, revise, and continue.**

Start with a story, screenplay excerpt, or references. Establish the scene, develop the visual world, and compile model-native prompts and scoped repair instructions.

**v2.7.0 stable · Capture Design & Dream Decode** · [Download ZIP](https://github.com/popopo-99/zy-cinematic-realism/releases/download/v2.7.0/zy-cinematic-realism-v2.7.0.zip) · [SHA-256](https://github.com/popopo-99/zy-cinematic-realism/releases/download/v2.7.0/zy-cinematic-realism-v2.7.0.zip.sha256) · [Release notes](RELEASE_NOTES.md#release-notes-en) · [Installation](docs/getting-started_EN.md) · [60-second start](#quick-start) · [Screenplay example](docs/titanic-story-to-frame.md) · [Examples](#showcase)

- **Camera & Lens Arsenal and conversational photography guidance.** Say “keep the background readable,” or specify a camera, lens, focal length and aperture. [53 camera-language terms](zy-cinematic-realism/references/camera-language-dictionary.md), the [camera and lens library](zy-cinematic-realism/references/equipment-library.md) and the [film/shot library](zy-cinematic-realism/references/cinema-shot-library.md) connect on demand within one Scene Master. [Snowy Western equipment walkthrough in Chinese](docs/v2.7-camera-arsenal-snow-western.md) · [Capture Design guide in Chinese](docs/capture-design.md)

  > Use `$zy-cinematic-realism` to look up the ARRI Signature Prime 35mm. Explain what keeps the subject sharp with a smooth transition into out-of-focus areas. Then look up the German bunker sequence in *1917*. Cite the interview, list the documented focal length, and flag the aperture and subject distance as unknown if the source gives neither.

- **Dream Decode and media adaptation.** Assign each reference a role such as identity, composition or style. Extract how it handles form, values, materials and color. Save approved rules in a Style Capsule when you need them across scenes, with the intended medium guiding the transfer.
- **One conversational entry with optional professional output.** Start in everyday language and get a plain-text prompt by default. Ask for a Capture Plan to review the setup, or request a full Jury JSON Brief with a HEX palette and color roles directly.

After installing the complete Skill in Codex or a ChatGPT workspace with Skills, try this request. Paste the resulting prompt into Seedream 5.5 when you are ready to generate.

```text
Use $zy-cinematic-realism.
A daylight forest portrait, sharp eyes and recognizable background trees, 21:9.
Choose the equipment. Give me a plain-text Seedream 5.5 prompt directly.
```

[Quick-start guide in Chinese](docs/v2.7-quick-start.md) · [Jury contribution and sources](docs/capture-design-credits.md) · [Archived v2.6.0 notes](RELEASE_NOTES.md#造梦师-v260--从画面到资产)

![Two detectives sit apart in silence on a night bus after a failed interrogation](docs/images/hero-night-bus.webp)

<sub>The author's existing AIGC work: distance, seat occlusion, and practical light express a failed investigation. Not regenerated as a v2.4 test result. [Original image](docs/images/hero-night-bus.png)</sub>

A visual-creation Skill for ChatGPT / Codex. You get a copyable prompt, with brief visual decisions, a Decode Card, or continuity planning when needed. Image generation requires the features available in your environment; installing the Skill does not automatically invoke an API or select the underlying model.

The technical name and invocation remain `zy-cinematic-realism` / `$zy-cinematic-realism`.

<a id="input-card"></a>
<a id="quick-start"></a>
## Start in 60 Seconds

After installation, copy:

```text
Use $zy-cinematic-realism.
A woman just off work holds hot coffee inside a convenience store on a rainy night,
looking away from camera. Give me a Midjourney prompt directly.
```

Start by saying what you want to make. Include the subject, action, location and established target model in one sentence, with any framing, light or ratio choices you already have.

Continue naturally:

```text
Keep the person, action, and light.
Only move the camera
outside the awning,
looking through glass.
```

Add “prompt only” for a copyable prompt without explanation. Ask for the Scene Master, four-axis director breakdown, or continuity plan when you want depth. The Skill keeps the established model; it asks once only when an unknown target materially affects compilation. You can request a model-neutral version first.

**Not installed?** See [installation](docs/getting-started_EN.md). Without a Skills entry point, paste the [self-contained chat starter](docs/chat-starter-en.md); this basic edition omits the complete director library and model parameter adapters.

## One style, two outputs · Observatory case

The observatory scene was compiled into a plain-text prompt and a Jury JSON Brief with 15 HEX colors. The public walkthrough includes the original prompts and observations from one output per group. The images are held locally, and several variables may account for their differences. [Original prompts and observations in Chinese](docs/v2.7-style-output-case.md) · [60-second tutorial in Chinese](docs/v2.7-video-tutorial.md)

## Visual comparisons · Published historical cases

The following images are already archived in this repository. **They are not the unreleased v2.7 observatory A/B outputs**, and they do not establish a controlled quality ranking of models or directors.

### One Scene Master, four model interpretations (v2.0.0 historical samples)

<table>
<tr>
<td width="50%"><img src="docs/images/v2/model-compiler-gpt-image-2.webp" alt="Historical GPT Image 2 interpretation" width="100%"><br><strong>GPT Image 2</strong></td>
<td width="50%"><img src="docs/images/v2/model-compiler-midjourney.webp" alt="Historical Midjourney interpretation" width="100%"><br><strong>Midjourney</strong></td>
</tr>
<tr>
<td><img src="docs/images/v2/model-compiler-seedream-5-pro.webp" alt="Historical Seedream 5.0 Pro interpretation" width="100%"><br><strong>Seedream 5.0 Pro</strong></td>
<td><img src="docs/images/v2/model-compiler-nano-banana.webp" alt="Historical Nano Banana interpretation" width="100%"><br><strong>Nano Banana</strong></td>
</tr>
</table>

[Four-model comparison notes](docs/model-comparison.md)

### One evidence room, six director perspectives (v1.2.0 historical samples)

<table>
<tr>
<td width="33%"><img src="docs/images/director-style-comparison/baseline.webp" alt="No-director baseline" width="100%"><br><strong>Baseline</strong></td>
<td width="33%"><img src="docs/images/director-style-comparison/wong-kar-wai.webp" alt="Wong Kar-wai reference" width="100%"><br><strong>Wong Kar-wai</strong></td>
<td width="33%"><img src="docs/images/director-style-comparison/stanley-kubrick.webp" alt="Stanley Kubrick reference" width="100%"><br><strong>Stanley Kubrick</strong></td>
</tr>
<tr>
<td><img src="docs/images/director-style-comparison/denis-villeneuve.webp" alt="Denis Villeneuve reference" width="100%"><br><strong>Denis Villeneuve</strong></td>
<td><img src="docs/images/director-style-comparison/david-fincher.webp" alt="David Fincher reference" width="100%"><br><strong>David Fincher</strong></td>
<td><img src="docs/images/director-style-comparison/terrence-malick.webp" alt="Terrence Malick reference" width="100%"><br><strong>Terrence Malick</strong></td>
</tr>
</table>

[Six complete historical prompts and test context](docs/director-style-comparison.md)

<a id="core-workflows"></a>
<a id="continuity"></a>
<a id="prompt-doctor"></a>
<a id="use-cases"></a>
## Start with What You Have

- **Story / screenplay**: “Develop a scene art concept to discuss with the director.” / “Choose key frames where the relationship changes.”<br>→ Art concepts explore candidate spaces, materials, character looks, props, and light; narrative key frames show one specific moment

- **Idea**: “Two detectives ride a night bus after a failed interrogation. Give me a cinematic still prompt.”<br>→ Brief decisions and a target-native prompt

- **Reference**: “A supplies color; B supplies composition. Replace the content with a watchmaker before dawn.”<br>→ Roles, core rules, and a new-scene prompt

- **Repair**: “Identity and framing are right. Fix only the commercial-looking light.”<br>→ Up to three dominant failures and scoped repair

- **Asset pack**: “This direction works. Prepare the references needed for a reverse and an evidence close-up.”<br>→ Reuse or derive only needed assets, with scoped roles, proposed extensions, and prop state

- **Series**: “Eight urban-knight shots; preserve face, armor, garage, and sources.”<br>→ Continuity, shot list, and controlled deltas

- **Variation**: “Same scene, compile for Seedream.” / “Change only the camera.”<br>→ Transcode or a one-variable variation

- **Resume**: “Make a handoff card with accepted changes and the next step.”<br>→ Complete portable project state

References contribute only within assigned roles. Paper illustration does not default to photography; an identity reference does not take over the medium. Analysis-only requests receive no unwanted generation prompt.

For an existing story or script, one sentence describing the task is enough. Analysis-only requests stay analysis-only. An art concept or frame plan still needs model-native prompt compilation; the Skill does not generate images automatically.

<a id="asset-pack"></a>
## From an Accepted Frame to the Next Shot

Determine which references a reverse, rear view, hand insert, or new scene actually needs. A character sheet may clearly show the outfit; the narrative image keeps the user's visual grammar.

```text
Use $zy-cinematic-realism:
Continue this look. The next shots are a rear-view exit and an evidence insert.
Prepare the necessary asset plan and prompts; do not generate images yet.
Mark unseen back/shoe designs as proposals and reuse sufficient references.
```

![Two detectives examine an audio cassette on a night bus](docs/images/last-bus-testimony/master.png)

[Last Bus Testimony: actual prototype](docs/last-bus-testimony-asset-pack.md) follows look correction, role-scoped references, a close view, reverse, dawn exterior, and targeted repair. The user confirmed the set usable. This is one qualitative example, not proof of general gains; New York, retro low-key rendering and the wide ratio belong to this example.

<a id="story-to-frame"></a>
## Screenplay to Frames: Titanic's Third-Class Dance

An awkward first dance, active participation after removing her shoes, and laughter after being caught beside a table. Read the change, develop a shared visual world, then turn actions and relationships into key frames.

[Workflow and actual result status](docs/titanic-story-to-frame.md): script facts, interpretation, and new directing proposals lead into reference decoding, external generation, and inspection. The case shows the P01 direction and the new P02/P03 images confirmed usable by the user, together with the supplied prompts and actual result observations.

<table>
<tr>
<td width="33%"><img src="docs/images/titanic-story-to-frame/accepted-p01.webp" alt="P01 established visual direction" width="100%"><br><strong>P01 · Entering the dance</strong></td>
<td width="33%"><img src="docs/images/titanic-story-to-frame/accepted-p02.webp" alt="P02 taking the lead" width="100%"><br><strong>P02 · Taking the lead</strong></td>
<td width="33%"><img src="docs/images/titanic-story-to-frame/accepted-p03.webp" alt="P03 shared laughter by the table" width="100%"><br><strong>P03 · Relationship shift</strong></td>
</tr>
</table>

### Original Short Story: Art Concepts and Relationship Key Frames

[The Last Photo trial](docs/last-photo-art-development.md): three follow-up external images are approved by the user for case display: an invitation through an empty chair, a shoulder lean with a small smile, and an empty-room art concept. They show the different purposes of art development and relationship key frames; production details remain open.

<a id="showcase"></a>
## Three Ways to See the Method

### 1. Choose a Specific Story Moment

![A detective revisits case files beside a table lamp at home](docs/images/scene-private-aftermath.webp)

A task lamp, unfinished coffee, and doorway viewpoint show that the case continues. Action, space, and sources come before lens or film labels. Waiting and aftermath are options; requested daylight joy, celebration, and climactic action remain valid directions.

```text
Use $zy-cinematic-realism:
A detective comes home late, coat still on, and checks the case files again beside a table lamp.
Eye-level view from the doorway. Give me a model-neutral prompt using practical sources.
```

[More story moments, boxing, and historical work](docs/visual-guide_EN.md). Images are existing author work; reusable calls do not promise identical regeneration.

<a id="director-method"></a>
<a id="creative-grammar"></a>
### 2. Change How the Scene Is Witnessed

<table>
  <tr>
    <td width="50%"><img src="docs/images/director-style-comparison/baseline.webp" alt="Historical no-director evidence-room baseline" width="100%"><br><strong>No-director baseline</strong><br>Investigative action</td>
    <td width="50%"><img src="docs/images/director-style-comparison/wong-kar-wai.webp" alt="Historical strong Wong Kar-wai evidence-room interpretation" width="100%"><br><strong>Wong Kar-wai · historical strong mode</strong><br>Reflections, obstruction, and nocturnal relationships</td>
  </tr>
</table>

v2.4 honors **subtle / clear / strong**; unspecified strength defaults to clear. Subtle uses selected compatible traits. Strong changes only open decisions. Locked action, camera, composition, and sources are not reselected to manufacture difference.

```text
Use $zy-cinematic-realism:
A young officer searches a video shop during a blackout for a tape. Subtle Diao Yinan reference.
Keep medium framing, the searching action, and the doorway camera. Give me an MJ prompt.
```

[38-director index](zy-cinematic-realism/references/directors/index.md) · [Strength and locks](zy-cinematic-realism/references/director-routing.md) · [Six historical calls and prompts](docs/director-style-comparison.md)

<a id="dream-decode"></a>
### 3. Decode the Rules, Replace the Content

The night-bus cover lets us discuss cool practical light with small warm highlights, subject-to-space relationships, glass reflection, and selective visibility. The bus, detectives, and seats do not have to enter the next scene.

```text
Use $zy-cinematic-realism:
Use only the attached night-bus image's color, exposure, and material relationships.
New scene: an elderly watchmaker closes a pocket watch before dawn. Chest-up medium framing is locked.
Do not import the bus, detectives, or clothing. Decode, then give a model-neutral prompt.
```

[Reference, five core rules, complete reuse card, and transfer prompt](docs/dream-decode-example.md). **This is a text worked example grounded in an actual reference. The transferred image has not been generated; it is not an image-level v2.4 comparison.**

Reuse the card in the same conversation; supply its full contents again in a new one. Reattach accessible images when identity or editing depends on them.

<a id="install-codex"></a>
<a id="use-chatgpt"></a>
<a id="install"></a>
## Install or Upgrade

| Environment | Entry point |
| --- | --- |
| Codex | [Install from GitHub or a local folder](docs/getting-started_EN.md#install-codex) |
| ChatGPT with Skills | [Upload the complete installation ZIP](docs/getting-started_EN.md#use-chatgpt) |
| No Skills entry point | [Paste the self-contained basic chat edition](docs/chat-starter-en.md) |

Download the [complete v2.7.0 package](https://github.com/popopo-99/zy-cinematic-realism/releases/download/v2.7.0/zy-cinematic-realism-v2.7.0.zip) ([SHA-256 checksum](https://github.com/popopo-99/zy-cinematic-realism/releases/download/v2.7.0/zy-cinematic-realism-v2.7.0.zip.sha256)), or install the complete source from [main](https://github.com/popopo-99/zy-cinematic-realism/tree/main/zy-cinematic-realism). [Upgrade and compatibility notes](RELEASE_NOTES.md#release-notes-en)

The installation ZIP has one top-level `zy-cinematic-realism/` folder. Replace the complete old folder and avoid duplicate installations. **SKILL.md alone does not include its referenced method library.**

<a id="model-router"></a>
<a id="model-comparison"></a>
<a id="advanced"></a>
## Go Deeper

`Scene Master + Visual Grammar → Independent Model Compiler → Result Repair`

Story or screenplay work reads character change, develops scene art concepts or narrative key frames for the requested purpose, then joins this pipeline.

Model syntax can change; locked scene facts cannot change silently.

| Topic | Documentation |
| --- | --- |
| Develop art concepts or narrative key frames from a story | [Story to Frame workflow](zy-cinematic-realism/references/story-visual-development.md) · [Titanic example](docs/titanic-story-to-frame.md) |
| Story, directors, and cinematography | [Visual guide and historical work](docs/visual-guide_EN.md) |
| Reference roles, medium, and decode | [Dream Decode](zy-cinematic-realism/references/dream-decode.md) · [Decode Card](zy-cinematic-realism/references/decode-card.md) |
| Iteration and a new conversation | [Project Handoff Card](zy-cinematic-realism/references/project-handoff.md) |
| Prepare references for later shots | [Asset Pack workflow](zy-cinematic-realism/references/asset-pack.md) · [Actual prototype](docs/last-bus-testimony-asset-pack.md) |
| Series continuity | [Continuity Bible](zy-cinematic-realism/references/continuity-cards.md) |
| Scoped repair | [Prompt Doctor](zy-cinematic-realism/references/result-repair.md) |
| Model compilation and selection | [Compiler](zy-cinematic-realism/references/prompt-compiler.md) · [Router](zy-cinematic-realism/references/model-routing.md) |
| Historical four-model image comparison | [One Scene Master, multiple interpretations](docs/model-comparison.md) |
| Release changes | [Release notes](RELEASE_NOTES.md#release-notes-en) · [CHANGELOG](CHANGELOG.md) |

Supports GPT Image 2.5 with explicit GPT Image 2 compatibility, Midjourney V8.2, Seedream 5.5, explicit Seedream 5.0 Pro requests, Nano Banana, and model-neutral work. Adapters record when documentation was checked. Available controls depend on your current interface.

<a id="repository-structure"></a>
<a id="validation"></a>
## Validation Status

The v2.7 equipment walkthrough records an actual text exchange. The observatory case records exploratory observations from user-supplied images. The v2.6 records for text trials, image revisions and feedback on the asset workflow remain available.

**A worked example and general improvement are separate claims.** Historical images are not retests for this upgrade; Expected entries in manual regression are specifications, not execution records. See the validation record for the new example's generation, comparison, and check status.

[v2.7 validation scope](RELEASE_NOTES.md#release-notes-en) · [v2.6 validation record](docs/validation-v2.6.md) · [v2.5 validation history](docs/validation-v2.5.md) · [v2.4 validation history](docs/validation-v2.4.md) · [Manual regression and image comparison protocol](zy-cinematic-realism/tests/manual-regression.md)

The repository root contains tutorials and work; `zy-cinematic-realism/` is the installable Skill. `scripts/` provides static checks and packaging. The ZIP excludes the showcase gallery.

<a id="community"></a>
## Build Dream Director Together

Thanks to everyone who tested, shared, and supported this project. The [complete Special Thanks list and community illustration](docs/community.md) remain available.

Useful feedback includes the input, target model, reference roles, actual result, and what must remain. [Open an issue](https://github.com/popopo-99/zy-cinematic-realism/issues).

<a id="license"></a>
## Attribution and Licensing

Author: **ZY / popopo-99**. Licensed under [CC BY-NC 4.0](LICENSE). Personal study, non-commercial creation, and attributed adaptations follow the license. Commercial use and repackaging require the permissions described in the [complete licensing guide](docs/licensing.md). Generated prompts and user works do not automatically belong to the project author.

[Attribution, restrictions, and commercial contact](docs/licensing.md) · [NOTICE](NOTICE.md)

> Make the frame a specific moment inside a story before deciding which lens or film stock it uses.
