# ZY Cinematic Realism Skill

> **别再只往 Prompt 里塞 `cinematic`。先让故事发生。**

把一句简单的画面想法，变成具有叙事瞬间、真实空间、明确摄影机位置、可信光源和克制胶片质感的英文 AIGC Prompt。

`一句话想法` → `找到故事瞬间` → `架好摄影机` → `建立真实光源` → `Final Prompt + Avoid`

![两个侦探在失败后的夜班公交车上沉默而坐](docs/images/hero-night-bus.png)

<p align="center"><em>真正起作用的不是“两个侦探坐公交车”，而是“一次失败以后，他们隔着几排座位沉默地回去”。</em></p>

## 这不是一包“万能电影词”

很多所谓电影感 Prompt，删掉 `35mm / Kodak / anamorphic / film grain` 后，就只剩下“一个人站在一个很有氛围的地方”。

这套 Skill 会先替你解决更重要的问题：

- **故事**：这一刻之前发生了什么？之后还会发生什么？
- **人物**：角色在做什么小动作，而不是摆什么姿势？
- **空间**：雨水、磨损、杂物和旧物怎样参与叙事？
- **摄影机**：观众到底站在哪里看？隔着门、玻璃、座椅还是人群？
- **光线**：光来自窗户、路灯、荧光灯，还是场景里真的存在的灯？

摄影参数最后才加入。它们负责强化画面，不负责替代故事。

## 60 秒上手

### 1. 给 AI 一个想法

你不需要会写专业摄影参数。最少告诉它这 5 件事：

```text
谁 + 在哪里 + 刚刚发生了什么 + 此刻的小动作 + 最不想要什么
```

直接复制这个例子到 Codex：

```text
请使用 $zy-cinematic-realism：

1980 年代纽约，一次重要审讯失败后的深夜。
两个性格完全不同的侦探坐夜班公交车回警局，隔着几排座位，没有交谈。
一个看着窗外的雨，另一个盯着空座位。
不要人物海报感，不要英雄姿势，要像真实犯罪电影中段被偶然截取的一帧。
```

如果你只写了一句话也没关系，Skill 会补全缺失的故事、场景、摄影机和光线逻辑；只有会明显改变创作方向的信息，它才会向你确认。

### 2. 看懂 Skill 的输出

它默认给你三部分：

1. **画面理解**：用几句话确认它选中了哪个故事瞬间。
2. **Final Prompt**：可直接交给生图或生视频模型的完整英文提示词。
3. **Avoid**：针对当前场景的负面约束，不是机械复制的一长串词。

<details>
<summary><strong>展开看一个缩短版输出</strong></summary>

```text
A restrained frame from a 1980s New York crime drama.

Late at night, inside a nearly empty city bus moving through a rain-soaked neighborhood.
Two detectives sit several rows apart after an important interrogation has failed. Neither
speaks. One watches the city dissolve through rain and window reflections; the other stares
past an empty seat, his wet coat still buttoned.

The camera observes from the last row at seated eye level, partially blocked by worn seat
backs and metal handrails. Both characters remain small and off-center inside the bus.

Available practical light only: aged green fluorescent tubes overhead and intermittent warm
streetlights passing through wet windows. Natural exposure, muted color response, visible
35mm grain, subtle halation and slight vibration from the moving vehicle.

Avoid: promotional poster composition, hero pose, characters looking at camera, perfect
symmetry, clean modern bus, artificial rim light, excessive lens flare, HDR, CGI appearance.
```

</details>

### 3. 把结果交给生图模型

- 复制 `Final Prompt` 到你常用的生图或生视频模型。
- 模型有单独的 Negative Prompt 输入框，就把 `Avoid` 放进去。
- 没有负面词输入框，就把 `Avoid` 保留在 Final Prompt 结尾。
- 第一张图不是终点。先看故事、机位和光线是否正确，再决定要不要改焦段或胶片。

### 4. 不满意时，用一句话纠偏

不要每次推倒重写。直接告诉 Skill 哪里仍然“像 AI”：

```text
人物太像海报：让摄影机退到公交车后排，用座椅遮挡，人物缩小并偏离中心。

灯光太假：删除轮廓光，只保留车内旧荧光灯和窗外经过的橙色路灯。

环境太干净：加入磨损座椅、旧广告、地面雨水和被遗忘的报纸，但不要堆无关物品。

画面没有故事：改成冲突结束后的沉默，不要选择角色正面对峙的高潮时刻。
```

