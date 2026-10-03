# Installation and First Use


<a id="install-codex"></a>
## Install in Codex

According to the current OpenAI documentation, Codex discovers Skills in the user-level `$HOME/.agents/skills` and project-level `.agents/skills` directories. You can also ask the built-in `$skill-installer` to install from another GitHub repository. See [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills).

### Method 1: Ask Codex to install from GitHub

Enter this in Codex:

```text
Use $skill-installer to install zy-cinematic-realism from this GitHub repository:
https://github.com/popopo-99/zy-cinematic-realism/tree/main/zy-cinematic-realism
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

<a id="use-chatgpt"></a>
## Use in ChatGPT

### If your account has a Skills installation entry point

According to the current OpenAI documentation, Personal Skills are generally available to ChatGPT Business, Enterprise, Healthcare, and Edu users, subject to workspace settings and permissions. Do not assume the feature is enabled for every ChatGPT account. See [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066).

If Skills are available in your account or workspace:

1. Open **Plugins** in the sidebar.
2. Open **Skills** in the Plugin Directory.
3. Choose **Create**, then **Upload from your computer**.
4. Upload `zy-cinematic-realism-v2.4.0.zip` from the latest Release.
5. After scanning and installation finish, enter `$zy-cinematic-realism` or describe a cinematic prompt task directly.

Personal Skills currently need to be added separately in desktop and web/mobile interfaces; they do not automatically synchronize across those interfaces.

### If your account does not have a Skills entry point

Paste the full [self-contained chat starter](chat-starter-en.md) into an AI conversation that can read text and, when needed, images. Add your idea or references. It includes basic scene creation, reference roles, medium preservation, and scoped repair without requiring repository access.

This basic edition does not contain all 38 directors, creative cards, or model parameter adapters. Full capability requires the complete installed folder or access to the relevant references. **Pasting SKILL.md alone is not a complete installation.**

### Check the installation

```text
Use $zy-cinematic-realism:
A woman just off work holds hot coffee with both hands inside a rainy-night convenience store, looking away from camera.
Give me a Midjourney prompt and briefly explain the key visual decisions.
```

Expect a scene-specific prompt without another model question. If the Skill is missing, check for an accidentally nested duplicate folder. Replace the complete old folder when upgrading; avoid duplicate installations.

### Resume in a new conversation

Supply the full Decode Card or Project Handoff Card again. Reattach accessible images when identity depends on them; text cards do not replace visual identity references. The Skill does not automatically save projects or synchronize cards between conversations.

[Back to README](../README_EN.md) · [Project Handoff Card rules](../zy-cinematic-realism/references/project-handoff.md)

---

This card is optional; one sentence is enough to start.


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

