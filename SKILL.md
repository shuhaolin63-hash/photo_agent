---
name: "photo_agent"
description: "摄影诊断AI Agent系统。当用户上传照片请求摄影点评、构图分析、修图建议、风格对标大师时触发。支持人像/风光/纪实/星空/生态/建筑/静物全品类诊断。触发词：摄影诊断、构图分析、修图建议、风格对标、点评照片、照片分析、怎么修图、Lightroom参数、醒图参数。"
---

# 摄影诊断AI Agent技能

## 技能概述

基于多Agent协作架构的智能摄影诊断系统。用户上传照片后，系统自动执行完整诊断流程：

**场景识别 → 构图/光影/色彩诊断 → 大师风格对标 → 修图方案生成 → PDF诊断报告输出**

## 触发条件

### 直接触发

| 意图 | 触发词示例 |
|------|-----------|
| 综合诊断 | `帮我分析这张照片` `照片点评` `摄影诊断` `这张照片拍得怎么样` `水平怎么样` |
| 构图分析 | `构图分析` `构图怎么样` `三分法` `九宫格分析` |
| 光影分析 | `光线分析` `曝光怎么样` `过曝` `欠曝` `光影诊断` |
| 色彩评估 | `色彩分析` `色温` `偏色` `白平衡` `色调评估` |
| 风格对标 | `风格对标` `像不像XX风格` `大师风格` `对标大师` `和大师比` |
| 修图建议 | `怎么修图` `修图建议` `后期怎么调` `Lightroom参数` `醒图参数` `PS怎么调` |

### 间接触发

用户**上传了图片**且文本包含：`拍得好不好` `水平怎么样` `快门/光圈/ISO` `怎么提高` `有什么问题` 等。

## 工作流程

```
用户上传照片 + 文本指令
        │
        ▼
   ┌─────────────┐
   │  main_agent  │  场景识别 + 任务调度
   └──────┬──────┘
          │
    ┌─────┴─────┐
    ▼           ▼
品类Agent    style_agent     ← 可并行
(诊断报告)   (大师对标)
    │           │
    └─────┬─────┘
          ▼
   retouch_agent  (修图方案)
          │
          ▼
  pdf_export_agent  (PDF报告)
```

## 项目文件结构

```
photo_agent/
├── SKILL.md                          ← 技能注册文件（本文件）
├── agent_config.yaml                 ← 项目配置(技术栈/Agent定义/调度协议)
├── 摄影_skills/                      ← 核心知识库
│   ├── skill_main.md                 ← 技能入口文档
│   ├── skill_dispatch/               ← 调度系统
│   │   ├── dispatch_rule.txt         ← 场景识别规则 + Agent分配矩阵
│   │   ├── executor.txt              ← 统一JSON输入输出规范 + Prompt模板
│   │   └── scene_lib/README.md       ← 5大场景33子场景CLIP标签定义
│   ├── skill_analysis/               ← 图像分析知识库
│   │   ├── base_element/             ← 曝光三要素 / 对焦景深
│   │   ├── composition/              ← 九宫格规则 / 引导线 / 对称框架
│   │   ├── light_color/              ← 白平衡 / HSL调整 / 光线方向
│   │   └── scene_match/              ← CLIP场景分类逻辑
│   ├── skill_master_ref/             ← 大师资料库
│   │   ├── portrait_master/          ← 10位人像大师 + 汇总
│   │   ├── landscape_master/         ← 4位风光大师 + 汇总
│   │   ├── documentary_master/      ← 6位纪实大师 + 汇总
│   │   ├── starry_nature_master/     ← 9位星空+生态大师 + 汇总
│   │   ├── architecture_master/      ← 4位建筑大师 + 汇总
│   │   ├── still_life_master/        ← 3位静物大师 + 汇总
│   │   └── other_genre_master/       ← 其他品类汇总
│   ├── skill_style_match/            ← 风格匹配
│   │   ├── style_feature.txt         ← CLIP风格特征提取规则
│   │   └── style_suggest.txt         ← 风格推荐 + 发展路径建议
│   ├── skill_retouch/                ← 修图方案
│   │   ├── retouch_rule.md           ← 修图总则 + 伦理规范 + 工作流程
│   │   ├── portrait_retouch/         ← 人像磨皮 / 调色
│   │   ├── landscape_retouch/        ← 风光HDR / 调色
│   │   ├── starry_retouch/           ← 星空降噪 / 叠加
│   │   └── universal_param/          ← 醒图参数模板(~840行) + Lightroom参数
│   └── skill_export_pdf/             ← PDF报告生成
│       ├── pdf_template.md           ← 7章报告模板
│       ├── mark_lib/README.md        ← 构图标注规范
│       ├── problem_lib/README.md     ← 常见问题分类库
│       └── retouch_suggest_lib/README.md ← 修图建议模板库
├── agents/                            ← 9个Agent定义文档
│   ├── main_agent.md                 ← 主控调度Agent
│   ├── portrait_agent.md             ← 人像诊断Agent
│   ├── landscape_agent.md            ← 风光诊断Agent
│   ├── documentary_agent.md          ← 纪实诊断Agent
│   ├── starry_agent.md              ← 星空诊断Agent
│   ├── still_life_agent.md          ← 静物诊断Agent
│   ├── style_agent.md               ← 风格对标Agent
│   ├── retouch_agent.md             ← 修图建议Agent
│   └── pdf_export_agent.md          ← PDF导出Agent
├── reference/                         ← 参考图库(341张)
│   ├── ref_photo_sample/             ← 9张问题对照样本(过曝/模糊/倾斜)
│   ├── master_works/                 ← 大师作品参考
│   │   ├── portrait_master_photos/  ← 人像: 10张WikiMedia原作 + 150张风格参考
│   │   ├── landscape_master_photos/ ← 风光: 20张WikiMedia原作 + 30张风格参考
│   │   ├── documentary_master_photos/← 纪实: 16张WikiMedia原作 + 75张风格参考
│   │   └── other_master_photos/     ← 其他: 100张(星空25/生态25/建筑25/静物25)
│   └── photography_textbook/        ← 摄影教材(待补充)
├── assets/                            ← 素材资源
│   ├── grid9_mask/                   ← 构图蒙版(三分法/黄金分割/对角线)
│   ├── element_chart/                ← 曝光三角图解
│   ├── style_palette/                ← 色轮参考图
│   └── pdf_mark_pic/                 ← PDF标注图标(待补充)
└── scripts/                           ← 处理脚本
    ├── dispatch_script.txt           ← 调度伪代码
    ├── composition_check_script.txt  ← 构图检测伪代码
    ├── master_compare_script.txt     ← 风格比对伪代码
    ├── retouch_analysis_script.txt   ← 修图分析伪代码
    └── pdf_render_script.txt         ← PDF生成伪代码
```

