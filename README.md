# Photo Agent

> 摄影诊断AI Agent系统 — 上传照片，获得构图、光影、色彩、风格对标、修图参数的完整诊断报告。

## 这是什么

Photo Agent 是一个面向摄影爱好者和专业摄影师的 AI 诊断技能。基于多 Agent 协作架构，当你在 TRAE/Claude Code 等 AI IDE 中上传一张照片并请求分析时，系统会自动执行：

**场景识别 → 构图/光影/色彩诊断 → 大师风格对标 → 修图方案生成 → PDF诊断报告输出**

支持 7 大摄影品类：人像、风光、纪实、星空、生态、建筑、静物。

## 它做什么

| 能力 | 说明 |
|------|------|
| **构图诊断** | 三分法合规度、黄金分割、引导线、视觉重心、对称性分析 |
| **光影分析** | 直方图评估、高光溢出/阴影死黑检测、曝光偏差、光线质量 |
| **色彩评估** | 色温偏差、白平衡、HSL 通道分析、色彩和谐度 |
| **风格对标** | 与 36 位大师作品进行 5 维度对比（用光/构图/色调/叙事/后期） |
| **修图建议** | 醒图/Lightroom 参数表 + 分步工作流 + 10 套场景预设 |
| **PDF 报告** | 7 章结构化诊断报告，含评分、雷达图、修图方案 |
| **学习路径** | 基于诊断结果的针对性提升建议和大师学习推荐 |

## 安装

### TRAE

```bash
# 安装到当前项目
mkdir -p .trae/skills
git clone https://github.com/shuhaolin63-hash/photo_agent.git .trae/skills/photo_agent
```

### Claude Code

```bash
# 安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/shuhaolin63-hash/photo_agent.git .claude/skills/photo_agent
```

### OpenClaw

```bash
# 安装到全局
git clone https://github.com/shuhaolin63-hash/photo_agent.git ~/.openclaw/workspace/skills/photo_agent
```

## 使用

上传一张照片，搭配以下任意指令即可触发：

| 意图 | 示例 |
|------|------|
| 综合诊断 | `帮我分析这张照片` `摄影诊断` `这张照片拍得怎么样` |
| 构图分析 | `构图分析` `构图怎么样` `三分法` |
| 光影分析 | `光线分析` `曝光怎么样` `过曝` `欠曝` |
| 色彩评估 | `色彩分析` `色温` `偏色` `白平衡` |
| 风格对标 | `风格对标` `像不像XX风格` `大师风格` |
| 修图建议 | `怎么修图` `Lightroom参数` `醒图参数` `PS怎么调` |

## 诊断模式

| 模式 | 触发方式 | 执行流程 |
|------|---------|---------|
| 完整诊断 | 上传照片 + "帮我分析" | 全部 5 步：分类 → 诊断 → 对标 → 修图 → PDF |
| 单项分析 | "只做构图分析" | 仅执行指定模块 |
| 风格对标 | "这张像哪位大师" | CLIP 匹配 + LLM 深度分析 |
| 修图方案 | "给我修图参数" | 诊断 + 参数表 + 工作流 |
| 学习路径 | "我想提高人像水平" | 大师对比 + 针对性建议 |

## 评分体系

| 维度 | 权重 | 评估要点 |
|------|------|---------|
| 构图 | 30% | 主体位置、三分法/黄金分割、引导线、画面平衡 |
| 光影 | 25% | 曝光准确性、光质适配、明暗层次、高光/阴影控制 |
| 色彩 | 20% | 白平衡、色彩和谐度、色调意图、饱和度 |
| 清晰度 | 15% | 对焦准确度、运动模糊、噪点水平 |
| 创意 | 10% | 视角独特性、情感表达、叙事性 |

## 技术依赖

| 组件 | 用途 |
|------|------|
| GPT-4o / 通义千问 | 语义分析、诊断生成 |
| CLIP ViT-L/14@336px | 场景识别、风格匹配 |
| SAM 2.1 | 图像分割、主体提取 |
| OpenCV 4.10 | 直方图/锐度/水平线量化分析 |
| ReportLab / WeasyPrint | PDF 报告生成 |
| Python 3.10+ | 运行环境 |

