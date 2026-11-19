<!--
Copyright (c) 2026 ZY / popopo-99
SPDX-License-Identifier: CC-BY-NC-4.0
-->

# Camera-language text regression

These cases are specifications. CL01–33 originate in P0. P1 refines CL13 to assess the requested short explanation and adds CL34 for the full professional definition. Historical P0 execution records remain intact. The remaining P1 cases extend retrieval and compatibility coverage. Their presence and static validation do not establish executed passes.

Run explicit Skill requests against the current entry and the references each request needs. Keep the previous regression files and their historical results.

For execution, supply only this protocol, the selected case's Setup and User text, and the current Skill. Keep Expected and Failure from the executor until its complete response has been saved. Cases are independent unless a Setup supplies history. Record the actual entry path, references read, complete unedited response, and any unavailable prerequisite. Library retrieval cases also require the actual index/detail read trace and resolved stable ID.

Review complete relationships, state transitions, source scope, and output format. A pass satisfies the case's requirements without a conflicting action. A partial has a specific omission or ambiguity. A fail violates a core requirement. Mark an unexecuted case pending. Term counts, keyword hits, and an executor's satisfaction are insufficient evidence. These cases assess text design. Generated-image fidelity and video-model execution require separate evidence.

## CL01 — Near-ground colloquial camera request

**User**

```text
请使用本Skill。巷子里一个人站在我面前，镜头贴着地，人显得很有压迫感。给中文模型中立提示词，其他你选。
```

**Expected**

- Places the viewpoint near the ground and states a plausible viewing direction toward the person. Uses distance, subject scale, and surrounding space to make the pressure readable.
- Retains the person and alley. Any focal choice serves the intended result and remains an OPEN choice. Proceeds with a prompt using the supplied permission to choose.

**Failure**

- Changes to eye level or an unrelated overhead composition, substitutes a brand for spatial decisions, or blocks on a novice/expert selection.

## CL02 — Expert parameters and format scope

**User**

```text
请使用本Skill。室内两人对话，ARRI ALEXA 35，Cooke S4/i 50mm T2.0，中近景，越肩。给一条中文模型中立提示词，机位与站位的开放细节你选。
```

**Expected**

- Preserves every supplied equipment value, the T notation, the medium-close framing, and the over-shoulder relationship.
- Uses a compatible Super 35 context. Leaves an unspecified capture mode/crop unresolved or clearly provisional. Keeps actual focal length, effective image area, and delivery ratio conceptually separate.
- Describes the near shoulder, dialogue subject, and clear focal target consistently with the framing.

**Failure**

- Replaces 50mm or T2.0 with a default, relabels T as f, assumes a full-frame mode, or computes equivalence from a delivery ratio alone.

## CL03 — Fixed position with rightward pan

**User**

```text
请使用本Skill。镜头不动，向右摇镜。用一句话把这个拍法说清楚。
```

**Expected**

- Resolves the colloquial request as a rightward Pan with camera position maintained and viewing direction rotated. Gives the requested concise explanation.

**Failure**

- Describes a rightward translating camera, a zoom, or a fully frozen orientation while claiming the pan occurs.

## CL04 — Dolly Zoom intent in a still

**User**

```text
请使用本Skill。走廊中央站着一个人，人物不变大，背景改变透视。我要一张静态图，只写中文模型中立提示词，必要时加一句最短说明。
```

**Expected**

- Recognizes the likely Dolly Zoom intent and limits the still to one chosen spatial/framing state or a suggested effect.
- Preserves the central person and corridor. Any explanation distinguishes a single image from the temporal change needed to demonstrate constant subject size across changing perspective.

**Failure**

- Claims the single still completes a five-second Dolly Zoom, combines incompatible before/after positions in one frame, or attributes a perspective change to focal-length change alone at a fixed viewpoint.

## CL05 — Dolly Zoom intent for a video instruction

**User**

```text
请使用本Skill。走廊中央站着一个人，人物不变大，背景改变透视。我要5秒视频的摄影运动说明，先给文本，不要调用工具。
```

**Expected**

- Describes coordinated camera translation and compensating focal-length change to maintain subject size while background perspective changes.
- Treats this as temporal instruction. Keeps any video-model execution claim dependent on actual supported capability and evidence.

**Failure**

- Supplies a fixed-viewpoint zoom as the whole mechanism, guarantees execution by an unspecified model, or silently creates a video-model router.

## CL06 — Fisheye with all straight lines preserved

**User**

```text
请使用本Skill。我要鱼眼，但所有直线都完全笔直。
```

**Expected**

- Identifies the conflict between a conventional curvilinear fisheye projection and preserving every scene straight line in the final image.
- Gives the smallest relevant choice or one focused question, such as retaining the fisheye deformation or selecting a straight-line projection. Keeps the user's intended wide spatial view available for resolution.

**Failure**

- Claims both universal straight-line preservation and conventional fisheye deformation are already satisfied, or rejects every wide-angle projection indiscriminately.

## CL07 — Existing 1917 scene-card research

**User**

```text
请使用本Skill。《1917》德军地下空间用了什么镜头？请按当前库里的来源回答，指出查到的事实和未知部分。
```

**Expected**

- Retrieves `shot-1917-basement` through the current cinema library and reports the source-supported 35mm Signature Prime scene fact.
- Separates the film-wide ALEXA Mini LF / Signature Prime production record and approximate 40mm prevalence from this scene's 35mm record. Keeps aperture, subject distance, and exact body allocation unknown.
- Attributes the historical statement to the existing production interview and keeps creative migration suggestions separate.

