<div align="center">

# Agent Speedup Estimator

**换一台更快的电脑，你的编程 Agent 到底能快多少？**

从本地 Claude Code 和 Codex 历史记录，估算硬件升级带来的实际收益。

[![Tests](https://github.com/hnewcity/agent-speedup-estimator/actions/workflows/tests.yml/badge.svg)](https://github.com/hnewcity/agent-speedup-estimator/actions/workflows/tests.yml)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](#快速开始)
[![MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

[![English](https://img.shields.io/badge/English-555555?style=for-the-badge)](../README.md)
[![简体中文](https://img.shields.io/badge/简体中文-selected-1f6feb?style=for-the-badge)](README.zh-CN.md)
[![日本語](https://img.shields.io/badge/日本語-555555?style=for-the-badge)](README.ja.md)
[![Español](https://img.shields.io/badge/Español-555555?style=for-the-badge)](README.es.md)

[快速开始](#快速开始) · [安装为 Skill](#安装为-skill) · [示例报告](example/report.md) · [英文完整参考](../README.md)

</div>

## 为什么需要它

新电脑能加快构建和测试，但无法加快远程服务器上的模型。本工具根据你已有的会话计时记录，估算硬件升级对**你实际使用方式**的影响。

举例：一次任务有 80 秒花在远程模型、20 秒花在本地工具。如果全部本地工作快一倍，总时间会从 100 秒变成 90 秒，整体约 **1.11 倍**。实际估算还会考虑工具耗时中无法随硬件缩短的部分。

> 这是估算工具，不是跑分工具。保守、预期、乐观三种情形展示不同假设，不是统计置信区间，也不提供购买建议。

## 你会得到什么

- 模型、工具、人工回复、空闲等耗时的拆解。
- 构建、测试、安装、脚本、Git、文件操作等工作负载分类。
- 基于 Geekbench 6 参考分数的对比，支持四个默认档位和自定义目标。
- 三种情形下的端到端提速、工具提速及预计节省时间。
- Markdown 摘要、可交互的离线 HTML 报告和 JSON 数据。
- Skill 和独立 Python 命令行两种用法。

基础分析仅依赖 Python 标准库，不发送网络请求，不执行历史记录中的命令。**报告支持英文和简体中文**；上方按钮切换的是 README 文档。

## 快速开始

需要 **Python 3.9+**、用于克隆仓库的 Git，以及包含受支持计时字段的本地 Claude Code 或 Codex 历史记录。

```bash
git clone https://github.com/hnewcity/agent-speedup-estimator.git
cd agent-speedup-estimator
python skills/agent-speedup-estimator/scripts/agent_speedup.py --lang zh --out ./agent-speedup-report
```

Windows 找不到 `python` 时用 `py -3`；macOS/Linux 可用 `python3`。完成后用浏览器打开 `agent-speedup-report/report.html`。

| 输出文件 | 用途 |
| --- | --- |
| `report.md` | 阅读结果摘要 |
| `report.html` | 切换目标电脑、查看图表和表格，支持离线打开 |
| `summary.json` | 在其他工具中复用汇总数据 |

压缩的 Codex 历史（`.jsonl.zst`）需要 **Python 3.14+**，或在较早版本中安装可选依赖：

```bash
python -m pip install zstandard
```

无法读取的压缩文件会计数并提示。没有可用计时记录时返回退出码 `2`，可通过 `--claude-dir` 或 `--codex-dir` 指定目录。

## 安装为 Skill

### 方式一：让 Agent 帮你安装

把下面这段话直接复制给能操作终端和文件的 Codex、Claude Code 或其他编程 Agent：

```text
请帮我安装这个 Skill：https://github.com/hnewcity/agent-speedup-estimator 。根据 README，将完整的 skills/agent-speedup-estimator 文件夹（包括 scripts/ 和 data/）安装到我当前使用的编程 Agent 的用户级 skills 目录，保留已有的本地修改。安装后，在安装目录中用 Python 3.9+ 运行 scripts/agent_speedup.py --help 验证，并告诉我安装路径。
```

### 方式二：使用 curl 安装

需要 `curl` 和 `tar`，无需安装 Git。下面的命令下载 `main` 分支源码包，只提取 Skill 文件夹。运行 Skill 仍需 Python 3.9+。重复安装会覆盖目标 Skill 文件夹中的同名文件，请先保留本地修改。

**macOS / Linux**：默认安装到 Codex；安装到 Claude Code 时，将 `skill_dir` 改成 `"$HOME/.claude/skills"`。

```bash
skill_dir="$HOME/.agents/skills"
mkdir -p "$skill_dir"
curl -fsSL https://github.com/hnewcity/agent-speedup-estimator/archive/refs/heads/main.tar.gz |
  tar -xz -C "$skill_dir" --strip-components=2 agent-speedup-estimator-main/skills/agent-speedup-estimator
```

**Windows PowerShell**：使用现代 Windows 自带的 `curl.exe` 和 `tar.exe`。安装到 Claude Code 时，将 `$skillDir` 改成 `"$HOME/.claude/skills"`。

```powershell
$skillDir = "$HOME/.agents/skills"
$archive = [System.IO.Path]::GetTempFileName()
curl.exe -fL https://github.com/hnewcity/agent-speedup-estimator/archive/refs/heads/main.tar.gz -o $archive
if ($LASTEXITCODE -ne 0) { throw "Download failed" }
New-Item -ItemType Directory -Force $skillDir | Out-Null
tar.exe -xzf $archive -C $skillDir --strip-components=2 agent-speedup-estimator-main/skills/agent-speedup-estimator
if ($LASTEXITCODE -ne 0) { throw "Extraction failed" }
Remove-Item -LiteralPath $archive
```

安装后的文件夹为所选 skills 目录中的 `agent-speedup-estimator/`。可运行 `python /path/to/agent-speedup-estimator/scripts/agent_speedup.py --help` 验证，Windows 也可使用 `py -3`。

### 方式三：从 Git 克隆目录手动复制

将 [`skills/agent-speedup-estimator`](../skills/agent-speedup-estimator) **整个文件夹**复制到对应位置，保留 `scripts/` 和 `data/`：

| Agent | 用户级目录 | 项目级目录 |
| --- | --- | --- |
| Codex | `~/.agents/skills/agent-speedup-estimator/` | `.agents/skills/agent-speedup-estimator/` |
| Claude Code | `~/.claude/skills/agent-speedup-estimator/` | `.claude/skills/agent-speedup-estimator/` |

[英文安装章节](../README.md#install-as-a-skill)提供 macOS/Linux 和 PowerShell 的复制命令。Codex 未识别新 Skill 时可重启。然后告诉 Agent：

> 用 agent-speedup-estimator 看一下这台电脑是否拖慢了我的编程 Agent，比较一下换成 Apple M4 Pro 的效果，并解释估算假设。

也可以直接问：“换台新电脑能让我的 Agent 快多少？”默认输入和执行方式见 [SKILL.md](../skills/agent-speedup-estimator/SKILL.md)。

## 常用命令

在仓库根目录运行：

```bash
# 最近 30 天，比较指定 CPU
python skills/agent-speedup-estimator/scripts/agent_speedup.py --days 30 --target "Apple M4 Pro" --lang zh

# 比较多个目标
python skills/agent-speedup-estimator/scripts/agent_speedup.py --target "Apple M4" --target "AMD Ryzen 9 9950X" --lang zh

# 自定义 Geekbench 6 分数；这里的数字仅用于演示参数
python skills/agent-speedup-estimator/scripts/agent_speedup.py --current-gb6 1500 6000 --custom-target "目标电脑" 3000 15000 --lang zh

# 查看 CPU 列表和所有参数
python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus
python skills/agent-speedup-estimator/scripts/agent_speedup.py --help
```

默认扫描 `~/.claude/projects`、`~/.codex/sessions` 和 `~/.codex/archived_sessions`，尊重 `CLAUDE_CONFIG_DIR`、`CODEX_HOME` 环境变量。可用 `--agents` 选择 Agent，用 `--current-disk` / `--target-disk` 指定磁盘类型，用 `--sensitivity` 加载自定义假设。完整参数见[英文参考](../README.md#more-examples)。

同一输出目录中的同名报告会被覆盖。未知目标名称会产生提示；所有指定目标都未匹配时，使用默认档位。`--days` 按记录或轮次结束时间筛选，不会切开跨越边界的工作。

## 估算原理

先读取时间戳和工具调用时长，在内存中将命令分类。单会话内并行工具调用的重叠时间会分摊；默认单条命令超过 300 秒的部分，在保守和预期情形下不随硬件缩短，乐观情形仍参与缩放。

```text
预计耗时 = 原耗时 × (1 − CPU 占比 − 磁盘占比
                     + CPU 占比 / CPU 速度比
                     + 磁盘占比 / 磁盘速度比)

整体提速 = (模型耗时 + 原工具耗时) / (模型耗时 + 预计工具耗时)
```

CPU 速度比按类别权重混合单核和多核分数；磁盘使用启发式比例。各项占比在 0 到 1 之间，CPU 与磁盘占比之和不能超过 1。本机基准依次采用分数表匹配、已记录的替代芯片或线程数粗略估计。后两种会在报告中标明并扩大区间，也可用 `--current-gb6` 提供实测值。

## 数据与限制

[`data/`](../skills/agent-speedup-estimator/data) 包含分数来源、默认档位、替代芯片与三种情形的敏感度假设。

- 假设模型在远程、工具在本地运行；不建模本地大模型、远程构建、GPU 升级或内存不足。
- 模型时间是从计时间隔推断的，可能混入网络和调度开销；审批等待也可能进入工具耗时。
- Codex 需要带起止时间的 `item_completed` 或任务边界字段；其他格式可能没有可用数据。
- 不同并发会话的时间相加，因此节省小时数是累计 Agent 工作量，不等于日历时间。
- 分数不能完整反映编译器、散热和内存带宽。Windows/Linux 默认取检测到的最快磁盘类型，macOS 假设 NVMe，必要时手动覆盖。
- 分数来自链接的公开页面，是有日期的参考快照，不是 Geekbench 官方平均值或实时产品推荐。

## 隐私

JSON 会话记录在本地内存中解析。报告只包含汇总耗时、粗粒度类别、允许的命令类型、活动日期和硬件信息；不包含提示词、回复、命令原文、会话路径或会话 ID。CLI 不上传历史，不调用 API，不执行会话命令。可选依赖安装属于单独的网络操作。

报告仍可能暴露机器配置和工作规律，分享前请检查。仓库会忽略个人报告和原始会话文件。[公开示例](example/report.md)完全使用合成计时和虚构硬件，通过[示例脚本](../examples/generate_demo.py)生成。

## 开发与许可

```bash
python -m unittest discover -s skills/agent-speedup-estimator/tests -v
python examples/generate_demo.py
```

自动测试覆盖分类、计时、压缩、分数解析、估算边界、参数校验和两个适配器的隐私。GitHub Actions 在 Linux、Windows、macOS 上测试 Python 3.9 和 3.14。贡献代码、数据或翻译前请阅读 [CONTRIBUTING.md](../CONTRIBUTING.md)，使用合成数据复现问题。

[MIT 许可证](../LICENSE) © 2026 hnewcity。本项目独立开发，与 OpenAI、Anthropic、Primate Labs 无隶属关系。
