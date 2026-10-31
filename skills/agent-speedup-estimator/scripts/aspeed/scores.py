from __future__ import annotations

import json
import re
from pathlib import Path
from typing import List, Optional, Tuple

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
_NOISE = re.compile(r"\((?:r|tm)\)|\bcpu\b|\bprocessor\b|@\s*[\d.]+\s*ghz|\bwith\b.*$|\bw/\b.*$", re.I)
_SUFFIX_BLOCK = re.compile(r"^\s*(?:pro|max|ultra|plus|x\b|3d)", re.I)


def load_json(name: str, data_dir: Optional[Path] = None) -> dict:
    with open((data_dir or DATA_DIR) / name, encoding="utf-8") as fh:
        return json.load(fh)


def normalize(name: str) -> str:
    s = _NOISE.sub(" ", name.lower())
    return re.sub(r"\s+", " ", s).strip()


def find_cpu(name: str, cpus: List[dict]) -> Optional[dict]:
    target = normalize(name)
    best: Optional[Tuple[int, dict]] = None
    for cpu in cpus:
        for alias in cpu.get("aliases", []) + [cpu["name"].lower()]:
            m = re.search(r"(?<![\w-])" + re.escape(alias) + r"(?![\w-])", target)
            if not m or _SUFFIX_BLOCK.match(target[m.end():]):
                continue
            if best is None or len(alias) > best[0]:
                best = (len(alias), cpu)
    return best[1] if best else None


def resolve_baseline(cpu_name: str, lang: str = "en", data_dir: Optional[Path] = None) -> Tuple[Optional[dict], str, str, float]:
    """Return (cpu_record, source, note, uncertainty). source is 'table', 'proxy' or '' when nothing matched."""
    cpus = load_json("cpu_scores.json", data_dir)["cpus"]
    exact = find_cpu(cpu_name, cpus)
    if exact:
        return exact, "table", "exact match in cpu_scores.json", 1.0
    target = normalize(cpu_name)
    for p in load_json("proxies.json", data_dir)["proxies"]:
        if p["match"] in target:
            stand_in = find_cpu(p["use"], cpus)
            if stand_in:
                return stand_in, "proxy", p["note"].get(lang) or p["note"]["en"], float(p.get("uncertainty", 1.15))
    return None, "", "", 1.0


def estimate_from_specs(threads: int, lang: str = "en", data_dir: Optional[Path] = None) -> Tuple[dict, str, float]:
    """Last resort when a CPU has no score: scale a documented anchor chip by thread count."""
    cfg = load_json("proxies.json", data_dir)["fallback"]
    anchor = find_cpu(cfg["use"], load_json("cpu_scores.json", data_dir)["cpus"])
    t = min(32, max(2, threads or cfg["threads"]))
    multi = round(anchor["gb6_multi"] * (t / cfg["threads"]) ** cfg["thread_exponent"])
    scores = {"gb6_single": anchor["gb6_single"], "gb6_multi": multi}
    return scores, cfg["note"].get(lang) or cfg["note"]["en"], float(cfg["uncertainty"])
