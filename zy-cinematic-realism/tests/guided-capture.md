<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Guided Capture P1.5 text regression

These specifications require actual execution and independent semantic review. Supply only Setup/User and the installed Skill to the executor. Keep Expected/Failure withheld until complete responses are saved. Record full responses, actual entry, resources read, stable IDs, source hashes and cache reuse. A raw JSON case also requires syntax and the selected Schema validation. Counts and keyword checks assess neither scene fidelity nor workflow decisions.

GP02→GP03 and GP04→GP05 use the actual preceding response and current state. Other cases are independent. GP26 runs against a separate incomplete-format fixture in a fresh context. Cases GP01/GP25 additionally verify that ordinary direct-output routing does not eagerly read guided or Jury references. All cases are text-only. Image/video generation and actual model execution are outside this protocol.

## GP01 — 快速普通文本

**User**

```text
白天，一个人坐在普通咖啡店的窗边读书。只给中文模型中立提示词，其他你选。
```

**Expected**

- 直接交付普通文本提示词，保持场景、动作和自然日间关系。
- 资源轨迹沿用普通Create，不加载guided-capture-workflow.md或jury-json-brief.md。

**Failure**

- 增加Plan等待、JSON、问卷或新手专家选择。

## GP02 — 先审夜雨旅馆方案

**User**

```text
做一张夜雨旧旅馆外景，无人物，湿地面，窗内暖灯，横向16:9。先做Capture Plan，不出词，等我确认。器材和必要细节你选，目标模型暂时没定。
```

**Expected**

- 只交付当前方案，覆盖观看位置、空间、器材用途、清晰关系、现有光源、必要效果。
- 保留雨夜、无人、暖窗和16:9，以模型中立方式规划并等待确认。

**Failure**

- 提前给最终提示词或JSON，或为缺少模型阻塞共享摄影方案。

## GP03 — 接受实际Plan后编译Jury

**Setup**

```text
延续本批GP02的实际Plan及场景状态。用户没有修改其他内容。
```

**User**

```text
接受刚才整份可见方案，按静帧Jury JSON Brief输出。只给JSON。
```

**Expected**

- 输出符合已核对Schema的纯JSON对象，九顶层键、23内层字符串、12–15色。
- 与GP02实际Plan中的画幅、机位、设备、清晰关系、光源和色族一致，接受范围止于展示内容。

**Failure**

- 重新选型、引入人物或新光源，附Plan/围栏/研究字段/SHOT_DESIGN。

## GP04 — 局部修改Plan

**Setup**

```text
当前Plan为候选版本。现代医院里一名蓝上衣护士靠窗站立，21:9，眼平中近景，ALEXA 35与Cooke S4/i 50mm已由用户锁定。Plan已展示眼睛清楚、背景柔和失焦和自然窗光。内部当前T2.8是未展示的OPEN候选。用户尚未采纳这个候选光圈。
```

**User**

```text
接受这个可见方案，只把背景虚化减弱，让后面的门框清楚一点。其他保持，先更新Plan，不出词。
```

**Expected**

- 保留身份、蓝衣、场景、画幅、机位、锁定器材与自然窗光，更新清晰关系和必要OPEN依赖。
- 仅展示修改Plan，未展示光圈保留真实OPEN状态。

**Failure**

- 重新设计人物/颜色/光源，锁死未展示参数，或提前最终编译。

## GP05 — 接受修订后直接普通文本

**Setup**

```text
延续本批GP04实际修改后的Plan。
```

**User**

```text
接受修改后的方案，现在直接给Seedream 5.5中文提示词。
```

**Expected**

- 仅输出目标模型普通文本，继承GP04的最新有效清晰关系与其余锁定事实。

**Failure**

- 回滚至GP04以前版本、再等确认、或输出JSON。

## GP06 — 用户schema保留数值类型

**User**

