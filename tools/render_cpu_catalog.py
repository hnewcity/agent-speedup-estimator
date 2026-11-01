"""Generate a browsable GitHub catalog from the shipped inventory and scores."""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/agent-speedup-estimator/scripts"))
from aspeed.scores import load_catalog  # noqa: E402


def main():
    data = load_catalog()
    cpus = data["cpus"]
    groups = defaultdict(list)
    for c in cpus:
        groups[(c["vendor"], c["generation"])].append(c)
    lines = ["# CPU and Mac catalog", "", "[English README](../README.md) · [中文](README.zh-CN.md) · [Data scope, sources and maintenance](cpu-data.md)", "",
             f"Snapshot: **{data['as_of']}**. **{len(cpus)} inventory entries**, including **{sum(bool(c.get('gb6_single')) for c in cpus)} entries eligible for GB6-based comparisons**.", "",
             "Counts include CPU configurations and Mac configurations separately. A listing is not independent confirmation of release or availability. Missing data remains visible. Source coverage can omit OEM, regional and build-to-order configurations.", "",
             "`reference-gb6`: CPU reference pair. `cpu-reference-gb6`: Mac estimate using a CPU reference, not a measured Mac score. `missing-gb6`: no usable pair. `version-conflict`: chart version is inconsistent and its scores are excluded.", "",
             "| Vendor | Inventory | CPU references | Mac CPU references | No usable pair |", "|---|---:|---:|---:|---:|"]
    for vendor in ("Intel", "AMD", "Apple"):
        rows = [c for c in cpus if c["vendor"] == vendor]
        count = Counter(c["score_status"] for c in rows)
        lines.append(f"| {vendor} | {len(rows)} | {count['reference-gb6']} | {count['cpu-reference-gb6']} | {sum(not c.get('gb6_single') for c in rows)} |")
    lines += ["", "Names with a CPU/GPU core count identify that exact source-listed configuration. Expand a generation below, or search the JSON with `--list-cpus --search TEXT`.", ""]
    for (vendor, generation), rows in sorted(groups.items()):
        lines += ["<details>", f"<summary>{vendor} · {generation} ({len(rows)} entries)</summary>", "", "| CPU / Mac configuration | Platform | GB6 single / multi | Status |", "|---|---|---:|---|"]
        for c in rows:
            name = c["name"].replace("|", "\\|")
            source = c["source_urls"][0]
            score = f"{c['gb6_single']} / {c['gb6_multi']}" if c.get("gb6_single") else "—"
            lines.append(f"| [{name}]({source}) | {', '.join(c['platforms'])} | {score} | {c['score_status']} |")
        lines += ["", "</details>", ""]
    lines += ["Derived catalog: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). [Sources, contributors and transformations](../skills/agent-speedup-estimator/data/SOURCES.md).", ""]
    (ROOT / "docs/cpu-catalog.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated docs/cpu-catalog.md ({len(cpus)} entries).")


if __name__ == "__main__":
    main()