**Failure**

- Answers 40mm using the film-wide majority, invents an aperture or body allocation, treats an uninspected frame as observed, or generalizes this evidence into a director-wide habitual equipment claim.

## CL08 — Accepted appearance with less background blur

**Setup**

```text
同一项目的当前候选为眼平、半身人像、人物眼睛清楚、自然窗光，内部记录58mm与T2.8均为OPEN。用户只看到了画面，未见机身、镜头、焦距或光圈记录。其认可范围为当前人物、衣服、构图、光线与眼睛清晰的外观。此处提供的是文字状态，执行者没有待检查的图片。
```

**User**

```text
这张图不错，只让背景少虚一点。给我修改用的中文模型中立提示词，再简短说明哪些接受范围和参数状态继续沿用。
```

**Expected**

- Changes background clarity while preserving the accepted visible result. May adjust necessary OPEN aperture/focus dependencies without treating the unseen parameters as user choices.
- Records the revised candidate consistently and keeps original source, acceptance, lock, and scope distinctions. Describes a text edit with image inspection unavailable in this fixture.

**Failure**

- Promotes all hidden equipment values to USER-LOCKED because of overall praise, redesigns the person/light/viewpoint to reduce blur, or claims actual image inspection or repair completion.

## CL09 — Prompt-only permission to choose

**User**

```text
请使用本Skill。白天，一个邮递员在普通住宅门口把一封信递给住户。只给我提示词，其他你选。
```

**Expected**

- Returns a directly usable ordinary Chinese model-neutral prompt and resolves necessary open choices within the scene.
- Keeps the letter handoff and ordinary daytime location physically coherent.

**Failure**

- Adds a teaching table, mode menu, JSON payload, model questionnaire, or mandatory equipment selection before the prompt.

## CL10 — Fisheye-style perspective in illustration

**User**

```text
请使用本Skill。插画主体做鱼眼式透视。主体是一位骑车经过拱门的邮递员，保留纸本水彩、纸纹和手绘边缘。只给中文模型中立提示词。
```

**Expected**

- Keeps paper watercolor, pigment/paper behavior, and drawn edges as the Primary Medium making logic.
- Applies the requested curved wide spatial construction to the archway and surrounding space while keeping the cyclist's action readable.

**Failure**

- Converts the scene to live-action photography, replaces paper behavior with photographic skin/capture texture, or adds camera hardware solely because the word fisheye appears.

## CL11 — Fisheye dictionary route

**User**

```text
从本Skill当前摄影词典检索“鱼眼 / Fisheye”。简短给出稳定ID、分类、可见结果和一句静帧用法。
```

**Expected**

- Reads the index and `term-fisheye` detail card. Resolves it to Optical Lens & Projection and explains curvilinear projection with scope for center/edge placement.
- The still example expresses observable geometry with an appropriate projection assumption.

**Failure**

- Resolves a different ID, equates every ultra-wide view with fisheye, or supplies an unsupported exact product as required equipment.

## CL12 — Wide-angle at a fixed viewpoint

**User**

```text
从本Skill当前摄影词典检索“广角 / Wide-angle”。给稳定ID，再解释机位不变时换更广的镜头会怎样，并给一句静帧用法。
```

**Expected**

- Reads `term-wide-angle`, identifies the wider field of view for a given format, and keeps viewpoint-dependent perspective distinct from focal-length-dependent framing.
- Gives a coherent view showing more surroundings. Describes any close-distance perspective emphasis with the corresponding camera position.

**Failure**

- Claims focal length alone changes perspective with the viewpoint fixed or requires fisheye curvature for an ordinary wide-angle view.

## CL13 — Telephoto and distance relationships

**User**

```text
从本Skill当前摄影词典检索“长焦 / Telephoto”。给稳定ID，简短解释“背景压缩”需要哪些机位条件，再给一句静帧用法。
```

**Expected**

- Reads `term-telephoto` and gives a concise explanation focused on the requested compression conditions. A full optical definition is optional for this short question.
- Connects comparable framing at greater camera distance with the apparent compression of depth. The example makes camera distance and subject/background relationships clear.

**Failure**

- Promises compression from focal length alone at an unchanged viewpoint, gives a universal millimeter threshold independent of format, or equates long focal length with guaranteed shallow depth of field.

## CL14 — Close-up as framing

**User**

```text
从本Skill当前摄影词典检索“特写 / Close-up”。给稳定ID和分类，解释它如何落实到人物手中一枚钥匙的静帧。
```

**Expected**

- Reads `term-close-up`, classifies it under Framing & Shot Size, and makes the key and relevant hand contact dominate the frame.
- Keeps the focal length and camera distance subject to the intended framing and physical scene.

**Failure**

- Defines close-up as a required optical lens family, guarantees a fixed focal length, or omits the requested key/hand relationship.

## CL15 — Low Angle and height versus orientation

**User**

```text
从本Skill当前摄影词典检索“仰拍 / Low Angle”。给稳定ID，解释“低机位平拍”和“低机位向上看”的区别，各用一句普通话。
```

**Expected**

- Reads `term-low-angle` and identifies Camera Position & Orientation.
- Separately describes near-ground/low camera height and upward viewing direction. The two examples make the differing orientation observable.

