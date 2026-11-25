<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# 电影与场景方法库

本库供专业入口按导演、摄影指导、影片或画面诉求检索。先明确用户希望迁移的空间关系、人物距离、光线与焦外特征，再选择成像方案。向小白解释时，将方法改写成可见的画面变化。

核验日期为 **2026-11-17**。本版收录 7 部影片、10 张场景方法卡。场景资料均来自已打开核验的制作访谈或器材厂商制作报道，画面观察栏保留独立状态。

## 记录与调用规则

| 字段 | 含义与使用方式 |
| --- | --- |
| 制作记录 | 来源确认该片使用过的摄影机、镜头、介质或后期工艺，适用范围随原文记录 |
| 场景实参 | 来源把具体参数与某一场景或段落明确关联时填写。精确焦段、光圈、对焦距离缺项均填未知 |
| 制作访谈描述 | 摄影师、导演或制作团队解释的现场方法，保留其场景范围 |
| 画面观察 | 根据实际查看的帧、片段作出的描述，需要记录版本与画面定位。本版各卡当前均为待补 |
| 创作选择 | 为用户的新场景重新确定的参数与提示词，明确标为建议，便于与历史实参核对 |

专业用户问“某片同款”，先引用制作记录与场景实参，再给新场景的选择依据。用户给出截图时，可以补充画面观察，并保留镜头型号与焦段的证据状态。用户希望直接出词时，将创作选择编译成普通文本，按请求提供必要的参数说明。

原始焦距须连同画幅、镜头类型和画面裁切理解。历史 f 值与制作报道中的 T 值按来源保留。有关现代器材的特征与使用条件，查阅[器材库](equipment-library.md)。

## 证据类型与事实范围

以下类型分别记录依据的性质，可并列使用。每次断言同时保留来源、作品版本、适用段落及未知项。

| 类型 | 事实范围 |
| --- | --- |
| `manufacturer_spec` | 某产品及版本的厂家规格或明确标注身份的原规格资料，详见器材卡 |
| `film_production_record` | 来源确认某片制作使用过的配置、工艺与制作方法 |
| `sequence_record` | 来源明确关联某段场景的方法或参数 |
| `shot_specific_record` | 来源明确定位某一单镜头的器材或实参，须有单镜头定位依据 |
| `frame_observation` | 已实际查看的画面版本、帧或时间码所支持的可见关系 |
| `creative_proposal` | 为新场景提出的摄影选择与迁移方法 |
| `model_test` | 有模型版本、输入与输出上下文的实际测试记录 |

当前影片卡的制作记录按 `film_production_record` 调用，场景卡的访谈描述及已确认场景实参按 `sequence_record` 调用，创作选择与文本片段按 `creative_proposal` 调用。当前逐镜头实参、直接帧观察和电影案例的模型实测均保持待补状态。器材库里的厂家规格与 Jury 历史反馈保留各自范围。

导演、摄影指导的姓名只标记本片职务。查询某人的“惯用”型号时，需要多部作品的直接制作证据，并说明作品样本。查询具体场景先匹配下方场景定位，缺少的焦距、光圈、机位和距离保持未知。画面观察仅描述可见几何、清晰关系或光线，真实器材身份另需制作依据。

