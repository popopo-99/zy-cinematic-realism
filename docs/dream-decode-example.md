# 解梦示例 / Worked Dream Decode Example

**状态：实际参考图＋文本迁移示例；迁移图未生成，图像增益未验证。** / **Status: actual reference plus a text transfer example; transferred image not generated, image gains unvalidated.**

[中文 README](../README.md) · [English README](../README_EN.md)

## 参考图 / Reference

![作者的夜班公交作品](images/hero-night-bus.webp)

作者：ZY / popopo-99。这里只分析图片可见的色彩、曝光、材质与空间关系，不据此断言实际相机、镜头、胶片或制作方法。附图时请提供实际可访问图片；一个文件名本身不能当作图像输入。

Role: visual grammar only. Observable medium: photographic / cinematic rendering; actual production metadata is not inferred. No distinct abnormal event is required, so Expression Mechanism is omitted.

## 新场景与锁定 / New Scene and Locks

凌晨，一个老修表师在修表铺里合上怀表。胸像中景，动作、地点与人物身份意图锁定；参考的公交大空间不能把人物改回远景。参考图中的侦探、公交、原服装、座椅、广告均不迁移。

Before dawn, an elderly watchmaker closes a pocket watch at the workbench. Chest-up medium framing is USER-LOCKED. The reference cannot replace it with a wide bus scene. Identity specifics are not established by a visual-grammar-only reference.

## 五条核心梦律 / Five Core Rules

1. 大面积暗部与局部可见区域形成层级，不把所有人物、物件与背景等量照亮。 / Large dark regions and selective visibility form a hierarchy.
2. 冷色环境实际光与小面积暖色亮点形成关系，不使用全画面橙青滤镜。 / Cool practical light contrasts with small warm highlights rather than a blanket grade.
3. 反射发生在玻璃或金属等真实表面上，受光源和观察位置约束。 / Reflections belong to physical surfaces and the viewpoint.
4. 环境线条与前后层次表达观察距离；新景别不同就适配层次，不照搬原坐标。 / Spatial layering conveys distance but adapts to the new framing.
5. 表面不均匀可见，不把所有材料变成同样清晰或同样光亮。 / Different materials retain uneven, selective visibility.

## 可复制复用卡 / Complete Reuse Card

```text
解梦卡｜冷暖实际光与选择性可见度
类型：Visual Grammar / Dream Decode Card，非最终 Prompt
媒介：摄影式视觉表现；仅依据可见行为，不确定实际拍摄工艺。
核心规则：
1. 大面积暗部与少量可读区域形成层级，保留关键动作的可见性。
2. 冷色环境实际光与小面积暖色亮点并存，拒绝全局橙青色偏。
3. 玻璃与金属反射来自现场光源和观察位置。
4. 空间层次表达观察距离，但按新景别适配。
5. 不同材料的可见度、反射和细节随光线变化，不均匀锐化。
强继承：曝光层级、局部冷暖关系、表面选择性可见度。
条件继承：构图、人物占比、遮挡、反射与光线方向；只在新场景允许时适配。
不继承：公交、侦探、原服装、座椅、广告、原故事事件。
允许变化：人物、地点、道具、景别；新场景自己的光源必须解释色彩关系。
失效警报：照搬远景；所有物件等亮；添加无来源霓虹；带回公交或侦探。
存储状态：本卡仅为当前文本；新对话必须重新提供全文。
```

## 迁移 Prompt / Transfer Prompt

以下是模型中立的编译示例，激活前五条中的 1、2、3、5；用户锁定的胸像景别优先于第 4 条的原图空间布局。新场景的修表工作台、现场顶灯和台灯属于本示例的设计决定，不是从参考图识别到的事实。

```text
Before dawn inside a small watch-repair shop, an elderly watchmaker closes a pocket watch at the workbench, his attention still on the hinged case. A chest-up medium view at bench height keeps his hands and the watch readable. A cool overhead work light illuminates the bench, with a small warm task lamp reaching the watch and fingertips; the rest of the room falls into dense, uneven shadow. The watch catches only those existing sources, and faint glass-cabinet reflections follow the same light arrangement. Skin, cloth, wood, and metal retain different levels of visibility and reflection. Preserve the medium framing and closing gesture. Do not import the bus, detectives, original wardrobe, seat layout, or advertisements from the style reference; avoid global teal-orange grading, decorative neon, and uniform advertising polish.
```

## 下一步怎样验证 / How to Verify

固定此参考、新场景、模型与可见设置，比较合理基础 Prompt 与解梦编译 Prompt，至少三对结果。记录媒介与视觉规律保真、场景完整性、来源残留和人类创作评价；有无增益以实际结果为准。照片参考的这个文本示例不能替代纸本插画或风格化 3D 的回归。

[图像级手动对照协议](../zy-cinematic-realism/tests/manual-regression.md#image-level-dream-decode-regression--图像级解梦回归人工)