**Failure**

- Treats low camera height as proof of upward tilt or substitutes a wide-angle lens for the requested orientation distinction.

## CL16 — Dolly In and a single frame

**User**

```text
从本Skill当前摄影词典检索“推进 / Dolly In”。给稳定ID，解释这个运动，再给一条适合单张图片的表达。
```

**Expected**

- Reads `term-dolly-in`, identifies forward camera translation, and describes the resulting changing viewpoint over time.
- The still example chooses a reached position, framing state, or suggestive action/spatial cue and states the temporal limit when needed.

**Failure**

- Substitutes a fixed-position zoom for translation or says the single still proves completion of an actual timed camera move.

## CL17 — Pan dictionary route

**User**

```text
从本Skill当前摄影词典检索“摇摄 / Pan”。给稳定ID，解释摄影机的位置与朝向分别如何变化。
```

**Expected**

- Reads `term-pan`, retains the camera pivot position, and describes horizontal rotation of the viewing direction over time.
- Treats a single still as at most a selected orientation or suggested motion cue.

**Failure**

- Moves the camera bodily sideways or changes focal length as the defining pan action.

## CL18 — Zoom dictionary route

**User**

```text
从本Skill当前摄影词典检索“变焦 / Zoom”。给稳定ID，解释摄影机固定位置时的变化，并说明单张图能证明什么。
```

**Expected**

- Reads `term-zoom` and explains changing focal length / angle of view at a maintained camera position.
- Keeps perspective tied to viewpoint and limits the still to one framing state or suggestive evidence.

**Failure**

- Describes physical forward motion as required zoom behavior or certifies a temporal focal-length change from one static frame.

## CL19 — Rack Focus dictionary route

**User**

```text
从本Skill当前摄影词典检索“焦点转移 / Rack Focus”。给稳定ID。前景钥匙与后景人脸之间转焦，单张图和连续画面分别怎样描述？
```

**Expected**

- Reads `term-rack-focus` under Focus & Image Behavior and explains temporal change of the focus plane/target.
- A still chooses which target is currently sharp, with the other plane's clarity stated. A sequence can specify the direction and order of focus transfer.

**Failure**

- Claims one still completes both ordered focus states or uses camera translation/zoom as the definition of rack focus.

## CL20 — Swirly Bokeh scope

**User**

```text
从本Skill当前摄影词典检索“旋焦 / Swirly Bokeh”。给稳定ID和实现条件。人物脸要清楚，树林只在外围失焦背景产生轻微环绕趋势。
```

**Expected**

- Reads `term-swirly-bokeh`, classifies the effect under Focus & Image Behavior, and places the swirl in the out-of-focus peripheral background.
- Mentions useful scene/focus conditions and preserves the face and physical tree geometry. Any equipment connection stays within existing evidence.

**Failure**

- Applies global rotational motion blur to the person and trees, promises the effect from a model name alone, or invents a required equipment card.

## CL21 — Simultaneous Locked-off and Truck

**User**

```text
请使用Prompt Check，先检查不要改写。视频0到5秒同一时间段：Locked-off，摄影机位置与朝向始终固定；同时摄影机向右Truck两米。其余场景已定。
```

**Expected**

- Marks a CONFLICT tied to the same camera, same interval, and incompatible position requirements.
- Keeps inspection scope and identifies the smallest temporal or movement decision needed for resolution.

**Failure**

- Declares simultaneous fixed position and two-meter translation compatible, gives only a keyword-count warning, or silently rewrites the prompt.

## CL22 — Sequential Locked-off then Truck

**User**

```text
请使用Prompt Check，先检查不要改写。视频0到2秒Locked-off，位置与朝向固定；2到5秒解除固定，摄影机向右Truck两米。两个阶段按顺序发生。
```

**Expected**

- Accepts the temporal compatibility of the two phases and preserves their explicit order.
- Can flag a genuinely unspecified transition detail as WEAK/RISK with its scope, while keeping the described sequence valid.

**Failure**

- Reports a fixed/Truck contradiction solely because both phrases occur anywhere in the prompt or merges the two phases into one simultaneous interval.

## CL23 — Fixed tripod pivot with Pan

**User**

```text
请使用Prompt Check，先检查不要改写。摄影机安装在位置固定的三脚架上，云台向右Pan，摄影机的支点不平移，朝向可以转动。
```

**Expected**

- Treats the fixed support position and permitted pan rotation as compatible. Explains the position/orientation distinction if clarification is useful.

**Failure**

- Equates the fixed tripod position with a locked viewing direction or diagnoses a Truck movement.

## CL24 — Fisheye with a line through image center

**User**

```text
请使用Prompt Check，先检查不要改写。使用常规旋转对称的等距鱼眼投影，让穿过成像中心的一条场景直线保持直；其他离轴建筑线条允许弯曲。
```

**Expected**

- Evaluates the stated projection and line position. Accepts that a scene line whose projection passes through the center can remain straight while other lines curve.

**Failure**

- Reports an inevitable conflict from the co-occurrence of fisheye and straight or expands the single-line constraint into preservation of all straight lines.

## CL25 — Rectilinear ultra-wide projection

**User**

```text
请使用Prompt Check，先检查不要改写。普通超广角，直线投影rectilinear，建筑直线保持笔直；允许边缘物体因广视角出现拉伸。
```

**Expected**

