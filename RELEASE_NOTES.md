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
