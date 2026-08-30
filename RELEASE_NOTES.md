# 造梦师 v2.0.0

## Model Compiler Edition

**同一个画面，不同模型，说不同的语言。**

很多创作者已经遇到同一个问题：一条在某个模型里有效的 Prompt，换到另一个模型后，人物关系、空间、光线甚至故事时刻都会悄悄变化。原因不只是模型能力不同，也在于每个模型接收和组织视觉指令的方式不同。

v2.0.0 不再把最终 Prompt 当作唯一成果。它先建立一个稳定的 `Scene Master`，锁定人物、故事瞬间、动作、场景、机位、构图、光线、道具、时间、天气与限制，再把这套视觉方案编译成目标模型更容易执行的原生表达。

`Scene Master → Creative Grammar → Model Compiler → Result Repair`

模型语言可以改变，画面设计不能偷偷改变。

## Model Router

不知道从哪个模型开始时，Router 会根据任务是首次生成、精确编辑、多轮修改、转码还是连续镜头，建议适配路径。它是启发式建议，不是永久排名。

## Four Native Model Adapters

本版内置四条原生编译路径：

- **GPT Image 2**：结构清晰的自然语言视觉说明与编辑说明。
- **Midjourney**：高密度视觉语言与模型原生参数位置。
- **Seedream 5.0 Pro**：明确的空间、主体关系与视觉 brief。
- **Nano Banana**：直接、适合多轮编辑的任务措辞。

同一个 Scene Master 会得到不同的原生 Prompt，也会得到不同的模型解释；这不是对“完全一致结果”的承诺。

## Prompt Transcode

Transcode Lock 允许你把现有 Prompt 或 Scene Master 转到另一个模型，同时明确哪些事实必须保持、哪些句法可以改变。角色、动作、地点、道具、光线与叙事关系不会因为换模型而被默认重写。

## Multi-model Pack

一次请求即可得到同一 Scene Master 的四模型版本。它适合并行测试视觉方向，也便于看清差异来自模型解释，而不是来自四条互相漂移的 Prompt。

## Continuity Bible

连续镜头先建立 `Base Lock`，锁定身份、服装、道具、地点与光线；每一镜只增加一条 `Shot Delta`。这种结构让脸、衣服、关键道具和空间变化都有依据，适合角色组图、分镜和多镜叙事。

## Prompt Check

生成前先检查：是否有互相冲突的机位、没有来源的光、空泛风格词、过度拥挤的信息，或物理上无法同时成立的关系。Prompt Check 会指出问题并给出最小改动建议。

## Prompt Doctor

结果失败时先诊断，再修复。若画面太像广告，Prompt Doctor 可以只调整摄影机位置、人物姿态和光线层级，同时精确保留角色身份、服装、车辆与地点；不再因为一个局部问题把整条 Prompt 推倒重写。

## One Variable Remix

只改变一个声明变量，其余 Scene Master 全部锁定。例如只改变观察位置、天气或视觉中心，适合做可比较的 A/B 方向。

## Creative Shuffle

Creative Shuffle 不是随机堆词，而是在叙事和物理边界内提供多个可落地方案。每个方向都会说明真正改变了哪些光线、曝光、摄影机、空间、调度与视觉中心。

## New Creative Grammar

v2.0.0 保留 38 位导演的四轴视觉指纹，并新增 16 张风格卡和 8 张摄影卡。导演、风格和摄影参考不只是标签，而会进入当前场景的光影反差、色彩曝光、镜头机位、构图空间与人物调度。

## Upgrade

下载 `zy-cinematic-realism-v2.0.0.zip`，解压或导入其中唯一的顶级文件夹 `zy-cinematic-realism/`。

如果从 v1.x 升级，请用新文件夹完整替换旧的 `zy-cinematic-realism/`，不要同时安装多个同名副本。显式调用仍然是：

```text
请使用 $zy-cinematic-realism
```

## License

项目继续采用 CC BY-NC 4.0。个人学习与非商业创作可免费使用；分享改编版本时请保留作者、许可证与仓库来源，未经许可不得重新打包售卖或用于商业产品。

## Thanks

感谢所有参与试用、比较不同模型结果、报告 Prompt 漂移和连续性问题的创作者。你们的反馈让 v2.0.0 从“一条更长的 Prompt”真正走向了一套可检查、可转码、可修复的视觉方案。