- Accepts the requested straight-line projection with potential peripheral stretching and keeps projection behavior distinct from scene perspective.

**Failure**

- Requires curved lines from the ultra-wide term alone, treats peripheral stretching as proof of fisheye, or rewrites the projection without authorization.

## CL26 — Ordinary text by default

**User**

```text
请使用本Skill。自然窗光下，一位修表师在木桌前看一枚怀表，近景，眼睛和表盘清楚。用Cooke S4/i 50mm的摄影语境，给中文模型中立提示词。
```

**Expected**

- Delivers ordinary Chinese prompt text with the specified subject, action, focal targets, light, and equipment context.
- Integrates relevant visual relationships while keeping internal capture records separate from the requested prompt.

**Failure**

- Automatically exports JSON, a capture schema, research ledger, or parameter table because equipment was named.

## CL27 — Explicit raw JSON with an existing schema

**Setup**

```text
当前用户认可的schema及候选值为：
{"scene":{"subject":"修表师","action":"看怀表","place":"窗边木桌"},"capture":{"camera":"ARRI ALEXA 35","lens":"Cooke S4/i 50mm","aperture":"T2.0","viewpoint":"眼平近景","focus":"眼睛与表盘清楚"},"delivery":{"aspect_ratio":"2:3"}}
这份schema的键与层级属于本次用户要求，候选值的来源与原有状态继续沿用。
```

**User**

```text
沿用这个schema和当前摄影选择，导出完整有效的原始JSON。只要JSON对象。
```

**Expected**

- Returns one parseable JSON object with the supplied keys and hierarchy, retaining the values and T notation.
- Keeps capture under the existing schema and preserves the 2:3 delivery intent.

**Failure**

- Adds a preface/code fence, replaces the schema, introduces a second capture state, changes parameters, or inserts invented API controls.

## CL28 — OPEN candidate continuity through transcode

**Setup**

```text
当前模型中立Scene Master只有一份。画面为自然窗光下的半身人像，眼平观察、58mm、T2.8、眼睛清楚、外围树叶轻微旋焦，交付2:3。人物穿蓝衬衫是USER-LOCKED。摄影参数和机位是正在使用的OPEN候选，未被用户逐项接受。只有提示词，没有生成图。
```

**User**

```text
把当前方案转成Seedream 5.5。先给提示词，再用一句话说明候选与结果状态。
```

**Expected**

- Compiles through the selected adapter while retaining the current 58mm, T2.8, eye-level view, focus, swirl scope, source light, blue shirt, and 2:3 ratio.
- Keeps OPEN candidate status and prompt-only execution status. Uses the same Scene Master as the basis.

**Failure**

- Recommends a new default focal length during transcoding, promotes candidates to accepted/locked, copies another adapter's incompatible syntax, or claims a generated result.

## CL29 — Current candidate and scoped acceptance in handoff

**Setup**

```text
旧候选85mm和暖黄灯光已被用户明确拒绝。当前有效候选为58mm、自然窗光、蓝衬衫、半身眼平，摄影参数仍为OPEN。用户只认可了当前人物、衣服、构图与自然窗光的外观，未见隐藏的器材参数。最新修改已经让背景稍清楚，清晰关系以这个版本为准。只有文字记录。
```

**User**

```text
整理简短项目交接摘要，让下次继续当前版本。
```

**Expected**

- Carries forward the active 58mm candidate, revised background clarity, cumulative current state, and the stated acceptance scope.
- Preserves OPEN status for unseen equipment choices and the rejected status of the superseded proposal. Records available evidence as text.

**Failure**

- Restores 85mm or warm light, marks every internal parameter USER-LOCKED, loses the latest clarity edit, or claims a stored/inspected image.

## CL30 — Favourite evidence and creative migration

**User**

```text
请使用本Skill。查当前《宠儿》宫廷室内场景卡，告诉我这场到底用了哪枚镜头，再给我一个可迁移到现代市政大厅群像的方法。只依据现有来源。
```

**Expected**

- Reads `shot-favourite-room` and distinguishes production-wide 6mm fisheye / Primo availability from the unknown exact focal length, aperture, and camera height of an individual room image.
- Transfers a source-supported spatial/group-power method into the requested modern hall, with new decisions presented as creative choices.

**Failure**

- Assigns 6mm to every room image, invents per-shot settings, claims direct frame observation from the interview alone, or imports the film's cast/costume/plot into the new scene.

## CL31 — Retained locked procedural gesture

**User**

```text
请使用本Skill。正面桌边平视，女维修员右手握黄铜钥匙，正插入锁孔。室内唯一顶灯。动作、机位、光源和钥匙锁定，强烈参考芬奇，只给中文模型中立Prompt。
```

**Expected**

- Retains the right-handed insertion, brass key, front eye-level observation, and sole ceiling source. Makes hand/key/lock contact readable.
- Applies compatible director treatment within open choices and returns only the requested prompt.

**Failure**

- Adds window/task lighting, changes insertion into turning/withdrawal, moves the viewpoint to satisfy style, or adds an unsolicited capture table.

## CL32 — Retained paper medium and action relationships

**User**

```text
请使用本Skill。一段童话：纸做的小狐狸把一片叶子举在头顶，跑过雨中的纸桥，桥另一端的纸兔子撑着一把小伞等它。做成一张剪纸拼贴插画，保留纸边、折痕和手工搭建感。只给中文模型中立Prompt。
```

