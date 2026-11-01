<div align="center">

# Agent Speedup Estimator

**Would a faster computer actually make your coding agent faster?**

Turn local Claude Code and Codex history into a hardware upgrade estimate.

[![Tests](https://github.com/hnewcity/agent-speedup-estimator/actions/workflows/tests.yml/badge.svg)](https://github.com/hnewcity/agent-speedup-estimator/actions/workflows/tests.yml)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](#quick-start)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Local analysis](https://img.shields.io/badge/Analysis-local%20only-6F42C1)](#privacy)

[![English](https://img.shields.io/badge/English-selected-1f6feb?style=for-the-badge)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-555555?style=for-the-badge)](docs/README.zh-CN.md)
[![日本語](https://img.shields.io/badge/日本語-555555?style=for-the-badge)](docs/README.ja.md)
[![Español](https://img.shields.io/badge/Español-555555?style=for-the-badge)](docs/README.es.md)

[Quick start](#quick-start) · [Install as a skill](#install-as-a-skill) · [Example report](docs/example/report.md) · [How it works](#how-it-works)

</div>

## Why this exists

A new laptop can speed up your builds and tests. It cannot speed up a model running on a remote server. This tool estimates how much that distinction matters **for your own agent workload**, using timing records you already have.

For intuition: if a run spends 80 seconds on remote model work and 20 seconds on local tools, making **all** local work twice as fast reduces the total from 100 to 90 seconds: **1.11× overall**. Actual estimates also account for the parts of tool time that do not scale with hardware.

> An estimate, not a benchmark. Conservative, expected and optimistic scenarios expose the assumptions; they are not statistical confidence intervals or purchase recommendations.

## What you get

- **A time breakdown** across model work, tools, human replies, idle gaps and other recorded activity.
- **Workload categories** for builds, tests, installs, scripts, Git, file operations and more.
- **Hardware comparisons** using bundled Geekbench 6 reference scores, the full scored catalog, an optional tier preset, or custom scores.
- **Three scenarios** with end-to-end speedup, tool speedup and estimated time saved.
- **Four output files:** readable Markdown, an interactive offline HTML report, structured results, and a JSON CPU catalog.
- **Two ways to use it:** an agent skill or a standalone Python command.

The analyzer makes no network requests and never executes commands from your transcripts. Basic use needs only the Python standard library. Report text supports **English and Simplified Chinese**; the language buttons above switch this README.

## Quick start

Requirements: **Python 3.9+**, Git to clone the repository, and local Claude Code or Codex history with supported timing records.

```bash
git clone https://github.com/hnewcity/agent-speedup-estimator.git
cd agent-speedup-estimator
python skills/agent-speedup-estimator/scripts/agent_speedup.py --lang en --out ./agent-speedup-report
```

Use `py -3` on Windows or `python3` on macOS/Linux if `python` is unavailable. Open `agent-speedup-report/report.html` in your browser when the command finishes.

| File | Use |
| --- | --- |
| `report.md` | Read or review the summary |
| `report.html` | Compare machines, inspect charts and switch to table views; no internet needed |
| `summary.json` | Reuse the aggregate results in your own tools |
| `cpu-catalog.json` | Inspect the full CPU and Mac inventory, including missing scores |

Compressed Codex files (`.jsonl.zst`) require **Python 3.14+** or the optional `zstandard` package on older Python versions:

```bash
python -m pip install zstandard
```

Unreadable compressed files are counted and reported. If no usable timing data is found, the command exits with code `2` and suggests explicit transcript directories.

## Install as a skill

### Option 1: Ask your agent to install it

Copy this prompt into Codex, Claude Code, or another coding agent with terminal and filesystem access:

```text
Install the agent-speedup-estimator skill from https://github.com/hnewcity/agent-speedup-estimator for the coding agent I am using. Follow the README and install the complete skills/agent-speedup-estimator folder, including scripts/ and data/, in my personal skills directory. Preserve any existing local edits. Verify the installation by running scripts/agent_speedup.py --help with Python 3.9+ from the installed folder, and tell me the installed path.
```

### Option 2: Install with curl

Requires `curl` and `tar`; Git is not needed. These commands download the `main` source archive and extract only the skill folder. Running the skill requires Python 3.9+. Matching files in an existing installation will be overwritten, so preserve local edits first.

**macOS / Linux** — the default destination below is Codex. For Claude Code, change `skill_dir` to `"$HOME/.claude/skills"`.

```bash
skill_dir="$HOME/.agents/skills"
mkdir -p "$skill_dir"
curl -fsSL https://github.com/hnewcity/agent-speedup-estimator/archive/refs/heads/main.tar.gz |
  tar -xz -C "$skill_dir" --strip-components=2 agent-speedup-estimator-main/skills/agent-speedup-estimator
```

**Windows PowerShell** — uses `curl.exe` and `tar.exe`, included in modern Windows. For Claude Code, change `$skillDir` to `"$HOME/.claude/skills"`.

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

The installed folder is `agent-speedup-estimator/` inside your chosen skills directory. You can verify it by running `python /path/to/agent-speedup-estimator/scripts/agent_speedup.py --help` (or `py -3` on Windows).

### Option 3: Copy from a Git clone

Copy the entire [`skills/agent-speedup-estimator`](skills/agent-speedup-estimator) folder, including `scripts/` and `data/`, into your agent's skill directory.

| Agent | Personal skill location |
| --- | --- |
| Codex | `~/.agents/skills/agent-speedup-estimator/` |
| Claude Code | `~/.claude/skills/agent-speedup-estimator/` |

From the cloned repository, on macOS/Linux:

```bash
# Codex
mkdir -p ~/.agents/skills
cp -R skills/agent-speedup-estimator ~/.agents/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -R skills/agent-speedup-estimator ~/.claude/skills/
```

On Windows PowerShell:

```powershell
# Codex
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
Copy-Item -Recurse skills/agent-speedup-estimator "$HOME/.agents/skills/"

# Claude Code
New-Item -ItemType Directory -Force "$HOME/.claude/skills" | Out-Null
Copy-Item -Recurse skills/agent-speedup-estimator "$HOME/.claude/skills/"
```

Choose the block for the agent you use. For a project-only installation, use `.agents/skills/` for Codex or `.claude/skills/` for Claude Code in that project. See the [Codex skill documentation](https://developers.openai.com/codex/skills/) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills) for discovery details.

Then ask your agent:

> Use agent-speedup-estimator to check whether my computer is slowing down my coding agents. Compare it with an Apple M4 Pro and explain the assumptions.

Or simply:

> Would a new laptop make my coding agent faster?

The [skill instructions](skills/agent-speedup-estimator/SKILL.md) guide automatic input discovery, fallback scores and how to explain the result. If Codex does not pick up the installation, restart it.

## CPU and Mac coverage

[Browse the complete model list](docs/cpu-catalog.md) · [Scope, data states and sources](docs/cpu-data.md)

The catalog spans Intel Core 4th generation through Core / Core Ultra Series 3, AMD Zen families from early Ryzen through current source-listed Ryzen AI, Threadripper and EPYC, and Apple M1–M6 chip configurations plus Intel/Silicon Macs from 2013 onward. Exact counts and per-generation tables are in the linked catalog. Source-listed models are not independent release or availability confirmations; OEM, regional and build-to-order omissions may remain.

Reports now compare **all entries with usable Geekbench 6 reference pairs** by default. The offline HTML has search, vendor/generation/platform filters and 25-row pages, plus a separate inventory showing missing data. Apple CPU-core bins are distinct. Mac estimates using CPU references are explicitly labeled; they are not measured Mac scores. Geekbench 6 and 7 are never mixed.

```bash
python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus --vendor Apple --generation M2
python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus --search "Core i7-4" --json
python skills/agent-speedup-estimator/scripts/agent_speedup.py --vendor AMD --generation "Zen 4"
```

Each report also exports `cpu-catalog.json`. Use `--target-set tiers` for the small curated preset.

## More examples

Run these commands from the repository root:

```bash
# Last 30 days, with a named target
python skills/agent-speedup-estimator/scripts/agent_speedup.py --days 30 --target "Apple M4 Pro (14-CPU 20-GPU)" --lang en

# Compare two targets
python skills/agent-speedup-estimator/scripts/agent_speedup.py --target "Apple M4 (10-CPU)" --target "AMD Ryzen 9 9950X"

# Your own Geekbench 6 scores; these numbers are illustrative inputs
python skills/agent-speedup-estimator/scripts/agent_speedup.py --current-gb6 1500 6000 --custom-target "My next computer" 3000 15000

# An explicit history folder
python skills/agent-speedup-estimator/scripts/agent_speedup.py --agents codex --codex-dir /path/to/sessions

# A Chinese report
python skills/agent-speedup-estimator/scripts/agent_speedup.py --lang zh

# Supported CPUs and all options
python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus
python skills/agent-speedup-estimator/scripts/agent_speedup.py --help
```

| Option | Purpose |
| --- | --- |
| `--agents claude,codex` | Choose agent histories |
| `--claude-dir`, `--codex-dir` | Override transcript roots |
| `--days N` | Include records/turns ending in the last N days; boundary-spanning work is not clipped |
| `--target NAME` | Compare an exact scored CPU/Mac configuration or catalog ID; repeatable |
| `--target-set all\|tiers` | All scored entries by default; optional curated tiers |
| `--list-cpus` | List every catalog entry, including missing scores; no transcripts required |
| `--search TEXT`, `--vendor`, `--generation`, `--platform` | Filter the inventory or default report comparisons |
| `--scored-only` | Limit the CPU listing to entries with paired GB6 scores |
| `--custom-target NAME SINGLE MULTI` | Add a target using positive Geekbench 6 scores |
| `--current-cpu`, `--current-gb6 SINGLE MULTI` | Override the CPU name or baseline scores |
| `--current-disk`, `--target-disk` | Set `hdd`, `sata`, `nvme`, `nvme_gen4` or `unknown` |
| `--cap SECONDS` | Per-command hardware sensitivity cap; default 300 |
| `--max-stall`, `--max-human` | Stall and idle thresholds; defaults 300 and 1800 seconds |
| `--sensitivity FILE` | Load custom CPU/disk assumptions |
| `--lang auto\|en\|zh` | Choose the report language |
| `--out DIR`, `--no-html`, `--json` | Set output directory, skip HTML, or print JSON |

Default input roots are `~/.claude/projects`, `~/.codex/sessions` and `~/.codex/archived_sessions`; `CLAUDE_CONFIG_DIR` and `CODEX_HOME` are respected. Reports overwrite files of the same name in `--out`. Unknown, ambiguous or unscored named targets exit with an explanation; they are never silently replaced. Use an exact configuration name or ID from `--list-cpus`.

## How it works

1. **Read timing records.** Claude Code uses message timestamps and tool-use/result pairs. Codex uses supported `event_msg` records, item start/end times and timed task boundaries.
2. **Classify tool work.** Command text is inspected in memory and reduced to a category plus an allowlisted command family, such as `pytest`, `git` or `npm`.
3. **Account for overlap.** Concurrent tool calls share wall time within a session. Long commands are capped in the conservative and expected scenarios; the optimistic scenario also scales time beyond the cap.
4. **Apply hardware ratios.** CPU speed blends single-core and multi-core Geekbench 6 ratios with a category-specific weight. Disk ratios use a damped heuristic, not a storage benchmark.
5. **Keep estimated model time fixed.** Add projected tool time back to model time to calculate the overall speedup.

For a category's hardware-sensitive time:

```text
projected_time = original_time × ((1 − cpu_share − disk_share)
                                + cpu_share / cpu_speed_ratio
                                + disk_share / disk_speed_ratio)

overall_speedup = (model_time + original_tool_time)
                 / (model_time + projected_tool_time)
```

Each CPU/disk share is between 0 and 1, and their sum cannot exceed 1. The baseline uses a score-table match, then a documented stand-in, then a rough thread-count estimate. Stand-ins and estimates are flagged and widen the scenario range. Use `--current-gb6` to supply measurements instead.

## Data and limitations

| Data | Contents |
| --- | --- |
| [`cpu_catalog.json`](skills/agent-speedup-estimator/data/cpu_catalog.json) | Source-listed CPU and Mac configurations, including missing-score entries |
| [`cpu_scores.json`](skills/agent-speedup-estimator/data/cpu_scores.json) | Dated reference scores and a source URL for each CPU |
| [`tiers.json`](skills/agent-speedup-estimator/data/tiers.json) | Entry, mainstream, performance and workstation comparisons |
| [`proxies.json`](skills/agent-speedup-estimator/data/proxies.json) | Stand-ins and the thread-count fallback |
| [`sensitivity.json`](skills/agent-speedup-estimator/data/sensitivity.json) | Three sets of workload assumptions |

- **Remote models, local tools:** local LLM inference, remote builds, GPU upgrades and memory pressure are not modelled. Inspect workloads using SSH, cloud tools or opaque MCP calls before relying on a result.
- **Approximate attribution:** model time is inferred from gaps that can include network and orchestration overhead. Approval waits may appear as tool time.
- **Schema dependence:** Codex logs need `item_completed` timing fields or timed task boundaries. Older or different formats may contribute no usable data.
- **Aggregate hours:** concurrent sessions are summed. Saved hours are aggregate agent time, not elapsed calendar time.
- **Hardware heuristics:** scores do not capture compilers, cooling or memory bandwidth. Disk detection chooses the fastest class on Windows/Linux and assumes NVMe on macOS; override it if needed.
- **Reference values:** bundled scores come from public pages and are not official Geekbench averages. They are a dated snapshot, not live product or price recommendations.

## Privacy

Transcript JSON records are parsed locally in memory. Reports contain **aggregate timings, coarse categories, allowlisted command families, activity dates and hardware details**. Prompt text, responses, raw commands, transcript paths and session IDs are excluded from report output.

The CLI does not upload history, make API calls or execute transcript commands. The optional package installation is a separate network operation. Reports can reveal your machine configuration and work patterns; review them before sharing.

The repository ignores personal reports and transcript files. The checked-in [example](docs/example/report.md) uses entirely synthetic timings and fictional hardware, generated by [`examples/generate_demo.py`](examples/generate_demo.py).

## Development

```bash
python -m unittest discover -s skills/agent-speedup-estimator/tests -v
python examples/generate_demo.py
```

Tests cover classification, attribution, compression, score resolution, projection bounds, input validation and privacy across both adapters. GitHub Actions runs on Linux, Windows and macOS with Python 3.9 and 3.14.

See [CONTRIBUTING.md](CONTRIBUTING.md) for adapters, data updates and translations. No real user transcripts are needed for contributions.

## License

Code: [MIT](LICENSE). Derived CPU catalog: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), with [source attribution](skills/agent-speedup-estimator/data/SOURCES.md). © 2026 hnewcity. Independent community project; not affiliated with OpenAI, Anthropic or Primate Labs. Product names belong to their respective owners.
