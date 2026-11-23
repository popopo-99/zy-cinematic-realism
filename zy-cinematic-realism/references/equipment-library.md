<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
Source: https://github.com/popopo-99/zy-cinematic-realism
-->

# 器材武器库

## 按画面目标取用

普通用户描述希望看到的画面即可。先依据[摄影设计](capture-design.md)完成观看位置、人物占比和清晰关系，再按需要读取相关卡片。专业用户可直接使用器材名称、稳定 ID 和参数。一次浏览优先给出与当前场景相关的少量选项。

| 想要的画面 | 可查看的条目 | 编译时需要落实的条件 |
| --- | --- | --- |
| 人物清楚，树林背景轻微环绕 | [Helios 44-2](#lens-helios-44-2) | 中心对焦、外围失焦纹理、主体背景分离 |
| 树叶间亮点呈明亮圆环 | [Trioplan 100](#lens-trioplan) | 开放光圈、逆光亮点、背景失焦 |
| 清晰自然的人物与空间层次 | [Signature Prime](#lens-signature-prime)、[Supreme Prime](#lens-supreme-prime)、[S4/i S35](#lens-cooke-s4i) | 先选机位、视角、对焦范围，再写细节与过渡 |
| 低照度下保留细节和有动机的光 | [Master Prime](#lens-master-prime)、[VENICE 2](#cam-sony-venice2)、[VISION3 500T](#media-kodak-5219) | 保留场景现有光源，安排曝光与允许的噪点或颗粒 |
| 有节制的老镜头质地 | [Speed Panchro](#lens-speed-panchro)、[Canon K-35](#lens-k35) | 明确需要的反差、焦点过渡与强光行为 |
| 椭圆焦外与宽银幕光学特征 | [Panavision C](#lens-panavision-c)、[Atlas Orion](#lens-atlas-orion)、[Ultra Panavision 70](#lens-ultra-panavision70) | 有效画幅、变形倍率、散景光点与入镜强光分别处理 |
| 小物件近在眼前，同时交代周围环境 | [Laowa 24mm Probe](#lens-laowa24-probe) | 贴近小主体、低机位、微观尺度与足够照明 |
| 明亮日景，细腻胶片颗粒 | [VISION3 50D](#media-kodak-5203) | 日光条件、细颗粒、明确的色彩与反差 |
| 受控钨丝灯场景中的细腻负片外观 | [VISION3 200T](#media-kodak-5213) | 光源色温、曝光与最终白平衡 |
| 印片后的浓郁黑位与中性高光 | [Kodak 2383](#media-kodak-2383) | 在最终色彩处理中使用印片外观描述 |
| 夜景强亮点边缘带红色卤光 | [CineStill 800T](#media-cinestill-800t) | 暗背景中的强高光边界、局部强度 |
| 灯光周围柔和扩散，皮肤保持细节 | [Black Pro-Mist](#filter-black-pro-mist) | 滤镜强度、光源亮度、局部反差与面部细节 |

### 型号索引

| 类型 | 卡片 |
| --- | --- |
| 数字摄影机与相机 | [ALEXA 35](#cam-alexa-35)、[ALEXA Mini LF](#cam-mini-lf)、[ALEXA LF](#cam-alexa-lf)、[ALEXA 65](#cam-alexa-65)、[VENICE 2](#cam-sony-venice2)、[V-RAPTOR X](#cam-red-vraptor-x)、[Sony α7 IV](#cam-sony-a7iv) |
| 球面镜头 | [Signature Prime](#lens-signature-prime)、[Supreme Prime](#lens-supreme-prime)、[Master Prime](#lens-master-prime)、[Cooke S4/i](#lens-cooke-s4i)、[Speed Panchro](#lens-speed-panchro)、[Canon K-35](#lens-k35)、[Helios 44-2](#lens-helios-44-2)、[Trioplan](#lens-trioplan) |
| 变形宽银幕与特殊镜头 | [Panavision C](#lens-panavision-c)、[Ultra Panavision 70](#lens-ultra-panavision70)、[Atlas Orion](#lens-atlas-orion)、[Laowa Probe](#lens-laowa24-probe) |
| 胶片与印片外观 | [Kodak 5219](#media-kodak-5219)、[Kodak 5213](#media-kodak-5213)、[Kodak 5203](#media-kodak-5203)、[Kodak 2383](#media-kodak-2383)、[CineStill 800T](#media-cinestill-800t) |
| 扩散滤镜 | [Tiffen Black Pro-Mist](#filter-black-pro-mist) |

## 使用依据

每卡“资料事实”沿用 `manufacturer_spec` 类型，并保留卡片原有来源身份，如原厂手册镜像或租赁商保存的原规格。“画面用途”“需要落实”“可选文本”属于 `creative_proposal`。Helios 卡中的 Jury 历史反馈单独按 `model_test` 理解，仅覆盖所载版本与上下文。来源核对日期继续使用各卡记录。

从[摄影术语索引](camera-language-dictionary.md)进入本库时，先核对条目的原理与条件，再按型号确认版本、覆盖、卡口和所需效果条件。型号名、焦距或品牌查询可直接定位下方稳定 ID。需要影片实例时继续查询[电影库的事实范围](cinema-shot-library.md#证据类型与事实范围)，将电影制作记录与当前器材候选分别记录。原理适配的候选器材仍需在当前场景中完成机位、光源和清晰关系设计。

- 每张卡的“资料事实”来自已打开核对的厂家、原厂技术文档或明确标记的原厂手册镜像。“画面用途”和“可选文本”是将资料转成当前创作目标的建议。厂家关于外观的描述保留其来源身份。
- 机身名称用于表达器材语境。色彩、反差、高光、噪点、颗粒、景深和镜头效果各自需要具体描述。生成模型对这些描述的执行程度需依据实际结果判断。
- 焦距均按镜头实际焦距理解。视角需要结合有效成像区域、裁切和变形倍率。透视需要结合摄影机位置与主体距离。交付宽高比单独记录。
- 实拍器材方案需要分别核对卡口、转接、后组空间、像场覆盖和记录模式。卡片的格式说明用于初筛。选用全画幅模式前，应核对具体镜头在该模式下的覆盖资料。
- 可选文本按当前主体、媒介和模型裁剪。用户要普通文本时直接编译，用户明确需要结构化载荷时再导出对应格式。
- 电影制作记录与具体镜头的摄影依据见[电影摄影参考库](cinema-shot-library.md)。影片使用某个系列的记录只支持该资料覆盖的范围。

本库沿用 Jury 提出的“器材视觉签名”组织思路，把器材名称、可见效果、触发条件与提示词表达联系起来。此处技术资料于 2026-11-17 重新核对。Jury 早期 Seedream 5.0 Pro 的个别反馈记录在相关卡片中，其他模型及 Seedream 5.5 的执行表现保持待观察状态。

## 数字摄影机与相机

<a id="cam-alexa-35"></a>
### ARRI ALEXA 35

- **稳定 ID 与别名**　`cam-alexa-35`，ALEXA35。
- **资料事实**　Super 35 数字电影摄影机。厂家标称 17 档动态范围，使用 REVEAL Color Science。2026-11-17 的厂家页面已归入历史机型，并列出 ALEXA 35 Xtreme 后继产品。
- **画面用途**　为 Super 35 视角体系、受控高光与层次清楚的数字底片建立摄影语境。
- **需要落实**　具体镜头、焦距、有效拍摄模式、机位、光源和最终色彩处理。
- **误用检查**　把肤色、色温和高光过渡写成可见目标。把胶片颗粒、柔光和眩光留给对应介质或光学选择。
- **可选文本**　`ARRI ALEXA 35，Super 35 摄影语境，肤色自然，亮部保留层次，暗部保留必要细节`。
- **来源与核对**　厂家产品页，2026-11-17。[ARRI ALEXA 35](https://www.arri.com/en/cine-systems/cine-cameras/legacy-cine-cameras/alexa-35)

<a id="cam-mini-lf"></a>
### ARRI ALEXA Mini LF

- **稳定 ID 与别名**　`cam-mini-lf`，Mini LF，ALEXA MINI LF。
- **资料事实**　紧凑型 large-format 数字电影摄影机，提供多种记录格式。厂家资料同时介绍 ARRIRAW 的 REVEAL 后期工作流。
- **画面用途**　适合将人物近距离观看与环境层次结合的 LF 摄影方案，也可用于手持或稳定器摄影语境。
- **需要落实**　有效记录区域、覆盖该区域的镜头、观看距离、景别和对焦范围。
- **误用检查**　“LF”作为传感器格式语境使用。需要浅景深时继续指定清晰平面、焦段或视角、光圈与主体背景距离。
- **可选文本**　`ALEXA Mini LF，靠近人物的中近景，脸部自然清晰，背景保留空间关系并适度失焦`。
- **来源与核对**　厂家产品页，2026-11-17。[ARRI ALEXA Mini LF](https://www.arri.com/en/cine-systems/cine-cameras/alexa-mini-lf)

<a id="cam-alexa-lf"></a>
### ARRI ALEXA LF

- **稳定 ID 与别名**　`cam-alexa-lf`，ALEXA Large Format。
- **资料事实**　厂家说明其传感器略大于传统全画幅，原生记录 4.5K，系统采用 LPL 卡口，并提供 PL-to-LPL 转接方案。
- **画面用途**　用于有明确 LF 摄影参照的场景、宽阔空间中的人物和需要保留大画幅摄影语境的方案。
- **需要落实**　传感器记录模式、镜头像场、机位与实际焦距。电影中的定制镜头仍需使用该片资料核对。
- **误用检查**　转接能力与像场覆盖分别查证。电影级低饱和色调、柔光或颗粒在成像处理中独立指定。
- **可选文本**　`ARRI ALEXA LF，宽阔环境中的人物近景，面部与环境尺度协调，亮部柔和过渡`。
- **来源与核对**　厂家产品页，2026-11-17。[ARRI ALEXA LF](https://www.arri.com/en/cine-systems/cine-cameras/alexa-lf)

<a id="cam-alexa-65"></a>
### ARRI ALEXA 65

- **稳定 ID 与别名**　`cam-alexa-65`，Alexa65。
- **资料事实**　65mm 格式数字电影摄影机。厂家列出 54.12 × 25.58mm 有效成像区域、Open Gate 6560 × 3100，并提供专用镜头与工作流系统。
- **画面用途**　适合精细环境、宽阔空间与贴近人物并存的摄影设计。先描述空间尺度，再确定焦距与景深。
- **需要落实**　所选记录模式、与有效区域相配的镜头覆盖、机位和人物占比。
- **误用检查**　镜头卡口与大像场覆盖逐项核对。65mm 数字摄影的颗粒外观按用户目标另行设置。
- **可选文本**　`ALEXA 65 摄影语境，人物与广阔环境共同入画，近处皮肤和远处地形具有清楚的层次关系`。
- **来源与核对**　厂家租赁系统与技术表，2026-11-17。[ARRI Rental ALEXA 65](https://www.arrirental.com/en/cameras/digital-65-mm-cameras/alexa-65)

<a id="cam-sony-venice2"></a>
### Sony VENICE 2

- **稳定 ID 与别名**　`cam-sony-venice2`，VENICE2，Sony Venice II。
- **资料事实**　全画幅数字电影摄影机，厂家提供 8K 与 6K 传感器选择，支持机内 X-OCN 记录。具体双基础感光度与模式依传感器版本查证。
- **画面用途**　用于全画幅数字摄影、现有光源夜景及需要保留丰富明暗层次的方案。
- **需要落实**　传感器版本、有效记录区域、镜头覆盖、场景光源与预期噪点程度。
- **误用检查**　夜景亮度、混合光颜色和暗部细节分别描述。机型比较仅使用具体版本已核实的规格。
- **可选文本**　`Sony VENICE 2，全画幅数字电影摄影，沿用街道现有光源，脸部保留自然色阶，暗部仍有可辨细节`。
- **来源与核对**　厂家产品页，2026-11-17。[Sony VENICE 2](https://pro.sony/en_NL/products/digital-cinema-cameras/venice2)

<a id="cam-red-vraptor-x"></a>
### RED V-RAPTOR [X] 8K VV

- **稳定 ID 与别名**　`cam-red-vraptor-x`，V-RAPTOR X，V-RAPTOR [X]。
- **资料事实**　原厂操作指南列出 8192 × 4320 全局快门 CMOS、40.96 × 21.60mm 传感器，以及依机身版本采用的锁定式 Nikon Z 或 Canon RF 卡口。
- **画面用途**　用于全局快门摄影语境、动作瞬间和结构清楚的数字成像。运动表现需要同步写清主体状态与曝光时间意图。
- **需要落实**　具体机身版本、镜头像场、记录模式、动作清晰程度与光线。
- **误用检查**　全局快门信息主要关系运动采样。单张提示词中的线条稳定、运动拖影和锐度仍需明确表达。
- **可选文本**　`RED V-RAPTOR [X] 8K VV，动作瞬间，建筑竖线稳定，主体轮廓清晰，保留衣物运动形态`。
- **来源与核对**　原厂操作指南技术表，2026-11-17。[RED V-RAPTOR X Technical Specifications](https://docs.red.com/955-0225/955-0225_V2.0%20Rev-A%20RED%20PS,%20V-RAPTOR%20%5BX%5D%208K%20VV%20Operation%20Guide/Content/B_TechSpecs/Specs_V-RAPTOR%20%5BX%5D.htm)

<a id="cam-sony-a7iv"></a>
### Sony α7 IV

- **稳定 ID 与别名**　`cam-sony-a7iv`，A7 IV，A7IV，ILCE-7M4。
- **资料事实**　约 3300 万有效像素的全画幅混合相机。厂家说明视频 4K 60p 使用 Super 35 模式，全画幅模式最高 4K 30p。
- **画面用途**　用于自然日光人像、日常摄影与洁净数字底片语境。可将老镜头的局部光学特征叠加在数字基础上。
- **需要落实**　静态照片或视频模式、有效裁切、所用镜头与转接条件。
- **误用检查**　保留用户指定的机身。需要旋焦时，继续落实镜头、开放光圈、背景距离和外围失焦范围。
- **可选文本**　`Sony α7 IV，白天自然光人像，眼睛清楚，肤质自然，洁净数字成像，背景虚化按镜头与距离安排`。
- **来源与核对**　厂家发布资料，2026-11-17。[Sony Alpha 7 IV 发布资料](https://sony.mediaroom.com/2021-10-21-Sony-Electronics-Alpha-7-IV-Goes-Beyond-Basic-with-33-Megapixel-Full-frame-Image-Sensor-and-Outstanding-Photo-and-Video-Operability)

## 球面镜头

<a id="lens-signature-prime"></a>
### ARRI Signature Prime

- **稳定 ID 与别名**　`lens-signature-prime`，Signature Primes，ARRI SP。
- **资料事实**　LPL 卡口 large-format 球面定焦系列。厂家列出 12–280mm 范围，多数型号为 T1.8，并用柔和肤色、柔顺焦外描述该系列。
- **画面用途**　自然人物、清楚的主体与柔顺焦点过渡。需要的暖度与反差以当前光源和最终色彩决定。
- **需要落实**　具体焦距、型号最大 T 值、对焦目标、背景分离与有效画幅覆盖。
- **误用检查**　查具体型号的技术表，较长焦距型号有不同最大 T 值。根据场景需要控制眩光。
- **可选文本**　`ARRI Signature Prime，皮肤细节清楚，焦点向背景平顺过渡，柔顺焦外，亮部层次细腻`。
- **来源与核对**　厂家产品与技术表，2026-11-17。[Signature Prime](https://www.arri.com/en/cine-lenses/signature-lenses/signature-primes-zooms/signature-primes)、[技术数据](https://www.arri.com/en/cine-lenses/signature-lenses/signature-primes-zooms/arri-signature-lenses-technical-data)

<a id="lens-supreme-prime"></a>
### ZEISS Supreme Prime

- **稳定 ID 与别名**　`lens-supreme-prime`，Supreme Primes。
- **资料事实**　覆盖 Super 35 至 FF+ 的球面定焦系列，多数型号最大光圈为 T1.5。厂家强调系列匹配、平顺的清晰到失焦过渡与温和锐度。
- **画面用途**　既保留皮肤纹理与空间细节，又需要柔顺景深过渡的人物或环境摄影。
- **需要落实**　具体焦距的最大 T 值、有效画幅、对焦平面与背景距离。
- **误用检查**　Supreme Prime 与 Supreme Prime Radiance 分别查证。需要特殊眩光时核对具体系列与光源条件。
- **可选文本**　`ZEISS Supreme Prime，主体纹理清楚，锐度自然，清晰区域向失焦背景柔和过渡`。
- **来源与核对**　厂家产品与技术表，2026-11-17。[ZEISS Supreme Prime](https://www.zeiss.com/photonics-and-optics/en/cinematography/lenses/supreme-prime-lenses.html)

<a id="lens-master-prime"></a>
### ARRI/ZEISS Master Prime

- **稳定 ID 与别名**　`lens-master-prime`，Master Primes，ARRI Master Prime。
- **资料事实**　ARRI 与 ZEISS 联合开发、ZEISS 制造的 PL 球面镜头系列。厂家列出 12–150mm、T1.3，并强调对反差、眩光和呼吸效应的控制。格式定位为 Super 35。
- **画面用途**　可用光摄影、清晰且受控的画面结构，以及需要较大通光量的摄影方案。
- **需要落实**　主体前后位置、对焦面、具体 T 值与有效画幅覆盖。多个人物同时清楚时先安排站位。
- **误用检查**　历史 Zeiss f/0.7 特制镜头资料按原型号使用。Master Prime 的 T1.3 作为本系列技术事实记录。
- **可选文本**　`ARRI/ZEISS Master Prime，沿用场景现有光源，主体轮廓与细节清楚，反差受控，对焦准确`。
- **来源与核对**　厂家产品与技术资料，2026-11-17。[ARRI Master Prime](https://www.arri.com/en/cine-lenses/arri-zeiss-fujinon-lenses/master-primes/master-primes)、[ARRI 球面镜头格式表](https://www.arri.com/resource/blob/73154/fe7dce5f8611542754461abc8253c796/3-2-0-arri-prime-lenses-spherical-data.pdf)

<a id="lens-cooke-s4i"></a>
### Cooke S4/i S35

- **稳定 ID 与别名**　`lens-cooke-s4i`，S4/i，S4i，Cooke S4。用户只写 S4 时保留原话并按语境识别版本。
- **资料事实**　PL 卡口 Super 35 球面系列，带 /i 镜头数据。厂家介绍系列色彩匹配、全开时对眩光和像差的控制，并列出主要型号 T2。
- **画面用途**　需要自然皮肤、清晰主体和细腻空间关系的人物摄影。暖度通过光源、白平衡和后期目标具体控制。
- **需要落实**　S35 或 FF 版本、具体型号的最大 T 值、机位与对焦范围。
- **误用检查**　S4/i S35、miniS4/i 与 S4 FF/i 使用各自规格。系列颜色匹配的实拍属性只用于资料说明。
- **可选文本**　`Cooke S4/i S35，人物肤色自然，细节清楚，明暗层次柔顺，背景按景深安排渐次退开`。
- **来源与核对**　厂家产品与技术表，2026-11-17。[Cooke S4/i S35](https://cookeoptics.com/lens/s4-i-prime/)

<a id="lens-speed-panchro"></a>
### Cooke Speed Panchro

- **稳定 ID 与别名**　`lens-speed-panchro`，Speed Panchros，旧版 Panchro。
- **资料事实**　历史球面镜头家族，存在不同代际、老化状态和重装版本。Cooke 的回顾文章说明旧镜个体色偏可能不同，部分高阶像差在开放光圈下更明显，会影响反差。Panchro/i Classic 是后续重新设计的产品。
- **画面用途**　有节制的旧镜反差、柔顺高光与可见皮肤纹理，可用于时期感或亲密人物摄影。
- **需要落实**　具体代际、焦距、重装版本和所需效果强度。强光进入镜头时再安排对应眩光行为。
- **误用检查**　以用户指定的版本为准。旧镜老化产生的色偏需要独立依据与创作授权。
- **可选文本**　`Cooke Speed Panchro，温和局部反差，皮肤纹理可辨，明亮边缘柔顺，保留场景本身的色彩关系`。
- **来源与核对**　厂家技术回顾，2026-11-17。[Cooke The Panchro look](https://cookeoptics.com/news-and-events/recreating-the-panchro-look/)

<a id="lens-k35"></a>
### Canon K-35

- **稳定 ID 与别名**　`lens-k35`，K35，Canon K35。
- **资料事实**　历史高速非球面电影镜头系列。Vantage 提供的原广告与租赁规格列出多种焦距，18/24mm 为 T1.5，35/50/85mm 为 T1.3。实际套组与重装版本需要逐项核对。Canon 官方历史记录其 1977 年获奥斯卡技术奖。
- **画面用途**　可作为老镜头人物摄影和低照度方案的候选。温和反差、焦外和高光处理需在当前提示词明确指定。
- **需要落实**　具体焦距、版本、像场、光圈与实际强光方向。当前卡片提供规格依据，外观选择依用户目标和授权参考完成。
- **误用检查**　按所选镜头或套组资料使用实际焦距与光圈。影片使用记录在电影库按作品核对。
- **可选文本**　`Canon K-35，人物清晰且保留自然肤质，背景平顺失焦，局部反差温和，高光扩散保持轻微`。
- **来源与核对**　租赁商保存的原广告与规格、厂家历史，2026-11-17。[Vantage Canon K-35 PDF](https://www.vantagefilm.com/file/edee/downloads/rentals/canonk35.pdf)、[Canon 历史](https://global.canon/en/corporate/history/03.html)

<a id="lens-helios-44-2"></a>
### Helios-44-2 58mm f/2

- **稳定 ID 与别名**　`lens-helios-44-2`，Helios 44-2，Гелиос-44-2，2/58。
- **资料事实**　1971 年 ZENIT-E 原厂手册的公开镜像列出 58mm、f/2–f/16、最近对焦约 0.5m，与 M42×1 镜头连接体系。原厂归档站本次访问遇到重定向，规格依据已打开的手册镜像保留。
- **画面用途**　中心人物清楚、外围失焦纹理呈环绕趋势的树林人像。旋焦属于此处候选效果描述。
- **需要落实**　开放光圈、中心附近对焦、人物与细碎背景拉开距离、外围有可失焦的叶片或亮点。强度依据构图和实际结果调整。
- **误用检查**　写清效果只作用于失焦背景，同时保留人物与环境结构。Jury 早期 Seedream 5.0 Pro 有个别 16:9 反馈，画幅与效果关系仍缺乏确定依据。
- **可选文本**　`Helios 44-2 58mm，f/2，对焦眼睛，中心人物清楚，外围失焦树叶轻微环绕，subtle swirly bokeh, sharp center, swirled out-of-focus edges`。
- **来源与核对**　原厂手册镜像、Jury 历史反馈，2026-11-17。[ZENIT-E 1971 手册镜像](https://eugigufo.net/files/photovideo/inyaz/zeniteeng.pdf)、[原厂归档地址](https://www.zenitcamera.com/mans/zenit-e/zenit-e-eng.html)

<a id="lens-trioplan"></a>
### Meyer Optik Görlitz Trioplan 100 f2.8 II

- **稳定 ID 与别名**　`lens-trioplan`，Trioplan 100，Trioplan 100mm f/2.8 II。
- **资料事实**　现代复刻版本为 100mm、f/2.8–f/22、三片结构、15 片光圈叶片，厂家列出 60mm 像圈。厂家说明开放至 f/2.8、逆光时更容易出现鲜明肥皂泡散景。
- **画面用途**　人像或自然近景中，让失焦亮点边缘较亮、中心较空，呈圆环感。
- **需要落实**　背景亮点、逆光或背光关系、主体背景分离、开放光圈与正确对焦。
- **误用检查**　只在背景原有光点位置安排环状焦外，保持主体皮肤与环境结构自然。旧版 Trioplan 使用其具体版本规格。
- **可选文本**　`Trioplan 100mm f/2.8，主体清楚，失焦背景亮点呈明亮圆环，defocused background highlights with bright ring outlines and hollow centers`。
- **来源与核对**　厂家产品与技术表，2026-11-17。[Trioplan 100 f2.8 II](https://www.meyer-optik-goerlitz.com/en/lenses/trioplan-100-f2.8-ii)

## 变形宽银幕与特殊镜头

<a id="lens-panavision-c"></a>
### Panavision C Series

- **稳定 ID 与别名**　`lens-panavision-c`，C-Series，C Series Anamorphic。
- **资料事实**　经典 2× 变形宽银幕系列。厂家描述其渐进景深、明显的变形镜头眩光和富有特点的焦外。不同焦距与版本的最大 T 值各异。
- **画面用途**　具有椭圆失焦高光、选择性水平眩光和层次感的宽银幕画面。
- **需要落实**　有效拍摄区域、解压倍率、焦距、背景光点、强光方向和允许的边缘行为。
- **误用检查**　先保证人物在最终解压画面中的比例。需要水平眩光时保留明确的强光来源。
- **可选文本**　`Panavision C Series anamorphic，主体自然，背景高光呈竖向椭圆，入镜强光形成受控水平眩光`。
- **来源与核对**　厂家产品与光学历史，2026-11-17。[C Series](https://www.panavision.com/camera-and-optics/optics/product-detail/c-c-series)、[Panavision 光学历史](https://www.panavision.com/highlights/highlights-detail/celebrating-70-years-of-optical-innovation)

<a id="lens-ultra-panavision70"></a>
### Ultra Panavision 70

- **稳定 ID 与别名**　`lens-ultra-panavision70`，Ultra Panavision，历史语境中的 APO Panatar。
- **资料事实**　Panavision 历史文章将 APO Panatar 棱镜及柱面版本记为 1.25×，与 MGM Camera 65 / Ultra Panavision 70 历史系统关联。现行 Ultra Panavision 70 产品页标示 1.3×。引用数字时同时保留具体来源与版本语境。
- **画面用途**　大画幅宽银幕、椭圆焦外、渐进失焦与古典柔顺质地。
- **需要落实**　历史系统或当前产品、有效区域、具体镜头、解压与裁切。最终宽高比依据完整流程确定。
- **误用检查**　Ultra Vista、Super Panavision 与 Ultra Panavision 分别识别。历史电影中的镜头与当前库存逐项核对。
- **可选文本**　`Ultra Panavision 70 摄影语境，宽阔横向构图，人物比例自然，背景有轻微椭圆焦外与柔顺焦点过渡`。
- **来源与核对**　厂家产品与光学历史，2026-11-17。[现行产品页](https://en-gb.panavision.com/camera-and-optics/optics/product-detail/ultra-panavision-70)、[历史光学系统](https://www.panavision.com/highlights/highlights-detail/celebrating-70-years-of-optical-innovation)

<a id="lens-atlas-orion"></a>
### Atlas Orion Series

- **稳定 ID 与别名**　`lens-atlas-orion`，Orion 2×，Atlas Orion Anamorphic。
- **资料事实**　前组 2× 变形宽银幕定焦系列。厂家提供 PL 及 EF 适配说明，并描述开放光圈下的球差光晕与受控眩光。具体型号最大 T 值不同。
- **画面用途**　复古变形宽银幕语境，椭圆失焦光点、选择性水平眩光和开放光圈的柔顺亮部。
- **需要落实**　具体焦距、T 值、有效画幅与覆盖。使用扩展附件时按该附件资料更新像场和曝光条件。
- **误用检查**　Orion 与 Orion Silver Edition 分别核对。系列主页面中的通用描述按所选型号裁剪。
- **可选文本**　`Atlas Orion 2x anamorphic，人物面部清楚，背景椭圆焦外，现有强光产生克制的水平眩光`。
- **来源与核对**　厂家产品与规格表，英文页超时后核对厂家西文页，2026-11-17。[Atlas Orion](https://atlaslensco.com/products/orion-series-anamorphic-lenses)、[已核对页面](https://atlaslensco.com/es/products/orion-series-anamorphic-lenses)

<a id="lens-laowa24-probe"></a>
### Laowa 24mm f/14 2X Macro Probe

- **稳定 ID 与别名**　`lens-laowa24-probe`，Laowa Probe，老蛙 24mm 探针镜头。
- **资料事实**　全画幅 24mm 手动微距镜头，最大光圈 f/14，最大放大倍率 2×，最短工作距离约 20mm。厂家将其定义为能交代环境的广角微距视角。
- **画面用途**　食物、器物或小生物的低机位极近景，同时保留周围环境的尺度线索。
- **需要落实**　小主体实际尺度、工作距离、清晰平面、机位高度与足够照明。照明继续遵循当前场景授权。
- **误用检查**　f/14 按原型号记录。近摄时仍需安排有限景深、背景辨识程度与焦点落点。
- **可选文本**　`Laowa 24mm f/14 Probe，贴近小物件的低机位广角微距，前方细节清楚，周围环境形成可读的微观空间`。
- **来源与核对**　厂家产品与技术表，2026-11-17。[Laowa 24mm f/14 Probe](https://www.venuslens.net/product/laowa-24mm-f-14-2x-macro-probe/)

## 胶片与印片外观

<a id="media-kodak-5219"></a>
### Kodak VISION3 500T 5219/7219

- **稳定 ID 与别名**　`media-kodak-5219`，5219，7219，VISION3 500T。
- **资料事实**　500 速度钨丝灯平衡彩色电影负片。厂家强调低照度用途、暗部颗粒控制与高光宽容度，并给出日光使用的色温转换滤镜建议。
- **画面用途**　现有光源夜景、室内混合光和需要可见但克制颗粒的负片外观。
- **需要落实**　35mm 或 16mm 等具体记录格式、曝光、白平衡与扫描或最终调色目标。
- **误用检查**　颗粒尺度随记录格式、曝光和后续流程描述。卤光强度以实际需求单独设置。
- **可选文本**　`Kodak VISION3 500T 负片外观，细微可见颗粒，夜景暗部保留层次，强高光柔顺过渡`。
- **来源与核对**　厂家产品资料，2026-11-17。[Kodak VISION3 500T](https://www.kodak.com/en/motion/product/camera-films/500t-5219-7219/features/)

<a id="media-kodak-5213"></a>
### Kodak VISION3 200T 5213/7213

- **稳定 ID 与别名**　`media-kodak-5213`，5213，7213，VISION3 200T。
- **资料事实**　200 速度钨丝灯平衡彩色电影负片。厂家描述其细腻影像结构，并将受控钨丝灯摄影列为主要适用条件。
- **画面用途**　照明充足的室内人物、窗光与室内光的受控混合，以及细腻负片质地。
- **需要落实**　现有光源色温、白平衡、曝光与颗粒强度。日光使用时记录希望保留或修正的冷暖关系。
- **误用检查**　最终画面暖度通过光源和色彩处理落实。库存与供应情况在真实采购任务中即时查证。
- **可选文本**　`Kodak VISION3 200T 负片外观，颗粒细腻，室内光线层次清楚，皮肤色阶平顺`。
- **来源与核对**　厂家产品资料，2026-11-17。[Kodak VISION3 200T](https://www.kodak.com/en/motion/product/camera-films/200t-5213-7213/features/)

<a id="media-kodak-5203"></a>
### Kodak VISION3 50D 5203/7203

- **稳定 ID 与别名**　`media-kodak-5203`，5203，7203，VISION3 50D。
- **资料事实**　低感光度日光平衡彩色电影负片。厂家强调细颗粒、日光高反差条件下的色彩细节与高光宽容度。
- **画面用途**　明亮外景、阳光下的皮肤与环境细节，以及细腻洁净的胶片质地。
- **需要落实**　日光条件、曝光、记录格式与最终反差。用户指定日间洁净感时让颗粒保持细微。
- **误用检查**　根据光线选择白平衡与颗粒外观。夜间使用的真实曝光可行性按具体摄影条件核对。
- **可选文本**　`Kodak VISION3 50D 负片外观，明亮自然日光，极细微颗粒，肤色与叶片细节清楚，高光保留层次`。
- **来源与核对**　厂家产品资料，2026-11-17。[Kodak VISION3 50D](https://www.kodak.com/en/motion/product/camera-films/50d-5203-7203/features/)

<a id="media-kodak-2383"></a>
### Kodak VISION Color Print Film 2383/3383

- **稳定 ID 与别名**　`media-kodak-2383`，Kodak 2383，2383 print emulation。
- **资料事实**　彩色电影拷贝片，承担印片与放映链路中的成像。厂家描述浓郁黑位与中性高光。
- **画面用途**　作为最终色彩处理中的印片外观，为黑位密度、亮部与色彩关系提供参照。
- **需要落实**　输入素材的色彩与曝光、印片外观强度，以及需要保留的暗部细节。
- **误用检查**　拍摄记录介质沿用摄影机或负片设定，2383 写在印片外观或后期处理位置。具体 LUT 的表现按其制作者与色彩管理流程核对。
- **可选文本**　`Kodak 2383 print emulation，浓郁但有层次的黑位，中性高光，整体反差依据当前场景控制`。
- **来源与核对**　厂家产品与技术文档，2026-11-17。[Kodak 2383/3383](https://www.kodak.com/en/motion/product/post/print-films/vision-color-2383-3383/resources/)

<a id="media-cinestill-800t"></a>
### CineStill 800T

- **稳定 ID 与别名**　`media-cinestill-800t`，800Tungsten，CineStill 800 Tungsten。
- **资料事实**　面向静态摄影、兼容 C-41 流程的钨丝灯平衡彩色负片。厂家说明其采用无 rem-jet 设计，并描述暗背景中强高光边缘的红色卤光。
- **画面用途**　夜间街灯、橱窗和暗背景强光点周围的局部红色光晕，可用于用户明确需要的静态摄影外观。
- **需要落实**　场景中真实存在的强高光、暗亮交界、色温与卤光强度。面部和重要物件保留所需细节。
- **误用检查**　电影负片、扩散滤镜与此类静态摄影卤光各用对应资料。红色光晕的范围沿高光边界安排。
- **可选文本**　`CineStill 800T 静态摄影外观，夜景现有强亮点边缘带细微红色卤光，subtle red halation around intense highlights`。
- **来源与核对**　厂家 FAQ 与使用说明，2026-11-17。[CineStill FAQ](https://cinestillfilm.com/pages/frequently-asked-questions)、[800T 使用说明](https://cinestillfilm.com/blogs/news/cinestill-800t-in-your-toolbox)

## 扩散滤镜

<a id="filter-black-pro-mist"></a>
### Tiffen Black Pro-Mist

- **稳定 ID 与别名**　`filter-black-pro-mist`，Black Pro Mist，BPM，黑柔。
- **资料事实**　光学扩散滤镜系列。厂家说明其降低高光与反差、柔化细部并在光源周围产生扩散，且滤镜强度提高时溢光更明显。
- **画面用途**　削弱数字锐利感、适度柔化皮肤与灯光，同时保留需要辨识的面部结构。
- **需要落实**　用户指定的滤镜档位、光源大小与亮度、焦距、景别及扩散范围。缺少具体档位时以画面效果和强度表达。
- **误用检查**　滤镜扩散、介质卤光与天气雾分别描述。当前场景允许的光源继续提供扩散动机。
- **可选文本**　`轻度 Black Pro-Mist 扩散，强光边缘柔和溢出，局部反差略降，眼睛和面部轮廓清楚，肤质自然`。
- **来源与核对**　厂家产品资料，2026-11-17。[Tiffen Black Pro-Mist](https://tiffen.com/collections/shop-all/products/black-pro-mist-filter)

## 扩充卡片

新增型号使用稳定 ID，保留厂家原名与常见别名。先核对与本次用途有关的规格和版本，再描述画面目标、必要条件与可选文本。资料尚缺的字段明确写“待核对”，只将已有依据用于具体断言。影片案例按作品和段落记录其证据范围。模型执行反馈需要保留模型版本、输入、画幅、参考和返回结果的上下文。
