**中文** | [English](README_EN.md)

# 造梦师

## AI时代电影视觉指南 · v2.0.0

**DREAM DIRECTOR v2.0 — Model Compiler Edition**

> 先建立一个稳定的视觉方案，再把它翻译成不同模型最容易理解的语言。

![两个侦探在失败后的夜班公交车上沉默而坐](docs/images/hero-night-bus.png)

<p align="center">
  <strong>从一条 Prompt，到完整视觉方案。</strong>
</p>

<p align="center">
  <strong>One Scene Master. Different models. Native prompts.</strong>
</p>

造梦师不是新的生图模型，也不是一包“万能电影词”。它是一套给 ChatGPT / Codex 使用的电影视觉工作流：先锁定人物、故事瞬间、动作、场景、机位、构图、光线、道具、时间、天气与限制，再为目标模型编译原生 Prompt。

`Scene Master → Creative Grammar → Model Compiler → Result Repair`

对外品牌是 **造梦师 / DREAM DIRECTOR**；为保持安装路径、自动触发和显式调用兼容，技术名称始终是 `zy-cinematic-realism`，调用名始终是 `$zy-cinematic-realism`。

**[下载最新 Release](https://github.com/popopo-99/zy-cinematic-realism/releases/latest)**

## v2.0.0：从 Final Prompt 到 Model Compiler

旧工作流是：

`Idea → Skill → Final Prompt`

v2.0.0 变成：

`Idea → Scene Master → Creative Grammar → Model Compiler → GPT Image 2 / Midjourney / Seedream 5.0 Pro / Nano Banana`

`Scene Master` 是唯一事实源。它先锁定画面设计，再由 `Creative Grammar` 决定风格、摄影与调度，最后交给不同 `Model Compiler` 翻译。转码时可以改变句法、信息密度、参数位置和编辑措辞，但不能偷偷改变人物、动作、地点、光线或叙事关系。

```text
MODEL SYNTAX MAY CHANGE.
SCENE LOGIC MAY NOT.
```

**模型语言可以改变，画面设计不能偷偷改变。**

## 十个核心功能

- **Create** — 从一句想法建立 Scene Master，并编译为目标模型的原生 Prompt。例：`雨夜便利店里，一个女人握着热咖啡，不看镜头。`
- **Model Router** — 根据任务类型推荐更合适的适配路径。例：`我要先生成角色定妆，再连续修改道具，用哪个模型流程？`
- **Model Compiler** — 把同一个视觉方案翻译成某个模型更容易执行的表达。例：`把 Scene Master 编译为 Midjourney。`
- **Transcode** — 在保持场景事实不变的前提下换模型语言。例：`把这条 GPT Image 2 Prompt 转成 Seedream 5.0 Pro。`
- **Multi-model Pack** — 一次输出多种模型的原生版本。例：`同一场景同时给我四模型版本。`
- **Continuity Bible** — 锁定跨镜头人物、服装、道具、地点与光线。例：`做 8 镜下班女骑士连续组图。`
- **Prompt Check** — 生成前检查冲突、空泛和物理不成立的描述。例：`检查这条 Prompt 为什么可能做成海报。`
- **Prompt Doctor** — 根据失败结果只修真正出问题的变量。例：`人物太像商业广告，只修机位、姿态和光线层级。`
- **One Variable Remix** — 锁住全部核心事实，只改变一个变量。例：`只把观察位置从正面改到门外。`
- **Creative Shuffle** — 在可控边界内重新组合风格、摄影与调度。例：`给我三个克制、可落地的创意方向。`

## 同一个 Scene Master，四种模型会发生什么？

下面四张结果使用同一套核心视觉约束：黑马、银色盔甲人物、海岸、海浪与冷色写实环境。区别只在模型适配器与模型自身的解释方式；它们不是同一张图，也不承诺像素级一致。

<table>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/v2/model-compiler-gpt-image-2.webp" alt="GPT Image 2 对黑马、银色盔甲人物与海岸 Scene Master 的解释" width="100%">
      <br><strong>GPT Image 2</strong>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/v2/model-compiler-midjourney.webp" alt="Midjourney 对黑马、银色盔甲人物与海岸 Scene Master 的解释" width="100%">
      <br><strong>Midjourney</strong>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/v2/model-compiler-seedream-5-pro.webp" alt="Seedream 5.0 Pro 对黑马、银色盔甲人物与海岸 Scene Master 的解释" width="100%">
      <br><strong>Seedream 5.0 Pro</strong>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/v2/model-compiler-nano-banana.webp" alt="Nano Banana 对黑马、银色盔甲人物与海岸 Scene Master 的解释" width="100%">
      <br><strong>Nano Banana</strong>
    </td>
  </tr>
</table>

```text
Same Scene Master.
Different native prompts.
Different model interpretations.
```

## Model Router 与四个原生适配器

| 目标模型 | 编译重点 |
|---|---|
| GPT Image 2 | 结构清晰的自然语言视觉说明与编辑说明 |
| Midjourney | 高密度视觉语言与模型原生参数位置 |
| Seedream 5.0 Pro | 明确的空间、主体关系与视觉 brief |
| Nano Banana | 直接、适合多轮编辑的任务措辞 |

Router 是任务启发式工具，不是永久排名，也不宣称某个模型“最好”。模型能力和界面会变化；场景逻辑仍由 Scene Master 负责。

## 60 秒上手

### 1. 一句话创建并选择模型

```text
请使用 $zy-cinematic-realism：
雨夜便利店里，一个刚下班的女人双手握着热咖啡，不看镜头。
先告诉我适合的模型路径，再为 Midjourney 编译原生 Prompt。
不要广告摆拍、直视镜头和没有来源的轮廓光。
```

Skill 会先整理 Scene Master，再输出 Midjourney 原生表达。你不需要提前懂摄影参数，最少只要提供：

```text
谁 + 在哪里 + 刚刚发生了什么 + 此刻的小动作 + 最不想要什么
```

### 2. 转码、多模型、修复与 Remix

```text
Transcode：保持女人、便利店、雨夜、热咖啡和不看镜头不变，转成 GPT Image 2。

Multi-model Pack：同一个 Scene Master，同时输出四个模型的原生版本。

Prompt Doctor：结果太像咖啡广告。只修机位、人物姿态和光线层级，不改身份、服装、咖啡与地点。

One Variable Remix：只把摄影机从店内正面改到雨棚外隔着玻璃观察，其余完全锁定。
```

## 连续性：Base Lock + Shot Delta

例如要做 8 镜“都市女骑士下班”组图，先用 `Continuity Bible` 锁定角色脸、银色通勤盔甲、旧帆布包、折叠长枪、车站与冷暖光源。每一镜都由同一份 `Base Lock` 加一条有限的 `Shot Delta` 生成：只描述该镜新增的动作、机位或时间变化。

这能减少脸、服装、道具、地点和光线在镜头之间漂移；它不承诺模型输出完全相同，而是让变化有据可查。

## Prompt Doctor：修图，不推倒重写

如果结果太像商业广告，问题通常不在“电影感词”太少，而在摄影机太正、人物摆拍、主辅光没有层级。Prompt Doctor 会先诊断，再输出局部修复指令：

```text
CHANGE ONLY: camera position, posing, and light hierarchy.
PRESERVE EXACTLY: identity, wardrobe, car, and location.
```

修复不是重新创作。角色身份、服装、汽车和地点继续来自原 Scene Master，只有被点名的变量允许改变。

## Creative Grammar：不是滤镜，而是可执行决策

v2.0.0 保留 38 位导演的四轴视觉指纹，并新增 16 张风格卡与 8 张摄影卡。它们会实际改变光线、曝光、摄影机、空间、调度与视觉中心，而不是只附加一个风格标签。

- 风格卡可选择冷峻写实、潮湿黑色电影、静默日常、制度压迫等受控方向。
- 摄影卡可选择门框外观察、近距离被遮挡、远景负空间、程序性固定机位等观看方式。
- 导演参考继续作用于光影反差、色彩曝光、镜头机位与构图空间，不复制任何具体电影画面。

摄影参数最后才加入。它们负责强化一个已经成立的故事瞬间，不负责替代故事。

## 从一条故事里，选择不同的“那一刻”

Skill 不只是在同一个构图上换滤镜。它会帮你判断，故事里哪个瞬间最值得被看见。

### 审讯正在失控

![从单向玻璃外观察一场正在失控的审讯](docs/images/scene-interrogation.png)

摄影机没有坐在谈判桌旁，而是在单向玻璃外。玻璃反射、监听设备和大块暗部让观众更像一个不该在场的观察者。

### 回家以后，案件还没有结束

![侦探在深夜的公寓里独自阅读文件](docs/images/scene-private-aftermath.png)

人物不需要哭喊。桌上的信、没喝完的咖啡、门框遮挡和一盏台灯，就能说明“他仍然放不下”。

### 真相揭开后的沉默

![两名侦探站在河边的巨大负空间里](docs/images/scene-river-silence.png)

人物缩小、远离中心，城市与河面占据大部分画面。环境不再只是背景，而是在替角色说话。

### 主角离开，城市继续

![清晨城市街道上一辆逐渐驶远的警车](docs/images/scene-city-finale.png)

结尾不一定需要主角特写。隔着有划痕的玻璃看警车驶远，普通人开始新的一天，故事已经结束，但城市没有停下。

## 换个题材，方法仍然成立

![隔着拳台围绳捕捉拳手被击中的瞬间](docs/images/scene-boxer-corner.png)

动作场面也不需要干净、完整的英雄构图。前景拳绳与对手身体遮挡视线，轻微运动模糊保留击打速度，人物甚至没有处在完美对焦中——它更像摄影机在搏斗中抢到的一帧，而不是体育广告。

犯罪片可以用，拳击片、家庭剧情、科幻、古装或城市短片也可以用。核心始终是：

> **不要只说“两名拳手激烈搏斗”。要说清楚这是第几回合、重拳命中的前后哪一秒、摄影机隔着什么看见他们，以及动作模糊应该保留多少。**

## 用导演的方法重新观察同一个故事

### 导演四轴视觉指纹系统

导演库不再只是“导演名字 + 代表作品”，也不会把综合风格句追加在 Prompt 末尾。指定已支持导演时，Final Prompt 会在场景事实之后、详细摄影机设计之前，连续生成：

1. `Lighting and contrast signature`
2. `Color and exposure signature`
3. `Lens and camera signature`
4. `Composition and spatial signature`

四行都必须是当前场景的具体决定。相对无导演基准，至少三轴必须发生结构性变化，并且要重新选择时刻、视觉中心、摄影机位置、人物尺度、环境/人物/物件主导权中的至少三项。删掉导演姓名和片名后，四轴仍应明显可辨。

同一个故事因而会真正改变光影、色调、机位和构图，同时保留用户给定的年代、地点、人物、事件、真实空间和动机光。代表作品只提供模型识别锚点，系统不会复制其中任何具体场景。

| 地区 | 精选导演 | 最明显的四轴方向 |
|---|---|---|
| 华语电影 | 张艺谋、贾樟柯、王家卫、侯孝贤、杨德昌、刁亦男 | 从仪式性色彩秩序到社会转型、主观城市与层叠日常 |
| 日本电影 | 黑泽明、小津安二郎、岩井俊二、是枝裕和、黑泽清 | 从天气驱动的行动轴到家庭空间、季节记忆与不可见威胁 |
| 韩国及东南亚 | 奉俊昊、朴赞郁、李沧东、阿彼察邦 | 从阶级空间和物件欲望到道德观察与热带时间 |
| 欧洲作者电影 | 塔可夫斯基、库布里克、希区柯克、伯格曼 | 从元素记忆和制度几何到视线悬念与面孔关系 |
| 美国类型与作者 | 芬奇、林奇、斯科塞斯、科波拉、迈克尔·曼 | 从程序信息和心理异常到街头系统、家族权力与夜间职业网络 |
| 当代国际电影 | 诺兰、维伦纽瓦、马力克、卡隆、赵婷 | 从物理机制和环境尺度到身体触觉、连续社会空间与工作景观 |

[查看 38 位导演完整索引、别名和四轴摘要](zy-cinematic-realism/references/directors/index.md) · [查看按场景目标选择导演的推荐矩阵](zy-cinematic-realism/references/directors/recommendation-matrix.md)

```text
请使用 $zy-cinematic-realism：

1990 年代末，南方小城，一名年轻警察在停电后的录像厅里寻找失踪者留下的磁带。

导演参考：刁亦男
风格强度：强烈

请让该导演的光影反差、色彩曝光、镜头距离和空间构图分别形成明确、不可互换的视觉指令。
不要复制任何具体电影场景。
```

> 指定已支持导演时，`轻微 / 明确 / 强烈 / subtle / clear / strong / iconic` 都统一按“强烈”执行。

### 同场景四导演的根本差异

仍以“停电后的录像厅里寻找磁带”为固定故事事实：

| 导演 | 光影 | 色调与曝光 | 镜头 | 构图与空间 |
|---|---|---|---|---|
| 刁亦男 | 绿色应急灯与红色出口灯形成孤立硬光池 | 肤色疲惫、黑位密集、实际光源突兀剪切 | 稍迟一步的中广景旁观，追随动作之后才摇移 | 警察被离场人群和座椅切碎，危险藏在公共秩序里 |
| 大卫·芬奇 | 为磁带、手、登记表保留可读性的低照度 | 中性偏冷、纸白受控、次要区域进入精确暗部 | 门口的精确中景，极少移动，焦点连接信息节点 | 磁带—记录—手势形成可追溯证据链 |
| 王家卫 | 荧光灯、出口灯与雨夜门外光彼此污染 | 混合偏色、局部欠曝、实际亮源允许轻微漂移 | 隔着玻璃或座椅的压缩/轻微畸变近距观察 | 反射与遮挡把寻找变成一次错过的私人遭遇 |
| 杨德昌 | 录像厅、走廊与街道各保留普通实用光 | 真实荧光与城市材料色，不用情绪滤镜 | 邻厅或售票口的清晰中远景，保持上下文 | 建筑分隔警察、店员与离场顾客，社会关系比磁带更大 |

## 同一个故事，不同导演会看见什么？

这组压力测试固定同一个故事、人物、年代、地点和证据线索，只改变导演参考。v2.0.0 继续保留这些结构性差异，并把每个导演方向强制拆成光影反差、色彩曝光、镜头机位、构图空间四条连续签名，减少模型把差异压缩回一个综合风格句的风险。

这里的差异不是给同一张图更换滤镜，而是让不同导演重新决定“这一镜到底在看什么”。

固定场景：1980 年代中期，纽约曼哈顿，深夜警局证据室；一名疲惫侦探用城市车库员工卡比对墙上的黑白监控投影。

<table>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/baseline.webp" alt="无导演基准：1980年代纽约警局证据室" width="100%">
      <br>
      <strong>无导演基准</strong>
      <br>
      <sub>真实调查动作、合理机位与实用光源</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/wong-kar-wai.webp" alt="王家卫强烈模式：1980年代纽约警局证据室" width="100%">
      <br>
      <strong>王家卫</strong>
      <br>
      <sub>主观时间、遮挡反射与未完成的深夜关系</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/stanley-kubrick.webp" alt="斯坦利·库布里克强烈模式：1980年代纽约警局证据室" width="100%">
      <br>
      <strong>斯坦利·库布里克</strong>
      <br>
      <sub>制度几何、冷静距离与秩序中的不安</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/denis-villeneuve.webp" alt="丹尼斯·维伦纽瓦强烈模式：1980年代纽约警局证据室" width="100%">
      <br>
      <strong>丹尼斯·维伦纽瓦</strong>
      <br>
      <sub>空间压迫、负空间与环境中的渺小人物</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/david-fincher.webp" alt="大卫·芬奇强烈模式：1980年代纽约警局证据室" width="100%">
      <br>
      <strong>大卫·芬奇</strong>
      <br>
      <sub>程序信息、精确机位与受控的证据层级</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/images/director-style-comparison/terrence-malick.webp" alt="泰伦斯·马力克强烈模式：1980年代纽约警局证据室" width="100%">
      <br>
      <strong>泰伦斯·马力克</strong>
      <br>
      <sub>身体停顿、触觉干扰与不完整的投影时刻</sub>
    </td>
  </tr>
</table>

| 版本 | 镜头主要在看什么 |
|---|---|
| 无导演基准 | 侦探如何完成员工卡与监控投影的比对 |
| 王家卫 | 深夜孤独、反射、遮挡与不完整的心理关系 |
| 斯坦利·库布里克 | 个人如何被制度空间和几何秩序控制 |
| 丹尼斯·维伦纽瓦 | 渺小侦探如何面对比自己更沉重的证据系统 |
| 大卫·芬奇 | 卡片、投影、照片和文字如何组成严密的信息链 |
| 泰伦斯·马力克 | 疲惫身体、纸边、袖口与投影光如何打断程序动作 |

> 所有版本都保留相同故事事实。差异来自导演对具体时刻、视觉中心、机位、调度、光线、景深和质感的重新选择。

[查看六组完整调用文本、Final Prompt 与 Avoid](docs/director-style-comparison.md)

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

## 安装到 Codex

OpenAI 当前文档说明，Codex 会从用户级 `$HOME/.agents/skills` 与项目级 `.agents/skills` 目录发现 Skill；也可以让内置的 `$skill-installer` 从其他 GitHub 仓库安装。详见 [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills)。

### 方法一：让 Codex 从 GitHub 安装

在 Codex 中输入：

```text
请使用 $skill-installer，从下面的 GitHub 仓库安装 zy-cinematic-realism：
https://github.com/popopo-99/zy-cinematic-realism
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

## 在 ChatGPT 中使用

### 有 Skills 安装入口

根据 OpenAI 当前说明，Personal Skills 通常面向 ChatGPT Business、Enterprise、Healthcare 和 Edu 用户，实际可用性还会受到工作区设置和权限影响。不要假设所有 ChatGPT 账户都已经开放此功能。详见 [OpenAI：Skills in ChatGPT](https://help.openai.com/en/articles/20001066)。

如果你的账户或工作区已经开放 Skills：

1. 在侧边栏打开 **Plugins / 插件**。
2. 在 Plugin Directory 中进入 **Skills**。
3. 选择 **Create**，再选择 **Upload from your computer**。
4. 上传最新 Release 中的 `zy-cinematic-realism-v2.0.0.zip`。
5. 扫描和安装完成后，输入 `$zy-cinematic-realism`，或直接描述电影感 Prompt 任务。

Personal Skills 需要分别添加到桌面端和 Web / 移动端，目前不会自动跨这些界面同步。

### 没有 Skills 入口

仍然可以直接使用：

1. 打开 [`zy-cinematic-realism/SKILL.md`](zy-cinematic-realism/SKILL.md)。
2. 将文件内容复制到新的 AI 对话。
3. 在后面附上自己的画面想法。
4. 要求 AI 按照该工作流输出 `Final Prompt` 和 `Avoid`。

这种方式不需要 Codex，也不需要安装插件，只是每次可能需要重新提供规则。

## 仓库与安装包结构

仓库根目录是品牌说明、教程、授权与发布记录；`zy-cinematic-realism/` 才是可安装的 Skill 本体。

```text
zy-cinematic-realism/                 # GitHub 仓库根目录
├── README.md                          # 当前教程与展示页
├── README_EN.md                       # English guide and showcase
├── CHANGELOG.md                       # 版本记录
├── LICENSE                            # CC BY-NC 4.0
├── RELEASE_NOTES.md                   # v2.0.0 发布说明
├── docs/
│   └── images/                        # 作品示例图
├── scripts/
│   └── validate_director_library.py   # 导演库与 Markdown 链接校验
└── zy-cinematic-realism/              # 可安装 Skill 本体
    ├── SKILL.md
    ├── LICENSE
    ├── NOTICE.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   └── basic-prompt-template.md
    ├── references/
        ├── camera-and-light.md
        ├── cinematic-principles.md
        ├── model-routing.md
        ├── model-capability-matrix.md
        ├── prompt-compiler.md
        ├── prompt-check.md
        ├── result-repair.md
        ├── continuity-cards.md
        ├── style-cards.md
        ├── cinematography-cards.md
        ├── examples.md
        ├── director-routing.md
        ├── directors/
        │   ├── index.md
        │   └── recommendation-matrix.md
        ├── negative-prompts.md
        ├── models/
        │   ├── gpt-image-2.md
        │   ├── midjourney.md
        │   ├── seedream-5-pro.md
        │   └── nano-banana.md
        └── quality-checklist.md
    └── tests/
        └── manual-regression.md
```

v2.0.0 Release 安装包只有一层顶级 Skill 文件夹：

```text
zy-cinematic-realism-v2.0.0.zip
└── zy-cinematic-realism/
    ├── SKILL.md
    ├── LICENSE
    ├── NOTICE.md
    ├── agents/
    ├── assets/
    ├── references/
    └── tests/
```

## Copyright and License

The Skill source files include copyright notices.
The distributable Skill package contains its own license file.

Copyright:
ZY / popopo-99

License:
CC BY-NC 4.0

## 使用与授权

《造梦师：AI时代电影视觉指南 v2.0.0》采用 [Creative Commons Attribution-NonCommercial 4.0 International](LICENSE)（CC BY-NC 4.0）授权。

你可以：

- 用于个人学习和非商业创作
- 根据自己的项目修改工作流
- 在保留署名、许可证和来源的情况下分享改编版本

你不可以：

- 将本 Skill 或轻微修改版本重新打包售卖
- 删除作者与来源信息后冒充原创发布
- 未经授权放入付费课程、会员资源、提示词合集或商业产品

转载请注明：

```text
作者：ZY / popopo-99
项目：造梦师：AI时代电影视觉指南
仓库：https://github.com/popopo-99/zy-cinematic-realism
许可证：CC BY-NC 4.0
```

商业合作或授权请联系：

- 抖音：2053586074
- 邮箱：zhang.yanpo@foxmail.com

Skill 生成的具体 Prompt 和用户据此创作的作品，不自动归项目作者所有；用户仍需遵守其所使用 AI 平台的规则和适用法律。

## 最后只记住一句话

> **先让画面成为故事中的一个真实瞬间，再考虑它使用什么镜头和胶片。祝你玩得开心。**

示例图由作者使用 AIGC 创作，用于展示这套工作流追求的叙事与摄影方向。
