# CPU coverage and data maintenance

[Browse the complete catalog](cpu-catalog.md) · [English README](../README.md) · [中文](README.zh-CN.md)

The estimator separates **inventory** from **usable Geekbench 6 reference scores**. Its default report compares every scored entry, including older or slower CPUs. Search, vendor, generation and platform filters and 25-row pages keep the HTML report usable. `--target-set tiers` selects the small curated comparison instead.

## Scope

- Intel Core desktop, mobile and embedded SKUs from the 4th generation through 14th generation, Core M, and the newer Core / Core Ultra Series 1–3, including source-listed Plus variants.
- AMD Zen families: Ryzen desktop/mobile/PRO, Ryzen AI and AI Max, Threadripper/PRO, Zen-based Athlon, handheld Ryzen Z, Ryzen Embedded and EPYC.
- Apple M1–M6 chip configurations listed by the sources, plus Intel and Apple Silicon Mac model/configuration records from 2013 onward. CPU-core bins and source-listed GPU bins remain separate.

This is a dated snapshot of the cited public lists, **not a guarantee of every worldwide OEM, regional or build-to-order SKU**. A source listing is not independent confirmation that a product has launched or is available to buy. Some sources list future products (for example, newer EPYC generations); those entries retain the same `source-listed` status and are not presented as verified releases. Do not invent a Pro, Max or Ultra variant just because another generation has one.

The catalog counts CPU configurations and Mac configurations separately. A Mac and the chip inside it are two inventory entries, not two distinct CPU designs. Stepping changes without a distinct public model name, RAM/storage options and all possible GPU-only Mac build-to-order combinations are not exhaustively enumerated.

## Data states and matching

| State | Meaning |
|---|---|
| `reference-gb6` | Both single-core and multi-core GB6 reference values are available for this CPU |
| `cpu-reference-gb6` | A Mac is mapped to an independently sourced CPU reference; this is not a measured result from that Mac |
| `missing-gb6` | Inventory entry with no complete verified GB6 score pair in this snapshot |
| `version-conflict` | Mac chart/detail pages have conflicting benchmark-version labels; their scores are excluded |

The Geekbench Mac chart identified itself as **Geekbench 7** when collected on 2026-11-01, while some detail pages said both 6 and 7. Those chart values are not imported into the GB6 score table. The independently labeled CPU-Monkey GB6 single-core and multi-core charts provide the new reference pairs. Their numbers are public reference values, not official Geekbench averages or measurements performed by this project.

Intel suffixes, AMD PRO and AF variants and Apple core configurations are preserved. An ambiguous alias such as `Apple M4 Pro` fails instead of selecting a core bin. Use the exact catalog name or ID, for example `Apple M4 Pro (12-CPU 16-GPU)`. A target without scores also fails explicitly; it is never silently replaced with a default target. The baseline still supports documented estimates, clearly labeled in the report.

For Mac projections, the CPU must match by exact Intel model, or by Apple family and CPU-core configuration, with an explicit GPU-bin match where available. Ambiguous references with different score pairs are left unresolved. The report labels CPU-based Mac estimates, including their cooling, power and memory limitations. GPU performance is not modeled.

## Inspect and export

```bash
# Full inventory, including entries with no scores; no transcript scan required
python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus

# Filter and machine-readable export
python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus --vendor Apple --generation M2 --json
python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus --vendor Intel --generation "Core 4th" --scored-only

# Apply filters to the default report comparisons
python skills/agent-speedup-estimator/scripts/agent_speedup.py --vendor AMD --generation "Zen 4"
```

Each report includes `cpu-catalog.json` and the full catalog in `summary.json`. HTML filtering changes only the visible page; all included comparisons remain in the report data and Markdown. The public demo uses synthetic activity and a synthetic baseline; its CPU reference data is sourced.

## Refresh workflow

The production skill uses only Python's standard library. Maintenance importers live in `tools/` and accept saved DOM snapshots; they do not scrape or call hidden website endpoints. Install `beautifulsoup4` only to run the inventory importer.

1. Read the public source pages and verify their visible title, benchmark version, filters and data. Save the relevant table DOM, not scripts or private browser state. Wikipedia snapshots are arrays of `{html, section, context}` (nearest-to-outer heading text); see `import_cpu_catalog.py` for the specific page filenames. Apple family snapshots contain `{url, rows:[{name,url,cells}]}`; Mac snapshots contain table HTML. The importer removes footnotes and expands row/column spans.
2. Preserve the scope of the source tables. Check malformed tables, optional `(PRO)` variants, suffixes and deduplication. Update section selection when a source table layout changes. Do not treat a truncated family page as a complete inventory.
3. Save paired GB6 search batches as `[{query, single:[{name,url,score,specs}], multi:[...]}]`. The charts return at most 20 rows per query; subdivide capped groups and inspect missing entries. Join by product URL and exact name, never by rank. A single-only or multi-only value is not eligible for projections.
4. Run `python tools/import_cpu_catalog.py SNAPSHOT_DIRECTORY`, then `python tools/import_cpu_scores.py SNAPSHOT_DIRECTORY/gb6-batches.json`. Inspect supplemental records and their generation/platform metadata. The import date is explicit in each importer; update it only when refreshing the sources.
5. Run the tests, `python tools/render_cpu_catalog.py`, and `python examples/generate_demo.py`. Inspect the HTML with a large catalog and a search returning no matches. Review changes before publishing.

Raw research snapshots stay outside the published dataset. The normalized catalog and scores retain per-entry source URLs and dates. Update the sources and attribution when adding a new source.

## Sources and license

See [data/SOURCES.md](../skills/agent-speedup-estimator/data/SOURCES.md) for attribution. The code is MIT. The derived catalog and its generated catalog tables use CC BY-SA 4.0, with Wikipedia contributor attribution and a description of transformations. Benchmark facts retain their source attribution; the MIT code license does not claim ownership of third-party material.
