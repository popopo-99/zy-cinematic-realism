# v1.2.0：同一个证据室，六种导演视角

## 测试说明

这组六图固定同一个故事、人物、年代、地点和证据线索，只改变导演参考。无导演版本使用基础 cinematic realism；导演版本不填写强度，以验证指定导演时默认按“强烈”模式执行。v1.2.0 将原有综合风格句拆分为连续的光影反差、色彩曝光、镜头机位、构图空间四轴签名。每组保留一名侦探、员工卡、幻灯机、黑白监控投影和1980年代纽约警局证据室，并应用真实机位、真实光源与 Anti-AI Cleanup。

## 固定故事

1980年代中期，纽约曼哈顿，一个借来的警局证据室，深夜刚过。一名疲惫的便衣侦探在搭档已经回家后，独自留下继续核对一起装甲运钞车抢劫案的新线索。一台便携式幻灯机把一张刚洗出来的黑白监控人脸投射到贴满证物照片、地图和打字纸的墙上。侦探站在墙前，手里拿着一张城市车库员工卡，正在将它与投影人脸进行比对。附近还有卷边的纸张、遮蔽胶带、冷掉的咖啡、文件盒、旧荧光灯和使用已久的金属文件柜。画幅为16:9。

## 无导演基准

![无导演基准：1980年代纽约警局证据室](images/director-style-comparison/baseline.webp)

### 用户调用文本

```text
请使用 $zy-cinematic-realism：

1980年代中期，纽约曼哈顿，一个借来的警局证据室，深夜刚过。

一名疲惫的便衣侦探在搭档已经回家后，独自留下继续核对一起装甲运钞车抢劫案的新线索。

一台便携式幻灯机把一张刚洗出来的黑白监控人脸投射到贴满证物照片、地图和打字纸的墙上。侦探站在墙前，手里拿着一张城市车库员工卡，正在将它与投影人脸进行比对。

附近还有卷边的纸张、遮蔽胶带、冷掉的咖啡、文件盒、旧荧光灯和使用已久的金属文件柜。只有一名侦探；保持1980年代纽约的年代一致性；保持真实机位、真实光源和物理可信；不增加现代数字屏幕；不改变为海报、广告或概念艺术。16:9。
```

### Final Prompt

```text
A grounded 16:9 observed live-action frame in a borrowed Manhattan police evidence room just after midnight in the mid-1980s. One tired plainclothes detective remains after his partner has gone home, checking a new armored-car robbery lead by holding a city garage employee card beside a newly developed black-and-white surveillance face projected from a portable slide projector onto a wall of evidence photographs, maps, typed pages, curled paper, and masking tape. Use a physically plausible stable medium observation from a doorway. The employee card, his hand, the projected face, and one nearby taped photograph form the two fully readable narrative zones; cold coffee, file boxes, fluorescent tubes, and used metal filing cabinets recede into partial shadow, obstruction, or soft distance. Projector white and weak aging fluorescent spill provide limited neutral illumination, with matte paper, tired skin, dead metal, dull walls, natural exposure falloff, and unresolved dark corners.
```

### Avoid

```text
waxy skin, plastic metal, HDR contrast, lifted blacks, uniform sharpness, glossy crime-drama lighting, decorative decay, luxury office, modern digital screen, poster composition, advertising polish
```

## 王家卫

![王家卫强烈模式：1980年代纽约警局证据室](images/director-style-comparison/wong-kar-wai.webp)

### 用户调用文本

```text
请使用 $zy-cinematic-realism：

1980年代中期，纽约曼哈顿，一个借来的警局证据室，深夜刚过。一名疲惫的便衣侦探在搭档已经回家后，独自留下继续核对一起装甲运钞车抢劫案的新线索。一台便携式幻灯机把一张刚洗出来的黑白监控人脸投射到贴满证物照片、地图和打字纸的墙上。侦探站在墙前，手里拿着一张城市车库员工卡，正在将它与投影人脸进行比对。附近还有卷边的纸张、遮蔽胶带、冷掉的咖啡、文件盒、旧荧光灯和使用已久的金属文件柜。只有一名侦探；保持1980年代纽约的年代一致性；保持真实机位、真实光源和物理可信；不增加现代数字屏幕；不改变为海报、广告或概念艺术。

导演参考：王家卫

16:9。
```

