"""Join saved GB6 chart rows by product URL, never by rank. Maintenance only.

Usage: python tools/import_cpu_scores.py research/gb6-batches.json
Input: [{query, single:[{name,url,score,specs}], multi:[...]}].
Only use snapshots whose visible headings explicitly identify Geekbench 6.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "skills/agent-speedup-estimator/data"
AS_OF = "2026-11-01"


def key(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace("+", " plus ")).strip("-")


def canonical(name):
    name = name.replace(" processor ", " ").replace(" HX PRO ", " PRO HX ")
    return {"AMD Ryzen 3 1200 [12nm]": "AMD Ryzen 3 1200 (AF)",
            "AMD Ryzen 5 1600 [12nm]": "AMD Ryzen 5 1600 (AF)",
            "AMD Ryzen 9 9950X3D2": "AMD Ryzen 9 9950X3D2 Dual Edition",
            "AMD Ryzen 7 4700S": "AMD 4700S"}.get(name, name)


def aliases(name):
    values = {name, re.sub(r"^(Intel|AMD|Apple) ", "", name)}
    if name.startswith("Intel Core "):
        values.add(name.replace("Intel Core ", ""))
    if name.startswith("Apple "):
        # Shared aliases intentionally remain ambiguous for configurations.
        base = name.split(" (")[0]
        values.update([base, base.replace("Apple ", "")])
    return sorted(values)


def main(path):
    catalog = json.loads((DATA / "cpu_catalog.json").read_text(encoding="utf-8"))
    entries = {c["id"]: c for c in catalog["cpus"]}
    by_name = {}
    for c in entries.values():
        if c["kind"] == "cpu":
            for n in [c["name"], c.get("source_name", "")]:
                if n:
                    by_name[key(n)] = c
    batches = json.loads(path.read_text(encoding="utf-8"))
    single, multi = {}, {}
    for batch in batches:
        for mode, dest in [("single", single), ("multi", multi)]:
            for row in batch[mode]:
                if not row.get("url") or not row.get("score"):
                    continue
                if row["url"] in dest and dest[row["url"]]["score"] != row["score"]:
                    raise ValueError("Conflicting snapshots: " + row["name"])
                dest[row["url"]] = row
    scores = {}
    for url in sorted(single.keys() & multi.keys()):
        a, b = single[url], multi[url]
        if a["name"] != b["name"]:
            raise ValueError("Mismatched product identity: " + url)
        entry = by_name.get(key(canonical(a["name"])))
        if entry is None:
            # Supplement only requested product families, preserving source provenance.
            name = canonical(a["name"])
            vendor = name.split()[0]
            if vendor not in ("Intel", "AMD", "Apple"):
                continue
            if vendor == "Intel" and not name.startswith("Intel Core "):
                continue
            gen = "Source-listed (see product page)"
            if vendor == "Intel":
                match = re.search(r"Core i\d-(\d+)", name)
                if match:
                    digits = match.group(1)
                    if len(digits) < 4:
                        continue  # i7-950 is first-gen, not ninth-gen.
                    number = int(digits[:2] if len(digits) >= 5 else digits[0])
                    if number < 4:
                        continue
                    gen = f"Core {number}th gen"
                elif "Core Ultra" in name:
                    m = re.search(r"Core Ultra X?\d (\d)", name)
                    gen = "Core Series " + m.group(1) if m else gen
            if vendor == "AMD" and not any(x in name for x in ("Ryzen", "EPYC", "Athlon", "4700S", "4800S")):
                continue
            # Do not add old non-Zen Athlons returned by a broad filter.
            if vendor == "AMD" and "Athlon" in name:
                continue
            platform = "workstation" if "Threadripper" in name else "server" if "EPYC" in name else "laptop" if re.search(r"(?:HX|HS|HQ|U|H|P|V|G7)$", name) else "desktop"
            entry = {"id": key(name), "name": name, "vendor": vendor, "kind": "cpu", "generation": gen,
                     "platforms": [platform], "source_urls": [urljoin("https://www.cpu-monkey.com", url)],
                     "source_section": "Geekbench 6 reference chart", "checked_on": AS_OF,
                     "listing_status": "source-listed", "score_status": "missing-gb6"}
            entries[entry["id"]] = entry
        entry["aliases"] = sorted(set(aliases(entry["name"]) + [a["name"]]))
        scores[entry["id"]] = {
            "id": entry["id"], "name": entry["name"], "aliases": entry["aliases"],
            "vendor": entry["vendor"], "generation": entry["generation"], "platforms": entry["platforms"],
            "class": entry["platforms"][0], "benchmark": "Geekbench 6",
            "gb6_single": int(a["score"].replace(",", "")), "gb6_multi": int(b["score"].replace(",", "")),
            "source_url": urljoin("https://www.cpu-monkey.com", url),
            "score_source_urls": ["https://www.cpu-monkey.com/en/cpu_benchmark-geekbench_6_single_core",
                                  "https://www.cpu-monkey.com/en/cpu_benchmark-geekbench_6_multi_core"],
            "checked_on": AS_OF, "score_kind": "public-reference",
            "source_name": a["name"],
        }
    # Retain previously attributed x86 references if a new chart pair is unavailable.
    old = json.loads((DATA / "cpu_scores.json").read_text(encoding="utf-8"))["cpus"]
    for c in old:
        if c["name"].startswith("Apple "):
            continue  # Legacy Apple links now conflict on the benchmark version.
        e = by_name.get(key(c["name"]))
        if e and e["id"] not in scores:
            scores[e["id"]] = {**c, "id": e["id"], "aliases": aliases(e["name"]),
                               "vendor": e["vendor"], "generation": e["generation"], "platforms": e["platforms"],
                               "benchmark": "Geekbench 6", "checked_on": c.get("checked_on", "2026-10-30"),
                               "score_kind": "public-reference"}
    catalog["cpus"] = sorted(entries.values(), key=lambda c: (c["vendor"], c["kind"], c["name"]))
    for entry in catalog["cpus"]:
        if entry["id"] in scores:
            entry["score_status"] = "reference-gb6"
    (DATA / "cpu_catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    payload = {"schema_version": 1, "scale": "Geekbench 6 CPU; public reference values, not official averages or machine-specific measurements",
               "as_of": AS_OF, "cpus": sorted(scores.values(), key=lambda c: c["name"])}
    (DATA / "cpu_scores.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Paired scores:", len(scores), dict(Counter(c["vendor"] for c in scores.values())))
    print("Single-only:", len(single.keys() - multi.keys()), "Multi-only:", len(multi.keys() - single.keys()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot_file", type=Path)
    main(parser.parse_args().snapshot_file)
