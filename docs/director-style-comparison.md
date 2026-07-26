# 同一个证据室，六种导演视角

## 测试说明

这组六图固定同一个故事、人物、年代、地点和证据线索，只改变导演参考。无导演版本使用基础 cinematic realism；导演版本不填写强度，以验证指定导演时默认按“强烈”模式执行。每组保留一名侦探、员工卡、幻灯机、黑白监控投影和1980年代纽约警局证据室，并应用真实机位、真实光源与 Anti-AI Cleanup。

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

Reselect the visual center around an incomplete private encounter between the detective, his reflection in scratched filing-cabinet glass, and the projected face interrupted by paper edges. Use an obstructed side view through a half-open doorway and reflective metal, compressed proximity with the card held just off the projection rather than perfectly aligned, selective motion smear from a slight turn, split focus between the reflected eye and the card, stale fluorescent green mixed with projector white and faint corridor sodium spill, muted burgundy paper tabs and dead grey metal. Let the room feel fragmented and delayed, with only the reflected profile and the card edge fully readable; keep secondary evidence, coffee, boxes, and cabinets incomplete in shadow and soft distance, with matte surfaces and no glossy neon treatment.
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

Reselect the visual center around the detective held inside a deliberate institutional geometry: filing cabinets, ceiling fluorescents, the evidence wall, and the projector table establish formal planes while his checking gesture introduces human instability. Use a measured normal-to-wide lens from a cool, physically possible witness position, ritualized blocking with the detective offset against a strict wall grid, controlled middle-deep focus, practical fluorescent light with a hard projector patch, restrained neutral color, precise shadow boundaries, and clean but unglamorous capture texture. Keep the employee card and projected face readable but subordinate to the ordered room; let coffee, boxes, tape, and secondary papers fall into dry, unflattering tonal areas.
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

Reselect the visual center around the detective’s small stalled figure against the severe scale of the borrowed institution. Use a measured wide camera down a long aisle, with dark filing cabinets occupying a heavy foreground plane and the projected face reduced to a distant functional light patch. Keep the detective’s card gesture understandable but not central; use sparse blocking, controlled negative space, patient stillness, weighty failing fluorescents and projector white, restrained grey-brown material color, middle-to-deep contextual focus, dense unglamorous texture, and real darkness where the practical light does not reach. The system of cabinets, paper, and locked evidence should outweigh the individual without haze or spectacle.
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

Organize the room through exact procedural information hierarchy: the employee card, projected face, typed time markers, taped photographs, file surfaces, and the detective’s checking hand form a controlled chain of visual evidence. Use precise physically plausible camera placement at the evidence-room threshold, restrained movement, disciplined focus that connects card, hand, and projection while leaving secondary boxes and cabinets incomplete, low illumination with high narrative readability, neutral-to-cool material response, controlled shadow detail, matte paper, tired skin, and clean spatial causality without glossy crime-drama polish.
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

Let bodily duration and tactile interruption outrank procedural clarity: the detective has just shifted his card below its perfect comparison position while staying at the evidence wall, and a curled typed-paper edge catches his sleeve as he takes one human step through the projector beam. Use a nearby physically possible 24-28mm camera drifting behind and to the side of his shoulder; partial body, uneven paper, and masking tape fracture the projected face. Let focus breathe from sleeve and paper edge toward the projection, with the card remaining visible near the frame edge rather than ideal. Mix dead fluorescent contamination with projector white, leave dull skin, matte paper, dead metal, incomplete evidence, cold coffee, and unresolved corners in uneven exposure, and retain captured texture instead of polished beauty.
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
