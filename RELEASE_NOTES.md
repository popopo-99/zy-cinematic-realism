# 造梦师 v2.5.0 — 剧本到画面

**DREAM DIRECTOR v2.5.0 — Story to Frame**

**状态：发布候选，尚未发布 GitHub Release。** 当前通过审查分支或本次交付的 v2.5.0 候选 ZIP 安装；实际构建、图片与检查结果见[验证记录](docs/validation-v2.5.md)。

v2.5 从一段可读剧本开始，先理解人物的目标、阻力和变化，再开发视觉世界与关键画面。服装、空间、光线和机位各自服务这个变化，最后接入已有 Scene Master、连续性设定与模型编译。

- **自然语言入口：**“我有一段剧本，先帮我找人物变化，再开发视觉世界和关键画面。”不必先记住模式名。
- **事实与设计分开：**原文明示、剧情解读和新导演建议分别呈现；可读取的片段是分析依据，电影记忆与剧照不作为剧本证据。
- **先建立视觉世界：**为人物、空间、衣饰、材质与光线形成可继续修改的共同设定；已接受的方向进入后续关键帧与局部修复。
- **每帧一个瞬间：**保留原稿动作顺序与地点，选一个可见动作成为关键画面；只有分析需求时先交分析。
- **《泰坦尼克号》实战：**取 James Cameron 署名剧本第 85、87 场三等舱舞会，展示“剧情分析 → 视觉提案 → 参考解梦 → Image2 外部生成 → 检查”。用户评价 P01“效果还不错”，认可它作为后续视觉方向；案例仅展示这张修订图。P02/P03 视觉未通过，已停止图片迭代。配图为原创视觉开发，非电影剧照；来源与新增设计见[案例页](docs/titanic-story-to-frame.md)。
- **同步上手文档：**中英文首页、安装教程与自包含聊天入门版增加剧本入口，基础聊天版仍明确自身范围。

静态检查、文本行为验证和用户图片反馈分别记录。两版文字输出及同一次压缩修订已保存；原计划六图比较未完成，后续参考驱动的外部修订不属于受控 A/B，不据此宣布新版胜出。查看[文字比较](docs/titanic-comparison-v2.5.md)、[本次验证记录](docs/validation-v2.5.md)与[CHANGELOG](CHANGELOG.md)。

