# Cinegraphic / 电影图形主义

> **Not a filter. A visual system.**  
> **不是滤镜，是一套视觉系统。**

Cinegraphic is a reusable image-to-poster prompting system that translates ordinary images into cinematic, editorial, mid-century-inspired graphic posters.

Cinegraphic 是一套可复用的图像转海报提示词系统：把普通照片、人物图、电影感场景或参考构图，重新设计成具有电影海报感、编辑插画感与复古印刷质感的现代主义作品。

## Reference / 参考效果

The intended reference set is the three before/after comparison images prepared for this style: romance/red-gold, temporal/blue-gray, and noir/red-black.

本风格的参考图为三组 Before / After 对照：红金情绪人物、蓝灰时空构图、黑红权力人物。它们用于说明同一套视觉系统如何适配不同题材，而不是固定套一种红色滤镜。

> Binary reference image asset: `assets/reference-grid.png`

The comparison examples are used only to explain the visual transformation logic. Third-party source imagery shown for comparative study is **not** covered by this repository's MIT license; rights remain with the respective rightsholders.

对比图只用于说明视觉转译逻辑。示例中出现的第三方原始海报素材**不属于**本仓库 MIT License 的授权范围，其权利仍归原权利人所有。

## Core visual grammar / 核心视觉语言

- Mid-century modern poster composition / 20 世纪中叶现代主义构图
- Editorial illustration / 编辑插画
- Vintage cinema poster design / 复古电影海报
- Restricted 3–5 color palettes / 3–5 色限制色体系
- Geometric facial and body planes / 人物几何切面
- Oversized typography as composition / 巨型字体参与构图
- Strong negative space and asymmetric hierarchy / 大面积留白与非对称层级
- Screen-print, Risograph and paper grain / 丝网印刷、Risograph 与纸张颗粒
- Simplified architecture and environmental silhouettes / 建筑与环境几何化

The objective is not to make an image simply look old. The objective is to make it look **designed**.

目标不是把图片简单“做旧”，而是让它看起来像真的被设计过。

## Choose a prompt / 选择版本

### 1. Local / Open Model — Maximum Reference Fidelity

Best for FLUX, Qwen Image, SDXL, ComfyUI and other local/open image workflows when you are working with images you own, created, or have permission to transform.

适合 FLUX、Qwen Image、SDXL、ComfyUI 等本地或开源工作流。用于你拥有、自己创作或已获授权的参考图片，优先保留原图人物关系、动作、构图与视觉层级。

**[English + 中文 prompt →](prompts/local-reference-faithful.md)**

### 2. Hosted / Guardrail-Friendly — Original Reinterpretation

Best for ChatGPT, Gemini and other hosted tools that may apply third-party similarity protections. It extracts high-level visual structure first, then rebuilds an original Cinegraphic poster from scratch.

适合 ChatGPT、Gemini 等可能存在第三方相似性保护的平台。先抽取情绪、构图和视觉层级，再从零重构一张原创 Cinegraphic 海报。

**[English + 中文 prompt →](prompts/hosted-original-reinterpretation.md)**

## Quick use / 快速使用

1. Upload one reference image. / 上传一张参考图。
2. Choose the local or hosted prompt. / 根据平台选择对应提示词。
3. Paste the full prompt together with the image. / 将完整提示词和图片一起提交。
4. Replace optional placeholders such as `{TITLE}`, `{ACCENT_COLOR}` or `{ASPECT_RATIO}`. / 如有需要替换标题、强调色、画幅比例等占位符。
5. Generate, review hierarchy, then iterate only on composition or typography. / 先生成，再只针对构图、字体层级和人物比例做迭代。

## Recommended ratios / 推荐比例

- `3:4` — social cover / 社交封面
- `2:3` — classic poster / 经典电影海报
- `4:5` — editorial / 编辑视觉
- `16:9` — landscape key art / 横版主视觉

## Local image-to-image strength / 本地图生图强度参考

- `0.35–0.55` — preserve more of the original composition / 更多保留原构图
- `0.55–0.75` — stronger Cinegraphic transformation / 更明显的 Cinegraphic 转译
- `0.75+` — loose reinterpretation / 更自由的重新设计

These values are model-dependent and should be treated as starting points rather than universal settings.

具体数值会因模型和工作流不同而变化，以上仅作为起始参考。

## Author

**Bryce Yu / 碳基玩家Bryce**

## License

Prompt text and documentation in this Cinegraphic folder are released under the repository's MIT License. Reference images and third-party source material are excluded unless explicitly stated otherwise.