### Final Prompt

```text
A grounded 16:9 observed live-action frame in a borrowed Manhattan police evidence room just after midnight in the mid-1980s. One tired plainclothes detective remains after his partner has gone home, continuing to compare a city garage employee card with a newly developed black-and-white surveillance face projected onto a wall of evidence photographs, maps, typed pages, curled paper, and masking tape.

Director and visual reference: Wong Kar-wai, drawing strongly from the visual language associated with In the Mood for Love, Chungking Express, and Fallen Angels.

Lighting and contrast signature: stale ceiling fluorescents, projector white, and faint corridor sodium spill create broken local pools across scratched metal; the reflected profile and card edge receive intermittent highlights while secondary evidence falls into dense, incomplete shadow.

Color and exposure signature: fluorescent green, projector-neutral white, muted burgundy paper tabs, tired skin, and dead grey metal contaminate one another through real sources; clipped practicals and partial underexposure are allowed without a global neon wash.

Lens and camera signature: observe from an obstructed side position behind a half-open doorway with compressed proximity, selective motion smear from a slight turn, and split focus between the reflected eye and card rather than perfect card-to-projection alignment.

Composition and spatial signature: make the incomplete encounter among detective, reflection, and interrupted projected face the visual center; reflective metal, paper edges, doorway, coffee, boxes, and cabinets fracture the room, leaving only one emotional fragment fully readable.
```

### Avoid

```text
generic neon filter, smoking pose, cheongsam, romantic glamour, perfect card-to-face alignment, waxy skin, uniform sharpness, beauty lighting, poster composition, commercial polish
```

## 斯坦利·库布里克

![斯坦利·库布里克强烈模式：1980年代纽约警局证据室](images/director-style-comparison/stanley-kubrick.webp)

### 用户调用文本

```text
请使用 $zy-cinematic-realism：

1980年代中期，纽约曼哈顿，一个借来的警局证据室，深夜刚过。一名疲惫的便衣侦探在搭档已经回家后，独自留下继续核对一起装甲运钞车抢劫案的新线索。一台便携式幻灯机把一张刚洗出来的黑白监控人脸投射到贴满证物照片、地图和打字纸的墙上。侦探站在墙前，手里拿着一张城市车库员工卡，正在将它与投影人脸进行比对。附近还有卷边的纸张、遮蔽胶带、冷掉的咖啡、文件盒、旧荧光灯和使用已久的金属文件柜。只有一名侦探；保持1980年代纽约的年代一致性；保持真实机位、真实光源和物理可信；不增加现代数字屏幕；不改变为海报、广告或概念艺术。

导演参考：斯坦利·库布里克

16:9。
```

### Final Prompt

```text
A grounded 16:9 observed live-action frame in a borrowed Manhattan police evidence room just after midnight in the mid-1980s. One tired plainclothes detective remains after his partner has gone home, holding a city garage employee card near a black-and-white surveillance face projected from a portable slide projector onto an evidence wall of photographs, maps, typed paper, curled edges, and masking tape.

Director and visual reference: Stanley Kubrick, drawing strongly from the visual language associated with 2001: A Space Odyssey, The Shining, and Barry Lyndon.

Lighting and contrast signature: ceiling fluorescents and a hard projector patch establish formal, repeated light planes with precise shadow boundaries; no beauty key separates the detective from the institutional room.

Color and exposure signature: restrained neutral paper, dead metal, faded paint, and tired skin stay inside disciplined midtones, with practical whites protected and coffee, boxes, and tape left in dry, unflattering tonal areas.

Lens and camera signature: use a measured normal-to-wide lens from a physically possible position aligned with the room's governing axis, controlled middle-deep focus, and no casual movement.

Composition and spatial signature: filing cabinets, ceiling fixtures, evidence wall, and projector table establish deliberate geometry; the detective remains offset against the grid, and his imperfect checking gesture becomes the single human break in order.
```

### Avoid

```text
automatic symmetry, corridor cliché, extreme wide-angle distortion, red bathroom imagery, glossy institutional set, waxy skin, HDR, polished vignette, poster composition, luxury production design
```

## 丹尼斯·维伦纽瓦