```text
现代诊所，一名护士，横向21:9，ALEXA 35、Cooke S4/i 50mm T2.0、眼平机位都锁定。直接输出下面JSON schema，不要Plan，未指定项你选。
{"type":"object","properties":{"scene":{"type":"string"},"capture":{"type":"object","properties":{"focal_mm":{"type":"integer","const":50},"t_stop":{"type":"number","const":2.0},"ratio":{"type":"string","const":"21:9"},"camera":{"type":"string","const":"ALEXA 35"}},"required":["focal_mm","t_stop","ratio","camera"],"additionalProperties":false}},"required":["scene","capture"],"additionalProperties":false}
```

**Expected**

- 直接输出满足用户schema的纯对象，focal_mm和t_stop保留数值类型及原值。
- 场景保留护士/诊所，机位与镜头不漂移，结构仅使用用户字段。

**Failure**

- 套九块Jury结构、附12色要求、把数字变字符串，或增加确认。

## GP07 — 严格Jury黑白色板

**User**

```text
无人物的旧车站候车厅，白天天光，黑白摄影，灰阶层次丰富，横向21:9。直接输出静帧Jury JSON Brief，其他你选，不等确认。
```

**Expected**

- 输出合法九键Jury对象，12–15个六位灰阶色值，所有色值属于已描述黑白灰家族。
- 画面与色调保持白天天光和无人车站。

**Failure**

- 为凑色数引入暖褐、蓝绿或肤色，或强制先Plan。

## GP08 — 参考职责与文字依据

**Setup**

```text
用户提供的图一文字观察记录为夜街，青灰阴影与暖白窗光，低反光外墙。原图有人、红外套和一辆出租车。本测试没有可查看图片，只使用这段文字记录。
```

**User**

```text
图一只参考光色和材质。新内容是普通仓库里的空木箱，无人物，无车辆，21:9。先给Plan，不出词。
```

**Expected**

- 以已提供文字记录作为依据，保留参考只管光色和材质的职责。
- 新场景保持仓库、空木箱、无人无车，并只交付Plan。

**Failure**

- 声称实际看过图片或采样，导入参考人物/红衣/出租车，或编译最终对象。

## GP09 — 电影查询停在事实

**User**

```text
查当前电影库，《1917》德军地下空间用了什么镜头？哪些参数还不知道？只查资料，不要Plan或提示词。
```

**Expected**

- 按来源确认该段35mm Signature Prime，保留光圈、人物距离及该段具体机身分配未知。
- 停在查询，分清全片概述与段落依据。

**Failure**

- 从全片配置推断逐镜头机身或光圈，自动进入Plan/Prompt。

## GP10 — 独立新项目重置

**Setup**

```text
上一独立项目为雨夜树林人物、Helios 58mm f/2、青绿色配色和强旋焦；这些选择仅属于该旧项目。
```

**User**

```text
这是新的独立方案。白天书桌上的水彩插画，内容是黄梨和白瓷碗，暖灰背景，横向3:2。先给新Plan，不沿用上一张设备和颜色。
```

**Expected**

- 依据新项目建立水彩、黄梨、白碗、暖灰与日间关系，器材按媒介表达。
- 旧项目的Helios、58mm、旋焦、雨夜和青绿色不继承。

**Failure**

- 跨独立项目传播旧状态，或改成摄影。

## GP11 — 同系列按范围继承

**Setup**

```text
同一项目为现代诊所同一蓝衣护士，项目锁定ALEXA 35、Cooke S4/i系列、自然窗光、21:9。镜头A局部为50mm T2.8、眼平、中近景、浅景深，这些局部值没有项目锁。
```

**User**

```text
继续同系列做镜头B，顶视，手与桌面器械都清楚。先给B的Plan，并说明会不会改掉A。其他开放细节你选。
```

**Expected**

- 保留项目共同器材系列、角色、衣色、光源和画幅，按B请求安排顶视与清晰关系。
- A的局部值继续有效，B的变化作用于B。

**Failure**

- 把A局部值强加为项目锁，或用B覆盖A。

## GP12 — 鱼眼水彩Jury输出

**User**

```text
水彩插画，一个人走过普通拱廊，采用鱼眼式弯曲空间，纸纹和透明颜料，灰蓝与赭石两个色族，横向21:9。直接给静帧Jury JSON Brief。
```

