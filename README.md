# ZY Cinematic Realism Skill

把一句简单的画面想法，扩写成具有叙事瞬间、真实空间、明确摄影机位置、可信光源和克制胶片质感的英文 AIGC Prompt。

它不是一组 `cinematic / 8K / masterpiece` 风格词，而是一套让 ChatGPT、Codex 或兼容 Agent 按电影导演与摄影指导的顺序组织画面的工作流。

## 能做什么

- 把中文或英文场景想法扩写为完整英文电影单帧 Prompt
- 自动补足故事瞬间、人物小动作和环境使用痕迹
- 设计可想象的摄影机位置、构图、焦段与画幅
- 建立来自窗户、路灯、荧光灯、台灯等真实来源的光线逻辑
- 生成与当前场景对应的精简 Avoid 负面提示词
- 诊断并重写海报感、概念图感、游戏渲染感或过度 AI 化的 Prompt

## 仓库结构

```text
zy-cinematic-realism/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── basic-prompt-template.md
└── references/
    ├── camera-and-light.md
    ├── cinematic-principles.md
    ├── examples.md
    ├── negative-prompts.md
    └── quality-checklist.md
```

仓库根目录的 `zy-cinematic-realism/` 文件夹就是可安装 Skill；`README.md` 只用于 GitHub 展示，不属于 Skill 本体。

## 安装到 Codex

将完整的 `zy-cinematic-realism` 文件夹复制到个人 Skills 目录，然后重新打开 Codex：

```text
%USERPROFILE%\.codex\skills\zy-cinematic-realism
```

也可以把仓库克隆后，仅复制其中同名的 Skill 文件夹。

## 使用

显式调用：

```text
请使用 $zy-cinematic-realism：

两个 1980 年代纽约侦探在审讯结束后，凌晨坐在警局楼梯间。
一个脾气暴躁，一个冷静缜密。
不要人物海报感，要像真实犯罪电影中段被偶然截取的一帧。
```

Skill 默认输出：

1. 简短的画面理解
2. 完整英文 `Final Prompt`
3. 当前场景专属 `Avoid`

安装后，遇到“电影感 Prompt”“降低 AI 感”“电影单帧”“设计摄影机位置与真实光源”等任务时也可以自动触发。

## 不安装也能用吗？

可以。打开 `zy-cinematic-realism/SKILL.md`，把内容与自己的场景想法一起发给支持长文本提示的 AI。安装版的优势是可以重复调用，并按需读取模板、检查表和案例。

## 设计原则

> 先让画面成为故事中的一个真实瞬间，再考虑它使用什么镜头和胶片。

摄影参数只能强化画面，不能代替故事、人物、场景和光线逻辑。
