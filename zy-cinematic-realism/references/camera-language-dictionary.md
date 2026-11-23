<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# 摄影语言词典

## 使用约定

本词典是按需读取的概念参考。先用下表找到术语，再读取相关卡片。术语解析产生的观看目标、景别、机位、运动和清晰关系回写现有 Scene Master 的 `Camera / Viewpoint` 与其中的 Capture Design，沿用[摄影设计](capture-design.md)的来源、锁定、接受状态和范围。器材事实仍查[器材库](equipment-library.md)，影片依据仍查[电影与场景方法库](cinema-shot-library.md)，最终提示词继续经过[既有编译器](prompt-compiler.md)。

口语输入先确定希望看到的差异，解释可见变化与推荐原因。专业输入保留用户给出的型号、实际焦距、f/T 值、有效画幅和运动参数。按当前任务补齐 OPEN 决策，简短提问用简短回答，完整专业定义按需展开。每卡完整字段用于资料查询，直接出词时只取当前画面需要的内容。

关联检索沿“术语 → 原理与条件 → 适用器材 → 有来源的电影或场景 → 迁移方法”逐层取用。关联数组允许为空，资料缺口保持待核验。两组关联各自的证据范围须分别核对，具体电影器材断言须有制作来源。器材事实、作品/段落实参、画面观察、创作建议及模型实测沿用现有库的证据类型。

## 分层与分类索引

常用层覆盖日常景别、机位、清晰关系与基本运动；进阶层用于光学结构、复合动作和跨镜头关系。按用户的实际目标检索，专业参数可以直接进入相应卡片。别名可能跨概念，需结合上下文和可见目标消歧。

索引中的 `term-*` 链接登记正式条目与所在文件。维护时新增或修改卡片及其索引链接即可，校验器动态读取目标文件、字段和关联资料。首批链接保留在[兼容页](camera-language-p0.md)。

### 光学与投影