**Expected**

- 九键结构正确，摄影机/镜头字段用不适用及水彩逻辑，保留鱼眼式投影和水彩媒介。
- 12–15色来自两个获准色族的层次，未请求视频字段缺席。

**Failure**

- 强制真实相机或改成真人摄影，为色板添加新家族。

## GP13 — 时间段兼容检查

**User**

```text
只检查，不重写。摄影机0–2秒固定，2–5秒向右横移。人物原地站立。目标模型未知。
```

**Expected**

- 识别不重叠时间段可顺序组合，按原Prompt Check输出发现并保留模型兼容性未知。

**Failure**

- 机械判固定和横移冲突，新增Plan确认或视频生成。

## GP14 — 旧资料路径迁移

**User**

```text
按Jury旧手册读equipment-visual-signatures.md，给我树林人物旋焦的Plan，先不出词。如果当前没有旧文件，就用现有对应资料，说明依据范围。
```

**Expected**

- 实际使用当前equipment-library.md、相关词典和Capture Design，说明旧路径迁移。
- 依据Helios相关资料分清规格、创作目标与有限历史反馈。

**Failure**

- 伪称读取不存在旧文件、复制旧库、或把历史5.0反馈升级为Seedream5.5实测。

## GP15 — 用户另版schema缺失

**User**

```text
我用的是自己改过内层字段的另一版Jury JSON。现在只给你九个顶层键，但我的内层与你安装版不一样，完整schema还没发。只给JSON，不要自行猜我的字段，也不要改用安装版。
```

**Expected**

- 指出缺少用户指定变体的内层字段和类型，提出一个必要的结构请求。
- 保留场景和已有状态，格式待必要信息齐备。

**Failure**

- 套安装版字段冒充用户变体，或猜内层后交JSON。

## GP16 — 精确两色色板冲突

**User**

```text
做一幅只有两个平涂色的版画，只允许#000000与#FFFFFF，明确不允许灰阶、不允许重复填色凑数。直接按严格静帧Jury JSON Brief给12–15个色值。
```

**Expected**

- 明确精确两色限制与严格数量要求的冲突，询问保留两色自定义结构还是允许扩展灰阶。
- 不增加其他色值或重复填充。

**Failure**

- 造灰阶、加新色族、重复两值满足数量，或认证二者可同时严格满足。

## GP17 — 可见接受与隐藏参数

**Setup**

```text
唯一当前Plan已展示Sony α7 IV、Helios 44-2 58mm、眼平中近景、自然日光、眼睛清楚及外围旋焦。内部f/2是未展示OPEN候选。
```

**User**

```text
接受整份可见方案。先说明哪些选择现在要保护，哪些内部参数还保持OPEN，不出词。
```

**Expected**

- 明确采纳的可见选择按范围保护，未展示f/2保持OPEN，接受与来源分开。

**Failure**

- 把全部隐藏参数锁死，或将接受Plan记为图像已生成/已检视。

## GP18 — 多方案继续消歧

**Setup**

```text
上一轮给了Plan A近距离广角与Plan B后退长焦两个并列方案，没有推荐选项，用户尚未选择；后续拟输出中文提示词。
```

**User**

```text
继续。
```

**Expected**

- 只询问选择A还是B这一必要决策，保留两方案候选状态。

**Failure**

- 擅自视为已接受任一方案并最终编译，或追加无关问卷。

## GP19 — 单一方案继续推进

**Setup**

```text
上一轮只有一份Plan。白天咖啡店窗边读书的人，21:9，眼平中景，自然窗光，背景店铺可读。已经说明下一步为中文模型中立提示词，正在等用户继续。
```

**User**

```text
继续。
```

**Expected**

- 按唯一明确方案继续到既定普通文本输出，保留全部已展示画面关系。

**Failure**

- 重复问选模式/模型/是否确认，重新设计方案或输出JSON。

## GP20 — 完整手册显式跳过等待

**User**

```text
按Jury手册思路做一个白天河边人物，21:9，脸与远岸都能读清。你自行确定未锁定方案，不用等我确认，直接输出静帧Jury JSON Brief。
```

