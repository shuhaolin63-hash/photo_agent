# 主Agent（Main Agent）

## 一、职责描述

主Agent是Photo Agent系统的入口和调度中心，负责：
1. 接收用户上传的照片和需求
2. 对照片进行初步分析（EXIF提取、题材分类）
3. 将任务分类分发到各专项Agent
4. 收集各Agent的分析结果
5. 汇总生成综合诊断报告
6. 协调PDF导出Agent生成最终报告

## 二、输入规范

```json
{
    "image_path": "用户照片的绝对路径",
    "task_type": "full_diagnosis | composition_only | style_match_only | retouch_only | quick_review",
    "user_note": "用户的附加说明（可选）",
    "output_format": "pdf | json | text",
    "language": "zh-CN"
}
```

## 三、处理逻辑

```
步骤1：接收与校验
  - 校验照片文件格式（支持JPG/PNG/HEIF/RAW）
  - 校验文件大小（最大100MB）
  - 校验图片分辨率（最小640x480，最大200MP）

步骤2：EXIF提取
  - 提取相机/镜头/光圈/快门/ISO/白平衡/焦距
  - 提取GPS坐标（如有）
  - 提取拍摄日期时间

步骤3：题材分类
  - 使用CLIP模型进行零样本分类
  - 分类候选：portrait/landscape/documentary/street/starry/still_life/food/architecture/sport/macro
  - 选择置信度最高的分类

步骤4：任务分发
  根据task_type分发到对应Agent：
  - full_diagnosis → 专项Agent + style_agent + retouch_agent + pdf_agent
  - composition_only → composition_check模块
  - style_match_only → style_agent
  - retouch_only → retouch_agent
  - quick_review → 简化版所有Agent

步骤5：结果收集
  - 收集各Agent的返回结果
  - 检查结果完整性
  - 处理可能的Agent超时或错误

步骤6：结果汇总
  - 计算综合评分
  - 整理优势/不足列表
  - 按优先级排序改进建议
  - 生成总结文字

步骤7：报告生成（如需PDF）
  - 调用pdf_export_agent生成PDF报告
  - 返回报告文件路径
```

## 四、输出格式

```json
{
    "status": "success | error",
    "report_id": "PD-20260713-001",
    "timestamp": "2026-07-13T14:30:00+08:00",
    "subject_type": "landscape",
    "summary": {
        "overall_score": 72.5,
        "strengths": ["光线运用出色", "色彩丰富"],
        "weaknesses": ["水平线轻微倾斜", "暗部细节不足"],
        "top_priorities": [...]
    },
    "details": {
        "specialist": { "..." },
        "composition": { "..." },
        "style_match": { "..." },
        "retouch": { "..." }
    },
    "pdf_path": "output/photo_report_20260713_143000.pdf"
}
```

## 五、Prompt模板

```
你是Photo Agent的主调度器。

任务：
1. 分析用户上传的{subject_type}类型照片
2. 协调各专项Agent完成完整诊断
3. 生成综合评分和改进建议

照片信息：
- 路径：{image_path}
- EXIF：{exif_summary}
- 用户说明：{user_note}

请按以下结构组织回复：

## 综合评分：{score}/100

## 优势
- {strength_1}
- {strength_2}

## 不足
- {weakness_1}

## 改进优先级
1. [高/中/低] {fix_1}
2. [高/中/低] {fix_2}

## 风格对标
最接近的大师：{master_name}（匹配度{match_score}%）

## 修图建议
{retouch_summary}

## 学习路径
{learning_path}
```
