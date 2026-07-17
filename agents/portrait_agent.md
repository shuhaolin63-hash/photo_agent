# 人像诊断Agent（Portrait Agent）

## 一、职责描述

人像诊断Agent负责对人像照片进行专业级分析，包括：
1. 人物面部表情和姿态评估
2. 肖像构图分析（中心化/三分法/环境肖像）
3. 人像光线分析（自然光/闪光灯/混合光）
4. 肤色和质感分析
5. 焦点和对焦准确性检查
6. 背景虚化和景深评估
7. 人像风格对标（兰格/麦凯瑞/阿维顿等）

## 二、输入规范

```json
{
    "image_path": "照片路径",
    "exif_data": {
        "camera": "Canon EOS R5",
        "lens": "RF 85mm f/1.2",
        "focal_length": 85,
        "aperture": 2.0,
        "shutter_speed": "1/250",
        "iso": 400
    },
    "subject_type": "portrait"
}
```

## 三、处理逻辑

```
步骤1：人脸检测
  - 检测画面中的人脸数量和位置
  - 定位眼睛、鼻子、嘴巴的关键点
  - 计算面部在画面中的占比

步骤2：肖像构图分析
  - 判断构图类型：特写/半身/全身/环境肖像
  - 评估主体位置（是否遵循三分法）
  - 评估画面比例（是否留有呼吸空间）
  - 检查是否切断了不合适的身体部位

步骤3：光线分析
  - 检测光照方向（正面/侧面/逆光/顶光）
  - 评估光质（硬光/柔光/混合光）
  - 检查是否存在不自然的阴影（如" raccoon eyes"）
  - 评估眼神光（catchlight）是否存在

步骤4：肤色分析
  - 评估肤色是否自然
  - 检测肤色偏色（偏黄/偏红/偏青）
  - 评估肤色均匀度

步骤5：对焦与锐度
  - 检查眼睛是否精准对焦
  - 评估面部锐度
  - 评估景深是否合适（人像虚化效果）

步骤6：背景评估
  - 评估背景虚化程度
  - 检查背景是否有干扰元素
  - 评估背景与人物的色彩关系

步骤7：情感表达评估
  - 评估被摄者的表情自然度
  - 评估照片的情感张力
  - 评估人像的整体"气场"
```

## 四、输出格式

```json
{
    "agent_type": "portrait",
    "score": 75,
    "portrait_type": "半身肖像",
    "face_detection": {
        "num_faces": 1,
        "face_position": "center-right",
        "face_ratio": 0.15,
        "eyes_focused": true
    },
    "composition": {
        "rule_of_thirds_score": 0.8,
        "breathing_space": "adequate",
        "crop_issues": "none"
    },
    "lighting": {
        "direction": "side",
        "quality": "soft",
        "catchlight": true,
        "unnatural_shadows": false
    },
    "skin_tone": {
        "natural": true,
        "cast": "slight_warm",
        "evenness": 0.7
    },
    "focus": {
        "eye_sharpness": "excellent",
        "overall_sharpness": "good",
        "dof_appropriate": true
    },
    "background": {
        "bokeh_quality": "smooth",
        "distractions": "minimal",
        "color_harmony": "good"
    },
    "strengths": ["光线柔和自然", "眼神对焦精准"],
    "weaknesses": ["背景有轻微干扰", "肤色略偏暖"],
    "priorities": [
        {"priority": 1, "fix": "去除背景干扰元素", "severity": "low"}
    ]
}
```

## 五、Prompt模板

```
你是人像摄影诊断专家。

请对以下人像照片进行专业分析：

## 基础信息
- 构图类型：{portrait_type}
- 拍摄参数：{exif_summary}

## 分析要点
1. 肖像构图是否合理？人物位置和比例如何？
2. 光线运用是否得当？光质和方向如何？
3. 肤色是否自然？有无偏色或暗角问题？
4. 对焦是否精准？眼睛是否清晰？
5. 背景处理如何？虚化是否自然？
6. 整体人像"气场"如何？情感表达是否到位？

## 对标大师
请将照片与以下人像大师的作品进行对比：
- 多萝西娅·兰格（移情肖像）
- 史蒂夫·麦凯瑞（色彩肖像）
- 理查德·阿维顿（纯白背景肖像）

请给出具体评分（0-100）和改进建议。
```
