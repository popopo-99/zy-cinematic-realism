# 安装与第一次使用

本文对应 **v2.5.0 正式版**。下载[完整安装 ZIP](https://github.com/popopo-99/zy-cinematic-realism/releases/download/v2.5.0/zy-cinematic-realism-v2.5.0.zip)（[SHA-256 校验文件](https://github.com/popopo-99/zy-cinematic-realism/releases/download/v2.5.0/zy-cinematic-realism-v2.5.0.zip.sha256)），或安装 [main 分支源码](https://github.com/popopo-99/zy-cinematic-realism/tree/main/zy-cinematic-realism)。更新说明见 [v2.5.0 Release](https://github.com/popopo-99/zy-cinematic-realism/releases/tag/v2.5.0)。


<a id="install-codex"></a>
## 安装到 Codex

OpenAI 当前文档说明，Codex 会从用户级 `$HOME/.agents/skills` 与项目级 `.agents/skills` 目录发现 Skill；也可以让内置的 `$skill-installer` 从其他 GitHub 仓库安装。详见 [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills)。

### 方法一：让 Codex 从 GitHub 安装

在 Codex 中输入：

```text
请使用 $skill-installer，从下面的 GitHub 仓库安装 zy-cinematic-realism：
https://github.com/popopo-99/zy-cinematic-realism
使用 main 分支，Skill 文件夹为 zy-cinematic-realism。
```

如果当前 Codex 界面提供 Skills 安装或本地导入入口，也可以选择 Release 下载的 ZIP，或解压后的 `zy-cinematic-realism` 文件夹。不同产品界面的入口可能不同。

### 方法二：手动安装

解压 [v2.5.0 安装 ZIP](https://github.com/popopo-99/zy-cinematic-realism/releases/download/v2.5.0/zy-cinematic-realism-v2.5.0.zip)，或从 [main 分支](https://github.com/popopo-99/zy-cinematic-realism/tree/main)下载源码，将完整的 `zy-cinematic-realism` 文件夹复制到用户级 Skills 目录。

**Windows**

```text
%USERPROFILE%\.agents\skills\zy-cinematic-realism
```

**macOS / Linux**

```text
$HOME/.agents/skills/zy-cinematic-realism
```

也可以只在某个项目中安装：

```text
项目目录/.agents/skills/zy-cinematic-realism
```

Codex 通常会自动发现变更；如果没有出现，请重新启动 Codex。安装后输入：

```text
请使用 $zy-cinematic-realism，把“两个侦探在审讯失败后坐夜班公交车回警局”转换成真实电影单帧 Prompt。
```

<a id="use-chatgpt"></a>
## 在 ChatGPT 中使用

### 有 Skills 安装入口

根据 OpenAI 当前说明，Personal Skills 通常面向 ChatGPT Business、Enterprise、Healthcare 和 Edu 用户，实际可用性还会受到工作区设置和权限影响。不要假设所有 ChatGPT 账户都已经开放此功能。详见 [OpenAI：Skills in ChatGPT](https://help.openai.com/en/articles/20001066)。

如果你的账户或工作区已经开放 Skills：

1. 在侧边栏打开 **Plugins / 插件**。
2. 在 Plugin Directory 中进入 **Skills**。
3. 选择 **Create**，再选择 **Upload from your computer**。
4. 下载并上传 [v2.5.0 完整安装包](https://github.com/popopo-99/zy-cinematic-realism/releases/download/v2.5.0/zy-cinematic-realism-v2.5.0.zip)，文件名为 `zy-cinematic-realism-v2.5.0.zip`。
5. 扫描和安装完成后，输入 `$zy-cinematic-realism`，或直接描述电影感 Prompt 任务。

Personal Skills 需要分别添加到桌面端和 Web / 移动端，目前不会自动跨这些界面同步。

### 没有 Skills 入口

打开[自包含聊天入门版](chat-starter-zh.md)，将全文粘贴到能读取文字、并在需要时读取图片的 AI 对话，再附上想法或参考图。它包含基础创作、参考职责、媒介保真和局部修复规则，不需要访问仓库文件。

这是基础聊天版，不包含完整的 38 位导演库、风格卡和模型参数适配器。完整能力需要安装整个 Skill 文件夹，或让对话能够访问其所需 references。**只复制 SKILL.md 不等于安装完整 Skill。**

### 确认安装成功

```text
请使用 $zy-cinematic-realism：
雨夜便利店里，一个刚下班的女人双手握着热咖啡，不看镜头。
给我 Midjourney Prompt，并简短说明关键画面决定。
```

应得到针对当前画面的 Prompt；已指定模型时不重复询问。若 Skill 未出现，检查是否误放成两层同名目录。升级时完整替换旧文件夹，避免同名副本。

### 从故事或剧本开始

安装后直接附上你要开发的故事或剧本节选，用普通中文说明任务：

```text
请使用 $zy-cinematic-realism：
我有一段短故事，先做给导演讨论的场景美术概念。
提出空间、材料、人物造型、道具和光线的候选设计。
区分原文事实、剧情解读和新增设计，先给模型中立方案。
下面是故事节选：
（在此粘贴你要开发的片段）
```

美术概念帮助导演讨论视觉世界，空间、材料、人物造型、道具与光线仍是候选设计。想看故事里的关系变化，也可以直接说“挑人物关系变化的关键画面”；每张只选一个具体瞬间，不要求先做美术概念。按你这次的请求展开，一句话就能开始。

会先根据可读文字理解人物的目标、阻力与变化；原文没有的设计会标为建议。若只想读懂剧情，写“先只分析，不给 Prompt”，就只交分析。

美术方案或关键画面计划还不是最终 Prompt。需要提示词时，可以说“把这个美术概念编译成 Midjourney Prompt”，或“保留已接受的视觉设定，把选定的关键画面编译成 Prompt”；若一开始已要求 Prompt，就直接编译。沿用对话中已确定的模型，也可以先要模型中立 Prompt；Skill 不自动生图，实际生成需要你所用环境的生图功能。

上传整个剧本时，说明想开发的场次；给电影名时，还需要可读取的片段或来源。电影记忆、字幕与电影剧照不能代替剧本文字证据。

[《泰坦尼克号》三等舱舞会实战](titanic-story-to-frame.md)展示原文动作怎样进入原创视觉开发，包含 P01 认可方向及用户确认可用的新 P02/P03，配图为原创开发结果，非电影剧照。

[《最后一张照片》美术概念与关键画面试用](last-photo-art-development.md)包含用户确认可用的空椅邀请、靠肩小笑和无人空间美术三张图，展示人物关系与场景设计的不同用途。

### 在新对话恢复

把完整解梦卡或项目交接卡重新提供给新对话。角色身份需要参考图时，也要重新附上可访问的图片；文字卡不能代替图片身份参考。Skill 不会自动保存项目或在对话之间同步卡片。

[返回 README](../README.md) · [项目交接卡规则](../zy-cinematic-realism/references/project-handoff.md)

---

这张卡片可选；一句话也能开始，无需填满表格。


## 完整输入卡片

第一次使用时，可以直接复制这张卡片。填不完也没关系：

```text
请使用 $zy-cinematic-realism：

故事类型：
时间与地点：
人物：
刚刚发生了什么：
此刻的小动作：
情绪：
希望的观察位置：
最不想出现的效果：
目标模型（不确定可留空）：

请输出：
1. Scene Master
2. 目标模型原生 Prompt
3. 当前场景专属约束与 Avoid
```

