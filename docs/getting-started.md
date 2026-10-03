# 安装与第一次使用


<a id="install-codex"></a>
## 安装到 Codex

OpenAI 当前文档说明，Codex 会从用户级 `$HOME/.agents/skills` 与项目级 `.agents/skills` 目录发现 Skill；也可以让内置的 `$skill-installer` 从其他 GitHub 仓库安装。详见 [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills)。

### 方法一：让 Codex 从 GitHub 安装

在 Codex 中输入：

```text
请使用 $skill-installer，从下面的 GitHub 仓库安装 zy-cinematic-realism：
https://github.com/popopo-99/zy-cinematic-realism/tree/main/zy-cinematic-realism
```

如果当前 Codex 界面提供 Skills 安装或本地导入入口，也可以选择 Release 下载的 ZIP，或解压后的 `zy-cinematic-realism` 文件夹。不同产品界面的入口可能不同。

### 方法二：手动安装

从 [Releases](https://github.com/popopo-99/zy-cinematic-realism/releases/latest) 下载并解压，将完整的 `zy-cinematic-realism` 文件夹复制到用户级 Skills 目录。

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
4. 上传最新 Release 中的 `zy-cinematic-realism-v2.4.0.zip`。
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

