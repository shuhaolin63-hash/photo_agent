# 星空诊断Agent（Starry Agent）

## 一、职责描述

星空诊断Agent负责对星空/天文摄影照片进行专业级分析，包括：
1. 星空子类型识别（银河/星轨/深空/极光/月景）
2. 银河核心可见度和构图
3. 星点质量评估（圆度、拖尾、噪点）
4. 曝光参数评估（ISO/曝光时间/光圈）
5. 前景与星空的平衡
6. 色彩和降噪处理评估
7. 星空大师对标

## 二、输入规范

```json
{
    "image_path": "照片路径",
    "exif_data": {
        "camera": "Nikon Z6 II",
        "lens": "Nikkor Z 14-24mm f/2.8 S",
        "focal_length": 14,
        "aperture": 2.8,
        "shutter_speed": "20",
        "iso": 3200
    },
    "subject_type": "starry"
}
```

## 三、处理逻辑

```
步骤1：星空子类型识别
  - 分类：银河拱桥/银河核心/星轨/深空天体/极光/月景/星空全景
  - 不同子类型适用不同的评价标准

步骤2：银河分析（如适用）
  - 银河核心是否可见
  - 银河结构/层次是否清晰
  - 银河在构图中的位置

步骤3：星点质量评估
  - 星点是否圆（无拖尾）
  - 星点是否过曝（光晕）
  - 星点数量和密度
  - 500法则是否遵守（是否有星轨）

步骤4：曝光参数评估
  - ISO选择是否合理
  - 曝光时间是否合适（不过长导致星轨）
  - 光圈是否足够大
  - 结合EXIF判断参数是否最优

步骤5：前景评估
  - 是否有前景元素
  - 前景是否清晰
  - 前景与星空的曝光是否平衡
  - 前景是否增强了叙事

步骤6：噪点评估
  - 星空区域噪点水平
  - 暗部区域噪点水平
  - 降噪是否过度（星星变成光斑）
  - 是否使用了叠加技术

步骤7：色彩评估
  - 天空背景色彩是否自然
  - 银河色彩是否保留（金黄色核心/蓝紫色臂）
  - 是否有光污染影响
  - 分离色调处理是否恰当

步骤8：500法则验证
  - 计算最大无星轨曝光时间
  - 与实际曝光时间对比
  - 判断是否存在星轨拖尾
```

## 四、输出格式

```json
{
    "agent_type": "starry",
    "score": 68,
    "sub_type": "银河核心",
    "milky_way": {
        "core_visible": true,
        "structure_clarity": 0.6,
        "position_in_frame": "center",
        "score": 72
    },
    "star_quality": {
        "roundness": "good",
        "trailing": "none",
        "overexposure": "minimal",
        "density": "high",
        "score": 75
    },
    "exposure_params": {
        "iso_reasonable": true,
        "exposure_time_ok": true,
        "aperture_wide_enough": true,
        "rule_500_compliant": true,
        "optimal": false,
        "suggestion": "可尝试ISO 6400+曝光10秒获得更多银河细节",
        "score": 70
    },
    "foreground": {
        "has_foreground": true,
        "foreground_sharp": true,
        "exposure_balanced": false,
        "narrative_contribution": "medium",
        "score": 60
    },
    "noise": {
        "sky_noise": "medium",
        "shadow_noise": "high",
        "over_denoised": false,
        "score": 60
    },
    "color": {
        "sky_natural": true,
        "milky_way_color": "partial",
        "light_pollution": "moderate",
        "score": 68
    },
    "strengths": ["银河核心清晰可见", "星点质量良好"],
    "weaknesses": ["前景与星空曝光不平衡", "暗部噪点明显"],
    "priorities": [
        {"priority": 1, "fix": "建议使用双曝光合成解决前景曝光", "severity": "medium"},
        {"priority": 2, "fix": "加强降噪处理", "severity": "medium"}
    ]
}
```

## 五、Prompt模板

```
你是星空摄影诊断专家。

请对以下星空照片进行专业分析：

## 基础信息
- 星空子类型：{sub_type}
- 拍摄参数：{exif_summary}
- 最大无星轨时间（500法则）：{max_exposure}s

## 分析要点
1. 银河：核心是否可见？结构是否清晰？构图位置如何？
2. 星点：是否圆？有无拖尾？密度如何？
3. 曝光：ISO/时间/光圈是否合理？是否遵守500法则？
4. 前景：是否有前景？清晰度？与星空曝光平衡？
5. 噪点：星空和暗部噪点水平？降噪是否过度？
6. 色彩：天空背景色彩？银河色彩？光污染？

请给出具体评分（0-100）和改进建议，特别是拍摄参数优化和后期处理建议。
```
