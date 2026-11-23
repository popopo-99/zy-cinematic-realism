<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Jury JSON Brief 静帧编译格式

## 结构依据与适用范围

本配置于 2026-11-18 核对 Jury 安装版 `references/soul-cinema-json-brief.md` 及用户提供的 `Jury_JSON_Brief.md`。两份资料的静帧 JSON 示例可解析，九个顶层键、全部内层字段、类型和示例一致。流程方法来自 Jury《双入口使用手册 v2.5.3》。

安装版来源 SHA-256 为 `60620023de0ebecc05478df21478675ef2019f7802a371f432eae7cf70a05832`。用户提供 Brief 的 SHA-256 为 `2e2e5d3cdb7b86807619c010ecc14a77bb9f763699e888f8745404d4d7bd94ba`。

本轮将这些已取得的完整静帧字段与约束形式化为 [JSON Schema](../assets/jury-json-brief-still.schema.json)。该机器 Schema 由本次集成整理，原资料提供字段规范与结构示例。适配范围为静帧 Jury JSON Brief；来源中另有条件式视频分支，视频格式的编译与验证由相应独立任务处理。

只有用户明确选择 Jury JSON Brief 时加载本配置。普通文本、用户自有 schema 和其他 JSON 结构继续采用各自的输出合约。快速与引导阶段由[工作流](guided-capture-workflow.md)决定。

## 输出与类型

输出一个合法 JSON 对象，使用以下阅读顺序。对象键顺序可调整，所有字段和类型需符合 Schema。字符串填写当前确定内容；历史或地域等无依据的字段可写“未指定”。摄影化选择依据当前任务授权，忠实格式转换携带当前已有值，未指定型号仍如实表达。

| 顶层键 | 类型 | 内层必需字段 |
| --- | --- | --- |
| `scene_title` | string | 简短工作标题 |
| `Caption` | string | 可独立理解的完整当前画面描述 |
| `STYLE` | object | `Artistic Medium`、`Aesthetic Movement / Genre`、`Cultural / Historical Influence` |
| `COMPOSITION` | object | `Framing`、`Layout`、`Perspective` |
| `SCENE` | object | `Subject Characteristics`、`Setting`、`Geographic / Cultural Context` |
| `CINEMATOGRAPHY_AND_LIGHTING` | object | `Lighting Style`、`Color Palette`、`Overall Color Tone`、`Tone & Mood` |
| `CAMERA_AND_LENS` | object | `Camera Type and Era`、`Camera model`、`Lens model`、`Lens size`、`Lens Effects`、`Depth of Field`、`Film Grain / Noise` |
| `PHYSICAL_ATTRIBUTES` | object | `Material & Texture`、`Physics & Effects`、`Execution Style` |
| `hex_values` | array of string | 12–15 个 `#RRGGBB` 六位色值 |

六个内层对象共有 23 个必需字段，全部为非空字符串。顶层标题与 Caption 也是字符串。静帧对象的全部合法字段由此表及机器 Schema 给出。用户自有数值或布尔字段依据其自有 schema 保留原类型。

机器 Schema 的 `examples` 保留来源中的完整结构示意，示意值说明字段用途。最终输出逐字段填写当前画面内容。

## 从现有记录映射

| 字段 | 当前事实与表达来源 |
| --- | --- |
| `scene_title` / `Caption` | Scene Master 的当前主体、动作、空间、时间、天气与可见关系 |
| `STYLE.Artistic Medium` | 获准 Primary Medium 及其制作逻辑 |
| `STYLE.Aesthetic Movement / Genre` | 当前获准的类型、Director 或 Creative Grammar，落实其具体行为 |
| `STYLE.Cultural / Historical Influence` | 当前明确的传统与年代，缺项如实说明 |
| `COMPOSITION.Framing` / `Layout` / `Perspective` | 当前画幅、景别、主体尺度、空间层次、机位高度朝向和距离 |
| `SCENE.Subject Characteristics` / `Setting` / `Geographic / Cultural Context` | 当前主体与服装、地点时间天气、已有地域背景 |
| `CINEMATOGRAPHY_AND_LIGHTING` | 现有 `Light / Value`、Source Light Map 及当前配色、曝光和情绪关系 |
| `CAMERA_AND_LENS.Camera Type and Era` / `Camera model` / `Lens model` | 当前 Capture Design 的成像类别、机身和镜头；型号与可见用途一并表达 |
| `CAMERA_AND_LENS.Lens size` | 已有实际焦距与取景目标，和有效画幅、机位、人物占比相容 |
| `CAMERA_AND_LENS.Lens Effects` | 当前必要光学行为的形态、位置、强度与来源；真实扩散滤镜注明滤镜来源 |
| `CAMERA_AND_LENS.Depth of Field` | 对焦目标、清晰平面与允许失焦的区域 |
| `CAMERA_AND_LENS.Film Grain / Noise` | 当前介质及颗粒／噪声选择，洁净数字风格可写无明显颗粒 |
| `PHYSICAL_ATTRIBUTES.Material & Texture` | 当前表面、材质状态及其受光行为 |
| `PHYSICAL_ATTRIBUTES.Physics & Effects` | 当前实际物理关系和有来源的天气、动作、反射等 |
| `PHYSICAL_ATTRIBUTES.Execution Style` | 制作与后期取向、卤光或后期扩散、编辑保留／改变范围及场景特定限制 |
| `hex_values` | 当前 Color Palette / Lighting Style 中已有颜色家族的设计色板 |

