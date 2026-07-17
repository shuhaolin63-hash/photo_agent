# 风格对标Agent（Style Agent）

## 一、职责描述

风格对标Agent负责分析用户照片的整体风格特征，并将其与摄影大师的风格进行比对，包括：
1. 提取照片的风格特征向量（色调/影调/构图/光影/题材）
2. 使用CLIP模型进行向量比对
3. 基于特征向量的精确匹配
4. 检测混合风格
5. 生成个性化风格发展建议
6. 推荐学习路径

## 二、输入规范

```json
{
    "image_path": "照片路径",
    "subject_type": "landscape",
    "master_library_path": "master_style_vectors.json"
}
```

## 三、处理逻辑

```
步骤1：CLIP向量提取
  - 使用CLIP Vision Encoder（ViT-B/32）
  - 将图像缩放至224x224
  - 提取512维图像嵌入向量
  - L2归一化

步骤2：CLIP粗筛
  - 计算用户向量与所有大师向量的余弦相似度
  - 过滤低相似度结果（<0.3）
  - 返回Top-5候选大师

步骤3：特征向量精排
  - 对Top-5候选大师进行详细特征比对
  - 计算加权欧氏距离：
    - color: 权重0.25
    - tone: 权重0.25
    - composition: 权重0.25
    - light: 权重0.15
    - subject: 权重0.10
  - 距离越小匹配度越高

步骤4：匹配度计算
  - match_score = (1 - normalized_distance) * 100
  - 匹配度分级：
    - 90-100%：高度匹配
    - 70-89%：中度匹配
    - 50-69%：低度匹配
    - <50%：风格差异较大

步骤5：混合风格检测
  - 如果Top-2差距 <10%，判定为混合风格
  - 分析混合比例和元素来源

步骤6：建议生成
  - 根据匹配度和差距分析，生成针对性建议
  - 包含短期/中期/长期学习路径
  - 推荐大师作品和书籍
  - 推荐具体练习
```

## 四、输出格式

```json
{
    "agent_type": "style",
    "clip_vector": [512 floats],
    "feature_vector": {
        "color": { "..." },
        "tone": { "..." },
        "composition": { "..." },
        "light": { "..." },
        "subject": { "..." }
    },
    "matches": [
        {
            "rank": 1,
            "master_id": "ansel_adams",
            "master_name": "安塞尔·亚当斯",
            "match_score": 78,
            "clip_similarity": 0.72,
            "match_level": "中度匹配",
            "similar_features": ["黑白影调", "三层纵深", "侧光"],
            "different_features": ["缺少前景引导线", "暗部细节不足"]
        }
    ],
    "mixed_style": null,
    "suggestions": {
        "short_term": "练习区域曝光系统，提高暗部细节保留",
        "medium_term": "尝试在三张照片中使用前景引导线",
        "long_term": "规划一个为期3个月的黑白风光专题项目",
        "recommended_reading": ["《摄影基础丛书》- Ansel Adams"],
        "recommended_exercises": [
            "连续7天只用黑白模式拍摄",
            "练习三层纵深构图"
        ]
    }
}
```

## 五、Prompt模板

```
你是摄影风格分析专家。

请分析以下照片的整体风格，并与摄影大师进行风格对标：

## 照片信息
- 题材：{subject_type}

## 分析要点
1. 色调：整体色调倾向？色彩饱和度？冷暖关系？
2. 影调：曝光/对比度？高光/暗部处理？色调范围？
3. 构图：构图风格？对称/不对称？留白程度？
4. 光影：光线方向/质量？戏剧性？
5. 氛围：整体情绪？独特气质？

## 大师风格库
以下大师可供对标：
- 风光：亚当斯/韦特/兰廷/沃特金斯
- 纪实：布列松/兰格/麦凯瑞/萨尔加多/史密斯/埃文斯
- 星空：Wally Pacholka / David Malin
- 建筑：Ezra Stoller / Julius Shulman
- 静物：Irving Penn

请给出：
1. Top-3最匹配的大师及匹配度
2. 与每位大师的相似点和差异点
3. 混合风格判断（如适用）
4. 风格发展建议（短期/中期/长期）
```
