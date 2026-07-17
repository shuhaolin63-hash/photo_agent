# 风光诊断Agent（Landscape Agent）

## 一、职责描述

风光诊断Agent负责对风光照片进行专业级分析，包括：
1. 风光构图分析（三层纵深、前景引导线、水平线）
2. 光线分析（黄金时刻、逆光、侧光、漫射光）
3. 影调分析（高动态范围、暗部/亮部细节）
4. 天空与地面的处理评估
5. 色彩和氛围分析
6. 风光风格对标（亚当斯/韦特/兰廷/沃特金斯）
7. HDR和滤镜使用建议

## 二、输入规范

```json
{
    "image_path": "照片路径",
    "exif_data": {
        "camera": "Sony A7R IV",
        "lens": "FE 16-35mm f/2.8 GM",
        "focal_length": 24,
        "aperture": 11,
        "shutter_speed": "1/125",
        "iso": 100,
        "filters_used": "ND 0.9 GND"
    },
    "subject_type": "landscape"
}
```

## 三、处理逻辑

```
步骤1：风光子类型识别
  - 分类：山脉/海洋/森林/沙漠/湖泊/城市天际线/田园/瀑布
  - 不同子类型适用不同的评价标准

步骤2：构图分析
  - 前景-中景-远景三层结构是否存在
  - 前景引导线是否有效
  - 水平线位置和倾斜度
  - 画面是否有明确的视觉中心
  - 是否使用了极简或密集构图
  - 负空间比例是否恰当

步骤3：光线分析
  - 光线方向和时段判断（黄金时刻/蓝调时刻/正午/阴天）
  - 光质评估（硬光/柔光）
  - 光影是否为画面增添了戏剧性
  - 是否存在曝光不均匀区域

步骤4：影调分析
  - 高光是否溢出（天空过曝）
  - 暗部是否有细节（岩石/树木死黑）
  - 整体对比度是否恰当
  - 直方图分布形态评估

步骤5：天空分析
  - 天空色彩和质感
  - 云层是否有层次
  - 天空是否过曝或平淡
  - 天空与地面的曝光平衡

步骤6：色彩分析
  - 整体色调倾向（暖/冷/中性）
  - 色彩饱和度是否恰当
  - 是否存在不自然的色彩
  - 季节/时间的色彩表现

步骤7：技术完成度
  - 焦点是否准确（全景深检查）
  - 锐度是否足够
  - 是否有明显的镜头问题（畸变/色差/暗角）
```

## 四、输出格式

```json
{
    "agent_type": "landscape",
    "score": 70,
    "sub_type": "山脉风光",
    "composition": {
        "has_three_layers": true,
        "leading_lines": ["river_diagonal"],
        "horizon_level": true,
        "horizon_angle": -0.5,
        "visual_center": "mountain_peak",
        "negative_space": "balanced",
        "score": 75
    },
    "lighting": {
        "time_of_day": "golden_hour",
        "direction": "side",
        "quality": "hard",
        "dramatic": true,
        "score": 80
    },
    "tonality": {
        "highlight_clip": false,
        "shadow_detail": true,
        "contrast": "medium_high",
        "dynamic_range": "wide",
        "score": 65
    },
    "sky": {
        "quality": "layered_clouds",
        "overexposed": false,
        "color_balance": "good",
        "score": 75
    },
    "color": {
        "temperature": "warm",
        "saturation": "natural",
        "harmony": "good",
        "score": 70
    },
    "technical": {
        "focus": "accurate",
        "sharpness": "good",
        "distortion": "minimal",
        "chromatic_aberration": "none",
        "vignetting": "slight",
        "score": 70
    },
    "strengths": ["光线戏剧性出色", "三层纵深结构清晰"],
    "weaknesses": ["暗部细节略有不足", "天空色彩可以更丰富"],
    "priorities": [
        {"priority": 1, "fix": "提亮前景暗部细节", "severity": "medium"},
        {"priority": 2, "fix": "增强天空渐变色彩", "severity": "low"}
    ]
}
```

## 五、Prompt模板

```
你是风光摄影诊断专家。

请对以下风光照片进行专业分析：

## 基础信息
- 风光子类型：{sub_type}
- 拍摄参数：{exif_summary}

## 分析要点
1. 构图：是否有前景-中景-远景三层结构？引导线是否有效？水平线如何？
2. 光线：光线时段/方向/光质如何？是否增强了画面的戏剧性？
3. 影调：高光/暗部是否都有细节？对比度是否恰当？
4. 天空：天空质量如何？与地面曝光是否平衡？
5. 色彩：整体色调是否和谐？饱和度是否恰当？
6. 技术：对焦、锐度、畸变等技术指标如何？

## 对标大师
请将照片与以下风光大师的作品进行对比：
- 安塞尔·亚当斯（黑白影调、三层纵深）
- 查理·韦特（极简留白、柔光）
- 弗兰斯·兰廷（生态叙事、色彩）

请给出具体评分（0-100）和改进建议。
```
