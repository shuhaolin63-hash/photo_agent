# 修图建议库说明

## 一、概述

本目录用于存储修图建议的模板和参考素材。当系统诊断出用户照片中的问题后，会从修图建议库中匹配相应的修图方案，生成个性化的修图教程。

## 二、建议库结构

```
retouch_suggest_lib/
├── exposure_fix/           # 曝光修正方案
│   ├── overexposure_fix.json
│   ├── underexposure_fix.json
│   └── highlight_recovery.json
├── composition_fix/         # 构图修正方案
│   ├── horizon_correction.json
│   ├── crop_recommendation.json
│   └── clutter_removal.json
├── color_fix/              # 色彩修正方案
│   ├── wb_correction.json
│   ├── saturation_adjust.json
│   └── color_cast_remove.json
├── focus_fix/              # 对焦修正方案
│   ├── sharpening_basic.json
│   └── noise_reduction.json
├── style_enhance/          # 风格增强方案
│   ├── bw_conversion.json
│   ├── film_simulation.json
│   └── color_grading.json
└── before_after/           # 修图前后对比示例
    ├── portrait/
    ├── landscape/
    └── street/
```

## 三、建议条目格式

每个修图建议条目使用JSON格式：

```json
{
    "id": "fix_001",
    "problem_code": "EXP-001",
    "problem_name": "过曝",
    "severity": "high",
    "description": "照片整体过曝，高光区域丢失细节",
    "applicable_subjects": ["portrait", "landscape", "street", "still_life"],
    "software": {
        "lightroom": {
            "steps": [
                {
                    "tool": "基础面板",
                    "params": {
                        "exposure": -0.5,
                        "highlights": -60,
                        "whites": -30
                    },
                    "note": "先降低全局曝光，再单独压回高光"
                },
                {
                    "tool": "色调曲线",
                    "params": {
                        "highlights_point": {"x": 0.75, "y": 0.65},
                        "whites_point": {"x": 0.9, "y": 0.8}
                    },
                    "note": "用曲线精确控制高光压回幅度"
                }
            ],
            "expected_result": "高光区域恢复细节，整体曝光恢复正常",
            "side_effects": "阴影可能变暗，需要同步调整"
        },
        "xingtuparams": {
            "steps": [
                {
                    "tool": "调整 > 光感",
                    "params": {"光感": -15},
                    "note": "降低整体亮度"
                },
                {
                    "tool": "调整 > 高光",
                    "params": {"高光": -30},
                    "note": "压回高光"
                }
            ]
        }
    },
    "tips": [
        "如果过曝严重（高光完全纯白），可能无法完全恢复",
        "RAW文件比JPEG有更多恢复空间",
        "建议拍摄时使用曝光补偿-0.3~-0.7预防过曝"
    ],
    "before_after_ref": "before_after/exposure/overexposure_fix_01.jpg"
}
```

## 四、常见修图建议分类

### 4.1 曝光修正

| 问题 | 修图方案 | 难度 | 预估耗时 |
|------|----------|------|----------|
| 过曝 | 降低曝光 + 压回高光 + 曲线控制 | 初级 | 30秒 |
| 欠曝 | 提升曝光 + 提亮阴影 + 降噪 | 初级 | 30秒 |
| 高光溢出 | 压回高光 + 白色滑块 + 曲线 | 中级 | 1分钟 |
| 暗部缺失 | 提亮阴影 + 黑色滑块 + 降噪 | 中级 | 1分钟 |
| 曝光不均 | 渐变滤镜 + 局部蒙版调整 | 中级 | 2分钟 |

### 4.2 构图修正

| 问题 | 修图方案 | 难度 | 预估耗时 |
|------|----------|------|----------|
| 水平线倾斜 | 裁剪工具旋转校正 | 初级 | 15秒 |
| 主体偏移 | 裁剪重新构图 | 初级 | 30秒 |
| 前景杂乱 | 克隆工具去除杂物 | 中级 | 2-5分钟 |
| 留白过多 | 裁剪放大主体 | 初级 | 30秒 |
| 透视畸变 | Transform面板校正 | 中级 | 1分钟 |
| 干扰物 | 克隆/修复画笔 | 中级 | 1-3分钟 |

### 4.3 色彩修正

| 问题 | 修图方案 | 难度 | 预估耗时 |
|------|----------|------|----------|
| 白平衡偏色 | 白平衡滑块/灰场校正 | 初级 | 15秒 |
| 过饱和 | 降低全局饱和度/HSL单通道 | 初级 | 30秒 |
| 不饱和 | 提升鲜艳度/饱和度 | 初级 | 15秒 |
| 色差/紫边 | 镜头校正面板/色差去除 | 初级 | 15秒 |
| 彩色噪点 | Color降噪 + Luminance降噪 | 中级 | 30秒 |

### 4.4 对焦/锐度修正

| 问题 | 修图方案 | 难度 | 预估耗时 |
|------|----------|------|----------|
| 轻微失焦 | 锐化面板 + Unsharp Mask | 中级 | 1分钟 |
| 全局模糊 | 锐化 + 清晰度增强 | 中级 | 1分钟 |
| 噪点 | 降噪面板 + AI降噪 | 初级 | 30秒 |

### 4.5 风格增强

| 方案 | 描述 | 难度 | 预估耗时 |
|------|------|------|----------|
| 黑白转换 | B&W面板 + 混色器 + 分离色调 | 中级 | 1-2分钟 |
| 胶片模拟 | 颗粒 + 色彩偏移 + 曲线 | 中级 | 2-3分钟 |
| 情绪色调 | 分离色调 + HSL + 渐变滤镜 | 中级 | 2-3分钟 |
| HDR效果 | 阴影/高光极端调整 + Dehaze | 中级 | 2分钟 |

## 五、建议生成逻辑

```
输入：问题诊断结果列表
│
├── 按严重程度排序（高→低）
│
├── 对每个问题匹配修图方案：
│   ├── 从retouch_suggest_lib中查找匹配条目
│   ├── 如果找不到精确匹配，选择最接近的方案
│   └── 根据用户照片的具体参数微调建议值
│
├── 检查修图方案之间的冲突：
│   ├── 例如：曝光修正可能影响对比度
│   ├── 例如：降噪可能影响锐度
│   └── 调整步骤顺序避免冲突
│
├── 生成修图步骤序列：
│   ├── 步骤1：基础校正（水平线/畸变/色差）
│   ├── 步骤2：曝光与影调
│   ├── 步骤3：色彩调整
│   ├── 步骤4：局部精修
│   ├── 步骤5：锐化与降噪
│   └── 步骤6：风格增强（可选）
│
└── 输出：修图教程JSON → 传递给PDF生成模块
```

## 六、修图前后对比示例管理

```
before_after/目录组织：
- 每个示例包含3个文件：
  1. before.jpg（修图前）
  2. after.jpg（修图后）
  3. metadata.json（修图参数记录）

metadata.json格式：
{
    "original_problem": "EXP-001",
    "fix_applied": "过曝修正",
    "software": "Lightroom Classic CC",
    "params": { ... },
    "difficulty": "初级",
    "time_spent": "30秒"
}
```
