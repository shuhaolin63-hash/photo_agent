# 静物诊断Agent（Still Life Agent）

## 一、职责描述

静物诊断Agent负责对静物/美食/建筑/微距照片进行专业级分析，包括：
1. 静物子类型识别（美食/产品/室内/微距/建筑）
2. 主体清晰度和质感表现
3. 布光分析（方向/数量/光比/质感）
4. 构图分析（角度/排列/留白/背景）
5. 色彩和色调分析
6. 景深控制评估
7. 背景处理评估

## 二、输入规范

```json
{
    "image_path": "照片路径",
    "exif_data": {
        "camera": "Canon EOS R5",
        "lens": "RF 100mm f/2.8 Macro",
        "focal_length": 100,
        "aperture": 8,
        "shutter_speed": "1/125",
        "iso": 200
    },
    "subject_type": "still_life"
}
```

## 三、处理逻辑

```
步骤1：静物子类型识别
  - 分类：美食/产品摄影/室内静物/微距花卉/建筑/商品
  - 不同子类型适用不同的评价标准

步骤2：主体分析
  - 主体是否清晰锐利
  - 质感表现如何（光泽/粗糙/透明/柔软）
  - 主体在画面中的大小是否合适
  - 主体形态是否吸引人

步骤3：布光分析
  - 光源方向和数量（单灯/双灯/自然光）
  - 主光与补光的光比
  - 高光和阴影的分布
  - 是否有不需要的反射/高光
  - 美食类：是否让食物看起来有食欲

步骤4：构图分析
  - 拍摄角度（俯拍/45度/平视/低角度）
  - 物品排列的节奏感和平衡感
  - 留白是否恰当
  - 背景是否简洁
  - 是否有道具增强叙事

步骤5：景深控制
  - 景深范围是否覆盖主体
  - 背景虚化是否自然
  - 微距类：焦点堆叠是否需要

步骤6：色彩分析
  - 色彩搭配是否和谐
  - 色温是否恰当
  - 美食类：色彩是否令人有食欲
  - 是否有色彩偏移
```

## 四、输出格式

```json
{
    "agent_type": "still_life",
    "score": 72,
    "sub_type": "美食",
    "subject": {
        "sharpness": "excellent",
        "texture_rendering": "good",
        "size_ratio": "appropriate",
        "appeal": "good",
        "score": 75
    },
    "lighting": {
        "direction": "side_back",
        "setup": "single_natural",
        "ratio": "2:1",
        "reflection": "controlled",
        "appetite_appeal": "good",
        "score": 70
    },
    "composition": {
        "angle": "45_degree",
        "arrangement_rhythm": "good",
        "negative_space": "balanced",
        "background_clean": true,
        "props": "minimal",
        "score": 70
    },
    "depth_of_field": {
        "covers_subject": true,
        "background_bokeh": "smooth",
        "needs_focus_stack": false,
        "score": 72
    },
    "color": {
        "harmony": "warm_tones",
        "temperature": "appropriate",
        "appetizing": true,
        "cast": "none",
        "score": 72
    },
    "strengths": ["主体质感表现出色", "色彩暖调令人有食欲"],
    "weaknesses": ["背景可以更简洁", "可以增加前景装饰"],
    "priorities": [
        {"priority": 1, "fix": "简化背景，去除多余元素", "severity": "low"},
        {"priority": 2, "fix": "增加前景道具增加层次感", "severity": "low"}
    ]
}
```

## 五、Prompt模板

```
你是静物/美食摄影诊断专家。

请对以下静物照片进行专业分析：

## 基础信息
- 静物子类型：{sub_type}
- 拍摄参数：{exif_summary}

## 分析要点
1. 主体：清晰度？质感表现？吸引力？
2. 布光：光源方向？光比？是否有不需要的反射？
3. 构图：拍摄角度？排列节奏？留白？背景？
4. 景深：是否覆盖主体？虚化是否自然？
5. 色彩：搭配是否和谐？是否令人有食欲/购买欲？

请给出具体评分（0-100）和改进建议。
```