## 项目结构

```
photo_agent/
├── SKILL.md                          技能注册文件
├── README.md                         项目说明（本文件）
├── INSTALL.md                        安装指南
├── LICENSE                           MIT 开源协议
├── agent_config.yaml                 项目配置（技术栈/Agent/调度/PDF）
├── 摄影_skills/                      核心知识库
│   ├── skill_main.md                 技能入口文档
│   ├── skill_dispatch/               调度系统
│   │   ├── dispatch_rule.txt         场景识别规则 + Agent 分配矩阵
│   │   ├── executor.txt              JSON 输入输出规范 + Prompt 模板
│   │   └── scene_lib/README.md       5 大场景 33 子场景 CLIP 标签
│   ├── skill_analysis/               图像分析知识库
│   │   ├── base_element/             曝光三要素 / 对焦景深
│   │   ├── composition/              九宫格 / 引导线 / 对称框架
│   │   ├── light_color/              白平衡 / HSL / 光线方向
│   │   └── scene_match/              CLIP 场景分类逻辑
│   ├── skill_master_ref/             大师资料库（36 位）
│   │   ├── portrait_master/          10 位人像大师 + 汇总
│   │   ├── landscape_master/         4 位风光大师 + 汇总
│   │   ├── documentary_master/       6 位纪实大师 + 汇总
│   │   ├── starry_nature_master/     9 位星空+生态大师 + 汇总
│   │   ├── architecture_master/     4 位建筑大师 + 汇总
│   │   ├── still_life_master/        3 位静物大师 + 汇总
│   │   └── other_genre_master/       其他品类汇总
│   ├── skill_style_match/            风格匹配
│   │   ├── style_feature.txt         CLIP 风格特征提取规则
│   │   └── style_suggest.txt         风格推荐 + 发展建议
│   ├── skill_retouch/                修图方案
│   │   ├── retouch_rule.md           修图总则 + 伦理 + 流程
│   │   ├── portrait_retouch/         人像磨皮 / 调色
│   │   ├── landscape_retouch/        风光 HDR / 调色
│   │   ├── starry_retouch/           星空降噪 / 叠加
│   │   └── universal_param/          醒图参数(~840行) + Lightroom 参数
│   └── skill_export_pdf/             PDF 报告
│       ├── pdf_template.md           7 章报告模板
│       ├── mark_lib/README.md        构图标注规范
│       ├── problem_lib/README.md     常见问题分类
│       └── retouch_suggest_lib/README.md  修图建议模板
├── agents/                            9 个 Agent 定义
│   ├── main_agent.md                 主控调度
│   ├── portrait_agent.md             人像诊断
│   ├── landscape_agent.md            风光诊断
│   ├── documentary_agent.md          纪实诊断
│   ├── starry_agent.md               星空诊断
│   ├── still_life_agent.md           静物诊断
│   ├── style_agent.md                风格对标
│   ├── retouch_agent.md             修图建议
│   └── pdf_export_agent.md           PDF 导出
├── reference/                         参考图库（341 张）
│   ├── ref_photo_sample/             9 张问题对照样本
│   ├── master_works/                 大师作品参考
│   │   ├── portrait_master_photos/  人像：10 原作 + 150 风格参考
│   │   ├── landscape_master_photos/ 风光：20 原作 + 30 风格参考
│   │   ├── documentary_master_photos/ 纪实：16 原作 + 75 风格参考
│   │   └── other_master_photos/     星空/生态/建筑/静物各 25 张
│   └── photography_textbook/         摄影教材（待补充）
├── assets/                            素材资源
│   ├── grid9_mask/                   构图蒙版（三分法/黄金分割/对角线）
│   ├── element_chart/                曝光三角图解
│   ├── style_palette/                色轮参考图
│   └── pdf_mark_pic/                 PDF 标注图标（待补充）
└── scripts/                           处理脚本
    ├── dispatch_script.txt           调度伪代码
    ├── composition_check_script.txt  构图检测伪代码
    ├── master_compare_script.txt     风格比对伪代码
    ├── retouch_analysis_script.txt   修图分析伪代码
    └── pdf_render_script.txt         PDF 生成伪代码
```

## 许可证

[MIT License](LICENSE)
