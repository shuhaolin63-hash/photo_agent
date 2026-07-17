# 安装指南

Photo Agent 支持在多种 AI IDE 中作为 Skill 插件安装使用。

## 前置要求

- AI IDE：TRAE / Claude Code / OpenClaw（任选其一）
- Python 3.10+（运行本地分析模块时需要）
- Git

## 安装方式

### 方式一：TRAE

```bash
# 克隆到当前项目的 .trae/skills 目录
mkdir -p .trae/skills
git clone https://github.com/shuhaolin63-hash/photo_agent.git .trae/skills/photo_agent
```

安装后 TRAE 会自动识别 `SKILL.md` 并注册技能。

### 方式二：Claude Code

```bash
# 克隆到当前项目的 .claude/skills 目录
mkdir -p .claude/skills
git clone https://github.com/shuhaolin63-hash/photo_agent.git .claude/skills/photo_agent
```

### 方式三：OpenClaw

```bash
# 克隆到全局 skills 目录
git clone https://github.com/shuhaolin63-hash/photo_agent.git ~/.openclaw/workspace/skills/photo_agent
```

## 验证安装

安装完成后，在 AI IDE 中输入以下任意指令测试：

```
帮我分析这张照片
```

上传一张照片配合上述指令，如果系统自动进入摄影诊断流程，说明安装成功。

## 可选：本地分析引擎

如需启用 OpenCV 本地量化分析（构图检测、直方图统计等），需安装 Python 依赖：

```bash
pip install opencv-python>=4.8 Pillow numpy scikit-learn
```

CLIP 和 SAM 模型需额外下载：

```bash
pip install torch transformers
# CLIP 模型会在首次运行时自动下载
# SAM 2.1 模型需手动下载到 ./models/ 目录
```

> 注意：本地分析引擎为可选项。即使不安装，LLM 仍可通过视觉理解完成诊断，只是缺少量化数据。

## 目录结构说明

| 路径 | 说明 |
|------|------|
| `SKILL.md` | 技能注册文件，AI IDE 通过此文件识别和加载技能 |
| `agent_config.yaml` | 全局配置：技术栈、Agent 定义、调度协议、PDF 模板 |
| `摄影_skills/` | 核心知识库：分析规则、大师资料、修图方案、报告模板 |
| `agents/` | 9 个 Agent 的职责定义和 Prompt 模板 |
| `reference/` | 参考图库：大师作品、问题样本 |
| `assets/` | 素材资源：构图蒙版、色轮、曝光三角图 |
| `scripts/` | 伪代码脚本：调度、构图检测、风格比对等 |

## 常见问题

**Q: 安装后 AI IDE 没有识别到技能？**

确保 `SKILL.md` 位于正确的 skills 目录下，且文件包含有效的 YAML frontmatter（`name` 和 `description` 字段）。

**Q: 参考图库很大，可以不下载吗？**

可以。`reference/` 目录中的图片是风格对标参考，不影响基础诊断功能。使用 `--depth 1` 浅克隆可跳过大文件：

```bash
git clone --depth 1 https://github.com/shuhaolin63-hash/photo_agent.git .trae/skills/photo_agent
```

**Q: 如何更新到最新版本？**

```bash
cd .trae/skills/photo_agent  # 或你安装的对应路径
git pull origin main
```
