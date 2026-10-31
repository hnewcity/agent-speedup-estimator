---
name: agent-speedup-estimator
description: Scan local Claude Code and Codex transcripts to measure how long agent runs spend on model time versus local tool time (builds, tests, installs, scripts), then estimate how much faster they would run on a new computer. Use when the user asks whether their computer is slowing their coding agents, whether to upgrade or buy a new laptop or desktop, or how much faster a specific chip would make Claude Code or Codex. 中文触发：电脑是不是拖慢了 agent、要不要换新电脑、换电脑能快多少。
---

# Agent speedup estimator

Reads the timing data that Claude Code and Codex already write to disk, splits each run into model time and local tool time, and projects how much of that a faster computer would remove.

Transcript records are parsed locally in memory. Command text is inspected only to assign coarse categories and allowlisted command families. Prompts, replies and command text are never copied to reports or printed. Reports contain aggregate timings, activity dates and hardware details; keep them private unless the user chooses to share them.

## Resolve routine inputs automatically

Use the user's requested machines, agents, period and available measurements. Otherwise use the defaults below without asking them to design the evaluation, and state the assumptions. Clarify only an ambiguity that materially changes the answer.

## Run it

```bash
python scripts/agent_speedup.py --out <a temp or user folder> --lang <zh|en>
```

Run from this skill's directory, or use the absolute path to its script. Use `py -3` on Windows if `python` is missing, `python3` elsewhere. Use `--lang zh` for Chinese and `--lang en` for other languages; explain the results in the user's language. Put `--out` outside the skill folder (the report contains the user's own data). The run writes `report.md`, `report.html` (self-contained, no network) and `summary.json`, and prints the Markdown summary.

## How inputs are resolved automatically

| Input | Default | What you do when it is missing |
|---|---|---|
| Transcripts | `~/.claude/projects`, `~/.codex/sessions`, `~/.codex/archived_sessions` (honours `CLAUDE_CONFIG_DIR`, `CODEX_HOME`) | If exit code 2 (nothing found), look for the folders yourself and re-run with `--claude-dir` / `--codex-dir`. If none exist, tell the user there is no local agent history to analyse. |
| Compressed Codex sessions (`.jsonl.zst`) | Read with Python 3.14+ `compression.zstd` | If sessions were skipped, prefer an available Python 3.14+ interpreter or install `zstandard` in an isolated environment when permitted, then re-run. Otherwise report the skipped count. |
| Current CPU score | Score table, then a documented stand-in (`data/proxies.json`), then an estimate from thread count | Nothing to do. The report flags stand-ins and estimates and widens the range. Optionally improve it: search the web for this CPU's Geekbench 6 single and multi scores and, only if you read real numbers on a page, re-run with `--current-gb6 SINGLE MULTI`. |
| Target machines | Four tiers from `data/tiers.json` (entry, mainstream, high-performance, workstation) | If the user named machines, pass `--target "NAME"` once per machine (`--list-cpus` shows the table). |
| A named target that is not in the table | — | Search for its Geekbench 6 scores and pass `--custom-target "NAME" SINGLE MULTI`. If you cannot find real numbers, use the closest chip in the table of the same vendor, class and generation as a stand-in, and say so. Never invent a score. |
| Disk | Detected; new machine assumed NVMe | Use `--target-disk` only if the user said what the new machine has. |
| Period | All history | Use `--days N` only if the user asked about a period. |

## What to tell the user

1. The headline: expected end-to-end speedup and its range for the most relevant machine (the one they named, else the mainstream tier), and the hours saved over the scanned period.
2. Why the gain is that size: the share of agent working time that is model time. That part runs on remote servers and does not change with the computer.
3. Which local categories carry the gain (usually builds, tests, installs), with hours.
4. A short comparison across tiers, so the user sees whether a more expensive machine buys more.
5. What was assumed: stand-in or estimated baseline, sensitivity priors, cap on long commands. One sentence each, taken from the report's notes.
6. Report the numbers only. Do not tell the user to buy or not buy.

Point the user to `report.html` for the full breakdown.

## Limits

- `data/sensitivity.json` holds the share of each category's time that scales with CPU and disk speed. These are priors, not measurements.
- This assumes remote models and local tools. Local model inference, SSH/cloud execution and GPU or RAM upgrades are not modelled. Timing gaps can include network and orchestration overhead, so model time is an approximation.
- Codex requires `event_msg` timing records with `item_completed` start/end fields or timed task boundaries. Other transcript schemas may yield no usable timing data.
- Overlaps are deduplicated within each session; concurrent sessions are summed, so saved hours are aggregate agent time, not elapsed calendar time.
- CPU scores are compared across x86 and Apple Silicon. Compiler, OS, memory bandwidth and cooling also matter.
- Time spent waiting for the user to approve a command is counted as tool time. A per-command cap (`--cap`, default 300 s) limits how much it can inflate the estimate.
- Scores in `data/cpu_scores.json` come from public pages (Geekbench model pages for Apple chips, cpu-monkey comparisons for x86), each with a `source_url`. They are not official Geekbench averages.

## Files

- `scripts/aspeed/adapters/` one parser per agent; add a new agent by returning `SessionTiming` objects.
- `scripts/aspeed/classify.py` command to category rules.
- `data/` score table, tiers, stand-ins, fallback and sensitivity priors.
- `tests/` run with `python -m unittest discover -s tests`.
