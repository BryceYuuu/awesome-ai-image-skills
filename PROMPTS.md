# Prompt Cheatsheet / 长版提示词

> 下面的内容以作者仓库的 SKILL.md / README.md 为基础，删除安装步骤、重复宣传与无关 FAQ，尽量保留真正影响最终效果的规则。  
> 使用前请先安装对应 Skill；仓库更新后，以原作者最新规则为准。

## 使用说明

1. 先安装对应 Skill，并确认 Agent 能识别提示词里的 `$skill-name`。
2. 上传照片、文章、截图、产品图等素材。
3. 把 `{标题}`、`{主题}`、`{颜色}` 等占位符替换成你的内容。
4. 长提示词可以整段复制，不建议只截第一句。

## 01. Gathered Scenes Zine / 拾景纸刊

**来源：** `README.md + SKILL.md`

```text
用 $scenes-gathered-zine-v1-3 把这张照片做成一张“拾景纸刊”风格的成品海报。

目标：把普通照片整理成像独立小刊物里的一页，既保留现场感，也让画面具有纸本编辑感。

执行要求：
1. 识别照片里最值得保留的视觉关系，把它作为整张作品的核心。
2. 保留原照片最有辨识度的主体与空间关系；允许撕纸拼贴、线稿、色块、纸张留白、轻微叠印和局部裁切。
3. 整体像温和、克制、带纸张纤维感的 zine / small press 页面。
4. 文字默认用中文，文案要少，只放标题、短注释或极短副标题。
5. 如果原图本身很强，优先保留摄影；不要为了“设计”把识别度做没。
6. 输出单张成品图，重点是“照片被整理成值得停留的一页”。
```

