"""Import saved, public DOM tables into a factual CPU inventory.

Maintenance only: pip install beautifulsoup4. No network access or runtime dependency.
Usage: python tools/import_cpu_catalog.py SNAPSHOT_DIRECTORY
See docs/cpu-data.md for the snapshot format, sources and licensing.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "skills/agent-speedup-estimator/data"
AS_OF = "2026-11-01"


def clean(value):
    return re.sub(r"\s+", " ", value).strip()


def grids(path):
    for idx, item in enumerate(json.loads(path.read_text(encoding="utf-8"))):
        soup = BeautifulSoup(item["html"], "html.parser")
        for sup in soup.select("sup, .sortkey, .mw-collapsible-toggle"):
            sup.decompose()
        table = soup.find("table")
        if not table:
            continue
        grid = []
        for ri, tr in enumerate(table.find_all("tr")):
            while len(grid) <= ri:
                grid.append([])
            ci = 0
            for cell in tr.find_all(["th", "td"], recursive=False):
                while ci < len(grid[ri]) and grid[ri][ci] is not None:
                    ci += 1
                val = clean(cell.get_text(" ", strip=True))
                rs, cs = [max(1, int(re.match(r"\d+", str(cell.get(k, 1))).group()))
                          for k in ("rowspan", "colspan")]
                for rr in range(ri, ri + rs):
                    while len(grid) <= rr:
                        grid.append([])
                    for cc in range(ci, ci + cs):
                        while len(grid[rr]) <= cc:
                            grid[rr].append(None)
                        grid[rr][cc] = val
                ci += cs
        yield idx, item, grid


def slug(name):
    # Preserve '+'; Ryzen Max and Max+ are different product families.
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace("+", " plus ")).strip("-")


def aliases(name):
    short = re.sub(r"^(Intel|AMD|Apple) ", "", name)
    return sorted({name, short}, key=str.lower)


def expand_pro(brand, sku):
    optional = bool(re.search(r"\(\s*PRO\s*\)", sku, re.I))
    pro = bool(re.search(r"\bPRO\b", sku, re.I))
    sku = clean(re.sub(r"\(?\s*PRO\s*\)?", " ", sku, flags=re.I))
    brand = brand.replace("MAX", "Max")
    names = [f"AMD {brand} {sku}"] if not pro or optional else []
    if pro:
        names.append(f"AMD {brand} PRO {sku}")
    return names


def main(snapshot_dir):
    entries = {}
    source_counts = Counter()

    def add(name, vendor, generation, platform, source, section, **extra):
        name = clean(name)
        key = slug(name)
        if key in entries:
            entry = entries[key]
            if source not in entry["source_urls"]:
                entry["source_urls"].append(source)
            if platform not in entry["platforms"]:
                entry["platforms"].append(platform)
            return
        entries[key] = {
            "id": key, "name": name, "kind": "cpu", "vendor": vendor,
            "generation": generation, "platforms": [platform], "aliases": aliases(name),
            "source_urls": [source], "source_section": section,
            "checked_on": AS_OF, "listing_status": "source-listed",
            "score_status": "missing-gb6", **extra,
        }
        source_counts[source] += 1

    intel_files = [
        ("wiki-intel-i7-tables.json", "List_of_Intel_Core_desktop_processors", "desktop", range(20, 43)),
        ("wiki-intel-mobile-tables.json", "List_of_Intel_Core_mobile_processors", "laptop", range(21, 77)),
        ("wiki-intel-embedded-tables.json", "List_of_Intel_Core_embedded_processors", "embedded", range(5, 30)),
        ("wiki-intel-tables.json", "List_of_Intel_processors", "laptop", range(2, 24)),
    ]
    for filename, page, default_platform, indices in intel_files:
        for idx, item, rows in grids(snapshot_dir / filename):
            if idx not in indices:
                continue
            context = " / ".join(item.get("context", []))
            gen = re.search(r"(\d+)(?:st|nd|rd|th) gen", context)
            series = re.search(r"Series (\d+(?: Plus)?)", context)
            generation = "Core " + (gen.group(1) + "th gen" if gen else "Series " + series.group(1) if series else "unspecified")
            generation = generation.replace("1th", "1st").replace("2th", "2nd").replace("3th", "3rd") if gen and int(gen.group(1)) < 10 else generation
            platform = default_platform
            if default_platform == "laptop" and page == "List_of_Intel_processors":
                platform = "embedded" if "Embedded" in context else "desktop" if context.startswith("Desktop") else "laptop"
            for row in rows:
                if len(row) < 2 or not re.fullmatch(r"Core (?:[im][3579]|M|(?:Ultra )?[X]?[3579])", row[0] or ""):
                    continue
                brand, sku = row[:2]
                if not re.fullmatch(r"[A-Za-z]?\d[\w-]*(?: Plus)?", sku or ""):
                    continue
                separator = "-" if re.fullmatch(r"Core [im][3579]", brand) else " "
                add("Intel " + brand + separator + sku, "Intel", generation, platform,
                    "https://en.wikipedia.org/wiki/" + page, item["section"])

    for idx, item, rows in grids(snapshot_dir / "wiki-amd-tables.json"):
        if idx > 53:
            continue
        section = item["section"]
        zen = re.search(r"Zen\s*([1-6]?\+?)", section)
        generation = ("Zen+" if zen.group(1) == "+" else "Zen " + (zen.group(1) or "1")) if zen else "Zen (varies by model)"
        platform = "embedded" if idx >= 46 else "handheld" if idx >= 44 else "laptop" if idx >= 21 else "workstation" if "Threadripper" in section else "desktop"
        for row in rows:
            if len(row) < 2:
                continue
            brand, sku = row[:2]
            if idx == 44:
                # This source has malformed header rowspans; model text remains explicit.
                models = [value for value in row if value and re.fullmatch(r"Z1(?: Extreme)?", value)]
                names = ["AMD Ryzen " + m for m in models]
            elif 46 <= idx <= 50 and re.fullmatch(r"[VR]\d[A-Za-z0-9]+", brand or ""):
                names = ["AMD Ryzen Embedded " + brand]
            elif brand and brand.startswith("Ryzen") and sku and re.search(r"\d", sku) and len(sku) < 36:
                names = expand_pro(brand, sku)
            elif brand == "AMD" and sku in ("4700S", "4800S"):
                names = ["AMD " + sku]
            else:
                continue
            for name in names:
                add(name, "AMD", generation, platform, "https://en.wikipedia.org/wiki/List_of_AMD_Ryzen_processors", section)

    for idx, item, rows in grids(snapshot_dir / "wiki-epyc-tables.json"):
        if not 2 <= idx <= 8:
            continue
        generation = {2: "Zen 1", 3: "Zen 2", 4: "Zen 3", 5: "Zen 4", 6: "Zen 5", 7: "Zen 6", 8: "Zen 1"}[idx]
        for row in rows:
            sku = row[0] or ""
            if not re.fullmatch(r"[0-9][0-9A-Z]{3,6}(?:\s*\(P\))?", sku):
                continue
            variants = [sku]
            if "(P)" in sku:
                base = sku.replace("(P)", "").strip()
                variants = [base, base + "P"]
            for variant in variants:
                add("AMD EPYC " + variant, "AMD", generation, "embedded" if idx == 8 else "server",
                    "https://en.wikipedia.org/wiki/Epyc", item["section"])

    for idx, item, rows in grids(snapshot_dir / "wiki-athlon-tables.json"):
        if not 9 <= idx <= 13:
            continue
        for row in rows:
            if not row[0] or not row[0].startswith("Athlon"):
                continue
            name = row[0] + (" " + row[1] if idx == 13 else "")
            if not re.search(r"\d", name):
                continue
            add("AMD " + name.replace("Pro", "PRO"), "AMD", "Zen 2" if idx == 13 else "Zen 1 / Zen+",
                "desktop" if idx < 11 else "laptop", "https://en.wikipedia.org/wiki/List_of_AMD_Athlon_processors", item["section"])

    apple = json.loads((snapshot_dir / "apple-family.json").read_text(encoding="utf-8"))
    for row in apple["rows"]:
        # Family cells concatenate the name with the core count ("M612C 12T").
        # Apple M-series has one thread per CPU core; use the separate T field.
        cores = re.search(r"(\d+)T\b", row["cells"][1])
        extra = {"cpu_cores": int(cores.group(1))} if cores else {}
        name = row["name"]
        if "CPU" not in name and cores:
            name = name.replace(" (", f" ({cores.group(1)}-CPU ", 1) if " (" in name else name + f" ({cores.group(1)}-CPU)"
        extra["source_name"] = row["name"]
        add(name, "Apple", re.search(r"M\d+", name).group(), "apple-silicon",
            urljoin(apple["url"], row["url"]) if row["url"] else apple["url"], "Apple M series", **extra)

    for item in json.loads((snapshot_dir / "mac-gb7-tables.json").read_text(encoding="utf-8")):
        soup = BeautifulSoup(item["html"], "html.parser")
        for row in soup.select("tbody tr"):
            link, description = row.select_one("td.name a"), row.select_one(".description")
            if not link or not description:
                continue
            machine, desc = clean(link.get_text()), clean(description.get_text())
            year = re.search(r"\b(20\d{2})\b", machine)
            if not year or int(year.group(1)) < 2013:
                continue
            cpu = desc.split(" @ ")[0]
            if cpu.startswith("Intel ") and slug(cpu) not in entries:
                add(cpu, "Intel", "Intel Mac CPU", "desktop" if "Xeon" in cpu else "laptop",
                    urljoin("https://browser.geekbench.com", link["href"]), "CPU identified by Mac model listing")
            generation = re.search(r"\bM\d+\b", cpu)
            name = machine + " — " + desc
            add(name, "Apple", generation.group() if generation else "Intel Mac", "laptop" if "MacBook" in machine else "desktop",
                urljoin("https://browser.geekbench.com", link["href"]), "Mac benchmark chart (GB7; inventory only)",
                kind="mac", cpu_name=cpu, configuration=desc, year=int(year.group(1)),
                score_status="version-conflict", aliases=[name],
                score_note="Chart says Geekbench 7; some detail pages say both 6 and 7. Chart scores are not imported.")

    records = sorted(entries.values(), key=lambda c: (c["vendor"], c["kind"], c["name"]))
    payload = {
        "schema_version": 1, "as_of": AS_OF,
        "scope": "Intel Core 4th generation onward; AMD Zen families; Apple M1-M6 configurations and Intel/Silicon Macs from 2013 onward",
        "completeness": "Snapshot of the cited public lists, not a guarantee of every OEM, regional SKU or build-to-order configuration. Listings do not independently verify release or availability.",
        "license": "CC-BY-SA-4.0; see docs/cpu-data.md and data/SOURCES.md",
        "cpus": records,
    }
    (DATA / "cpu_catalog.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Catalog:", len(records), dict(Counter(c["vendor"] for c in records)), dict(Counter(c["kind"] for c in records)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot_dir", type=Path)
    main(parser.parse_args().snapshot_dir)
