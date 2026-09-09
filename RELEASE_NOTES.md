# 造梦师 v2.1.1

## GPT Image 2.5 Compatibility Update

**OpenAI Adapter 更新到 ChatGPT Images 2.5 能力基线。原有 Scene Master 不需要因为模型升级而推倒重来。**

这是 v2.1 系列的兼容性补丁。Scene Master、Creative Grammar、Model Compiler、Prompt Doctor、Continuity Bible 与 Transcode 架构保持不变。

`MODEL SYNTAX MAY CHANGE. SCENE LOGIC MAY NOT.`

## 官方能力与迁移

[OpenAI 2.5 发布说明](https://openai.com/index/introducing-chatgpt-images-2-5/)更新了细节保真、自然光线与纹理、参考主体保留、编辑精度、多轮一致性和速度；生成延迟相对 Images 2.0 **最多降低 50%（up to 50%）**，不是画质提升 50%。官方资料核对日期：2026-09-09。

按照 [官方迁移指南](https://developers.openai.com/api/docs/guides/image-prompting)，已验证有效的 GPT Image 2 Prompt 优先原样测试 2.5，首轮尽量保持 Prompt、参考图、场景事实、画幅与限制一致。只在发现具体失败变量后局部修复。

## 本次更新

- 普通 GPT Image / ChatGPT 生图请求默认使用 2.5-compatible Adapter；保留 GPT Image 2 legacy compatibility 与原适配器文件路径。
- 强化 `CHANGE ONLY` / `PRESERVE EXACTLY`，明确修改区域、新状态和其余身份、几何、构图、光线与物件的保留边界；多轮优先一次修改一个有意义的变量。
- 明确 identity / wardrobe / object / location / composition / material / light 参考图职责，并尊重用户指定的优先级。
- 仅在 API 场景按任务考虑 [Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)（快速高质量生成）或 [Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)（高精度编辑、较长生成时间）。Skill 不锁定 ChatGPT / Codex 底层模型，也不向普通用户输出 API 配置。
- 同步中英文 README、能力矩阵、编译规则与回归测试。导演库、风格卡、摄影卡与其他模型适配器保持不变。

## Upgrade

从 [v2.1.1 Release](https://github.com/popopo-99/zy-cinematic-realism/releases/tag/v2.1.1) 下载 `zy-cinematic-realism-v2.1.1.zip`，导入或解压其中唯一顶级目录 `zy-cinematic-realism/`。升级时用新目录完整替换旧版，避免同时安装多个同名副本。调用名仍为 `$zy-cinematic-realism`。

## License

继续采用 CC BY-NC 4.0；保留作者、许可证与仓库来源。历史版本与原有致谢保留。

---

## Previous release — v2.1.0

# 造梦师 v2.1.0

## Midjourney V8.2 Adapter Migration

**Midjourney Adapter 正式迁移至 V8.2 能力基线。**

本次发布不是把旧版本参数机械改成 `--v 8.2`，也不是一次简单的版本号替换。v2.1.0 重新核对当前 Midjourney 官方能力，并升级 Model Compiler、Transcode、参考图与编辑工作流，同时继续以 Scene Master 作为唯一事实源。

`MODEL SYNTAX MAY CHANGE. SCENE LOGIC MAY NOT.`

## Midjourney V8.2

当用户只写：

```text
Midjourney
MJ
编译成 Midjourney
```

现在都会默认进入当前 **Midjourney V8.2 Adapter**。除非用户明确指定 legacy target，默认路径不会回退到 V6、V6.1 或 V7。

V8.2 当前已经是 Midjourney 默认模型，因此 Adapter 的版本基线与 Prompt 中是否显式出现 `--v 8.2` 被视为两件事。只有完整 Discord Prompt、显式版本锁定或避免版本漂移时，才需要考虑附加版本参数。

## 更自然的 Prompt Compiler

Midjourney Prompt 不再被理解成旧式 keyword soup，也不会靠 `masterpiece`、`8K`、`ultra detailed` 或 `award-winning` 等质量形容词堆出“电影感”。

Scene Master 会优先保存：

- Story
- Action
- Camera
- Composition
- Light
- Space
- Material
- Aspect Ratio

同时继续保护人物身份、故事时刻、前中后景、视觉中心、观察位置、光源因果、时间、天气、道具与限制。只有这些事实被锁定后，才会压缩为简洁、具体、自然、关系明确的 V8.2 视觉表达。

## Imagine / Edit Model 分流

普通生成与已有图片编辑现在明确分开：

- **Imagine / generation**：用于新画面和不要求确定性保留的视觉探索。
- **V8.2 Edit Model**：用于保留人物或物体、更换背景、局部修改、inpainting、outpainting、透视变化、多参考图组合与视觉重组。

编辑请求不会再被强行改写成普通 `/imagine` Prompt，也不会承诺 prompt-only remix 可以像局部编辑一样确定性保留未修改区域。Omni Reference、Character Reference 和独立 Retexture 不再作为当前 V8.2 默认路径。

## Reference Strategy

v2.1.0 明确区分每类参考图的职责：

- **Image Prompt**：影响内容、构图与颜色关系。
- **Style Reference**：影响风格、质感、色板、媒介与审美语言，不作为人物身份锁。
- **Edit Model Reference**：用于把用户提供的人物、物体或场景带入编辑、组合与重构。
- **Moodboard / Personalization**：提供更广义的用户审美方向，不锁定场景事实、构图或身份。

Skill 不会自动虚构图片 URL、`--sref` code、参考权重、seed、profile 或 style code。

## Smarter Parameters

Raw、Stylize、Seed、Version、Aspect Ratio、Visible Text 与其他 Midjourney 参数全部改为 **need-driven**：

- `--raw` 只在需要更严格的 Prompt 执行、较少自动美化或精确电影控制时考虑，不再是默认电影感后缀。
- Stylize 根据 adherence 与 aesthetic interpretation 的目标决定；没有必要时不输出 `--s`，也不凭空编造数值。
- `--seed` 只用于初始噪声控制、测试和实验，不作为人物身份、风格或连续性锁。
- 可见短文字使用双引号表达，但不承诺复杂字体、长文本或精确排版绝对可靠。
- Aspect Ratio 严格继承 Scene Master；例如 2:3 仍编译为 `--ar 2:3`，不会擅自变成 9:16。
- 参数只出现在文本 Prompt 之后，且只加入当前 V8.2 明确支持并真正服务任务的控制项。

## Transcode

例如：

```text
GPT Image 2 → Midjourney
```

现在必须经过：

```text
Source Prompt → Scene Master → Transcode Lock → Midjourney V8.2 Adapter
```

它不再只是删除 GPT Image 2 的段落标题，再补几个 Midjourney 参数。Character、Scene、Story Beat、Action、Camera、Composition、Light、Props、Time、Weather、Aspect Ratio 与 Restrictions 会先锁定，再重新组织为 V8.2 原生表达，并在输出前检查 semantic drift。

Seedream 或 Nano Banana 转到 Midjourney 时同样从 Scene Master 独立编译，不进行 Prompt-to-Prompt 连环翻译。

## Regression Coverage

新增专门的 Midjourney V8.2 回归测试，覆盖：

- 默认 V8.2 路由与 legacy target 隔离
- GPT Image 2 → Midjourney V8.2 Transcode
- Raw 与非 Raw 决策
- Edit Model 路由
- Style Reference 职责
- 禁止虚构参考数据
- seed 与连续性边界
- Aspect Ratio 与 SD / HD 限制
- Visible Text

## Special Thanks / 特别感谢

README 正式加入长期保留的 Special Thanks / 特别感谢章节，记录参与测试、反馈、分享和支持「造梦师 / DREAM DIRECTOR」成长的朋友。

## Upgrade

下载 `zy-cinematic-realism-v2.1.0.zip`，解压或导入其中唯一的顶级文件夹 `zy-cinematic-realism/`。

如果从旧版本升级，请用新文件夹完整替换原有 `zy-cinematic-realism/`，不要同时安装多个同名副本。显式调用仍然是：

```text
请使用 $zy-cinematic-realism
```

## License

项目继续采用 CC BY-NC 4.0。个人学习与非商业创作可免费使用；分享改编版本时请保留作者、许可证与仓库来源，未经许可不得重新打包售卖或用于商业产品。