**Expected**

- Retains the leaf-overhead running action, paper bridge, waiting rabbit at the other end, umbrella, paper edges, folds, and layered handmade construction.
- Uses the authorized medium's viewpoint and material language while maintaining the requested prompt-only scope.

**Failure**

- Converts to live-action/camera-equipment rendering, loses the action or spatial relation, or claims to have inspected an absent reference image.

## CL33 — Physically incompatible expert format request

**User**

```text
请使用本Skill做实拍摄影方案。我锁定ARRI ALEXA 35机身、Cooke S4/i S35 50mm T2.0，同时要求机身内部切换到36×24mm全画幅原生采集，任何裁切、拼接、换机或外接记录都不接受。先判断这些条件能否一起成立。
```

**Expected**

- Identifies the body's Super 35 image-area constraint and the requested unsupported native 36×24mm capture conflict.
- Preserves the explicit requested values while explaining the incompatibility and offering a focused decision if further planning needs a change. Keeps physical camera matching separate from image-prompt capability.

**Failure**

- Certifies a nonexistent native full-frame mode, silently substitutes an LF body/other lens, or treats delivery aspect ratio as proof of physical sensor dimensions.

## CL34 — Full professional telephoto definition

**User**

```text
从当前词典检索长焦，给稳定ID和完整专业定义。解释有效画幅、焦距、视角、后退机位与背景压缩的关系，也说清楚景深的条件。不要生成图片。
```

**Expected**

- Reads `term-telephoto`, defines the longer-focal-length/narrower-angle relationship relative to the effective image format, and distinguishes focal-length usage from the strict optical telephoto construction when relevant.
- Attributes perspective compression to viewpoint/distance in comparable framing, and explains that depth of field also depends on aperture, focus distance and framing conditions.

**Failure**

- Uses a universal format-independent focal threshold, attributes perspective change to focal length at fixed viewpoint, or guarantees shallow depth of field.

## CL35 — Rectilinear ultra-wide

**User**

```text
我想把人在大堂里显得很小，环境特别开阔，但柱子线条保持笔直。用词典解释该选哪种广角，给稳定ID和一条中文模型中立静帧提示词，其他你选。
```

**Expected**

- Retrieves a rectilinear wide/ultra-wide entry and protects straight-line projection while allowing perspective convergence.
- Makes the person's scale and environment readable without silently switching to fisheye curvature.

**Failure**

- Requires fisheye for all ultra-wide shots or equates straight lines with parallel verticals at every tilt angle.

## CL36 — Optical tilt, shift and camera tilt

**User**

```text
请从词典分别检索光学Tilt、光学Shift和摄影机Tilt，给三个稳定ID和各一句区别。我不要把所有移轴都解释成小人国。
```

**Expected**

- Separates lens tilt/focus-plane orientation, lens shift/framing within the image circle, and camera pitch rotation over time.
- Keeps miniature appearance conditional and distinguishes static lens settings from temporal camera rotation.

**Failure**

- Conflates the three operations or guarantees miniature appearance from shift alone.

## CL37 — Macro and equipment chain

**User**

```text
一枚戒指放在旧木桌上，我想非常近地看清划痕，同时看见一点桌面环境。查词典里的微距和适合的现有器材，给ID、条件及一句静帧用法。有电影案例再给，没有就留空。
```

**Expected**

- Retrieves `term-macro`, relates image magnification, working distance and finite close-focus depth of field, and can select `lens-laowa24-probe` with its actual conditions.
- Gives only evidence-supported film links or explicitly leaves the gap.

**Failure**

- Equates any detail crop with true macro, promises unlimited depth of field, invents a movie credit or changes the product aperture spec.

## CL38 — Framing family

**User**

```text
用同一个西部牛仔解释远景、全景、中景、中近景、特写、大特写、牛仔景别。按当前词典给ID和能看见身体哪些部分，不要给固定焦距。
```

**Expected**

- Retrieves the seven framing entries, uses readable body/environment proportions, and keeps conventional boundaries flexible.
- Explains the cowboy framing around the thigh/holster region without binding a shot size to a focal length.

**Failure**

- Treats shot size as a lens type or supplies mandatory focal lengths.

## CL39 — Height and static orientation

**User**

```text
词典里的眼平、俯拍、顶视、荷兰角各是什么？给ID。高处向前平看能不能算俯拍？歪一点的照片能证明镜头滚转了吗？简短回答。
```

**Expected**

- Distinguishes height from downward orientation and Dutch-angle state from proof of a roll movement.
- Retrieves the four relevant IDs and keeps the explanation concise.

**Failure**

- Equates every high position with high-angle shooting or treats a tilted horizon as proof of temporal roll.

## CL40 — POV versus over-shoulder

**User**

```text
同一个人从门外看屋里的人，主观视点和越肩有什么区别？给词典ID和各一句模型中立静帧用法。人物、门和房间沿用这个设定。
```

**Expected**

- Distinguishes the character-aligned viewpoint from seeing the observer's shoulder/head edge, while preserving the supplied space.

**Failure**

- Requires the observer's own shoulder in every POV or changes the scene to illustrate the terms.

## CL41 — Movement axes

**User**

```text
从词典查Dolly Out、Truck、Pedestal、Crane、Orbit和Roll，给稳定ID并用一句话区分运动。单张图能证明哪条轨迹真的发生了吗？
```

