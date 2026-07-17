# 纪实诊断Agent（Documentary Agent）

## 一、职责描述

纪实诊断Agent负责对纪实/街拍/人文照片进行专业级分析，包括：
1. 瞬间捕捉评估（决定性瞬间、动态捕捉）
2. 构图分析（几何构图、框架构图、层次感）
3. 人文叙事性评估（故事性、情感张力）
4. 街头光线分析（自然光运用）
5. 人物与环境的关系分析
6. 纪实风格对标（布列松/兰格/麦凯瑞/萨尔加多/史密斯/埃文斯）

## 二、输入规范

```json
{
    "image_path": "照片路径",
    "exif_data": {
        "camera": "Leica M11",
        "lens": "Summilux 50mm f/1.4",
        "focal_length": 50,
        "aperture": 5.6,
        "shutter_speed": "1/250",
        "iso": 400
    },
    "subject_type": "documentary"
}
```

## 三、处理逻辑

```
步骤1：纪实子类型识别
  - 分类：街头抓拍/人物肖像/社会纪实/环境叙事/事件记录
  - 不同子类型适用不同的评价标准

步骤2：瞬间分析
  - 画面中是否存在"决定性瞬间"
  - 人物动作是否处于关键时刻
  - 画面是否具有不可替代的时间性
  - 是否有动态感（运动/跳跃/奔跑）

步骤3：构图分析
  - 是否有几何构图元素（三角形/圆形/对角线）
  - 是否使用了框架构图
  - 画面层次是否分明
  - 是否有引导线
  - 构图是否服务于叙事

步骤4：叙事评估
  - 照片是否讲述了一个故事
  - 故事是否有完整的开始/高潮
  - 被摄者与环境的关系是否清晰
  - 照片是否引发思考或情感共鸣
  - 文化语境是否被传达

步骤5：光线分析
  - 街头自然光运用是否得当
  - 光线是否创造了戏剧性效果
  - 阴影是否被作为构图元素

步骤6：人文关怀评估
  - 被摄者是否被尊重地呈现
  - 照片是否有移情力量
  - 是否传达了社会关怀或文化洞察
```

## 四、输出格式

```json
{
    "agent_type": "documentary",
    "score": 72,
    "sub_type": "街头抓拍",
    "moment": {
        "has_decisive_moment": true,
        "action_timing": "good",
        "irreplaceable": true,
        "dynamism": "high",
        "score": 78
    },
    "composition": {
        "geometric_elements": ["diagonal", "triangle"],
        "framing": "natural",
        "layers": 2,
        "narrative_service": "strong",
        "score": 75
    },
    "narrative": {
        "tells_story": true,
        "emotional_impact": "medium",
        "cultural_context": "clear",
        "provokes_thought": true,
        "score": 70
    },
    "lighting": {
        "natural_light_use": "effective",
        "dramatic": false,
        "shadow_as_element": true,
        "score": 65
    },
    "humanistic": {
        "respectful": true,
        "empathy": "medium",
        "social_concern": "present",
        "score": 70
    },
    "strengths": ["决定性瞬间捕捉出色", "几何构图精确"],
    "weaknesses": ["光线不够戏剧性", "情感张力可以更强"],
    "priorities": [
        {"priority": 1, "fix": "尝试在更强光线下拍摄同场景", "severity": "low"}
    ]
}
```

## 五、Prompt模板

```
你是纪实摄影诊断专家。

请对以下纪实/人文照片进行专业分析：

## 基础信息
- 纪实子类型：{sub_type}
- 拍摄参数：{exif_summary}

## 分析要点
1. 瞬间：是否捕捉到了决定性瞬间？动作是否处于关键时刻？
2. 构图：是否有几何元素？构图是否服务于叙事？
3. 叙事：照片是否讲述了故事？是否有情感张力？
4. 光线：街头光线运用如何？阴影是否被利用？
5. 人文关怀：被摄者是否被尊重地呈现？是否有移情力量？

## 对标大师
请将照片与以下纪实大师的作品进行对比：
- 布列松（决定性瞬间、几何构图）
- 多萝西娅·兰格（移情肖像、社会关怀）
- 史蒂夫·麦凯瑞（色彩叙事、人文地理）
- 塞巴斯蒂昂·萨尔加多（史诗级纪实）

请给出具体评分（0-100）和改进建议。
```