这一步通常比继续添加 `masterpiece / epic / 8K` 更有效。

## 从一条故事里，选择不同的“那一刻”

Skill 不只是在同一个构图上换滤镜。它会帮你判断，故事里哪个瞬间最值得被看见。

### 审讯正在失控

![从单向玻璃外观察一场正在失控的审讯](docs/images/scene-interrogation.png)

摄影机没有坐在谈判桌旁，而是在单向玻璃外。玻璃反射、监听设备和大块暗部让观众更像一个不该在场的观察者。

### 回家以后，案件还没有结束

![侦探在深夜的公寓里独自阅读文件](docs/images/scene-private-aftermath.png)

人物不需要哭喊。桌上的信、没喝完的咖啡、门框遮挡和一盏台灯，就能说明“他仍然放不下”。

### 真相揭开后的沉默

![两名侦探站在河边的巨大负空间里](docs/images/scene-river-silence.png)

人物缩小、远离中心，城市与河面占据大部分画面。环境不再只是背景，而是在替角色说话。

### 主角离开，城市继续

![清晨城市街道上一辆逐渐驶远的警车](docs/images/scene-city-finale.png)

结尾不一定需要主角特写。隔着有划痕的玻璃看警车驶远，普通人开始新的一天，故事已经结束，但城市没有停下。

## 换个题材，方法仍然成立

![拳击回合间坐在角落休息的疲惫拳手](docs/images/scene-boxer-corner.png)

犯罪片可以用，拳击片、家庭剧情、科幻、古装或城市短片也可以用。核心始终是：

> **不要只说“一个疲惫的拳手”。要说清楚是哪一回合之后、他正在做什么、摄影机隔着什么看见他，以及场馆里哪盏灯真的亮着。**

## 万能输入卡片

第一次使用时，可以直接复制这张卡片。填不完也没关系：

```text
请使用 $zy-cinematic-realism：

故事类型：
时间与地点：
人物：
刚刚发生了什么：
此刻的动作：
情绪（克制一点）：
希望的观察位置：
最不想出现的效果：

请输出：画面理解、完整英文 Final Prompt、当前场景专属 Avoid。
```

更偷懒的版本只有一句：

```text
请使用 $zy-cinematic-realism，把“[你的想法]”写成像真实电影中途被截取的一帧，降低 AI 感。
```

## 安装到 Codex

### 方法一：下载 ZIP

1. 点击仓库右上角的 **Code → Download ZIP**。
2. 解压后找到仓库里的 `zy-cinematic-realism` 文件夹。
3. 将这个完整文件夹复制到：

```text
%USERPROFILE%\.codex\skills\zy-cinematic-realism
```

4. 重新打开 Codex，然后用上面的示例测试。

### 方法二：Git 克隆

```bash
git clone https://github.com/popopo-99/zy-cinematic-realism.git
```

克隆后，同样只需要把仓库中的 `zy-cinematic-realism/` 复制到个人 Skills 目录。

安装后，除了显式写 `$zy-cinematic-realism`，遇到“电影感 Prompt”“降低 AI 感”“电影单帧”“摄影机位置”“真实光源”等任务时也可以自动触发。

## 不安装也能用吗？

可以。打开 [`zy-cinematic-realism/SKILL.md`](zy-cinematic-realism/SKILL.md)，把内容和你的场景想法一起发给支持长文本提示的 AI。

安装版的优势是：不用每次复制整份规则，并且 AI 可以按需读取模板、检查表和案例。

## 仓库里有什么

```text
zy-cinematic-realism/
├── SKILL.md                      # 主工作流
├── agents/
│   └── openai.yaml              # Skill 元数据
├── assets/
│   └── basic-prompt-template.md  # 可复用模板
└── references/
    ├── camera-and-light.md       # 摄影机与真实光源
    ├── cinematic-principles.md   # 电影感原则
    ├── examples.md               # 完整案例
    ├── negative-prompts.md       # 场景化负面词
    └── quality-checklist.md      # 生成前自检
```

仓库根目录的 `README.md` 是你正在看的教程；`zy-cinematic-realism/` 才是可以安装的 Skill 本体。

## 最后只记住一句话

> **先让画面成为故事中的一个真实瞬间，再考虑它使用什么镜头和胶片。**

示例图由作者使用 AIGC 创作，用于展示这套工作流追求的叙事与摄影方向。