[作者仓库](https://github.com/Zeejay0/gathered-scenes-zine-skill)

## 02. GC Minimal Zine Poster

**来源：** `SKILL.md`

```text
用 $gc-minimal-zine-poster-v0-3 处理这张素材，生成一张 GC Minimal Zine Poster 风格的极简纸刊海报。

目标：大面积留白、单一重点元素、实验性小排版、老纸质感和一个克制的强调色。

执行要求：
1. 如果是人物/产品/宠物照片，保留身份、轮廓和关键识别特征。
2. 画面必须有大量负空间，只保留一个主视觉或一个小组视觉。
3. 可以使用旧纸、印刷轻瑕疵、细小标注、微型英文字、小编号。
4. 只允许一个明确强调色，其余保持简洁。
5. 文字走诗意编辑路线，不复制参考图原文，不写成长段。
6. 如果输入是文章/情绪/主题，先提炼一个视觉隐喻再生成。
7. 输出完成度高的最终海报。
```

[作者仓库](https://github.com/LiamGvchi/gc-minimal-zine-poster)

## 03. Travel Memory Sticker Card

**来源：** `SKILL.md`

```text
用 $travel-memory-sticker-card 把这张旅行照片做成一张横版 Travel Memory Sticker Card。

目标：左边是大幅安静主画面，右边是同主题拆出来的 6 个贴纸元素，底部是 3 个英文关键词。

执行要求：
1. 横版、纸张感明显、像收藏卡或旅行纪念卡。
2. 左侧保留最大主画面，维持地点、主体、氛围和空间关系。
3. 右侧拆出约 6 个带白边的贴纸：标志物、车辆、树、招牌、局部小景等。
4. 下方放 3 个简短英文关键词，概括地点气质。
5. 使用纸张颗粒、平涂色块、轻微剪贴感；不要保留无关水印。
6. 地标名称最多出现一次。
7. 同时成立“旅行纪念 + 贴纸收集 + 编辑排版”。
```

[作者仓库](https://github.com/carolinaaafy/travel-memory-sticker-card)

## 04. Photo Abstract Editorial

**来源：** `SKILL.md`

```text
用 $photo-abstract-editorial 把这张照片做成一张竖版 Photo Abstract Editorial 编辑作品。

目标：保留原始摄影本身，再从照片中提炼一个克制的抽象记忆面板。

执行要求：
1. 主区域保留原照片，不改成插画，不失去摄影质感。
2. 从色彩、空间关系、地平线、建筑轮廓、道路走向等视觉事实提炼极简抽象面板。
3. 抽象面板像“记忆切片”，不要和主图抢风头。
4. 版式有纸张感、留白和编辑秩序。
5. 可放一句简短英文标题，像作品题名而不是广告。
6. 让人同时看见“真实瞬间”和“抽象记忆”的对应关系。
```

[作者仓库](https://github.com/ZzzLc0405/photo-abstract-editorial)

## 05. Make Photo Stamp Archive

**来源：** `SKILL.md`

```text
用 $make-photo-stamp-archive 把这张照片做成照片档案拼接作品。

目标：原始照片 + 暖白纸张 + 一个与主体相关的手工图章。

执行要求：
1. 保留原照片本身，照片区域不要乱改。
2. 另一侧使用暖白、干净、略有旧化的纸张面板。
3. 图章可以是圆章、方章、异形章、建筑轮廓章或主题印章，小而精。
4. 可调整边框、尺寸、位置、墨色和极简小字，但整体克制。
5. 可改变左右/上下拼接方向，前提是保持档案感。
6. 不要做成商业海报。
```

[作者仓库](https://github.com/Dlcccc71913/skill-make-photo-stamp-archive)

## 06. XHS Cover Skill / 小红书封面生成器

**来源：** `SKILL.md + README.md`

```text
用 $xhs-cover 生成或修改一张 3:4 小红书封面。

执行要求：
1. 优先保证缩略图可读性，主标题和主视觉一眼能懂。
2. 标题是「{标题}」，可拆成 1–2 行；副标题和标签按重要程度排版。
3. 只保留一个明确主视觉中心：人物、产品、截图、插图或场景。
4. 信息层级清楚：主标题最强，其次关键信息，再其次点缀元素。
5. 如果我说“修改封面/上一张图基础上/不要重新做”，就在原结构上改。
6. 风格是「{风格}」；如果没给风格，默认醒目、干净、有记忆点，不低级堆料。
7. 不要为了热闹把所有元素都塞上去。
```

[作者仓库](https://github.com/Vivixiao980/xhs-cover-skill)

## 07. Photo Riso Poster

**来源：** `SKILL.md`

```text
用 $photo-riso-poster 把这张照片做成一张安静的 Risograph 海报。

执行要求：
1. 先观察主体数量、间距、遮挡、朝向、色彩角色和主要结构。
2. 用 2–3 个主要油印色，纸张有温度，不做全彩。
3. 主体保留识别度，但用简化轮廓、块面、网点和叠印重构。
4. 可加入标题、小号文字、编号、日期感元素，但都服务构图。
5. 如果输入只是主题，先提炼一个可图像化核心意象。
6. 成品安静、克制、像设计书里的一页，不做夸张复古商业海报。
```

[作者仓库](https://github.com/luckdvr/photo-riso-poster)

## 08. Pixel Style Poster Skill

**来源：** `SKILL.md`

```text
用 $pixel-style-poster-skill 生成一张 3:4 Pixel Style Poster。

执行要求：
1. 主题「{主题}」，主色「{颜色}」。
2. 主体可以是物件、动物、人物、植物或抽象意象，但必须转成清晰 dot-matrix / bitmap 主视觉。
3. 可以用大标题、微型英文字、反向半调背景或色块冲洗感。
4. 保留低分辨率质感、打印颗粒和位图放大感，但排版要高级。
5. 标题主导型或安静型都可以，但主题必须明确。
6. 如果提供照片，是转译到 bitmap 海报系统，不是简单像素滤镜。
7. 不要做成 8-bit 游戏画面、UI 或像素角色素材。
```

[作者仓库](https://github.com/v92388375-gif/pixel-style-poster-skill)

## 09. Ink Wash Poster

**来源：** `SKILL.md`

```text
用 $ink-wash-poster 生成一张水墨编辑海报。

执行要求：
1. 默认按“当代编辑水墨”处理，不做俗套古风装饰画。
2. 从主题中提炼一个核心视觉意象，再用墨色、留白和纸感表达。
3. 如果输入是照片，保留人物姿态或核心结构，再转译成水墨编辑封面。
4. 可见文字只使用我允许的标题/诗句，不乱加年份、标签、标语、印章字。
5. 纸张肌理、墨迹边缘、湿痕、淡墨层次都可以，但整体高级、疏朗。
6. 最终像文化刊物或展览视觉中的单张海报。
```

[作者仓库](https://github.com/TwentyfiveBTea/ink-wash-poster)

## 10. Travel Photo Soft Abstraction

**来源：** `README.md`

```text
用 $travel-photo-soft-abstraction 处理这张旅行照片。

执行要求：
1. 保留原图最重要的空间结构、主体位置、地平线、交通工具、人物和环境关系。
2. 做 soft abstraction：简化细节、柔化边缘、压缩色彩、整理块面或加入很轻的抽象图形。
3. 像旅行 zine 页面，不做重度滤镜，也不变成完全独立的插画。
4. 版式和纸感要克制，重点是“真实旅行图像被柔和整理过”。
5. 文字只放很少量的小字或作品名。
```

[作者仓库](https://github.com/wnby/travel-photo-soft-abstraction)

## 11. Travel Photo Abstraction

**来源：** `README.md`

```text
使用 $travel-photo-abstraction 分析我上传的照片，并生成“照片 + 抽象图形”的旅行编辑研究图。

执行要求：
1. 先分析颜色主次、地平线、建筑轮廓、道路方向、物体数量和节奏关系。
2. 把这些事实转译成极简抽象符号、块面、色条、路径或关系图。
3. 最终成品中要看得出抽象部分与原照片的对应关系。
4. 保留原照片可读性；抽象部分是理解方式，不是替代原图。
5. 整体像旅行视觉研究、设计练习册或编辑页。
```

[作者仓库](https://github.com/Evianis/travel-photo-abstraction)

## 12. PaperEcho / Photo to Art Card

**来源：** `README.md`

```text
使用 $photo-to-art-card，把这张照片制作成 PaperEcho / Photo to Art Card 风格作品卡。

执行要求：
1. 保留原图最重要的主体和情绪。
2. 可以走 Paper Study Print、4:5 旅行记忆卡或 Photo / Airy Illustration Diptych。
3. 允许轻柔插画化、空气感、纸张化转译或双联画编排，但不要信息过满。
4. 颜色和质感柔和、轻盈，像装进一本小卡册。
5. 文字只保留作品名、日期感或简短说明。
```

[作者仓库](https://github.com/Yu-0312/paper-echo-photo-cards)

## 13. Qingyun IP Poster

**来源：** `SKILL.md + README.md`

```text
用 $qingyun-ip-poster 为我设计一张高级竖版 IP 海报，必要时扩展成系列。

执行要求：
1. 比例优先 3:4 或 9:16，并为后续系列保留统一视觉逻辑。
2. 保留现实人物身份、真实照片特征和事实信息；姓名、职位、奖项、日期、Logo、引语不能瞎编。
3. 中文排版准确，主标题、身份信息、日期/事件层级清晰。
4. 只保留一个明确视觉中心和一个强调色。
5. 如果有现有账号截图/九宫格/旧海报，先诊断再建立稳定规则。
6. 示例图中的人名、奖项和文案都只是占位，不可套用。
7. 标题是「{标题}」。
```

[作者仓库](https://github.com/qingyunAGI/qingyun-ip-poster)

## 14. Yingzao · 营造

**来源：** `README.md`

```text
用 $yingzao 把我提供的建筑、城市、店铺、风物或主题素材做成一张编辑海报。

执行要求：
1. 建筑/场景主体必须突出。
2. 文字不要侵入建筑或纹样最核心部分，版式必须让位给主体。
3. 根据对象选择单体建筑、横版融合、风物主题等合适版式。
4. 多张同主题照片可以融合，但不要做成廉价拼图。
5. 可从真实地域元素提取克制的字形、留白装饰或色彩线索。
6. 整体像一本高质量地方视觉刊物里的成品海报。
```

[作者仓库](https://github.com/op7418/guizang-yingzao-skill)

## 15. Retro Stilllife Photography

**来源：** `README.md + SKILL.md`

```text
用 $retro-stilllife-photography 生成一张 3:4 复古雕塑感静物摄影。

执行要求：
1. 输入是具体物件、产品或食物，不做人像/生活方式房间/光滑 3D。
2. 主体重新摆拍，可堆叠、平衡、包裹、重复、倾斜重组。
3. 背景、光线和纸卡材质有复古摄影气质，像旧杂志或艺术指导过的工作室拍摄。
4. 可搭配约 3 个相关辅助物件，但主物件仍然最重要。
5. 不做海报排版，不加大量文字，重点是摄影感。
```

[作者仓库](https://github.com/qianyuning/retro-stilllife-photography)

## 16. Photo to Monthly Zine Postcard

**来源：** `README.md`

```text
用 $photo-to-monthly-zine-postcard 把这张照片做成一张 monthly zine postcard。

执行要求：
1. 保留原照片最重要的主题与氛围。
2. 整理成“月刊小卡 + 明信片”的版式语言，可带轻量标题、月份信息、小注释和纸张留白。
3. 版面不要做满，重点是安静、有编辑感、适合收藏。
4. 可用轻微旧纸、印刷颗粒和 zine 编排感，但不重度做旧。
5. 文字优先围绕月份、地点、心情或简短标题。
```

[作者仓库](https://github.com/shenchangyi/photo-to-monthly-zine-postcard)

## 17. Guizang Social Card Skill

**来源：** `SKILL.md + README.md`

```text
用 $guizang-social-card-skill 把我的文章、文案、截图、产品笔记、字幕、照片或视频整理成一组可发布社交卡图。

执行要求：
1. 小红书图文拆成约 3–6 张，每张只讲一个重点。
2. Editorial 适合叙事/旅行/阅读/生活方式；Swiss 适合拆条/数据/高信息密度。
3. 标题简短，视觉重点明确，不把制作指令写进可见文案。
4. 静态卡先检查裁切、安全区、主体、文字位置，再考虑组图节奏。
5. 优先抽核心观点，不机械搬运整篇文章。
6. 如果当前只要静态图文，不强行做 Live Photo。
```

[作者仓库](https://github.com/op7418/guizang-social-card-skill)

## 18. Street Photo Illustration

**来源：** `README.md + SKILL.md`

```text
用 $street-photo-illustration 处理这张街拍 / 旅行 / 生活方式照片，把人物转换成插画，同时保留真实环境。

执行要求：
1. 在 BLACK INK 与 COLOR CHIBI 两种模式里选择最合适的一种。
2. 人物转成插画，但保留动作、姿态、衣服、配饰、手持物和环境关系。
3. 原始环境继续保留摄影质感，不要整张图一起卡通化。
4. 可选少量环境感知小字/涂鸦，但不破坏主体。
5. 如果我要求不加文字，就只做人物插画化。
6. 一眼能看出“真实环境中的人物被转成插画了”。
```

[作者仓库](https://github.com/dacnay816y62-hub/street-photo-illustration-skill)

## 19. Photo Revival / 废片焕新

**来源：** `README.md + SKILL.md`

```text
用 $photo-revival 把这张普通照片重新画成白纸上的小幅手绘作品。

执行要求：
1. 保留原图最关键的主体与空间关系。
2. 主体只占整页约 10–16%，把大量空间留给白纸和呼吸感。
3. 可以做小幅水彩、彩铅、纸感插画或轻微拼贴，但要有“画在纸上”的感觉。
4. 颜色集中在主体和少量关键区域，其余保持空、轻、安静。
5. 文字只留一句很小的中文或手写批注。
6. 重点是让画面真的空下来，不继续堆元素。
```

[作者仓库](https://github.com/dacnay816y62-hub/photo-revival)

## 20. FANTASY 奇奇怪怪

**来源：** `README.md + SKILL.md`

```text
用 $fantasy-qiqiguaiguai 把生活碎片、照片、宠物、票据、物件或截图整理成一张有幽默感和编辑感的 3:4 社交海报。

执行要求：
1. 自动判断 T1 人像主体、T2 杂物拼贴、T3 全图压字中最合适的模板。
2. 只提炼一个主创意 / 主梗 / 主情绪，不要每个点都讲。
3. 允许幽默、黑色幽默、玩梗、编辑感标题，但都为主梗服务。
4. 宠物、食品、通勤碎片、票据、截图等可重新编排成一张图。
5. 真实账单、手机号、地址等隐私信息必须换成虚构内容。
6. 整体有网感，但不能乱。
```

[作者仓库](https://github.com/dacnay816y62-hub/fantasy-qiqiguaiguai-skill)
