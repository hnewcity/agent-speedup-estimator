<div align="center">

# Agent Speedup Estimator

**パソコンを買い替えると、コーディングエージェントはどれくらい速くなる？**

ローカルの Claude Code / Codex 履歴から、ハードウェア更新の効果を推定します。

[![Tests](https://github.com/hnewcity/agent-speedup-estimator/actions/workflows/tests.yml/badge.svg)](https://github.com/hnewcity/agent-speedup-estimator/actions/workflows/tests.yml)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](#クイックスタート)
[![MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

[![English](https://img.shields.io/badge/English-555555?style=for-the-badge)](../README.md)
[![简体中文](https://img.shields.io/badge/简体中文-555555?style=for-the-badge)](README.zh-CN.md)
[![日本語](https://img.shields.io/badge/日本語-selected-1f6feb?style=for-the-badge)](README.ja.md)
[![Español](https://img.shields.io/badge/Español-555555?style=for-the-badge)](README.es.md)

[クイックスタート](#クイックスタート) · [スキルとして使う](#スキルとして使う) · [サンプルレポート](example/report.md) · [英語の詳細リファレンス](../README.md)

</div>

## このツールについて

新しいパソコンはビルドやテストを高速化できますが、リモートサーバー上のモデルは高速化できません。このツールは既存の記録を使い、**実際の作業内容**に対する効果を推定します。

例えば、モデルに 80 秒、ローカルツールに 20 秒かかる処理では、ローカル部分がすべて 2 倍速になっても合計は 100 秒から 90 秒、全体では **1.11 倍**です。実際の推定では、ツール時間のうちハードウェアに依存しない部分も考慮します。

> ベンチマークではなく推定です。保守的・標準・楽観的な 3 シナリオは仮定の違いを示し、統計的な信頼区間や購入の推奨ではありません。

## 主な機能

- モデル、ツール、人の応答、アイドル時間などの内訳。
- ビルド、テスト、インストール、スクリプト、Git、ファイル操作の分類。
- Geekbench 6 の参照値がある全モデルを既定で比較。短いクラス別比較や独自スコアも指定できます。
- 全体とツールの速度比、および削減時間を 3 シナリオで表示。
- Markdown、対話的なオフライン HTML、JSON の出力。
- エージェント用スキルと Python CLI の両方に対応。

基本動作は Python 標準ライブラリのみで、ネットワーク要求や履歴中のコマンド実行は行いません。**レポートの言語は英語と簡体字中国語**です。上のボタンは README の言語を切り替えます。

## クイックスタート

**Python 3.9+**、リポジトリを取得する Git、対応する時刻情報を含むローカル履歴が必要です。

```bash
git clone https://github.com/hnewcity/agent-speedup-estimator.git
cd agent-speedup-estimator
python skills/agent-speedup-estimator/scripts/agent_speedup.py --lang en --out ./agent-speedup-report
```

`python` がなければ Windows では `py -3`、macOS/Linux では `python3` を使います。完了後に `agent-speedup-report/report.html` をブラウザーで開いてください。

| 出力 | 用途 |
| --- | --- |
| `report.md` | 要約の確認 |
| `report.html` | 比較対象、グラフ、表の切り替え。オフラインで利用可能 |
| `summary.json` | 集計データの再利用 |
| `cpu-catalog.json` | スコア未収録のモデルを含む CPU と Mac の全カタログ |

圧縮された Codex 履歴（`.jsonl.zst`）には **Python 3.14+**、または旧バージョンで次の追加パッケージが必要です。

```bash
python -m pip install zstandard
```

読めない圧縮ファイルの数を通知します。利用できる時刻情報がなければ終了コード `2` を返します。`--claude-dir` / `--codex-dir` で保存場所を指定できます。

## スキルとして使う

### 方法 1：エージェントにインストールを依頼する

ターミナルとファイルを操作できる Codex、Claude Code などに、次の文をそのまま貼り付けてください。

```text
https://github.com/hnewcity/agent-speedup-estimator のスキルをインストールしてください。README に従い、scripts/ と data/ を含む skills/agent-speedup-estimator フォルダー全体を、現在使っているコーディングエージェントの個人用 skills ディレクトリに配置してください。既存のローカル変更は保持してください。インストール先で Python 3.9+ を使って scripts/agent_speedup.py --help を実行して確認し、インストール先のパスを教えてください。
```

### 方法 2：curl でインストールする

`curl` と `tar` が必要です。Git は不要です。`main` のソースアーカイブからスキルのフォルダーだけを展開します。スキルの実行には Python 3.9+ が必要です。同名ファイルは上書きされるため、ローカルの変更は先に保存してください。

**macOS / Linux**：既定のインストール先は Codex です。Claude Code では `skill_dir` を `"$HOME/.claude/skills"` に変更します。

```bash
skill_dir="$HOME/.agents/skills"
mkdir -p "$skill_dir"
curl -fsSL https://github.com/hnewcity/agent-speedup-estimator/archive/refs/heads/main.tar.gz |
  tar -xz -C "$skill_dir" --strip-components=2 agent-speedup-estimator-main/skills/agent-speedup-estimator
```

**Windows PowerShell**：最近の Windows に付属する `curl.exe` と `tar.exe` を使用します。Claude Code では `$skillDir` を `"$HOME/.claude/skills"` に変更します。

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

選んだ skills ディレクトリに `agent-speedup-estimator/` が作られます。`python /path/to/agent-speedup-estimator/scripts/agent_speedup.py --help` で確認できます。Windows では `py -3` も使えます。

### 方法 3：Git で取得したフォルダーをコピーする

[`skills/agent-speedup-estimator`](../skills/agent-speedup-estimator) を `scripts/` と `data/` ごとコピーします。

| エージェント | 個人用ディレクトリ | プロジェクト用ディレクトリ |
| --- | --- | --- |
| Codex | `~/.agents/skills/agent-speedup-estimator/` | `.agents/skills/agent-speedup-estimator/` |
| Claude Code | `~/.claude/skills/agent-speedup-estimator/` | `.claude/skills/agent-speedup-estimator/` |

OS 別のコピーコマンドは[英語のインストール手順](../README.md#install-as-a-skill)にあります。Codex が認識しない場合は再起動してください。インストール後は次のように依頼できます。

> agent-speedup-estimator を使って、このパソコンがエージェントの速度を制限しているか調べてください。Apple M4 Pro と比較し、推定の前提も説明してください。

入力の自動検出と実行方針は [SKILL.md](../skills/agent-speedup-estimator/SKILL.md) を参照してください。

## コマンド例

リポジトリのルートで実行します。

```bash
# 過去 30 日間と指定 CPU
python skills/agent-speedup-estimator/scripts/agent_speedup.py --days 30 --target "Apple M4 Pro (14-CPU 20-GPU)" --lang en

# 複数の CPU を比較
python skills/agent-speedup-estimator/scripts/agent_speedup.py --target "Apple M4 (10-CPU)" --target "AMD Ryzen 9 9950X"

# 独自スコア。数値は引数の説明用です
python skills/agent-speedup-estimator/scripts/agent_speedup.py --current-gb6 1500 6000 --custom-target "My next computer" 3000 15000

python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus
python skills/agent-speedup-estimator/scripts/agent_speedup.py --help
```

既定では `~/.claude/projects`、`~/.codex/sessions`、`~/.codex/archived_sessions` を読み、`CLAUDE_CONFIG_DIR` と `CODEX_HOME` を尊重します。`--agents`、`--current-disk`、`--target-disk`、`--sensitivity` などの詳細は[引数一覧](../README.md#more-examples)を参照してください。

同じ出力先の同名ファイルは上書きされます。不明・曖昧・スコア不足の対象は明示的なエラーとなり、別の対象に置き換えません。`--list-cpus` の正確な構成名または ID を指定してください。`--days` は記録・ターンの終了時刻で選び、期間境界をまたぐ処理を分割しません。

## 推定の仕組み

時刻とツール実行時間を読み、コマンドをメモリー内で分類します。単一セッション内の並行呼び出しは重複時間を分配します。既定では 300 秒を超える部分を保守的・標準シナリオで固定し、楽観シナリオではその部分も高速化対象とします。

```text
projected_time = original_time × ((1 − cpu_share − disk_share)
                                + cpu_share / cpu_speed_ratio
                                + disk_share / disk_speed_ratio)
overall_speedup = (model_time + original_tool_time)
                 / (model_time + projected_tool_time)
```

CPU 比率は単一コアと複数コアの値をカテゴリ別の重みで混合し、ディスクには経験的な係数を使います。各比率は 0〜1、CPU とディスクの合計は 1 以下です。基準スコアは一致する CPU、明示された代替 CPU、スレッド数からの概算の順に選びます。概算は表示され、範囲を広げます。`--current-gb6` で実測値を指定できます。

## データと制約

[`data/`](../skills/agent-speedup-estimator/data) にスコアの出典、比較クラス、代替 CPU、感度の仮定があります。

- リモートモデルとローカルツールを想定します。ローカル LLM、リモートビルド、GPU 更新、メモリー不足はモデル化しません。
- モデル時間は記録の間隔から推定するため、通信や制御処理が混ざる場合があります。承認待ちがツール時間になることもあります。
- Codex は時刻付き `item_completed` またはタスク境界が必要です。異なる形式では利用可能な記録がない場合があります。
- 並行セッション間では時間を合算します。削減時間は累積エージェント時間で、実際の経過時間とは異なります。
- コンパイラー、冷却、メモリー帯域はスコアだけでは表せません。Windows/Linux は検出した最速のディスク種別、macOS は NVMe を仮定します。
- スコアは公開ページの時点付き参照値です。Geekbench 公式平均値や最新製品の推奨ではありません。

## プライバシー

JSON 履歴をローカルメモリー内で解析します。出力には集計時間、カテゴリ、許可されたコマンド種別、活動日、ハードウェア情報を含みます。プロンプト、応答、コマンド原文、履歴のパス、セッション ID は含みません。CLI は履歴を送信せず、API を呼び出さず、履歴のコマンドも実行しません。追加パッケージのインストールは別のネットワーク操作です。

レポートから作業パターンや構成が分かるため、共有前に確認してください。個人のレポートと履歴は Git の対象外です。[サンプル](example/report.md)は[生成スクリプト](../examples/generate_demo.py)による人工データと架空のハードウェアのみを使います。

## 開発とライセンス

```bash
python -m unittest discover -s skills/agent-speedup-estimator/tests -v
python examples/generate_demo.py
```

分類、時間配分、圧縮、スコア、推定の境界、入力検証、両アダプターのプライバシーをテストします。GitHub Actions は Linux、Windows、macOS と Python 3.9 / 3.14 を使用します。変更や翻訳は [CONTRIBUTING.md](../CONTRIBUTING.md) を参照し、実際の会話ではなく人工データを使ってください。

[MIT](../LICENSE) © 2026 hnewcity。OpenAI、Anthropic、Primate Labs とは無関係の独立したプロジェクトです。

## CPU と Mac のカタログ

[全モデル一覧](cpu-catalog.md) · [データと出典](cpu-data.md)

Intel Core 第4世代から Core / Core Ultra Series 3、AMD Zen 系列、Apple M1–M6 の掲載構成と2013年以降の Intel / Apple Silicon Mac を収録しています。地域・OEM・カスタム構成には欠落があり得ます。掲載は発売や販売状況の独立した確認ではありません。

既定では有効な Geekbench 6 の単一／複数コアの組を持つ全対象を比較します。HTML は検索、メーカー・世代・プラットフォームのフィルター、25件ずつのページ表示を備えます。スコア不足も一覧に残ります。Mac の CPU 参照値は実機の測定値とは区別され、Geekbench 6 と 7 は混在しません。

`--list-cpus --search "M2" --json` で検索・書き出し、`--target-set tiers` で短い比較を選べます。派生カタログは [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) で提供します（コードは MIT）。