**Expected**

- Distinguishes backward travel, lateral translation, camera vertical translation, crane-supported spatial travel, orbit around subject and optical-axis rotation.
- Marks actual trajectories as temporal and avoids asserting an executed move from one frame.

**Failure**

- Treats all elevation as camera tilt or confuses a rolled static frame with proof of roll motion.

## CL42 — Operating style and time scope

**User**

```text
我想先三脚架固定两秒，再手持跟随三秒。按词典解释Locked-off和Handheld，给ID。只评这个方案有没有逻辑冲突，不写视频模型提示词。
```

**Expected**

- Treats locked-off and handheld as operating/stability styles, recognizes non-overlapping intervals and retains the plan's sequence.
- Does not certify target-model video execution.

**Failure**

- Labels handheld a unique movement trajectory or flags sequential support styles as simultaneous conflict.

## CL43 — Depth of field colloquial goal

**User**

```text
我不懂参数。我想前面的手、站在中间的人、后面的门都能看清。用一句容易懂的话解释怎么做，再给中文模型中立静帧提示词，具体器材你选。
```

**Expected**

- Maps the request to multiple required readable planes, chooses coherent open focus/distance/aperture conditions and explains the visible reason briefly.
- Keeps one scene and does not require a beginner/expert choice.

**Failure**

- Promises every distance is infinitely sharp or blocks on a mode choice.

## CL44 — Bokeh, diffusion, flare and halation

**User**

```text
从词典查Bokeh、Diffusion、Lens Flare、Halation，给各自ID和产生条件。黑柔、CineStill 800T和变形镜头能不能当成同一种东西？只做解释。
```

**Expected**

- Separates out-of-focus rendering, optical diffusion, lens stray light/flare and medium-related halation.
- Preserves the still-photo scope of CineStill 800T, links equipment only within each card's evidence range, and avoids adding weather.

**Failure**

- Treats all glowing effects as interchangeable or presents CineStill as a film-production credit.

## CL45 — Composition and medium preservation

**User**

```text
我做木刻插画，人物站在窗边。查词典的中心构图、负空间、框中框、前景遮挡、空间分层、三分构图，给ID和六种可见安排的简短说明，保持木刻媒介。
```

**Expected**

- Retrieves six composition entries and expresses each arrangement in the supplied scene and medium.
- Keeps negative space meaningful, occlusion spatial and layering distinct from compulsory blur.

**Failure**

- Converts the scene to photographic rendering, forces lenses or equates spatial layers with mandatory shallow focus.

## CL46 — Editorial and temporal boundary

**User**

```text
检索插入镜头、正反打、一镜到底、视线匹配、180度轴线原则，给ID和各自用途。单张静帧能证明哪些剪辑关系？不要生成视频。
```

**Expected**

- Retrieves the five temporal/editorial entries, distinguishes insert content from its editing role, and identifies sequence-dependent relations.
- Explains the axis as continuity guidance with deliberate exceptions and long take as a sustained presentation whose physical single-take status needs production evidence.

**Failure**

- Claims a single frame proves shot/reverse-shot, eyeline match, axis compliance across cuts or an actual uncut production take.

## CL47 — Term to sourced film method

**User**

```text
我想做人物贴近镜头、周围危险还能看清的画面。按当前词典到器材库再到电影场景卡查，列出经过的ID和事实范围，最后把可迁移方法用于一个现代消防员进入仓库的静帧。型号你选，别把电影人物带进来。
```

**Expected**

- Retrieves wide-angle principles and relevant equipment and can use `shot-revenant-camp` within its source-confirmed method scope.
- Separates production facts from proposed equipment, retains the firefighter/warehouse and explicitly leaves unsupported per-shot settings unknown.

**Failure**

- Infers a specific camp-shot camera/lens from film-wide records or imports film characters/story.

## CL48 — Director habit scope

**User**

```text
库里《宠儿》用了6mm鱼眼，所以能说兰斯莫斯长期惯用6mm SF6吗？请用当前库回答，再说明我想借这个大房间人物关系时能迁移什么。
```

**Expected**

- Limits the 6mm SF6 fact to the supported production scope, keeps the director and DP's film-specific roles, and identifies the gap in a career-wide assertion.
- Transfers spatial/power relationships without fabricating a specific room shot's exact settings.

**Failure**

- Generalizes the director's long-term equipment habit from one film or identifies every palace room frame as 6mm.

## CL49 — Equipment appearance and modified versions

**User**

```text
画面有椭圆散景就能确定是Atlas Orion吗？《新蝙蝠侠》追车用了Helios，是否证明普通Helios 44-2都原生有椭圆散景？用现有库和词典回答，给来源范围。
```

**Expected**

- Treats visible bokeh shape as observation and keeps true equipment identification source-dependent.
- Separates film-modified Helios/Jupiter oval-iris versions from the stock 44-2 card and distinguishes Atlas production use from any particular frame.

**Failure**

- Certifies equipment from appearance or transfers the modified aperture construction to every stock Helios.

## CL50 — Empty associations

**User**

```text
查光学Shift，给词典ID和关联器材、电影ID。当前库没有就写空，仍然解释如何用于高楼静帧，不要补造型号或拍摄记录。
```

**Expected**

- Retrieves `term-optical-shift`, reports actual empty associations faithfully and gives a current creative method with vertical alignment and framing conditions.

**Failure**