## 四层诊断架构

### 第一层：分析层（OpenCV量化 + LLM语义理解）

| 分析维度 | 检测内容 | 量化方法 |
|---------|---------|---------|
| 构图诊断 | 九宫格主体偏离、地平线倾斜、引导线、框架构图 | OpenCV角点检测 + 霍夫变换 |
| 光影分析 | 直方图分布、高光/阴影裁剪、曝光偏差、光质 | 直方图统计 + CLAHE对比 |
| 色彩评估 | 色温偏差、白平衡、饱和度、HSL通道分布 | 色彩空间转换 + 统计分析 |
| 清晰度评估 | 对焦准确度、运动模糊、噪点水平 | Laplacian方差 + FFT频谱分析 |

参考知识库：`skill_analysis/` 下各子目录

### 第二层：对标层（CLIP向量匹配 + LLM深度分析）

- **匹配流程**：CLIP ViT-L/14@336px 提取图像特征向量 → 与大师作品特征库计算余弦相似度 → Top-3候选 → LLM逐维度深度对比
- **5维度雷达图**：用光风格 / 构图偏好 / 色调倾向 / 参考文档手法 / 后期处理
- **大师库规模**：36位大师，覆盖7个品类
- 参考知识库：`skill_master_ref/`、`skill_style_match/`

### 第三层：修图层（场景化参数方案）

- **醒图参数**：15个基础参数 + 8个人像专属参数 + HSL 8通道调整（详见 `xingtuparams.md` ~840行）
- **Lightroom参数**：对应LR参数映射（详见 `lr_params.md`）
- **10套场景预设**：日系清新 / 电影感 / 复古胶片 / 黑白经典 / 户外风光 / 日落金调 / 蓝调冷色 / 星空调色 / 静物质感 / 纪实纪实
- **局部调整**：径向滤镜、线性渐变、蒙版笔刷方案
- 参考知识库：`skill_retouch/`

### 第四层：输出层（结构化PDF报告）

- **7章结构**：照片概览 → 构图诊断 → 光影分析 → 色彩评估 → 风格对标 → 修图建议 → 总结提升
- **评分体系**：0-100分制，5维度加权评分
- 参考知识库：`skill_export_pdf/`

## 大师库详情（36位）

### 人像摄影（10位）

| 大师 | 风格特征 | 参考图数量 |
|------|---------|-----------|
| Annie Leibovitz | 好莱坞叙事人像、电影感布景、名人肖像 | 15张风格参考 |
| Yousuf Karsh | 经典黑白伟人肖像、戏剧性灯光 | 3张WikiMedia原作 |
| Richard Avedon | 极简纯白背景、捕捉真实情绪 | 15张风格参考 |
| Irving Penn | 经典时尚、精细布光、静物人像 | 15张风格参考 |
| Jeanloup Sieff | 法式简约、柔焦美学、广角人像 | 15张风格参考 |
| Diane Arbus | 边缘人群、直面闪光、挑衅性纪实 | 15张风格参考 |
| Arnold Newman | 环境肖像、人物与空间融合 | 15张风格参考 |
| August Sander | 系统化德国社会肖像、客观记录 | 1张WikiMedia原作 |
| Edward Weston | 极简人体、静物摄影、精密对焦 | 6张WikiMedia原作 |
| Cindy Sherman | 概念自拍、身份表达、角色扮演 | 15张风格参考 |

### 风光摄影（4位）