![丹尼斯·维伦纽瓦强烈模式：1980年代纽约警局证据室](images/director-style-comparison/denis-villeneuve.webp)

### 用户调用文本

```text
请使用 $zy-cinematic-realism：

1980年代中期，纽约曼哈顿，一个借来的警局证据室，深夜刚过。一名疲惫的便衣侦探在搭档已经回家后，独自留下继续核对一起装甲运钞车抢劫案的新线索。一台便携式幻灯机把一张刚洗出来的黑白监控人脸投射到贴满证物照片、地图和打字纸的墙上。侦探站在墙前，手里拿着一张城市车库员工卡，正在将它与投影人脸进行比对。附近还有卷边的纸张、遮蔽胶带、冷掉的咖啡、文件盒、旧荧光灯和使用已久的金属文件柜。只有一名侦探；保持1980年代纽约的年代一致性；保持真实机位、真实光源和物理可信；不增加现代数字屏幕；不改变为海报、广告或概念艺术。

导演参考：丹尼斯·维伦纽瓦

16:9。
```

### Final Prompt

```text
A grounded 16:9 observed live-action frame in a borrowed Manhattan police evidence room just after midnight in the mid-1980s. One tired plainclothes detective remains after his partner has gone home, standing at a distant evidence wall and comparing a city garage employee card with a black-and-white surveillance face from a portable slide projector. The room contains evidence photographs, maps, typed pages, curled paper, masking tape, cold coffee, file boxes, old fluorescent fixtures, and used metal filing cabinets.

Director and visual reference: Denis Villeneuve, drawing strongly from the visual language associated with Prisoners, Sicario, and Arrival.

Lighting and contrast signature: weighty failing fluorescents and distant projector white form broad severe value fields, while the long aisle and cabinet recesses retain real unreadable darkness.

Color and exposure signature: restrained grey-brown paper, paint, metal, and tired skin remain muted by the institution; protected practical whites and heavy midtones replace orange haze or science-fiction color.

Lens and camera signature: observe with a measured wide camera from the far aisle, patient stillness, and middle-to-deep contextual focus; the card gesture remains understandable but never receives a procedural close-up.

Composition and spatial signature: dark filing cabinets form a heavy foreground mass, the detective becomes a small stalled figure, and the projected face shrinks to a distant functional patch; negative space and locked evidence systems outweigh the individual.
```

### Avoid

```text
desert haze, orange fog, science-fiction spectacle, anonymous heroic silhouette, artificial mist, glossy black surfaces, HDR, uniformly visible room, luxury police set, advertising polish
```

## 大卫·芬奇

![大卫·芬奇强烈模式：1980年代纽约警局证据室](images/director-style-comparison/david-fincher.webp)

### 用户调用文本

```text
请使用 $zy-cinematic-realism：

1980年代中期，纽约曼哈顿，一个借来的警局证据室，深夜刚过。一名疲惫的便衣侦探在搭档已经回家后，独自留下继续核对一起装甲运钞车抢劫案的新线索。一台便携式幻灯机把一张刚洗出来的黑白监控人脸投射到贴满证物照片、地图和打字纸的墙上。侦探站在墙前，手里拿着一张城市车库员工卡，正在将它与投影人脸进行比对。附近还有卷边的纸张、遮蔽胶带、冷掉的咖啡、文件盒、旧荧光灯和使用已久的金属文件柜。只有一名侦探；保持1980年代纽约的年代一致性；保持真实机位、真实光源和物理可信；不增加现代数字屏幕；不改变为海报、广告或概念艺术。

导演参考：大卫·芬奇

16:9。
```

### Final Prompt