- Fabricates a library ID, movie credit or guaranteed correction independent of camera orientation/image-circle limits.

## CL51 — Prompt Check temporal logic

**User**

```text
只检查这段，不重写。0到2秒Locked-off；2到5秒绕人物Orbit；5到7秒停下。摄影机始终保持同一空间位置，人物也不动。目标模型未知。
```

**Expected**

- Recognizes the valid sequential operating changes and the actual conflict between orbit and a globally fixed camera position while the person remains stationary.
- Returns findings only and keeps model compatibility unknown.

**Failure**

- Misses the global invariant, flags all sequential transitions as conflict, rewrites the prompt or asks a model question before diagnosis.

## CL52 — Director and expert locks

**User**

```text
用Director思路做库布里克式稳定中心构图。我的场景是现代医院里的护士，Seedream 5.5，21:9，ALEXA 35、Cooke S4/i 50mm T2.0和眼平机位都锁定。只给中文提示词，其他你选。
```

**Expected**

- Uses relevant director grammar, preserves explicit scene/equipment/viewpoint/ratio/model and produces only a plain-text prompt.
- Avoids automatic historical f/0.7 substitution or importing film characters/props.

**Failure**

- Replaces locks based on a movie equipment credit or turns prompt-only into a library lecture/JSON.

## CL53 — Dream Decode authorized medium

**Setup**

```text
用户已提供并锁定文字Decode Card。Primary Medium为木刻版画，粗黑线、平涂、纸面纹理，人物在桥上。只授权迁移负空间和俯视构图，任何摄影器材选择都是OPEN。
```

**User**

```text
沿用这张文字Decode Card，增加广角式空间夸张和前景遮挡。给模型中立普通文本提示词，不改媒介，不需要我再上传图片。
```

**Expected**

- Uses the supplied textual card without claiming image inspection and carries requested geometry/composition through woodcut marks and medium constraints.
- Keeps the bridge/person and does not force a photographic camera body.

**Failure**

- Converts to live-action or claims to infer real source gear from an absent image.

## CL54 — Continuity and faithful transcode

**Setup**

```text
项目当前事实为现代诊所、同一护士、蓝色上衣、21:9。项目锁定ALEXA 35、Cooke S4/i、自然窗光。镜头A当前OPEN候选为50mm T2.8、眼平、中近景、浅景深；用户只在镜头B明确选用顶视和深景深。尚无图像生成。
```

**User**

```text
把镜头A从Seedream 5.5原样转成Nano Banana提示词，再说明镜头B的局部修改会不会改掉A。保留候选和锁定状态的区别。
```

**Expected**

- Preserves A's resolved open values and project locks during conversion and isolates B's shot-specific changes.
- Explains status without promoting candidates to accepted/locked or claiming image results.

**Failure**

- Re-selects open values on transcode, leaks B's top view/deep focus into A or marks ungenerated outputs accepted.

## CL55 — Still dolly zoom and minimal answer

**User**

```text
Seedream 5.5单张图，人在走廊里不变大，背景透视在五秒里变化，想要Dolly Zoom。用两句话说明怎么交付这个要求，先别生成提示词。
```

**Expected**

- Briefly separates a single selected still-state from the time-dependent dolly/zoom coordination, preserving the requested temporal intent for a sequence plan.
- Respects the two-sentence and explanation-only request.

**Failure**

- Claims the five-second process fits a single frame or expands into a model router or full prompt.

## CL56 — Anamorphic aspect ratio and film scope

**User**

```text
我要21:9，所以一定是变形宽银幕拍的对吧？《沙丘》能证明用的是Ultra Panavision 70吗？从词典和当前库回答，给稳定ID和未知范围。
```

**Expected**

- Separates output aspect ratio from anamorphic capture and uses `term-anamorphic` with the film's actual Ultra Vista 1.65×/H Series production scope.
- Keeps Ultra Panavision 70 distinct and leaves unspecified per-shot allocation unknown.

**Failure**

- Infers capture optics from 21:9 or substitutes the wrong Panavision lens family.

## CL57 — Swirly bokeh evidence chain

**User**

```text
查旋焦的术语ID、原理条件、已有器材、电影例子和迁移方法。我想知道哪些是规格、哪些是电影制作记录、哪些是创作建议、哪些真的测过Seedream 5.5。当前没有可靠例子就明确留空。
```

**Expected**

- Separates the Helios manual's specifications, proposed optical effect/conditions and Jury's scoped Seedream 5.0 Pro historical feedback.
- Avoids treating the Batman modified-lens record as proof of observed swirly bokeh or Seedream 5.5 success.

**Failure**

- Upgrades a proposed visual signature to verified manufacturer/film facts or converts 5.0 Pro feedback into 5.5 test evidence.

## CL58 — Short novice answer without mode gate

**User**

```text
人物清楚、后面的山看起来更近更大，要怎么拍？我是小白，三句话以内说原因和建议，不要器材清单，不出提示词。
```

**Expected**

- Explains backing the camera away and using a longer focal length to keep comparable subject scale, with relevant subject/background geometry.
- Fits the requested concise format, focuses on visible change and avoids a mode selection or mandatory equipment catalogue.

**Failure**

- Claims focal length alone changes perspective at fixed position or answers with a full dictionary card instead of the requested short guidance.

## CL59 — Broader focus-pulling wording

**User**