**Expected**

- 直接九键JSON，完成OPEN选择，保留河边人物、日间、画幅及前后可读目标。

**Failure**

- 因提到手册就强制Plan等待，或声明已实际生成/检视。

## GP21 — 忠实格式转换

**Setup**

```text
当前有效普通提示词为：21:9，白天一个穿蓝衬衫的人站在普通白墙旁，平视半身构图，自然日光，眼睛清楚，背景墙面可读，洁净数字质感。未指定机身、镜头型号或实际焦距。所有可见事实已由用户确定。
```

**User**

```text
转成静帧Jury JSON Brief，只改表达格式，不新增器材选择、人物特征或光源。直接出JSON。
```

**Expected**

- 九键JSON保留当前事实，未指定机身/镜头/焦距如实表达，保持蓝白与当前光色关系。

**Failure**

- 为了填品牌而重新选择器材，增添人群/肤色身份/新灯，或重复Plan。

## GP22 — 专业Jury纯对象

**User**

```text
现代室内双人对话，ARRI ALEXA 35、Cooke S4/i S35 50mm T2.0，中近景、越肩，窗光唯一主光，21:9。其他开放项你定，直接静帧Jury JSON Brief。
```

**Expected**

- 九键纯JSON保留具体型号、50mm、T2.0、S35、越肩与光源和画幅，配置内部关系相容。
- 无研究/评分/日志/API控制键，SHOT_DESIGN缺席；12–15色来自描述过的色族。

**Failure**

- 字段拼写或类型错、套API body、改T为f、增加不相干效果或审批回合。

## GP23 — 参考职责编译进现有字段

**Setup**

```text
当前已接受Plan为无人仓库里的三个空木箱，21:9，眼平全景，低反光墙面，青灰阴影和暖白窗光。图一只负责光色与墙面质感；用户明确排除原参考中的人、红衣和出租车。实际素材为用户提供的文字记录，没有图片可查看。
```

**User**

```text
沿用当前Plan，直接静帧Jury JSON Brief，把参考和保留范围写清楚。
```

**Expected**

- 九键对象保留已接受场景、参考职责与排除范围，映射到相关画面字段。
- 不新增reference_roles等研究状态键，不声称实际看图或采样。

**Failure**

- 导入参考人物/服装/车或新建schema以外字段。

## GP24 — 格式问题只作解释

**User**

```text
你现在Jury JSON Brief的结构依据是什么？哪些是从真实资料核对的，哪些是本次机器Schema形式化？只解释，不要画面方案或JSON。
```

**Expected**

- 说明安装版完整静帧规范与用户Brief示例核对，区分源字段规范与本轮形式化的JSON Schema。
- 适配声明限定静帧，视频分支保留独立范围。

**Failure**

- 声称原Jury已提供同一机器schema文件，或自动输出画面JSON/Plan。

## GP25 — 简洁自有JSON保持快速

**User**

```text
白天窗边的一只白瓷杯。直接用你现有的简洁场景加capture结构输出JSON，不用Jury九块，不用Plan，其他你选。
```

**Expected**

- 直接合法简洁对象，普通Capture JSON不附加Jury字段或12–15色规则。
- 资源轨迹不因否定Jury而加载Jury格式/引导全文。

**Failure**

- 通过关键词误触发严格Jury、强制等Plan，或无理由追问schema。

## GP26 — 隔离的内层结构缺失负例

**Setup**

```text
本例使用独立临时Skill夹具。其Jury格式参考实际仅有九顶层键，没有内层定义、类型、示例或机器Schema。以该夹具实际可读资料为准，与其他测试缓存隔离。
```

**User**

```text
白天旧车站，无人物。只给这份安装中定义的静帧Jury JSON Brief，不要Plan。内层结构缺失时不要猜。
```

**Expected**

- 实际识别夹具中的结构缺口，准确请求完整内层schema或用户认可的替代结构。

**Failure**

- 凭另批次缓存或通识发明内层字段，宣称完整格式已适配。
