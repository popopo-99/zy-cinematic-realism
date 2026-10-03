**中文** | [English](README_EN.md)

# 造梦师 · DREAM DIRECTOR

**把一个念头，变成可以生成、修改和延续的视觉方案。**

从故事想法、剧本节选或参考图出发，建立场景、开发视觉世界，再输出适合目标模型的 Prompt 和局部修复指令。

**v2.5.0 发布候选** · [当前稳定发布](https://github.com/popopo-99/zy-cinematic-realism/releases/latest) · [60 秒上手](#60-秒上手) · [剧本实战](#剧本实战泰坦尼克号三等舱舞会) · [看案例](#三种方式看见方法) · [安装教程](docs/getting-started.md)

![两个侦探在失败后的夜班公交车上沉默而坐](docs/images/hero-night-bus.webp)

<sub>作者此前的 AIGC 作品：用人物距离、座椅遮挡和实际光源表达一次失败后的沉默。展示方法方向，未重新生成为 v2.4 测试结果。[查看原图](docs/images/hero-night-bus.png)</sub>

这是给 ChatGPT / Codex 使用的视觉创作 Skill。你会得到可复制的 Prompt，必要时加上简短的画面决定、解梦卡或连续组图设定。它负责方案与提示词；实际生图需要你所用环境的生图功能，不因安装而自动调用 API 或锁定底层模型。

技术名称与调用名保持兼容：`zy-cinematic-realism` / `$zy-cinematic-realism`。

<a id="input-card"></a>
<a id="quick-start"></a>
## 60 秒上手

安装完成后，复制这一句开始：

```text
请使用 $zy-cinematic-realism：
雨夜便利店里，一个刚下班的女人
双手握着热咖啡，不看镜头。
给我 Midjourney Prompt。
简短说明时刻、机位与主要光源。
不要广告摆拍和无来源的轮廓光。
```

最少只要告诉它：**谁、在哪里、此刻在做什么、最不想要什么**。有固定景别、光线、画幅或模型时直接写上。

接着自然地修改，不必记住模式名：

```text
人物、动作和光线保留。
只把机位移到雨棚外，隔着玻璃观察。
```

只想复制 Prompt：加上“只给 Prompt”。想深入设计：要求展开 Scene Master（场景母版）、导演四轴或连续性设定。它会沿用对话中已确定的模型；未知且影响编译时才询问一次，也可以说“先给模型中立版本”。

**还没安装？** 看[完整安装教程](docs/getting-started.md)。没有 Skills 入口，可以复制[自包含聊天入门版](docs/chat-starter-zh.md)；基础聊天版不包含完整导演库和模型参数适配器。

<a id="core-workflows"></a>
<a id="continuity"></a>
<a id="prompt-doctor"></a>
<a id="use-cases"></a>
## 从你手上的材料开始

- **剧本**：“我有一段剧本，先帮我找人物变化，再开发视觉世界和关键画面。”<br>→ 剧情解读、视觉开发方向与可生成的单一瞬间

- **想法**：“两个侦探审讯失败后坐夜班公交回警局，给我电影单帧 Prompt。”<br>→ 简短画面决定与目标模型 Prompt

- **参考**：“图一只参考颜色，图二参考构图；内容换成凌晨修表的老人。”<br>→ 参考职责、核心规律与新场景 Prompt

- **修复**：“人物和构图对了，只修灯光太像广告的问题。”<br>→ 最多三个主导问题与局部修复指令

- **组图**：“做八张女骑士下班组图，脸、盔甲、车库和光源保持一致。”<br>→ 连续性设定、镜头列表与每镜变化

- **变化**：“场景不变，转为 Seedream。” / “只换机位。”<br>→ 转码或单变量变体

- **继续**：“整理项目交接卡，记录已经接受的改动和下一步。”<br>→ 可复制到新对话的完整项目状态

参考图只按你指定的职责参与；纸本插画不会默认变成摄影，角色参考也不会自动接管画风。解梦只分析图像时不会强行输出 Prompt。

<a id="story-to-frame"></a>
## 剧本实战：《泰坦尼克号》三等舱舞会

从生涩地跟随，到脱鞋后主动投入，再到桌边被接住后笑起来。先读人物变化，再开发共同的视觉世界，把动作和关系转成关键画面。

[看实战过程与真实结果状态](docs/titanic-story-to-frame.md)：区分原文事实、剧情解读和新导演建议，串起参考解梦、外部生成与检查。案例只展示用户认可作为后续视觉方向的 P01 修订图；P02/P03 视觉未通过，已停止图片迭代。

<a id="showcase"></a>
## 三种方式，看见方法

### ① 从故事里选一个具体瞬间

![深夜公寓里的侦探在桌灯旁继续阅读文件](docs/images/scene-private-aftermath.webp)

桌灯、没喝完的咖啡和门口观察的位置，说明案件还没有结束。动作、空间和光源先成立，镜头与胶片词最后加入。等待和余波是可选方法；你要晴天里的快乐、庆典或动作高潮时，会保留那个方向。

```text
请使用 $zy-cinematic-realism：
一个侦探深夜回家，外套还没脱，坐在台灯旁再次核对案件文件。
摄影机在门口平视，给我模型中立 Prompt，只用实际光源。
```

[查看更多故事瞬间、拳击与历史展示](docs/visual-guide.md)。图片是作者既有作品，调用示例供复用，不承诺重新生成完全相同的图。

<a id="director-method"></a>
<a id="creative-grammar"></a>
### ② 用导演的方法改变观看方式

<table>
  <tr>
    <td width="50%"><img src="docs/images/director-style-comparison/baseline.webp" alt="证据室场景的历史无导演基准" width="100%"><br><strong>无导演基准</strong><br>主要看调查动作</td>
    <td width="50%"><img src="docs/images/director-style-comparison/wong-kar-wai.webp" alt="证据室场景的历史王家卫强烈模式" width="100%"><br><strong>王家卫 · 历史强烈模式</strong><br>反射、遮挡与深夜关系</td>
  </tr>
</table>

v2.4 尊重 **轻微 / 明确 / 强烈**；不指定时默认明确。轻微选择少量兼容特征，强烈也只改变未锁定的决定。你固定的动作、机位、构图和光源不会为了制造差异被重选。

```text
请使用 $zy-cinematic-realism：
年轻警察在停电后的录像厅寻找磁带，轻微参考刁亦男。
中景、人物正在翻找磁带、机位在门口，这些保留。给我 MJ Prompt。
```

[38 位导演索引](zy-cinematic-realism/references/directors/index.md) · [强度与锁定规则](zy-cinematic-realism/references/director-routing.md) · [六组历史完整调用与 Prompt](docs/director-style-comparison.md)

<a id="dream-decode"></a>
### ③ 解梦：带走规律，换掉内容

以封面的夜班公交为参考，可以讨论冷色实际光源与小面积暖色亮点、人物与空间的关系、玻璃反射和选择性可见度；公交、侦探和座椅不必一起搬到新场景。

```text
请使用 $zy-cinematic-realism：
只参考所附夜班公交图的色彩、曝光和材质关系。
新场景是一个老人凌晨在修表铺里合上怀表；胸像中景已锁定。
不要带入公交、侦探或原来的服装。先解梦，再给模型中立 Prompt。
```

[查看参考图、五条核心梦律、完整复用卡与迁移 Prompt](docs/dream-decode-example.md)。**这是基于实际参考图的文本示例，迁移图尚未生成；不作为 v2.4 的图像效果对照。**

在当前对话中可以继续引用刚才的解梦卡；新对话必须重新提供完整卡片。需要身份参考或图像编辑时，还要重新附上可访问的图片。

<a id="install-codex"></a>
<a id="use-chatgpt"></a>
<a id="install"></a>
## 安装与升级

| 环境 | 入口 |
| --- | --- |
| Codex | [从 GitHub 或本地文件夹安装](docs/getting-started.md#install-codex) |
| ChatGPT 有 Skills 入口 | [上传完整候选 ZIP](docs/getting-started.md#use-chatgpt) |
| 没有 Skills 入口 | [自包含聊天入门版](docs/chat-starter-zh.md)，基础能力可直接粘贴 |

v2.5.0 尚未创建正式 Release。当前可从[审查分支](https://github.com/popopo-99/zy-cinematic-realism/tree/codex/story-to-frame/zy-cinematic-realism)安装源码，或导入本次交付的候选包 `zy-cinematic-realism-v2.5.0.zip`；正式发布后提供 Release 下载。

候选包只有一层顶级 `zy-cinematic-realism/` 文件夹。升级时完整替换旧目录，避免同时安装同名副本。**只复制 SKILL.md 无法带上它引用的完整方法库。**

<a id="model-router"></a>
<a id="model-comparison"></a>
<a id="advanced"></a>
## 进阶阅读

`场景母版 + 视觉规律 → 独立模型编译 → 结果修复`

剧本入口先经过 `人物变化 → 视觉世界 → 关键画面`，再接入上述流程。

模型语言可以变，已锁定的场景事实不能偷偷变。

| 想深入哪里 | 文档 |
| --- | --- |
| 从剧本开发视觉世界与关键画面 | [Story to Frame 工作流](zy-cinematic-realism/references/story-visual-development.md) · [《泰坦尼克号》实战](docs/titanic-story-to-frame.md) |
| 故事瞬间、导演与摄影方法 | [视觉指南与历史作品](docs/visual-guide.md) |
| 参考职责、媒介与解梦 | [解梦工作流](zy-cinematic-realism/references/dream-decode.md) · [解梦卡](zy-cinematic-realism/references/decode-card.md) |
| 持续修改与跨对话恢复 | [项目交接卡](zy-cinematic-realism/references/project-handoff.md) |
| 连续组图 | [Continuity Bible](zy-cinematic-realism/references/continuity-cards.md) |
| 局部修复 | [Prompt Doctor](zy-cinematic-realism/references/result-repair.md) |
| 模型编译与选择 | [Model Compiler](zy-cinematic-realism/references/prompt-compiler.md) · [Model Router](zy-cinematic-realism/references/model-routing.md) |
| 四模型历史图片对照 | [同一个 Scene Master 的解释](docs/model-comparison.md) |
| 本次升级与版本历史 | [v2.5 发布说明](RELEASE_NOTES.md) · [CHANGELOG](CHANGELOG.md) |

支持 GPT Image 2.5（保留显式 GPT Image 2 兼容）、Midjourney V8.2、Seedream 5.0 Pro、Nano Banana 及模型中立流程。适配器记录资料核对日期；界面能力变化时核对对应官方说明，不把任务启发式当作永久模型排名。

<a id="repository-structure"></a>
<a id="validation"></a>
## 验证状态

v2.5 围绕剧本事实、人物变化、视觉开发与单帧选择增加行为检查。静态校验、独立文本行为检查、实际图像对照与人类体验评测分别记录。

**个案展示与普遍增益分开判断。** 历史作品不是本次升级的重测结果；手动回归中的 Expected 是预期行为，不是执行记录。新案例的生成、比较与检查状态见验证记录。

[本次验证记录](docs/validation-v2.5.md) · [v2.4 验证历史](docs/validation-v2.4.md) · [完整手动回归与图像对照协议](zy-cinematic-realism/tests/manual-regression.md)

仓库根目录保存教程与作品；`zy-cinematic-realism/` 是可安装 Skill 本体。`scripts/` 提供静态校验与打包脚本，ZIP 不携带作品图库。

<a id="community"></a>
## 一起维护造梦师

感谢参与测试、反馈、分享和支持项目的每一位朋友。[完整 Special Thanks 名单与社区插画](docs/community.md)持续保留。

反馈时附上输入、目标模型、参考图职责、实际结果和最想保留的部分，会更容易定位问题。[提交 Issue](https://github.com/popopo-99/zy-cinematic-realism/issues)

<a id="license"></a>
## 使用与授权

作者：**ZY / popopo-99**。项目采用 [CC BY-NC 4.0](LICENSE)；个人学习与非商业创作、保留署名和来源的改编分享按许可证进行。商业使用或重新打包售卖需按[完整授权说明](docs/licensing.md)联系作者。Skill 生成的具体 Prompt 和作品不自动归项目作者所有。

[署名、限制与商业联系](docs/licensing.md) · [NOTICE](NOTICE.md)

> 先让画面成为故事中的一个具体瞬间，再考虑它使用什么镜头和胶片。
