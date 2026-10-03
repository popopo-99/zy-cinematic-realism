# 安装与第一次使用

本文对应 **v2.5.0 发布候选**，正式 GitHub Release 尚未创建。当前可安装[审查分支源码](https://github.com/popopo-99/zy-cinematic-realism/tree/codex/story-to-frame/zy-cinematic-realism)，或使用本次交付的候选包 `zy-cinematic-realism-v2.5.0.zip`。[当前稳定发布](https://github.com/popopo-99/zy-cinematic-realism/releases/latest)另有独立入口。


<a id="install-codex"></a>
## 安装到 Codex

OpenAI 当前文档说明，Codex 会从用户级 `$HOME/.agents/skills` 与项目级 `.agents/skills` 目录发现 Skill；也可以让内置的 `$skill-installer` 从其他 GitHub 仓库安装。详见 [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills)。

### 方法一：让 Codex 从 GitHub 安装

在 Codex 中输入：

```text
请使用 $skill-installer，从下面的 GitHub 仓库安装 zy-cinematic-realism：
https://github.com/popopo-99/zy-cinematic-realism
使用审查分支 codex/story-to-frame，Skill 文件夹为 zy-cinematic-realism。
```

如果当前 Codex 界面提供 Skills 安装或本地导入入口，也可以选择 Release 下载的 ZIP，或解压后的 `zy-cinematic-realism` 文件夹。不同产品界面的入口可能不同。

### 方法二：手动安装

从[审查分支](https://github.com/popopo-99/zy-cinematic-realism/tree/codex/story-to-frame)下载源码，或解压本次候选 ZIP，将完整的 `zy-cinematic-realism` 文件夹复制到用户级 Skills 目录。需要稳定版时使用 [Releases](https://github.com/popopo-99/zy-cinematic-realism/releases/latest)。

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
4. 上传本次交付的候选包 `zy-cinematic-realism-v2.5.0.zip`；正式 Release 尚未发布。
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

### 从一段剧本开始

安装后直接附上你要开发的剧本节选，用普通中文说明任务：

```text
请使用 $zy-cinematic-realism：
我有一段剧本，先帮我找人物变化，再开发视觉世界和关键画面。
区分原文事实、剧情解读和新导演建议。
每张关键画面只选一个具体瞬间，先给模型中立方案。
下面是剧本节选：
（在此粘贴你要开发的片段）
```

会先根据可读文字判断人物的目标、阻力与变化，再给视觉开发方案和关键画面；衣饰、灯光、机位等新增设计会标为建议。若只想先读懂剧情，写“先只分析，不给 Prompt”。选定方向后再说“保留这个视觉世界，把选定的关键画面编译成 Midjourney Prompt”，继续沿用已接受的设定。

上传整个剧本时，说明想开发的场次；给电影名时，还需要可读取的片段或来源。电影记忆、字幕与电影剧照不能代替剧本文字证据。

[《泰坦尼克号》三等舱舞会实战](titanic-story-to-frame.md)展示原文动作怎样进入原创视觉开发。案例配图为用户认可作为后续视觉方向的 P01 修订图，非电影剧照；后续画面的状态分别记录。

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