术语检索先经[词典原理与条件](camera-language-dictionary.md)，器材查询经[型号索引](equipment-library.md#型号索引)。作品或人员查询经下方影片表，场景查询经画面诉求表与场景定位。先核对事实边，再从场景卡“迁移条件”和“创作选择”抽取当前任务的方法。术语同时关联某器材和某影片时，逐项核对各边证据；历史器材与现代候选的关系只在来源明确支持的范围内成立。

## 快速索引

### 按影片、导演与摄影指导

| 影片与版本 | 导演 | 摄影指导 | 主要方法 |
| --- | --- | --- | --- |
| [《1917》2019](#film-1917) | Sam Mendes | Roger Deakins | 连续跟随、环境信息与人物距离、隧道压迫感 |
| [《荒野猎人》The Revenant，2015](#film-revenant) | Alejandro G. Iñárritu | Emmanuel Lubezki | 近距离广角、环境与人物共存、行动中的主观体验 |
| [《巴里·林登》Barry Lyndon，1975](#film-barry-lyndon) | Stanley Kubrick | John Alcott | 烛光、极浅景深、演员与光源的精确位置关系 |
| [《宠儿》The Favourite，2018](#film-favourite) | Yorgos Lanthimos | Robbie Ryan | 超广空间、宫廷群像、骑马场景的日光负片处理 |
| [《沙丘》Dune / Dune Part One，2021](#film-dune-2021) | Denis Villeneuve | Greig Fraser | 沙漠尺度、天空色彩、建筑反射光 |
| [《新蝙蝠侠》The Batman，2022](#film-batman-2022) | Matt Reeves | Greig Fraser | 中央叙事区、改造老镜头、车载近距离动作 |
| [《借刀杀人》Collateral，2004](#film-collateral) | Michael Mann | Paul Cameron、Dion Beebe | 城市夜景层次、车内环境光感、人物曝光控制 |

### 按画面诉求

| 用户想要的变化 | 入口 |
| --- | --- |
| 人在环境里，脸上的情绪也能读清 | [荒野猎人营地遇袭](#shot-revenant-camp) |
| 人物穿过狭窄空间，观众跟着紧张 | [1917 德军地下空间](#shot-1917-basement) |
| 保持人物距离，适当减少背景信息 | [1917 河流段落](#shot-1917-river) |
| 真实烛光照亮人物，空间逐渐落入暗部 | [巴里·林登赌局](#shot-barry-candle) |
| 大房间里的权力关系一眼可见 | [宠儿宫廷室内](#shot-favourite-room) |
| 日光环境更柔和，低对比仍保留材料 | [宠儿骑马段落](#shot-favourite-riding) |
| 人显得渺小，热而苍白的天空压住地面 | [沙丘厄拉科斯外景](#shot-dune-desert) |
| 厚重建筑里有柔软且方向明确的天光 | [沙丘光井长廊](#shot-dune-light-wells) |
| 近距离车内动作，保留边缘个性与焦外形状 | [新蝙蝠侠企鹅追车](#shot-batman-chase) |
| 夜里的城市有细节，车内人物受光含蓄 | [借刀杀人出租车](#shot-collateral-cab) |

同一张卡可以帮助多个诉求，检索结果按当前场景的适配度排序。

<a id="film-1917"></a>
## 《1917》2019

- 事实范围为 `film_production_record`，下列导演与摄影指导记录本片职务。器材与工艺按来源限定的全片或段落范围调用，具体场景另查所属场景卡。

- 导演 Sam Mendes，摄影指导 Roger Deakins。
- 制作记录为 ALEXA Mini LF、ARRI Signature Prime 与多种稳定和移动方案。Deakins 在访谈中估计约 99% 使用 40mm Signature Prime，另明确说明河流部分使用 47mm，德军地下空间使用 35mm。上述比例属于摄影师对全片的概括，具体场景按下方记录调用。[ARRI 制作访谈](https://www.arri.com/news-en/the-immersive-camera-movement-of-1917-)
- 数字摄影，当前来源未提供相应场景的拍摄胶片记录。器材详情见 [ALEXA Mini LF](equipment-library.md#cam-mini-lf) 与 [Signature Prime](equipment-library.md#lens-signature-prime)。

<a id="shot-1917-basement"></a>
### 德军地下空间与隧道感

| 项目 | 内容 |
| --- | --- |
| 场景定位 | 士兵进入德军地下空间的段落，按场景检索，时间码随发行版本补充 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 35mm Signature Prime。光圈、人物距离与该段具体机身分配未知 |
| 访谈描述 | Deakins 将该段的 35mm 选择与隧道感联系起来。全片摄影思路强调与持续移动的人物保持陪伴关系 |
| 迁移条件 | 适合有真实前后纵深、墙体距离和行进方向的狭窄场景。先确定机位与人物距离，再选择覆盖所需环境信息的视角 |
| 创作选择 | 新场景可采用低于眼高的近距离广角视角，让近侧墙体与通道终点共同约束人物。35mm 是历史实参，具体画幅与构图由新任务决定 |

普通文本片段可写成“摄影机紧随人物穿过低矮通道，肩背保持近距离，近处墙体从画面两侧掠过，通道纵深与出口方向清楚，人物行动始终是注意中心。”[来源](https://www.arri.com/news-en/the-immersive-camera-movement-of-1917-)

<a id="shot-1917-river"></a>
### 河流段落与背景信息取舍

| 项目 | 内容 |
| --- | --- |
| 场景定位 | 河流中的部分镜头 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 部分镜头使用 47mm Signature Prime。具体镜头编号、光圈与对焦距离未知 |
| 访谈描述 | Deakins 说明此处希望减少背景存在感，因此在全片主要 40mm 的基础上使用 47mm |
| 迁移条件 | 适合环境已经建立、当前需要把注意力交还人物的画面。构图、距离、光圈与背景距离共同决定分离程度 |
| 创作选择 | 新场景保持可辨认的河面与人物处境，将远岸细节逐渐虚化。依据画幅和人物大小重新确定焦距与拍摄距离 |

普通文本片段可写成“人物在河水中艰难前行，摄影机与他保持亲近的观察距离，眼睛与湿透的面部清楚，远岸和水面反光柔和失焦，仍能辨认身处河流。”[来源](https://www.arri.com/news-en/the-immersive-camera-movement-of-1917-)

<a id="film-revenant"></a>
## 《荒野猎人》The Revenant，2015

- 事实范围为 `film_production_record`，下列导演与摄影指导记录本片职务。器材与工艺按来源限定的全片或段落范围调用，具体场景另查所属场景卡。

- 导演 Alejandro G. Iñárritu，摄影指导 Emmanuel Lubezki。
- 制作记录为主要使用 ALEXA XT、ALEXA M 与 Master Prime，选定段落使用 ALEXA 65 与 Prime 65。Lubezki 说明近距离广角有助于同时传达演员情绪和所在环境。不同机身与镜头的场景分配按具体来源确认。[ARRI 制作报道](https://www.arri.com/news-en/alexa-xt-and-alexa-65-on-the-revenant-)
- 数字摄影。ASC 的制作回顾记录自然光与符合时代的火光，以及手持、Steadicam、Technocrane 等跟随方式。相关器材见 [ALEXA 65](equipment-library.md#cam-alexa-65) 与 [Master Prime](equipment-library.md#lens-master-prime)。[ASC 制作回顾](https://theasc.com/article/wrap-shot-the-revenant/)

<a id="shot-revenant-camp"></a>
### 猎人营地遇袭与行动中的视点

| 项目 | 内容 |
| --- | --- |
| 场景定位 | 猎人营地遭袭段落 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 广角与延长的连续行动是来源支持的方法。该段逐镜头机身、精确焦距、光圈和摄影机路线未知 |
| 访谈描述 | 导演解释，希望用延续的视点让观众体验遇袭过程。演员与摄影机的行动按长时间排演和调度协同完成 |
| 迁移条件 | 适合人物持续反应、环境危险与行动因果需要在同一空间里读清的场景。静帧提取决定性瞬间时，保留人物视线、威胁方向及环境线索 |
| 创作选择 | 新画面将机位放到人物附近，使用能同时容纳面部和近处行动环境的广角视角。根据动作密度确定景深，让必要的空间信息可读 |

普通文本片段可写成“摄影机贴近转身的猎人，脸上的惊惧清楚可见，近侧同伴的动作、营地的通路与远处危险方向形成连续的空间关系，自然日光随树冠遮挡变化。”[来源](https://theasc.com/article/wrap-shot-the-revenant/)

<a id="film-barry-lyndon"></a>
## 《巴里·林登》Barry Lyndon，1975

- 事实范围为 `film_production_record`，下列导演与摄影指导记录本片职务。器材与工艺按来源限定的全片或段落范围调用，具体场景另查所属场景卡。

- 导演 Stanley Kubrick，摄影指导 John Alcott。
- 制作记录包含 Arriflex 35BL 与 Kodak 5254。烛光段落使用 Ed DiGiulio 改造的非反光取景 Mitchell BNC 和 Zeiss 50mm f/0.7，另有加装光学附件形成的有效 36.5mm 版本。历史原文的部分访谈写作 t/0.7，器材说明使用 f/0.7，引用时保留其语境。[ASC 原始制作访谈与器材说明](https://theasc.com/article/flashback-barry-lyndon/)
- 导演的整体叙事和空间方法可结合 [Stanley Kubrick 档案](directors/stanley-kubrick.md) 阅读。当前器材库中的现代 Zeiss 系列有各自独立的光学记录。

<a id="shot-barry-candle"></a>
### 赌局中的烛光与精确人物位置

| 项目 | 内容 |
| --- | --- |
| 场景定位 | Barry 与 Lord Ludd 所在、Barry 输掉大笔金钱的赌局室内 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 该场景照明由蜡烛提供，吊灯上方金属反射片兼有回光作用。50mm 用于烛光段落绝大部分中近景，赌局各单镜头的 50mm / 36.5mm 分配未知 |
| 访谈描述 | 极快镜头带来极浅景深，演员位置与对焦距离需要精确协调 |
| 迁移条件 | 适合烛光、油灯等局部弱光推动人物关系的场景。先确定光源位置、面部受光与人物距离，再决定虚化强度 |
| 创作选择 | 新画面可采用稳定机位、克制动作和逐渐衰减的光照。f/0.7 的历史参数与新场景的可读性分别记录 |

普通文本片段可写成“烛台紧邻赌桌，暖光照亮人物靠近光源的一侧面颊，身后的房间渐暗，前后错开的面孔呈自然焦点衰减，手部停在牌面上方，空气与皮肤保持真实。”[来源](https://theasc.com/article/flashback-barry-lyndon/)

<a id="film-favourite"></a>
## 《宠儿》The Favourite，2018

- 事实范围为 `film_production_record`，下列导演与摄影指导记录本片职务。器材与工艺按来源限定的全片或段落范围调用，具体场景另查所属场景卡。

- 导演 Yorgos Lanthimos，摄影指导 Robbie Ryan。
- 制作记录包含 Panaflex Millennium XL2、Arricam ST / LT、Panavision Primo 10–100mm 球面定焦与 6mm SF6 Fisheye T2.8。35mm 负片以 Kodak Vision3 500T 5219 为主，另使用 200T 5213 和 50D 5203。[ASC 制作访谈](https://theasc.com/article/royal-trappings-the-favourite/)
- 胶片特征参考 [5219](equipment-library.md#media-kodak-5219)、[5213](equipment-library.md#media-kodak-5213)、[5203](equipment-library.md#media-kodak-5203)。6mm SF6 属于鱼眼光学，迁移时明确其几何变形和人物边缘位置。

<a id="shot-favourite-room"></a>
### 宫廷室内与可见的权力关系

| 项目 | 内容 |
| --- | --- |
| 场景定位 | Hatfield House 宫廷室内段落，包括可见天花的房间全景。来源同时说明女王房间的绿、金挂毯与软装色调 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 制作范围有 6mm 鱼眼及多枚 Primo。此处单个房间画面的具体焦段、光圈与机位高度未知 |
| 访谈描述 | 高低机位与宽阔视角容纳整间房的行动，摇摄时机引导注意，布景减少杂物并保留场所色彩 |
| 迁移条件 | 适合需要同时理解多个人物地位、距离与所在建筑的群像。使用极宽视角时，人物位置和边缘变形成为创作选择的一部分 |
| 创作选择 | 新场景先安排人物之间的远近、高低与遮挡，再决定普通广角或鱼眼。给面部保真有要求时，在成像方案中明确变形容许范围 |

普通文本片段可写成“低机位望入高挑宫廷房间，天花、地板和人物之间的空地都可见，掌权者占据稳定位置，来访者隔着长距离停在门侧，绿金织物统一室内色彩。”[来源](https://theasc.com/article/royal-trappings-the-favourite/)

<a id="shot-favourite-riding"></a>
### 女王与 Lady Sarah 骑马段落

| 项目 | 内容 |
| --- | --- |
| 场景定位 | 女王与 Lady Sarah 的骑马场景 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | Kodak Vision3 50D 5203，减感冲洗两档。该段具体镜头、焦段与曝光值未知 |
| 访谈描述 | Ryan 说明该处理用于降低这段画面的反差 |
| 迁移条件 | 适合日光下希望高光柔和、明暗关系更温和的场景。光线方向与衣物、马匹、草地的材料区分仍需具体设计 |
| 创作选择 | 生图提示词直接描述温和反差、浅色区域的渐变和自然材料层次。历史减感工艺作为可选的专业说明 |

普通文本片段可写成“日光中的两名骑马人物置于可辨认的草地环境，皮肤与浅色衣料高光柔和，马匹轮廓和草地层次清楚，明暗过渡温和，色彩保留自然差异。”[来源](https://theasc.com/article/royal-trappings-the-favourite/)

<a id="film-dune-2021"></a>
## 《沙丘》Dune / Dune Part One，2021

- 事实范围为 `film_production_record`，下列导演与摄影指导记录本片职务。器材与工艺按来源限定的全片或段落范围调用，具体场景另查所属场景卡。

- 导演 Denis Villeneuve，摄影指导 Greig Fraser。
- 制作记录为 ALEXA LF，1.43 展映段落使用 Panavision H Series 球面镜头，固定宽银幕段落使用定制调整的 Ultra Vista 1.65× 变形镜头。具体镜头需与展映版本、画面比例和段落关联。[ASC 制作访谈](https://theasc.com/article/dune-fear-is-the-mind-killer/)
- 摄影机详情见 [ALEXA LF](equipment-library.md#cam-alexa-lf)。本片采用数字摄影与胶片中间处理，采集介质和后期胶片工艺各有独立记录。后期流程由摄影与调色团队专访确认。[ASC 后期制作专访](https://theasc.com/article/dune-hybrid-finishing-digital-to-film-and-back/)

<a id="shot-dune-desert"></a>
### 厄拉科斯沙漠外景与炎热天空

| 项目 | 内容 |
| --- | --- |
| 场景定位 | 厄拉科斯日间外景段落，来源覆盖约旦实景和天空处理策略 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 相应外景使用大画幅数字摄影。各单镜头的球面 / 变形分配、焦段、光圈与人物比例未知 |
| 访谈描述 | 天空的低蓝色饱和度与炽热苍白感，由前期 LUT、现场曝光与最终调色共同形成 |
| 迁移条件 | 适合环境尺度和气候压力推动叙事的荒漠。人物大小、地形层次与天空占比按任务明确 |
| 创作选择 | 新画面可将人物缩小到环境尺度中，让天空和沙地保持亮度层次，肤色与服装保留细微色差 |

普通文本片段可写成“人物置于层层沙脊之间，身形相对环境显得渺小，天空明亮苍白、蓝色含量很低，沙地保留细微暖色差异，热而干燥的日光让遮蔽处更显重要。”[来源](https://theasc.com/article/dune-fear-is-the-mind-killer/)

<a id="shot-dune-light-wells"></a>
### 厄拉科斯官邸的光井长廊

| 项目 | 内容 |
| --- | --- |
| 场景定位 | 厄拉科斯官邸约 150 英尺长廊，一侧排列光井 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 宽景使用 Chroma-Q Studio Force II 模拟反射日光，人物近景更换 Digital Sputnik DS。具体焦段与光圈未知 |
| 访谈描述 | 光井将日光反射入厚重建筑，需要兼有环境柔和度、明确方向和墙面亮带 |
| 迁移条件 | 适合建筑本身决定光源路径的宫殿、堡垒、地下空间。先画清外部光线进入与反射的位置 |
| 创作选择 | 新场景可用沿走廊重复的侧向反射光建立空间节奏，让人物在亮暗交替的区域行动 |

普通文本片段可写成“厚石墙长廊沿一侧设置深光井，外部强日光经石面反射后进入，人物面部受光柔和且方向明确，对面墙上出现有节奏的亮带，前后空间依次落入暗部。”[来源](https://theasc.com/article/dune-fear-is-the-mind-killer/)

<a id="film-batman-2022"></a>
## 《新蝙蝠侠》The Batman，2022

- 事实范围为 `film_production_record`，下列导演与摄影指导记录本片职务。器材与工艺按来源限定的全片或段落范围调用，具体场景另查所属场景卡。

- 导演 Matt Reeves，摄影指导 Greig Fraser。
- 制作记录包含 ALEXA LF、ALEXA Classic，主要镜头为专门调整的 ARRI Rental Alfa Series 2。追车段落另采用改装的 Helios / Jupiter 静态摄影镜头与 Atlas Orion。Alfa Series 2 的边缘像差与中央构图区共同参与了影片设计。[ASC 摄影指导访谈](https://theasc.com/article/greig-fraser-batman/)
- 数字采集，后期有 Kodak Vision3 2254 胶片中间处理。关联卡见 [ALEXA LF](equipment-library.md#cam-alexa-lf)、[Atlas Orion](equipment-library.md#lens-atlas-orion) 与 [Helios 44-2](equipment-library.md#lens-helios-44-2)。本片改装镜头的椭圆光阑、电影化机械结构及具体镜片版本，作为独立制作版本记录。

<a id="shot-batman-chase"></a>
### 蝙蝠侠与企鹅的追车段落

| 项目 | 内容 |
| --- | --- |
| 场景定位 | 蝙蝠侠与 Penguin 的追车高潮段落 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 轻便车载与碰撞机位使用 ALEXA Classic，Iron Glass 改装 Helios / Jupiter 配有椭圆光阑，另有 Atlas Orion。各单镜头型号、焦段、光圈与距离未知 |
| 访谈描述 | 车载机位将摄影机与车内人物关系锁定，器材体积和边缘成像能力支持更偏离中央的构图 |
| 迁移条件 | 适合车内空间、人物动作与外界速度感相互作用的画面。先明确脸部清晰区、窗外焦外形状和边缘容许变化 |
| 创作选择 | 新静帧可用近距离车载视点，保留人物眼神与受力姿态，让窗外高光在焦外呈椭圆形。老镜头名称须伴随实际需要的画面行为 |

普通文本片段可写成“近距离车载视点锁住驾驶者的眼神和握紧方向盘的手，车窗外的灯点在焦外呈轻微椭圆形，画面边缘有克制的成像衰减，人物受力方向与车内结构清楚。”[来源](https://theasc.com/article/greig-fraser-batman/)

<a id="film-collateral"></a>
## 《借刀杀人》Collateral，2004

- 事实范围为 `film_production_record`，下列导演与摄影指导记录本片职务。器材与工艺按来源限定的全片或段落范围调用，具体场景另查所属场景卡。

- 导演 Michael Mann，摄影指导 Paul Cameron 与 Dion Beebe，二人在不同制作阶段参与。
- 制作记录为混合 HD 与 35mm。数字部分使用 Sony / Panavision HDW-F900、Thomson Viper 与 Zeiss DigiPrime，胶片部分包含 Panaflex / Pan-Arri 机身、Primo 及 Kodak 5279 / 5218。片中器材随制作阶段和拍摄任务切换。[ASC 制作访谈](https://theasc.com/article/hell-on-wheels-collateral/)
- 本条使用历史制作设备名称。城市夜景的材料层次、人物曝光与画面噪声，随当时的采集和后期流程理解。

<a id="shot-collateral-cab"></a>
### 出租车夜间对话与城市环境

| 项目 | 内容 |
| --- | --- |
| 场景定位 | Max 与 Vincent 的夜间出租车内段落 |
| 证据状态 | `sequence_record` 对应下列场景实参与访谈描述；`creative_proposal` 对应迁移条件与创作选择。`shot_specific_record`、`frame_observation`、`model_test` 待补 |
| 场景实参 | 车内照明设计包含定制 ELD 薄面板，后续加入 Mini Flo。部分阶段使用 F900，后续主要数字机位改用 Viper。具体镜头焦段未知 |
| 访谈描述 | 目标是环境光感，车内人物曝光为控制噪声作专门安排，最终调色再恢复所需亮度关系。真实车窗与眼镜反射参与了现场调整 |
| 迁移条件 | 适合人物受光需要含蓄、窗外夜城又承担叙事信息的场景。先确定车内亮度、车窗反射与外部灯光的关系 |
| 创作选择 | 新画面保留微亮的夜空和城市远景层次，让人物面部被低强度、宽面积的车内光照亮，眼镜与窗玻璃反射按机位控制 |

普通文本片段可写成“夜间出租车内的两个人物安静交谈，面部有低强度宽面积受光，车窗外的街灯、建筑与微亮夜空仍可辨认，玻璃反射有层次，眼神和肤色保持可读。”[来源](https://theasc.com/article/hell-on-wheels-collateral/)

## 维护与扩展

新增影片至少补齐一个有来源定位的场景卡，再加入索引。更新时记录影片版本、文字来源、访问日期、场景范围、已知参数与未知参数。来源出现分歧时并列保留原说法与适用版本。

用户提供实际截图或片段后，补充画面观察，记录可见的人物距离、空间比例、光源方向、景深、焦外与材料特征。需要查找精确焦段时，继续寻找拍摄日志、摄影指导逐镜头说明或可靠的制作记录。

## 署名与贡献说明

© ZY。随造梦师项目采用 CC-BY-NC-4.0，具体条款见项目许可证。

Jury 提供的资料中关于器材视觉签名、成像方案和影片器材核验的思路，为本模块设计提供了启发。本库的影片选择、场景方法卡、来源核验与创作迁移说明由本次升级重新整理。电影、摄影作品、器材名称及链接资料的权利归各自权利人所有。