Caption 使用完整当前画面描述，通常三至六句，复杂内容可按需要增加。主体、动作、见证位置、空间边界和光线关系要能独立读清。人口特征和具体事实沿用授权资料。静帧叙述选定时刻，连续运动留在相应时间计划中。

摄影机与镜头字段按当前媒介适配。写实或风格化CG可保留有用途的虚拟摄影机、镜头参照、等效视角和景深，并说明其虚拟用途。三渲二优先使用视点与渲染描述。绘画等媒介中无关的实体设备字段填写“不适用”及原因，视点、笔触、纸面或渲染逻辑进入相应构图和物理属性字段。实物定格摄影按当前媒介与用户授权处理。

卤光与后期扩散归入制作或介质表达，镜头眩光归入相应光学表达。Kodak 2383 使用 `print emulation` 放入配色或色调字段。事实依据继续读取当前[器材库](equipment-library.md)和[电影库](cinema-shot-library.md)，型号选择与历史实参保留各自来源范围。

## 色板与约束

12–15 的数量只作用于本静帧配置。可从已有颜色家族构造暗到亮的层次，黑白画面可采用获准灰阶。未实际采样时，色板表示近似设计值。用户锁定现有精确色值或仅允许少量平涂颜色时，先核对其与数量要求能否共存，冲突时请求允许扩展同家族色阶或选择自有结构。

当前对象字段由 Schema 限定。研究来源、评分、测试日志、API 控件与接受／锁定元数据放在方案或交接记录中。当前参考职责、保留／改变边界和模型相关限制写入对应的画面字段。静帧配置保持九键，`SHOT_DESIGN` 属于来源中的独立视频条件项。

用户指定结构文件而文件未读到、或只给了顶层键时，准确说明缺少的内层结构。可询问是否改用本已核对配置，获得选择后再编译。只分析规范时，直接回答分析请求。

## 编译检查

先按现有 Compiler Priority Gate 解析同一 Scene Master，再按当前模型表达与所选输出结构编译。核对来源与接受范围、当前 OPEN 候选、Caption 和各字段的一致性，以及参考内容的迁移范围。

结构检查使用机器 Schema 核对九个顶层键、23 个内层字段、类型、完整性和色值格式数量。JSON 文本应完整可解析，纯对象输出遵守当前请求。字段正确性与画面事实、色族、物理条件、模型实际表现分别检查。

## 风格胶囊映射

风格胶囊复用当前视觉语法。Medium与Rendering Logic写入STYLE，View / Lens Rules按适用性进入COMPOSITION与CAMERA_AND_LENS，Shading与Color Rules进入CINEMATOGRAPHY_AND_LIGHTING，Form、Material、Texture及执行约束进入PHYSICAL_ATTRIBUTES。人物和场景字段继续取自同一Scene Master。

胶囊、置信度和来源登记不新增顶层键。需要影响生成的参考职责与保留边界写入相关执行字段。CG设备字段标明虚拟参照，无法确认的真实生产器材保留未知。沿用已有Brief的hex_values时，保留原色值及其实际来源。Brief提供的十六进制值本身无法证明采样。缺少采样记录且用户未明确指定为精确配色约束时，在Color Palette中写明“近似设计色板，未经像素采样”。既有九键、23个内层字段与12–15色契约继续使用原机器Schema。