**Candidate install:** 从[审查分支](https://github.com/popopo-99/zy-cinematic-realism/tree/codex/story-to-frame/zy-cinematic-realism)安装，或导入本次交付的 `zy-cinematic-realism-v2.5.0.zip`，完整替换旧目录。正式 Release 下载待发布后提供。安装包保留单层 `zy-cinematic-realism/` 结构，调用为 `$zy-cinematic-realism`，许可证为 CC BY-NC 4.0。

**English:** Story to Frame reads character goals, resistance, and change before developing a visual world and individual key frames. Facts, interpretation, and new proposals remain distinct. The Titanic case connects this work with reference decoding and external Image2 generation, displaying only the P01 revision recognized by the user as the direction for later work. P02/P03 failed visual review, and image iteration has stopped. Actual text runs and an additional compression round are preserved. The planned image comparison was not completed; later reference-driven revisions do not establish an A/B winner. This is a release candidate, not a published GitHub Release.

---

## Previous release — v2.4.0

# 造梦师 v2.4.0 — 创作控制与继续使用

**DREAM DIRECTOR v2.4.0 — Creator Control & Continuity**

v2.4 围绕已有方法改善控制与入口：从一句话开始，明确哪些决定可以改，带着已接受的状态继续创作。

- **导演强度真实分流：**轻微选少量兼容特征，明确形成可辨识决定，强烈在未锁定维度中追求结构差异。不指定时默认明确；需要此前的强烈演绎请显式写“强烈 / iconic”。任何强度都不能覆盖用户固定的动作、机位、构图、光源与画幅。
- **四轴服务编译：**四轴仍是专业规划与检查结构，但不再强迫每条 Prompt 带相同标签。模型适配器和用户要求决定最终表达；只要 Prompt 就只给 Prompt。
- **可继续修改：**普通创作按需呈现少量关键画面决定；后续只改指定变量，并保留此前接受的修改。
- **跨对话交接：**按请求整理完整项目交接卡，记录已知状态、视觉规律、参考职责、累计修改、真实图像状态和下一步。新对话重新提供卡片与所需图片，不声称自动记忆。
- **第一次使用提前：**中英文 README 按上手、任务、案例、安装与进阶文档重排。长教程、历史作品、完整致谢和授权内容仍保留。
- **基础聊天版：**没有 Skills 入口时可用自包含入门文本；明确不包含完整导演库或参数适配器。只粘贴主 SKILL.md 不再被描述为完整安装。
- **作品与证据分开：**原作品保留历史标注，新增解梦文本示例标明尚未生成迁移图。PNG 的展示副本采用无损 WebP，原图保留；不宣称页面速度或生图质量已经提升。

这些是实现的行为与文档变化，不是已经证明的新旧版图像质量排名。查看 [验证记录](docs/validation-v2.4.md)、[CHANGELOG](CHANGELOG.md) 与 [手动图像对照协议](zy-cinematic-realism/tests/manual-regression.md)。

**Upgrade:** 下载 `zy-cinematic-realism-v2.4.0.zip`，完整替换旧目录。安装包只有一层顶级 `zy-cinematic-realism/`，包含 Skill、references、assets、tests、LICENSE 与 NOTICE；图库和仓库文档不进入包内。调用仍是 `$zy-cinematic-realism`，许可证仍是 CC BY-NC 4.0。

**English:** Director requests now honor subtle / clear / strong strength, with clear as the unspecified default and locked dimensions excluded from differentiation. Four axes remain internal planning rather than mandatory native-prompt labels. Opt-in handoff preserves cumulative state without invented persistence. Bilingual first-use docs and self-contained basic chat editions are included. Historical images and ungenerated text examples are labeled honestly. Static checks and independent text checks do not establish image-quality or human usability gains.

---

## Previous release — v2.3.0

# 造梦师 v2.3.0 — 解梦

**DREAM DIRECTOR v2.3.0 — Dream Decode**

> 不是复制参考图，而是判断什么值得被带走。

Dream Decode 不只描述参考图里有什么，还识别可迁移的视觉规律，并用新的 Scene Master 编译新画面。

- **Decode the visual logic：**区分来源内容与媒介、色彩、空间、材质和观看关系，提炼完整 5–8 条核心梦律，最终 Prompt 只激活相关的 3–5 条。
- **Preserve new scene intent：**用户明确指定的构图、景别等 `USER-LOCKED` 决策优先；参考图只合理填充或适配 `OPEN` 选择。
- **Reference Medium First：**纸本插画、风格化 3D 或游戏截图不会被默认改成摄影或现代写实渲染；摄影参考继续使用摄影逻辑。
- **Multi-reference roles：**每张图按指定职责贡献颜色、构图、人物或材质；冲突媒介不自动平均，明确要求融合时指定主媒介与次级构造规则。
- **Decode Card reuse：**将主要媒介、完整核心梦律、迁移范围、来源残留、失效警报以及有证据时的表达机制保存为可再次提供的卡片；卡片不是最终 Prompt 或自动数据库。
- **More precise repair：**先分清有效适配与真实漂移，再对媒介、表达机制或其他失效变量做局部修复。
- **Independent Model Compilers：**同一 Scene Master 可分别编译为 GPT Image、Midjourney、Seedream 和 Nano Banana 的原生 Prompt。

技术名称仍为 `zy-cinematic-realism`，显式调用仍为 `$zy-cinematic-realism`。原有 Create、Transcode、Continuity、Director、Style、Prompt Doctor 等工作流保持兼容；v2.3 是 v2.2 Dream Decode 基础的正式进化。许可证仍为 CC BY-NC 4.0。

安装包 `zy-cinematic-realism-v2.3.0.zip` 只包含一个顶级 `zy-cinematic-realism/` Skill 文件夹。解压后完整替换旧版目录，避免同时安装多个同名副本。

---

## v2.2.0 — 解梦基础（开发历史）

## Dream Decode

**造梦师会造梦了，现在也会解梦了。**

以前，造梦师主要从你的文字意图出发，建立 Scene Master，再编译成不同模型能够执行的 Prompt。

v2.2 新增「解梦」。

现在你可以提供一张或多张参考图片，让造梦师分析它们的构图、光线、色彩、材质、空间、镜头、人物关系与图像媒介特征，并进一步判断哪些是真正可以迁移的视觉规律，哪些只是参考图里的具体内容。

它不只是 Image-to-Prompt。

它试图回答：

> 这张图为什么会长成这样？

核心原则：

`TRANSFER VISUAL LOGIC. PRESERVE NEW SCENE INTENT.`

## 三层解梦

- **Scene Facts**：人物、服装、地点、建筑、道具、品牌、文字和事件等参考图的具体事实。仅参考画风时，这些内容不会进入新场景。
- **Visual Grammar**：色彩关系、光线与曝光行为、材质、纹理、媒介、渲染或捕捉特征、细节密度和反俗套规则等可迁移视觉语言。
- **Hybrid Decisions**：构图、机位、人物占比、焦点、遮挡、负空间、空间层次、调度与光线方向等同时服务场景和风格的决策。它们必须结合新 Scene Intent 决定保留、适配或放弃。

完整分析会进一步压缩成 5–8 条可执行的 **Core Visual Rules / 核心梦律**，并通过显式 **Transfer Scope / 迁移范围** 决定哪些规律强继承、哪些按新场景调整、哪些不得迁移。Prompt Compiler 优先使用核心梦律、迁移范围、相关视觉语法和 Scene Master，不会把完整解梦卡全量塞进最终 Prompt。

## Reference Role Router

每张参考图会先获得明确职责。用户指定永远优先，例如：

```text
图一：颜色与曝光
图二：构图与机位
图三：人物身份
图四：材质与纹理
```

Skill 不会把所有图片自动当成 Style Reference，也不会因为上传了图片就覆盖用户明确写出的 Scene Master Facts。

## 单图、多图与迁移

- **Single Decode**：分析一张图为什么呈现当前效果，而不是只列风格标签。
- **Consensus Decode**：从多张 moodboard 中寻找稳定共同规律，同时保留焦段等 Variable Traits。
- **Role-Based Decode**：按每张图的职责分别提取和组合，不做错误交集。
- **Decode Transfer**：用新的 Scene Master 加 Decoded Visual Grammar 重新编译，不在旧 Prompt 上机械替换名词。

同一份 `Scene Master + Decoded Visual Grammar` 仍会分别通过 GPT Image 2.5、Midjourney V8.2、Seedream 5.0 Pro 与 Nano Banana Adapter 独立编译。

## 解梦卡与解梦校正

**Decode Card / 解梦卡**把一次成功解梦命名化、结构化为可再次提供给 Skill 的视觉语法档案。正式 schema 包括一句话视觉定义、5–8 条 Core Visual Rules / 核心梦律、按需展开的 Visual Grammar、显式 Transfer Scope、Allowed Variation、Source Residue 与 Drift Warnings；系列或 Remix 才按需加入单轴复用原则。它不是最终生成 Prompt、永久数据库或对原图全部属性的复制。

当原始参考图与生成结果之间出现差异时，**Decode Repair / 解梦校正**会先区分 `Valid Adaptation` 与 `Actual Drift`。为服从新 Scene Intent 而调整人物占比、构图或机位属于有效适配；只有无正当原因破坏核心梦律、强继承规则或带回默认不继承内容的差异，才会作为最多三个主导漂移接入现有 Prompt Doctor：

```text
Dominant Drift
→ CHANGE ONLY
→ PRESERVE EXACTLY
→ target-native repair prompt
```

构图正确而光线和材质漂移时，只修光线与材质，不重做人物、动作、空间与机位。

## 与 v2 架构的关系

v2.2 没有推倒 v2 架构：

- Scene Master 继续是场景事实的唯一事实源。
- Decoded Visual Grammar 是并列的风格层，不混入场景事实。
- Model Compiler 继续按目标模型独立编译。
- Result Repair 继续执行最小范围修复。
- Continuity Bible 继续负责人物、服装、道具、地点、地理、故事状态与稳定光源；Decode Card 只提供系列共享视觉语言。
- Director、Style Card、Cinematography、Transcode、Prompt Check、One Variable Remix 与 Creative Shuffle 全部保持兼容。

## Regression Coverage

Dream Decode 手动回归扩展至 18 个案例，在原有 style-only、混合构图、多图路由、Decode Repair 与场景污染基础上，补充禁用术语、核心梦律压缩、显式迁移范围、有效适配、来源残留和按核心规则编译检查。

## Upgrade

从 v2.1.x 试用 v2.2 开发快照时，用新的 `zy-cinematic-realism/` 文件夹完整替换旧目录，避免同时安装多个同名副本。调用名仍为 `$zy-cinematic-realism`。v2.2.0 未创建或发布 ZIP、Git tag 或 GitHub Release。

## License

继续采用 CC BY-NC 4.0；技术 skill name、作者、许可证与仓库来源保持不变。

---

## Previous release — v2.1.1

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