```text
摄影师说这个镜头要pull focus，演员从门口一直走近，眼睛始终清楚。我需要换焦点到背景吗？查当前词典，三句话内解释。
```

**Expected**

- Interprets the supplied goal as continuous focus adjustment to retain the moving actor's eyes, preserving the same attention target.
- Explains the broader usage of pull focus while keeping rack focus between targets distinct.

**Failure**

- Forces a transfer to background solely because of the phrase pull focus.

## CL60 — Axis and take wording boundaries

**User**

```text
查当前词典。导演只说先建立axis of action，是否已经要求所有机位同侧？拍一个两秒的single take就一定是Long Take吗？简短说明。
```

**Expected**

- Separates the spatial relationship/action axis from the continuity principle and avoids importing extra camera-side locks.
- Distinguishes one uninterrupted production take from relatively long screen duration, retaining contextual ambiguity.

**Failure**

- Turns naming an axis into a mandatory same-side lock or equates any single take with a long take.

## CL61 — Novice original fisheye strategy

**Setup**

Seedream 5.5, single 21:9 still, no input image.

**User**

```text
我想拍一张西部雪镇的电影画面，中间站着一个女牛仔，两侧木建筑像用鱼眼看一样明显弯曲。
```

**Expected**

- Compiles an original scene with fisheye projection, off-axis architectural lines and natural central proportions.
- Uses the no-image creation path without requiring a reference image.
- Keeps curvature distinct from blur, swirly bokeh and a dark image border.

**Failure**

- Requires an unnecessary image, substitutes a different optical mechanism or gives only equipment names.

## CL62 — Professional projection and parameter preservation

**Setup**

Seedream 5.5, single 21:9 still, no input image.

**User**

```text
21:9 cinematic still, diagonal fisheye projection, pronounced off-axis curvature, central subject with natural proportions, rectilinear architecture rendered through fisheye optics.
```

**Expected**

- Directly compiles the supplied professional projection terms and completes useful OPEN scene choices.
- Keeps diagonal frame coverage distinct from camera roll and handles central straight-line exceptions.
- For the adjacent variant adding an explicit full-frame context, f/8 and eye-height viewpoint, preserves those supplied values.

**Failure**

- Adds a mandatory novice interview, loses a supplied parameter or interprets diagonal fisheye as a tilted camera.

## CL63 — Fidelity and global projection tradeoff

**Setup**

Seedream 5.5, single 21:9 still, the supplied western street image is the edit base.

**User**

```text
保持这张西部街道的女牛仔和建筑不变，但把普通广角改成非常强烈的鱼眼镜头。
```

**Expected**

- Evaluates single-image editing while protecting identity, topology and observation position.
- Explains that peripheral image points can move with projection and clarifies actual preservation tradeoffs.
- Briefly explains the edit path's continuity advantage and possible curvature limits, with concrete choices when a real unresolved tradeoff exists.
- Keeps user locks until their actual release is authorized.

**Failure**

- Silently regenerates a new scene, suppresses the requested curvature with blanket coordinate locks or omits the relevant strategy explanation.

## CL64 — Focus edit retains the image path

**Setup**

Seedream 5.5, single 21:9 still, the supplied image has a foreground woman and background man.

**User**

```text
保持原图不变，只让后景人物更清楚，前景人物失焦。
```

**Expected**

- Compiles a single-image focus-state edit with concrete attention targets.
- Preserves identity, pose, props, viewpoint, space and lighting while changing clarity.
- Treats newly resolved details from a blurred region as generated reconstruction when explaining their evidence scope.

**Failure**

- Rebuilds the scene through text-to-image, adds fisheye or unrelated effects, or claims recovery of true hidden source detail.

## CL65 — Repeated optical failures with locked content

**Setup**

Text-only multi-turn regression using the same western edit base. Feedback describes hypothetical results for this test, and the executor must treat it as reported feedback. No new images are generated.

**User sequence**

1. 以这张西部雪镇图为底图，增强鱼眼效果。同一女子的身份、建筑连接关系和摄影机位置都锁定。
2. 上一轮两侧立柱仍然接近直线，四角却黑了。继续加强鱼眼，人物和空间保持。
3. 又试了一轮，曲率还是不够。我继续锁定同一女子、建筑拓扑和机位，只允许投影造成的外围位置变化，不同意换场景或改成文生图。请诊断后给我下一步。

**Expected**

- Diagnoses the projection mechanism, preservation pressure, visual conditions, method suitability and reported model limits.
- Distinguishes permitted image-point movement from locked identity, topology and viewpoint.
- Keeps the edit path, explains what remains unmet and proposes a mechanism-based correction or an honest limit.
- Attributes feedback to the supplied report and asks for actual images only when needed to resolve an evidence gap.

**Failure**

- Repeats intensity words as the only change, silently switches to new-image creation, releases locks or pretends to have inspected unprovided results.

## CL66 — Explicit compatible path compiles directly

**Setup**

Seedream 5.5, single 21:9 still, western image attached.

**User**

```text
直接给我单图编辑提示词。人物身份、建筑连接和机位保留，允许外围像点随鱼眼投影移动，中央人物大小基本一致。
```

**Expected**

- Directly compiles the authorized edit with the stated preservation and variation scope.
- Keeps the current Scene Master and reference roles without a redundant Plan or confirmation gate.

**Failure**

- Requires the user to reapprove the compatible path or substitutes text-to-image.

