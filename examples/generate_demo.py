"""Generate the public example with synthetic transcripts and fictional hardware.

No user history or machine detection is used. Run from any working directory.
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "agent-speedup-estimator" / "scripts"))

from aspeed import cli  # noqa: E402
from aspeed.hardware import Hardware  # noqa: E402
from aspeed.report_html import render_html  # noqa: E402
from aspeed.report_md import render_md  # noqa: E402


def iso(t):
    return datetime.fromtimestamp(t, timezone.utc).isoformat().replace("+00:00", "Z")


def generate():
    out = ROOT / "docs" / "example"
    start = datetime(2026, 1, 1, 12, tzinfo=timezone.utc).timestamp()
    workloads = [("cargo build", 180), ("pytest", 90), ("npm install", 80), ("git status", 5)]
    hardware = Hardware(cpu_name="Demo baseline (synthetic)", cores=4, threads=8,
                        ram_gb=16.0, disk_class="sata", os_name="Synthetic example")
    with tempfile.TemporaryDirectory() as temp:
        claude, codex = Path(temp) / "claude", Path(temp) / "codex"
        claude.mkdir()
        codex.mkdir()
        for i in range(8):
            t = start + i * 3600
            command, duration = workloads[i % len(workloads)]
            rows = [
                {"type": "user", "timestamp": iso(t), "message": {"content": "Synthetic task"}},
                {"type": "assistant", "timestamp": iso(t + 60), "message": {"content": [
                    {"type": "tool_use", "id": "demo", "name": "Bash", "input": {"command": command}}]}},
                {"type": "user", "timestamp": iso(t + 60 + duration), "message": {"content": [
                    {"type": "tool_result", "tool_use_id": "demo", "content": "Synthetic result"}]}},
                {"type": "assistant", "timestamp": iso(t + 120 + duration), "message": {"content": "Synthetic reply"}},
            ]
            (claude / f"demo-{i}.jsonl").write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
            payloads = [
                {"type": "task_started", "turn_id": "demo", "started_at": t},
                {"type": "item_completed", "turn_id": "demo", "started_at_ms": t * 1000,
                 "completed_at_ms": (t + 60) * 1000, "item": {"type": "Reasoning"}},
                {"type": "item_completed", "turn_id": "demo", "started_at_ms": (t + 60) * 1000,
                 "completed_at_ms": (t + 60 + duration) * 1000,
                 "item": {"type": "CommandExecution", "command": command, "duration": {"secs": duration, "nanos": 0}}},
                {"type": "item_completed", "turn_id": "demo", "started_at_ms": (t + 60 + duration) * 1000,
                 "completed_at_ms": (t + 120 + duration) * 1000, "item": {"type": "AgentMessage"}},
                {"type": "task_complete", "turn_id": "demo", "started_at": t,
                 "completed_at": t + 120 + duration, "duration_ms": (120 + duration) * 1000},
            ]
            (codex / f"demo-{i}.jsonl").write_text("\n".join(json.dumps({"type": "event_msg", "payload": p}) for p in payloads), encoding="utf-8")
        with patch.object(cli, "detect", return_value=hardware), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            code = cli.main([
                "--agents", "claude,codex", "--claude-dir", str(claude), "--codex-dir", str(codex),
                "--current-gb6", "1500", "6000",
                "--lang", "en", "--out", str(out),
            ])
        if code:
            raise RuntimeError(f"Demo generation failed: {code}")

    data = json.loads((out / "summary.json").read_text(encoding="utf-8"))
    data["demo"] = True
    data["baseline"]["note"] = "Fictional scores for illustration only"
    data["notes"].insert(0, "SYNTHETIC EXAMPLE: activity, baseline hardware and baseline scores are fictional. Target CPU references come from the attributed public dataset. These projections are not measured results or a real user's history.")
    (out / "summary.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "report.md").write_text(
        "> Synthetic example — fictional activity and baseline; sourced target CPU references.\n\n" + render_md(data, "en"), encoding="utf-8")
    (out / "report.html").write_text(render_html(data, "en"), encoding="utf-8")
    print("Generated docs/example/report.md, report.html, summary.json and cpu-catalog.json from synthetic activity and baseline inputs.")


if __name__ == "__main__":
    generate()