| 大师 | 风格特征 | 参考图数量 |
|------|---------|-----------|
| Ansel Adams | 黑白大画幅、区域曝光法、荒野风光 | 12张WikiMedia原作 |
| Frans Lanting | 国家地理风格、自然生态叙事 | 15张风格参考 |
| Charlie Waite | 欧洲田园、极简风光、柔和光影 | 15张风格参考 |
| Carleton Watkins | 早期大画幅、美国西部、约塞米蒂 | 8张WikiMedia原作 |

### 纪实摄影（6位）

| 大师 | 风格特征 | 参考图数量 |
|------|---------|-----------|
| Henri Cartier-Bresson | 决定性瞬间、街头纪实、35mm | 15张风格参考 |
| Dorothea Lange | 大萧条社会纪实、人道主义 | 8张WikiMedia原作+15张风格参考 |
| Steve McCurry | 人文色彩叙事、阿富汗少女 | 15张风格参考 |
| Sebastiao Salgado | 黑白史诗、全球劳工与自然 | 15张风格参考 |
| W. Eugene Smith | 深度图片报道、水俣病 | 15张风格参考 |
| Walker Evans | 美国大萧条乡村纪实、建筑 | 8张WikiMedia原作 |

### 星空+生态摄影（9位）

Rogelio Bernal Andreo、Adam Block、Babak Tafreshi、Joel Sartore、Paul Nicklen、Nick Brandt、Steve Winter、Cristina Mittermeier（各含独立MD文档）

### 建筑摄影（4位）

Ezra Stoller、Julius Shulman、Iwan Baan、Michael Wolf（各含独立MD文档）

### 静物摄影（3位）

Robert Mapplethorpe、Paulette Tavormina、Laura Letinsky（各含独立MD文档）

## 评分标准

| 维度 | 权重 | 评估要点 |
|------|------|---------|
| 构图 | 30% | 主体位置精准度、三分法/黄金分割运用、引导线有效性、画面平衡 |
| 光影 | 25% | 曝光准确性、光质与场景适配、明暗层次丰富度、高光/阴影控制 |
| 色彩 | 20% | 白平衡准确性、色彩和谐度、色调意图表达、饱和度适中 |
| 清晰度 | 15% | 对焦准确度、无运动模糊、噪点可控、锐度适中 |
| 创意 | 10% | 视角独特性、情感表达力、叙事性、个人风格 |

## 9个Agent职责

| Agent | 职责 | 输入 | 输出 |
|-------|------|------|------|
| main_agent | 主控调度 | 用户图片+文本 | 场景分类结果+调度指令 |
| portrait_agent | 人像诊断 | 人像图片 | 光线/构图/肤色/姿态/背景诊断报告 |
| landscape_agent | 风光诊断 | 风光图片 | 层次/引导线/大气透视/HDR诊断报告 |
| documentary_agent | 纪实诊断 | 纪实图片 | 决定性瞬间/叙事/情感诊断报告 |
| starry_agent | 星空诊断 | 星空图片 | 星点锐度/光污染/堆栈质量诊断报告 |
| still_life_agent | 静物诊断 | 静物图片 | 布光/质感/景深/构图诊断报告 |
| style_agent | 风格对标 | 图片+品类 | Top-3大师匹配+5维度雷达图+差距分析 |
| retouch_agent | 修图建议 | 诊断结果 | 醒图/LR参数表+分步工作流+预设推荐 |
| pdf_export_agent | 报告导出 | 全部结果 | PDF文件(7章结构化诊断报告) |

## 使用模式

### 模式1：完整诊断（默认）
```
用户上传照片 + "帮我分析这张照片"
→ main_agent → 品类Agent(构图+光影+色彩) + style_agent(并行) → retouch_agent → pdf_export_agent
```

### 模式2：单项分析
```
用户: "只做构图分析" / "帮我看看曝光"
→ main_agent分类 → 品类Agent(仅执行指定模块) → 返回结果
```

### 模式3：风格对标
```
用户: "这张照片像哪位大师的风格？"
→ style_agent → CLIP特征匹配 → LLM深度分析 → Top-3大师+雷达图+差距报告
```

### 模式4：修图方案
```
用户: "给我醒图修图参数" / "Lightroom怎么调"
→ 品类Agent诊断 → retouch_agent → 参数表+工作流+预设推荐
```

### 模式5：学习路径
```
用户: "我想提高人像摄影水平"
→ skill_master_ref/portrait_master/ → 10位大师技法对比 → 针对性学习路径
```

## 技术依赖

| 组件 | 用途 | 版本 |
|------|------|------|
| GPT-4o / 通义千问 | 语义分析、诊断生成、报告撰写 | - |
| CLIP ViT-L/14@336px | 场景识别、风格特征匹配 | OpenAI |
| SAM 2.1 | 图像分割、主体提取、问题区域框选 | Meta |
| OpenCV | 直方图/锐度/水平线/色彩空间量化分析 | 4.10 |
| Pillow | 图像处理、蒙版叠加、格式转换 | - |
| ReportLab / WeasyPrint | PDF报告生成 | - |
| Python | 运行环境 | 3.10+ |