| 中文 / English | 常用别名 | 层次 | 详细条目 |
| --- | --- | --- | --- |
| 鱼眼 / Fisheye | 鱼眼镜头、鱼眼投影、Fisheye Lens | 常用 | [term-fisheye](camera-language/optics.md#term-fisheye) |
| 广角 / Wide-angle | 广角镜头、Wide Lens、Wide-angle Lens | 常用 | [term-wide-angle](camera-language/optics.md#term-wide-angle) |
| 超广角 / Ultra-wide-angle | 超广、直线超广角、Ultra-wide、Rectilinear Ultra-wide | 常用 | [term-ultra-wide-angle](camera-language/optics.md#term-ultra-wide-angle) |
| 长焦 / Telephoto | 长焦镜头、Long Lens、Telephoto Lens | 常用 | [term-telephoto](camera-language/optics.md#term-telephoto) |
| 微距 / Macro | 微距摄影、Macro Photography、Macro Lens | 进阶 | [term-macro](camera-language/optics.md#term-macro) |
| 变形宽银幕镜头 / Anamorphic | 变形镜头、Anamorphic Lens、变形宽银幕 | 进阶 | [term-anamorphic](camera-language/optics.md#term-anamorphic) |
| 镜头倾斜 / Optical Tilt | 倾斜镜头、Tilt Lens、倾斜焦平面 | 进阶 | [term-optical-tilt](camera-language/optics.md#term-optical-tilt) |
| 镜头平移 / Optical Shift | 移轴平移、Shift Lens、移轴、Rise and Fall | 进阶 | [term-optical-shift](camera-language/optics.md#term-optical-shift) |

### 景别与取景

| 中文 / English | 常用别名 | 层次 | 详细条目 |
| --- | --- | --- | --- |
| 极远景 / Extreme Long Shot | 大远景、大全景、ELS、Extreme Wide Shot、EWS | 常用 | [term-extreme-long-shot](camera-language/framing.md#term-extreme-long-shot) |
| 全景 / Long Shot | 全身景、LS、Full Shot、Wide Shot、远景 | 常用 | [term-long-shot](camera-language/framing.md#term-long-shot) |
| 中景 / Medium Shot | MS、Waist Shot、腰部以上景别 | 常用 | [term-medium-shot](camera-language/framing.md#term-medium-shot) |
| 中近景 / Medium Close-up | MCU、胸像景别、胸部以上景别 | 常用 | [term-medium-close-up](camera-language/framing.md#term-medium-close-up) |
| 特写 / Close-up | CU、近特写、脸部特写 | 常用 | [term-close-up](camera-language/framing.md#term-close-up) |
| 大特写 / Extreme Close-up | 极特写、ECU、XCU、局部大特写 | 常用 | [term-extreme-close-up](camera-language/framing.md#term-extreme-close-up) |
| 牛仔景别 / Cowboy Shot | 美国景、American Shot、Plan Américain、大腿以上景别 | 常用 | [term-cowboy-shot](camera-language/framing.md#term-cowboy-shot) |

### 机位位置与朝向

| 中文 / English | 常用别名 | 层次 | 详细条目 |
| --- | --- | --- | --- |
| 仰拍 / Low Angle | 仰视、低角度仰拍、Low-angle Shot | 常用 | [term-low-angle](camera-language/position.md#term-low-angle) |
| 俯拍 / High Angle | 俯视、高角度俯拍、High-angle Shot | 常用 | [term-high-angle](camera-language/position.md#term-high-angle) |
| 平视 / Eye Level | 眼平机位、Eye-level Shot、视线高度 | 常用 | [term-eye-level](camera-language/position.md#term-eye-level) |
| 顶视 / Overhead | 正顶拍、Top Shot、Top-down Shot、Bird's-eye View | 进阶 | [term-overhead](camera-language/position.md#term-overhead) |
| 荷兰角 / Dutch Angle | 倾斜构图、Dutch Tilt、Canted Angle、斜角镜头 | 进阶 | [term-dutch-angle](camera-language/position.md#term-dutch-angle) |
| 越肩 / Over-the-shoulder | 过肩镜头、OTS、Over Shoulder、越肩镜头 | 常用 | [term-over-the-shoulder](camera-language/position.md#term-over-the-shoulder) |
| 主观视点 / POV | 主观镜头、Point of View、第一人称视点、POV Shot | 常用 | [term-pov](camera-language/position.md#term-pov) |

### 运动与摄影机操作

| 中文 / English | 常用别名 | 层次 | 详细条目 |
| --- | --- | --- | --- |
| 推进 / Dolly In | 推进、推镜、向前移动、dolly in、push in | 常用 | [term-dolly-in](camera-language/movement.md#term-dolly-in) |
| 拉远 / Dolly Out | 拉远、拉镜、后退镜头、dolly out、pull back | 常用 | [term-dolly-out](camera-language/movement.md#term-dolly-out) |
| 横移 / Truck | 横移、侧移、truck、truck left、truck right、lateral tracking | 常用 | [term-truck](camera-language/movement.md#term-truck) |
| 摇摄 / Pan | 摇摄、横摇、左右摇镜、pan、pan left、pan right | 常用 | [term-pan](camera-language/movement.md#term-pan) |
| 俯仰摇摄 / Tilt | 俯仰摇摄、上下摇镜、纵摇、tilt、tilt up、tilt down | 常用 | [term-tilt](camera-language/movement.md#term-tilt) |
| 垂直升降 / Pedestal | 垂直升降、升镜、降镜、pedestal、pedestal up、pedestal down | 常用 | [term-pedestal](camera-language/movement.md#term-pedestal) |
| 摇臂镜头 / Crane Shot | 摇臂镜头、吊臂镜头、crane shot、jib shot、crane up | 进阶 | [term-crane](camera-language/movement.md#term-crane) |
| 环绕 / Orbit | 环绕、绕拍、弧形跟拍、orbit、arc shot | 进阶 | [term-orbit](camera-language/movement.md#term-orbit) |
| 滚转 / Roll | 滚转、镜头滚转、光轴旋转、roll、camera roll | 进阶 | [term-roll](camera-language/movement.md#term-roll) |
| 变焦 / Zoom | 变焦、推近、拉近、zoom、zoom in、zoom out | 常用 | [term-zoom](camera-language/movement.md#term-zoom) |
| 移动变焦 / Dolly Zoom | 移动变焦、滑动变焦、希区柯克变焦、眩晕变焦、dolly zoom、vertigo effect | 进阶 | [term-dolly-zoom](camera-language/movement.md#term-dolly-zoom) |
| 手持 / Handheld | 手持、肩扛、手持摄影、handheld、hand-held | 常用 | [term-handheld](camera-language/movement.md#term-handheld) |
| 固定机位 / Locked-off | 固定机位、锁定机位、固定镜头、locked-off、locked off、static camera | 常用 | [term-locked-off](camera-language/movement.md#term-locked-off) |

### 清晰关系与成像行为

| 中文 / English | 常用别名 | 层次 | 详细条目 |
| --- | --- | --- | --- |
| 景深 / Depth of Field | 景深、清晰范围、浅景深、深景深、深焦、depth of field、DOF、deep focus、shallow focus | 常用 | [term-depth-of-field](camera-language/focus.md#term-depth-of-field) |
| 焦点转移 / Rack Focus | 焦点转移、移焦、拉焦、rack focus、focus pull、pull focus | 常用 | [term-rack-focus](camera-language/focus.md#term-rack-focus) |
| 焦外 / Bokeh | 焦外、散景、焦外成像、bokeh、out-of-focus rendering | 常用 | [term-bokeh](camera-language/focus.md#term-bokeh) |
| 旋焦 / Swirly Bokeh | 旋焦、旋转散景、旋转焦外、swirly bokeh、swirl bokeh | 进阶 | [term-swirly-bokeh](camera-language/focus.md#term-swirly-bokeh) |
| 镜头眩光 / Lens Flare | 镜头眩光、耀斑、鬼影、lens flare、flare、veiling glare | 常用 | [term-lens-flare](camera-language/focus.md#term-lens-flare) |
| 扩散 / Diffusion | 扩散、柔光滤镜、黑柔、diffusion、diffusion filter、optical diffusion | 常用 | [term-diffusion](camera-language/focus.md#term-diffusion) |
| 卤光 / Halation | 卤光、胶片卤光、高光红晕、halation、film halation | 进阶 | [term-halation](camera-language/focus.md#term-halation) |

### 构图与空间组织

| 中文 / English | 常用别名 | 层次 | 详细条目 |
| --- | --- | --- | --- |
| 中心构图 / Centered Composition | 中心构图、居中构图、主体居中、centered composition、central framing | 常用 | [term-centered](camera-language/composition.md#term-centered) |
| 负空间 / Negative Space | 负空间、留白、空白空间、negative space、breathing room | 常用 | [term-negative-space](camera-language/composition.md#term-negative-space) |
| 框中框 / Frame within a Frame | 框中框、内框构图、门框构图、frame within a frame、internal framing | 常用 | [term-frame-within-frame](camera-language/composition.md#term-frame-within-frame) |
| 前景遮挡 / Foreground Occlusion | 前景遮挡、前景遮幅、遮挡构图、foreground occlusion、foreground masking | 常用 | [term-foreground-occlusion](camera-language/composition.md#term-foreground-occlusion) |
| 空间分层 / Spatial Layers | 空间分层、前中后景、纵深分层、spatial layers、depth staging、foreground middleground background | 常用 | [term-spatial-layers](camera-language/composition.md#term-spatial-layers) |
| 三分法构图 / Rule of Thirds | 三分法、三分构图、九宫格构图、rule of thirds、thirds composition | 常用 | [term-rule-of-thirds](camera-language/composition.md#term-rule-of-thirds) |

### 剪辑与时间镜头语法

| 中文 / English | 常用别名 | 层次 | 详细条目 |
| --- | --- | --- | --- |
| 插入镜头 / Insert Shot | 插入镜头、细节插镜、insert shot、insert | 常用 | [term-insert-shot](camera-language/temporal.md#term-insert-shot) |
| 正反打 / Shot / Reverse Shot | 正反打、反打、对话反打、shot reverse shot、shot/reverse shot | 常用 | [term-shot-reverse-shot](camera-language/temporal.md#term-shot-reverse-shot) |
| 长镜头 / Long Take | 长镜头、长时间镜头、一镜到底、long take、oner、single take | 常用 | [term-long-take](camera-language/temporal.md#term-long-take) |
| 视线匹配 / Eyeline Match | 视线匹配、视线衔接、eyeline match、eyeline matching | 进阶 | [term-eyeline-match](camera-language/temporal.md#term-eyeline-match) |
| 180°轴线原则 / 180-degree Rule | 180度轴线原则、180°原则、轴线规则、180-degree rule | 进阶 | [term-180-degree-rule](camera-language/temporal.md#term-180-degree-rule) |

## 语义边界

- 检索 pull focus、拉焦时，区分在目标间转移清晰重点和跟随移动主体保持合焦。检索 Axis of Action 时先建立关系轴，按需再讨论180°机位原则。Single Take 说明一次连续拍摄，Long Take 另需相对时长条件。

- 中文“镜头”依据上下文拆解。型号、焦距、光圈指向 Lens。特写、全景、越肩等指向 Shot 的景别或构图。推进、横移、摇摄等指向 Movement。多个含义可以在同一摄影方案中组合。
- 高度记录摄影机离地或相对人物的位置，朝向记录向上、水平或向下的俯仰。贴地机位仍可保持水平。“镜头贴着地，人显得很有压迫感”可落实低高度、向上看人物与人物占比，广角是可选手段。
- Pan 以摄影机位置基本固定、朝向水平转动为核心。Truck 以摄影机向侧面平移为核心。“镜头不动，向右摇镜”按固定位置向右 Pan 解析，保留相容的固定位置要求。
- Dolly 改变摄影机位置与空间关系。Zoom 改变焦距与取景范围，在固定位置下保留同一透视关系。两种动作可以按用户意图组合。
- “人物不变大，背景改变透视”可提示 Dolly Zoom 候选，通过位移与反向变焦协调主体画面尺度。靠近主体时缩短焦距，后退时延长焦距，具体变化量随主体距离协调。先核对空间、主体尺度和时间意图，再决定适用表达。
- Swirly Bokeh 描述失焦背景的环绕趋势，依赖光学特征、画幅、对焦和背景条件。后期旋转模糊另记为后期效果，并记录作用区域与用户授权。

## 媒介与时间边界

Primary Medium 沿用当前授权。插画中的“鱼眼式透视”可落实弯曲空间、夸张近远比例与画面边缘行为，保留插画的制作逻辑。实物定格与微缩摄影按既有摄影设计处理。

静帧选择一个时刻的构图、清晰关系和可见运动线索。Dolly In、Pan、Zoom、Rack Focus 和 Dolly Zoom 的时间过程须借助连续画面或多帧成立。用户提出时长或完整动作时，静帧提示词表达选定时刻与可见结果，时间意图保留为连续画面的要求。需要视频时，可向现有独立 Motion Skill 共享术语和可迁移的 Camera / Viewpoint 字段，具体目标模型的执行能力另行核验。

## 呈现标签

- `directly_visible_in_still` 表示静帧能直接观察到的结果。
- `inferred_or_suggested_in_still` 表示静帧能暗示的过程或成因，判断需保留推断范围。
- `requires_temporal_sequence` 表示完整行为需要连续画面或多帧。
- `video_instruction` 表示可交给目标视频模型的指令意图，实际执行需要相应验证。

标签可以组合。它们描述表达与观察条件，模型实测状态沿用现有记录。