```text
A grounded 16:9 observed live-action frame in a borrowed Manhattan police evidence room just after midnight in the mid-1980s. One tired plainclothes detective remains after his partner has gone home, verifying a new armored-car robbery lead by comparing a city garage employee card with a newly developed black-and-white surveillance face projected from a portable slide projector onto a wall of photographs, maps, typed pages, curled paper, and masking tape.

Director and visual reference: David Fincher, drawing strongly from the visual language associated with Se7en, Zodiac, and The Social Network.

Lighting and contrast signature: threshold fluorescents and projector light keep card, checking hand, typed time marker, and projected face readable inside low illumination; secondary boxes and cabinets enter controlled shadow.

Color and exposure signature: neutral-to-cool paper, tired skin, dull wall paint, and dead metal retain disciplined midtones, contained whites, and controlled blacks without a yellow-green cast.

Lens and camera signature: use exact physically plausible medium placement at the evidence-room threshold, restrained movement, and disciplined contextual focus linking card, hand, and projection.

Composition and spatial signature: arrange employee card, typed time markers, taped photographs, file surfaces, and checking gesture as a causal evidence chain; suppress secondary clutter so the information hierarchy remains precise rather than uniformly sharp.
```

### Avoid

```text
yellow-green filter, serial-killer cliché, rain-soaked darkness, crime-scene decoration, hacker neon, music-video movement, waxy skin, plastic metal, HDR, uniform sharpness, luxury workstation
```

## 泰伦斯·马力克

![泰伦斯·马力克强烈模式：1980年代纽约警局证据室](images/director-style-comparison/terrence-malick.webp)

### 用户调用文本

```text
请使用 $zy-cinematic-realism：

1980年代中期，纽约曼哈顿，一个借来的警局证据室，深夜刚过。一名疲惫的便衣侦探在搭档已经回家后，独自留下继续核对一起装甲运钞车抢劫案的新线索。一台便携式幻灯机把一张刚洗出来的黑白监控人脸投射到贴满证物照片、地图和打字纸的墙上。侦探站在墙前，手里拿着一张城市车库员工卡，正在将它与投影人脸进行比对。附近还有卷边的纸张、遮蔽胶带、冷掉的咖啡、文件盒、旧荧光灯和使用已久的金属文件柜。只有一名侦探；保持1980年代纽约的年代一致性；保持真实机位、真实光源和物理可信；不增加现代数字屏幕；不改变为海报、广告或概念艺术。

导演参考：泰伦斯·马力克

16:9。
```

### Final Prompt

```text
A grounded 16:9 observed live-action frame in a borrowed Manhattan police evidence room just after midnight in the mid-1980s. One tired plainclothes detective remains after his partner has gone home, still checking a new armored-car robbery lead with a city garage employee card and a newly developed black-and-white surveillance face projected onto a wall of photographs, maps, typed pages, curled paper, and masking tape.

Director and visual reference: Terrence Malick, drawing strongly from the visual language associated with Days of Heaven, The Thin Red Line, and The Tree of Life.

Lighting and contrast signature: dead fluorescent contamination and projector white cross the moving shoulder unevenly; skin becomes dull, some projection whites clip, and unresolved corners remain genuinely dark.

Color and exposure signature: tired skin, matte paper, dead metal, cold coffee, and uneven wall color keep unattractive material neutrals; exposure breathes as the body crosses the beam without a golden or prestige-grey wash.

Lens and camera signature: use a nearby physically possible 24–28mm spatial feeling one step behind and beside the shoulder, with a short human drift and focus breathing from sleeve and curled paper toward the broken projection.

Composition and spatial signature: the lowered card stays near the edge, partial body, uneven paper, and tape fracture the projected face, and one tactile sleeve-paper contact outranks complete evidence readability.
```

### Avoid

```text
golden backlight, pastoral metaphor, sky-gazing, fields, perfume-ad light, centered projection geometry, perfect card-to-face alignment, waxy skin, glossy old office, HDR, uniform sharpness, lifestyle advertising
```

## 简短对照总结

| 版本 | 镜头主要在看什么 |
|---|---|
| 无导演基准 | 侦探如何完成员工卡与监控投影的比对 |
| 王家卫 | 深夜孤独、反射、遮挡与不完整的心理关系 |
| 斯坦利·库布里克 | 个人如何被制度空间和几何秩序控制 |
| 丹尼斯·维伦纽瓦 | 渺小侦探如何面对比自己更沉重的证据系统 |
| 大卫·芬奇 | 卡片、投影、照片和文字如何组成严密的信息链 |
| 泰伦斯·马力克 | 疲惫身体、纸边、袖口与投影光如何打断程序动作 |

> 所有版本都保留相同故事事实。差异来自导演对具体时刻、视觉中心、机位、调度、光线、景深和质感的重新选择。
