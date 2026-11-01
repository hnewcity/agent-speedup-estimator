> Synthetic example — fictional activity and baseline; sourced target CPU references.

# Agent speedup estimate

**Expected end-to-end speedup on Intel Core Ultra 7 255H: 1.17x (range 1.11x – 1.23x), about 8m saved over the scanned period.**

- Scanned: 16 sessions, 2026-01-01 – 2026-01-02
- This machine: Demo baseline (synthetic) (4C/8T), 16.0 GB RAM, disk: sata
- Baseline score (Geekbench 6, single / multi): Demo baseline (synthetic), 1500 / 6000

## Where the time goes

|  | Claude Code | Codex | Total |
|---|---|---|---|
| Model (API) time | 16m | 16m | 32m |
| Local tool time | 12m | 12m | 24m |
| **Agent working** | 28m | 28m | 56m |
| Your replies and reading | 0s | 0s | 0s |
| Idle gaps (over 30 min) | 0s | 0s | 0s |
| Background tasks and sub-agents | 0s | 0s | 0s |
| Stalled (approvals, long gaps) | 0s | 0s | 0s |

**Hardware-sensitive time**: 17m (30%), the part of agent working time a faster computer can actually shorten.

## Local tool time by category

| Category | Runs | Time | Share | Median | p90 | Longest |
|---|---:|---:|---:|---:|---:|---:|
| Build, compile, lint | 4 | 12m | 51% | 180.0s | 180.0s | 3m |
| Tests | 4 | 6m | 25% | 90.0s | 90.0s | 2m |
| Dependency install | 4 | 5m | 23% | 80.0s | 80.0s | 80s |
| Git (local) | 4 | 20s | 1% | 5.0s | 5.0s | 5s |

Top command families: cargo 12m, pytest 6m, npm 5m, git 20s

## Projected speed on new hardware

| Target | Tier | Single-core | Multi-core | Tool time (Expected) | End to end (Expected) | range | Time saved |
|---|---|---:|---:|---:|---:|---:|---:|
| AMD Ryzen Threadripper PRO 9985WX | Zen 5 | 2.15x | 5.44x | 1.84x | **1.24x** | 1.15x – 1.32x | 11m |
| AMD Ryzen Threadripper PRO 9975WX | Zen 5 | 2.15x | 5.16x | 1.82x | **1.24x** | 1.15x – 1.32x | 11m |
| AMD Ryzen Threadripper 9980X | Zen 5 | 2.15x | 5.05x | 1.81x | **1.24x** | 1.15x – 1.31x | 11m |
| Apple M5 Max (18-CPU 32-GPU) | M5 | 2.89x | 4.88x | 1.89x | **1.25x** | 1.16x – 1.33x | 11m |
| Apple M5 Max (18-CPU 40-GPU) | M5 | 2.89x | 4.88x | 1.89x | **1.25x** | 1.16x – 1.33x | 11m |
| Mac Studio (2026) — Apple M5 Max @ 4.6 GHz (18 CPU cores, 32 GPU cores) | M5 | 2.89x | 4.88x | 1.89x | **1.25x** | 1.16x – 1.33x | 11m |
| Mac Studio (2026) — Apple M5 Max @ 4.6 GHz (18 CPU cores, 40 GPU cores) | M5 | 2.89x | 4.88x | 1.89x | **1.25x** | 1.16x – 1.33x | 11m |
| MacBook Pro (14-inch, 2026) — Apple M5 Max @ 4.6 GHz (18 CPU cores, 32 GPU cores) | M5 | 2.89x | 4.88x | 1.89x | **1.25x** | 1.16x – 1.33x | 11m |
| MacBook Pro (14-inch, 2026) — Apple M5 Max @ 4.6 GHz (18 CPU cores, 40 GPU cores) | M5 | 2.89x | 4.88x | 1.89x | **1.25x** | 1.16x – 1.33x | 11m |
| MacBook Pro (16-inch, 2026) — Apple M5 Max @ 4.6 GHz (18 CPU cores, 32 GPU cores) | M5 | 2.89x | 4.88x | 1.89x | **1.25x** | 1.16x – 1.33x | 11m |
| MacBook Pro (16-inch, 2026) — Apple M5 Max @ 4.6 GHz (18 CPU cores, 40 GPU cores) | M5 | 2.89x | 4.88x | 1.89x | **1.25x** | 1.16x – 1.33x | 11m |
| AMD Ryzen Threadripper 9970X | Zen 5 | 2.15x | 4.87x | 1.80x | **1.23x** | 1.15x – 1.31x | 11m |
| Apple M5 Pro (18-CPU 20-GPU) | M5 | 2.83x | 4.87x | 1.88x | **1.25x** | 1.16x – 1.33x | 11m |
| Mac mini (2026) — Apple M5 Pro @ 4.6 GHz (18 CPU cores, 20 GPU cores) | M5 | 2.83x | 4.87x | 1.88x | **1.25x** | 1.16x – 1.33x | 11m |
| MacBook Pro (14-inch, 2026) — Apple M5 Pro @ 4.6 GHz (18 CPU cores, 20 GPU cores) | M5 | 2.83x | 4.87x | 1.88x | **1.25x** | 1.16x – 1.33x | 11m |
| MacBook Pro (16-inch, 2026) — Apple M5 Pro @ 4.6 GHz (18 CPU cores, 20 GPU cores) | M5 | 2.83x | 4.87x | 1.88x | **1.25x** | 1.16x – 1.33x | 11m |
| Apple M3 Ultra (32-CPU 80-GPU) | M3 | 2.16x | 4.70x | 1.79x | **1.23x** | 1.15x – 1.31x | 10m |
| Mac Studio (2025) — Apple M3 Ultra @ 4.0 GHz (32 CPU cores, 80 GPU cores) | M3 | 2.16x | 4.70x | 1.79x | **1.23x** | 1.15x – 1.31x | 10m |
| AMD Ryzen Threadripper PRO 9965WX | Zen 5 | 2.15x | 4.59x | 1.79x | **1.23x** | 1.15x – 1.31x | 10m |
| AMD Ryzen Threadripper 7980X | Zen 4 | 1.93x | 4.43x | 1.74x | **1.22x** | 1.14x – 1.29x | 10m |
| Apple M4 Max (16-CPU 40-GPU) | M4 | 2.68x | 4.38x | 1.83x | **1.24x** | 1.15x – 1.32x | 11m |
| Mac Studio (2025) — Apple M4 Max @ 4.5 GHz (16 CPU cores, 40 GPU cores) | M4 | 2.68x | 4.38x | 1.83x | **1.24x** | 1.15x – 1.32x | 11m |
| MacBook Pro (14-inch, 2024) — Apple M4 Max @ 4.5 GHz (16 CPU cores, 40 GPU cores) | M4 | 2.68x | 4.38x | 1.83x | **1.24x** | 1.15x – 1.32x | 11m |
| MacBook Pro (16-inch, 2024) — Apple M4 Max @ 4.5 GHz (16 CPU cores, 40 GPU cores) | M4 | 2.68x | 4.38x | 1.83x | **1.24x** | 1.15x – 1.32x | 11m |
| Apple M3 Ultra (28-CPU 60-GPU) | M3 | 2.16x | 4.37x | 1.77x | **1.23x** | 1.14x – 1.30x | 10m |
| Mac Studio (2025) — Apple M3 Ultra @ 4.0 GHz (28 CPU cores, 60 GPU cores) | M3 | 2.16x | 4.37x | 1.77x | **1.23x** | 1.14x – 1.30x | 10m |
| Intel Core Ultra 9 285K | Core Series 2 | 2.18x | 4.31x | 1.77x | **1.23x** | 1.14x – 1.30x | 10m |
| AMD Ryzen Threadripper 7970X | Zen 4 | 1.96x | 4.24x | 1.73x | **1.22x** | 1.14x – 1.29x | 10m |
| AMD Ryzen Threadripper 9960X | Zen 5 | 2.15x | 4.22x | 1.76x | **1.23x** | 1.14x – 1.30x | 10m |
| Intel Core Ultra 7 270K Plus | Core Series 2 | 2.19x | 4.22x | 1.76x | **1.23x** | 1.14x – 1.30x | 10m |
| Apple M5 Pro (15-CPU 16-GPU) | M5 | 2.83x | 4.17x | 1.83x | **1.24x** | 1.15x – 1.32x | 11m |
| Mac mini (2026) — Apple M5 Pro @ 4.6 GHz (15 CPU cores, 16 GPU cores) | M5 | 2.83x | 4.17x | 1.83x | **1.24x** | 1.15x – 1.32x | 11m |
| MacBook Pro (14-inch, 2026) — Apple M5 Pro @ 4.6 GHz (15 CPU cores, 16 GPU cores) | M5 | 2.83x | 4.17x | 1.83x | **1.24x** | 1.15x – 1.32x | 11m |
| AMD Ryzen Threadripper PRO 7985WX | Zen 4 | 1.73x | 4.13x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD EPYC 4585PX | Zen 5 | 2.31x | 4.11x | 1.77x | **1.23x** | 1.14x – 1.30x | 10m |
| AMD Ryzen Threadripper PRO 7995WX | Zen 4 | 1.81x | 4.09x | 1.70x | **1.21x** | 1.13x – 1.28x | 10m |
| Apple M1 Ultra (20-CPU 48-GPU) | M1 | 1.60x | 4.00x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| Apple M1 Ultra (20-CPU 64-GPU) | M1 | 1.60x | 4.00x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| AMD Ryzen Threadripper 7960X | Zen 4 | 1.85x | 3.99x | 1.70x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD Ryzen Threadripper PRO 7965WX | Zen 4 | 1.85x | 3.99x | 1.70x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD EPYC 9554 | Zen 4 | 1.38x | 3.98x | 1.60x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core i9-14900KS | Core 14th gen | 2.23x | 3.97x | 1.75x | **1.22x** | 1.14x – 1.30x | 10m |
| AMD EPYC 9654 | Zen 4 | 1.35x | 3.87x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| AMD EPYC 9654P | Zen 4 | 1.35x | 3.87x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| Apple M4 Max (14-CPU 32-GPU) | M4 | 2.68x | 3.86x | 1.79x | **1.23x** | 1.15x – 1.31x | 10m |
| Mac Studio (2025) — Apple M4 Max @ 4.5 GHz (14 CPU cores, 32 GPU cores) | M4 | 2.68x | 3.86x | 1.79x | **1.23x** | 1.15x – 1.31x | 10m |
| MacBook Pro (14-inch, 2024) — Apple M4 Max @ 4.5 GHz (14 CPU cores, 32 GPU cores) | M4 | 2.68x | 3.86x | 1.79x | **1.23x** | 1.15x – 1.31x | 10m |
| MacBook Pro (16-inch, 2024) — Apple M4 Max @ 4.5 GHz (14 CPU cores, 32 GPU cores) | M4 | 2.68x | 3.86x | 1.79x | **1.23x** | 1.15x – 1.31x | 10m |
| Intel Core i9-14900K | Core 14th gen | 2.19x | 3.84x | 1.74x | **1.22x** | 1.14x – 1.29x | 10m |
| Intel Core i9-14900KF | Core 14th gen | 2.19x | 3.84x | 1.74x | **1.22x** | 1.14x – 1.29x | 10m |
| AMD Ryzen 9 9950X3D2 Dual Edition | Zen 5 | 2.35x | 3.82x | 1.75x | **1.22x** | 1.14x – 1.30x | 10m |
| Apple M4 Pro (14-CPU 20-GPU) | M4 | 2.63x | 3.78x | 1.78x | **1.23x** | 1.14x – 1.31x | 10m |
| Mac mini (2024) — Apple M4 Pro @ 4.5 GHz (14 CPU cores, 20 GPU cores) | M4 | 2.63x | 3.78x | 1.78x | **1.23x** | 1.14x – 1.31x | 10m |
| MacBook Pro (14-inch, 2024) — Apple M4 Pro @ 4.5 GHz (14 CPU cores, 20 GPU cores) | M4 | 2.63x | 3.78x | 1.78x | **1.23x** | 1.14x – 1.31x | 10m |
| MacBook Pro (16-inch, 2024) — Apple M4 Pro @ 4.5 GHz (14 CPU cores, 20 GPU cores) | M4 | 2.63x | 3.78x | 1.78x | **1.23x** | 1.14x – 1.31x | 10m |
| AMD Ryzen 9 9950X | Zen 5 | 2.27x | 3.74x | 1.74x | **1.22x** | 1.14x – 1.29x | 10m |
| AMD Ryzen AI Max+ 395 | Zen 5 | 2.05x | 3.72x | 1.71x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD Ryzen AI Max+ PRO 395 | Zen 5 | 2.05x | 3.72x | 1.71x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD Ryzen 9 9950X3D | Zen 5 | 2.29x | 3.69x | 1.73x | **1.22x** | 1.14x – 1.29x | 10m |
| Intel Core Ultra 7 265K | Core Series 2 | 2.14x | 3.61x | 1.71x | **1.21x** | 1.13x – 1.28x | 10m |
| Intel Core Ultra 7 265KF | Core Series 2 | 2.14x | 3.61x | 1.71x | **1.21x** | 1.13x – 1.28x | 10m |
| Apple M2 Ultra (24-CPU 60-GPU) | M2 | 1.79x | 3.58x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| Apple M2 Ultra (24-CPU 76-GPU) | M2 | 1.79x | 3.58x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| Mac Pro (2023) — Apple M2 Ultra @ 3.7 GHz (24 CPU cores, 60 GPU cores) | M2 | 1.79x | 3.58x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| Mac Pro (2023) — Apple M2 Ultra @ 3.7 GHz (24 CPU cores, 76 GPU cores) | M2 | 1.79x | 3.58x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| Mac Studio (2023) — Apple M2 Ultra @ 3.7 GHz (24 CPU cores, 60 GPU cores) | M2 | 1.79x | 3.58x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| Mac Studio (2023) — Apple M2 Ultra @ 3.7 GHz (24 CPU cores, 76 GPU cores) | M2 | 1.79x | 3.58x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| Apple M6 (12-CPU) | M6 | 3.11x | 3.56x | 1.81x | **1.24x** | 1.15x – 1.31x | 11m |
| Mac mini (2026) — Apple M6 @ 4.8 GHz (12 CPU cores, 12 GPU cores) | M6 | 3.11x | 3.56x | 1.81x | **1.24x** | 1.15x – 1.31x | 11m |
| AMD Ryzen Threadripper PRO 7955WX | Zen 4 | 2.01x | 3.51x | 1.68x | **1.21x** | 1.13x – 1.28x | 10m |
| Intel Core Ultra 9 290HX Plus | Core Series 2 | 2.12x | 3.51x | 1.70x | **1.21x** | 1.13x – 1.28x | 10m |
| Apple M3 Max (16-CPU 40-GPU) | M3 | 2.08x | 3.51x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| MacBook Pro (14-inch, Nov 2023) — Apple M3 Max @ 4.1 GHz (16 CPU cores, 40 GPU cores) | M3 | 2.08x | 3.51x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| MacBook Pro (16-inch, Nov 2023) — Apple M3 Max @ 4.1 GHz (16 CPU cores, 40 GPU cores) | M3 | 2.08x | 3.51x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD Ryzen 9 9955HX3D | Zen 5 | 2.19x | 3.49x | 1.70x | **1.21x** | 1.13x – 1.28x | 10m |
| Intel Core i9-13900KS | Core 13th gen | 2.00x | 3.49x | 1.68x | **1.21x** | 1.13x – 1.27x | 10m |
| AMD Ryzen 9 7950X | Zen 4 | 1.98x | 3.46x | 1.67x | **1.21x** | 1.13x – 1.27x | 9m |
| Intel Core Ultra 9 285HX | Core Series 2 | 1.98x | 3.46x | 1.67x | **1.21x** | 1.13x – 1.27x | 9m |
| Intel Core Ultra 7 265 | Core Series 2 | 2.08x | 3.46x | 1.68x | **1.21x** | 1.13x – 1.28x | 10m |
| Intel Core Ultra 7 265F | Core Series 2 | 2.08x | 3.46x | 1.68x | **1.21x** | 1.13x – 1.28x | 10m |
| Intel Core i9-14900 | Core 14th gen | 1.97x | 3.42x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| Intel Core i9-14900F | Core 14th gen | 1.97x | 3.42x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| Intel Core i9-13900K | Core 13th gen | 1.91x | 3.38x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| Intel Core i9-13900KF | Core 13th gen | 1.91x | 3.38x | 1.65x | **1.20x** | 1.13x – 1.27x | 9m |
| AMD Ryzen Threadripper PRO 3995WX | Zen 2 | 1.11x | 3.38x | 1.48x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen Threadripper PRO 9955WX | Zen 5 | 2.15x | 3.37x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD Ryzen Threadripper PRO 5995WX | Zen 3 | 1.37x | 3.36x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| Apple M4 Pro (12-CPU 16-GPU) | M4 | 2.63x | 3.35x | 1.74x | **1.22x** | 1.14x – 1.29x | 10m |
| Mac mini (2024) — Apple M4 Pro @ 4.5 GHz (12 CPU cores, 16 GPU cores) | M4 | 2.63x | 3.35x | 1.74x | **1.22x** | 1.14x – 1.29x | 10m |
| MacBook Pro (14-inch, 2024) — Apple M4 Pro @ 4.5 GHz (12 CPU cores, 16 GPU cores) | M4 | 2.63x | 3.35x | 1.74x | **1.22x** | 1.14x – 1.29x | 10m |
| AMD Ryzen Threadripper PRO 5975WX | Zen 3 | 1.37x | 3.33x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| AMD Ryzen 9 9900X | Zen 5 | 2.23x | 3.29x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD Ryzen 9 9900X3D | Zen 5 | 2.23x | 3.29x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| Intel Core i9-13900 | Core 13th gen | 1.92x | 3.29x | 1.64x | **1.20x** | 1.13x – 1.26x | 9m |
| Intel Core Ultra 5 250K Plus | Core Series 2 | 2.09x | 3.27x | 1.67x | **1.21x** | 1.13x – 1.27x | 9m |
| Intel Core i7-14700K | Core 14th gen | 1.95x | 3.26x | 1.65x | **1.20x** | 1.13x – 1.26x | 9m |
| Intel Core i7-14700KF | Core 14th gen | 1.95x | 3.26x | 1.65x | **1.20x** | 1.13x – 1.26x | 9m |
| AMD Ryzen Threadripper PRO 7975WX | Zen 4 | 1.79x | 3.25x | 1.62x | **1.19x** | 1.12x – 1.26x | 9m |
| AMD Ryzen 9 7950X3D | Zen 4 | 1.94x | 3.25x | 1.64x | **1.20x** | 1.13x – 1.26x | 9m |
| Apple M3 Max (14-CPU 30-GPU) | M3 | 2.08x | 3.23x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| MacBook Pro (14-inch, Nov 2023) — Apple M3 Max @ 4.1 GHz (14 CPU cores, 30 GPU cores) | M3 | 2.08x | 3.23x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| MacBook Pro (16-inch, Nov 2023) — Apple M3 Max @ 4.1 GHz (14 CPU cores, 30 GPU cores) | M3 | 2.08x | 3.23x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| Intel Core Ultra 5 250KF Plus | Core Series 2 | 2.11x | 3.19x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| Intel Core Ultra 9 285T | Core Series 2 | 2.09x | 3.17x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| AMD Ryzen 7 9850X3D | Zen 5 | 2.35x | 3.16x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| AMD Ryzen 9 7900X | Zen 4 | 1.95x | 3.15x | 1.63x | **1.20x** | 1.12x – 1.26x | 9m |
| Intel Core i7-14700F | Core 14th gen | 1.89x | 3.15x | 1.62x | **1.20x** | 1.12x – 1.26x | 9m |
| Intel Core i7-14700 | Core 14th gen | 1.89x | 3.15x | 1.62x | **1.20x** | 1.12x – 1.26x | 9m |
| AMD Ryzen Threadripper PRO 5965WX | Zen 3 | 1.37x | 3.14x | 1.52x | **1.17x** | 1.11x – 1.22x | 8m |
| Intel Core Ultra 9 275HX | Core Series 2 | 2.02x | 3.13x | 1.64x | **1.20x** | 1.13x – 1.26x | 9m |
| AMD Ryzen 9 9955HX | Zen 5 | 2.19x | 3.12x | 1.67x | **1.21x** | 1.13x – 1.27x | 9m |
| AMD Ryzen 9 PRO 9945 | Zen 5 | 2.19x | 3.10x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| Intel Core i9-13900F | Core 13th gen | 1.86x | 3.09x | 1.61x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core Ultra 9 285 | Core Series 2 | 2.17x | 3.07x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| Intel Core i7-14700T | Core 14th gen | 1.81x | 3.06x | 1.60x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core i9-14900HX | Core 14th gen | 1.95x | 3.05x | 1.62x | **1.20x** | 1.12x – 1.26x | 9m |
| AMD Ryzen 9 9850HX | Zen 5 | 2.09x | 3.05x | 1.64x | **1.20x** | 1.13x – 1.26x | 9m |
| AMD EPYC 75F3 | Zen 3 | 1.20x | 3.04x | 1.47x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen Threadripper PRO 7945WX | Zen 4 | 1.85x | 3.04x | 1.60x | **1.19x** | 1.12x – 1.25x | 9m |
| AMD Ryzen 7 9800X3D | Zen 5 | 2.20x | 3.04x | 1.66x | **1.20x** | 1.13x – 1.27x | 9m |
| AMD EPYC 7543 | Zen 3 | 1.14x | 3.01x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD EPYC 7543P | Zen 3 | 1.14x | 3.01x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD EPYC 7513 | Zen 3 | 1.14x | 3.01x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD EPYC 9254 | Zen 4 | 1.49x | 3.00x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| Intel Core Ultra 5 245 | Core Series 2 | 2.00x | 3.00x | 1.62x | **1.20x** | 1.12x – 1.26x | 9m |
| Apple M5 (10-CPU) | M5 | 2.87x | 2.98x | 1.73x | **1.22x** | 1.14x – 1.29x | 10m |
| MacBook Air (13-inch, 2026) — Apple M5 @ 4.5 GHz (10 CPU cores, 10 GPU cores) | M5 | 2.87x | 2.98x | 1.73x | **1.22x** | 1.14x – 1.29x | 10m |
| MacBook Air (13-inch, 2026) — Apple M5 @ 4.5 GHz (10 CPU cores, 8 GPU cores) | M5 | 2.87x | 2.98x | 1.73x | **1.22x** | 1.14x – 1.29x | 10m |
| MacBook Air (15-inch, 2026) — Apple M5 @ 4.5 GHz (10 CPU cores, 10 GPU cores) | M5 | 2.87x | 2.98x | 1.73x | **1.22x** | 1.14x – 1.29x | 10m |
| MacBook Pro (14-inch, 2025) — Apple M5 @ 4.6 GHz (10 CPU cores, 10 GPU cores) | M5 | 2.87x | 2.98x | 1.73x | **1.22x** | 1.14x – 1.29x | 10m |
| AMD Ryzen 9 7900X3D | Zen 4 | 1.93x | 2.98x | 1.61x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core i9-14900T | Core 14th gen | 1.96x | 2.98x | 1.62x | **1.19x** | 1.12x – 1.26x | 9m |
| AMD Ryzen AI Max+ 392 | Zen 5 | 1.93x | 2.97x | 1.61x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core Ultra 5 245K | Core Series 2 | 2.03x | 2.96x | 1.62x | **1.20x** | 1.12x – 1.26x | 9m |
| Intel Core Ultra 5 235 | Core Series 2 | 1.97x | 2.95x | 1.61x | **1.19x** | 1.12x – 1.26x | 9m |
| Intel Core Ultra 9 285H | Core Series 2 | 2.00x | 2.93x | 1.62x | **1.19x** | 1.12x – 1.26x | 9m |
| AMD Ryzen 9 8940HX | Zen 4 | 1.85x | 2.91x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core Ultra 5 245KF | Core Series 2 | 2.03x | 2.90x | 1.62x | **1.19x** | 1.12x – 1.26x | 9m |
| Intel Core Ultra 7 265HX | Core Series 2 | 2.00x | 2.90x | 1.61x | **1.19x** | 1.12x – 1.26x | 9m |
| Intel Core Ultra 7 255HX | Core Series 2 | 1.96x | 2.90x | 1.61x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core i7-13700K | Core 13th gen | 1.86x | 2.87x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core i7-13700KF | Core 13th gen | 1.86x | 2.87x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| AMD Ryzen Threadripper PRO 5955WX | Zen 3 | 1.37x | 2.87x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i5-14600K | Core 14th gen | 1.86x | 2.87x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core i5-14600KF | Core 14th gen | 1.86x | 2.87x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core Ultra X9 388H | Core Series 3 | 1.98x | 2.86x | 1.60x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core i9-13980HX | Core 13th gen | 1.88x | 2.85x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| AMD EPYC 74F3 | Zen 3 | 1.24x | 2.83x | 1.46x | **1.15x** | 1.10x – 1.20x | 7m |
| Intel Core Ultra X7 368H | Core Series 3 | 1.98x | 2.83x | 1.60x | **1.19x** | 1.12x – 1.25x | 9m |
| AMD Ryzen 9 7900 | Zen 4 | 1.86x | 2.81x | 1.58x | **1.19x** | 1.12x – 1.25x | 9m |
| AMD Ryzen 9 PRO 7945 | Zen 4 | 1.86x | 2.81x | 1.58x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core Ultra X7 358H | Core Series 3 | 1.95x | 2.79x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| AMD EPYC 7443P | Zen 3 | 1.17x | 2.78x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Intel Core i9-13950HX | Core 13th gen | 1.83x | 2.75x | 1.57x | **1.18x** | 1.11x – 1.24x | 9m |
| Apple M5 (9-CPU) | M5 | 2.75x | 2.75x | 1.69x | **1.21x** | 1.13x – 1.28x | 10m |
| Intel Core Ultra 7 265T | Core Series 2 | 1.97x | 2.74x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core i9-12900KS | Core 12th gen | 1.89x | 2.74x | 1.58x | **1.18x** | 1.12x – 1.24x | 9m |
| Intel Core i9-14901KE | Core 14th gen | 1.99x | 2.71x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| AMD Ryzen AI Max 390 | Zen 5 | 1.92x | 2.71x | 1.58x | **1.18x** | 1.12x – 1.24x | 9m |
| AMD Ryzen AI Max PRO 390 | Zen 5 | 1.92x | 2.71x | 1.58x | **1.18x** | 1.12x – 1.24x | 9m |
| Intel Core i9-12900K | Core 12th gen | 1.71x | 2.71x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| AMD Ryzen 9 7945HX | Zen 4 | 1.85x | 2.70x | 1.56x | **1.18x** | 1.11x – 1.24x | 9m |
| Intel Core i7-14700HX | Core 14th gen | 1.90x | 2.70x | 1.57x | **1.18x** | 1.12x – 1.24x | 9m |
| Intel Core i5-13600K | Core 13th gen | 1.76x | 2.70x | 1.55x | **1.18x** | 1.11x – 1.23x | 8m |
| Intel Core i5-13600KF | Core 13th gen | 1.76x | 2.70x | 1.55x | **1.18x** | 1.11x – 1.23x | 8m |
| AMD Ryzen 7 9700F | Zen 5 | 2.20x | 2.69x | 1.62x | **1.19x** | 1.12x – 1.26x | 9m |
| AMD Ryzen 7 9700X | Zen 5 | 2.24x | 2.69x | 1.62x | **1.20x** | 1.12x – 1.26x | 9m |
| Intel Core i5-14600 | Core 14th gen | 1.86x | 2.69x | 1.56x | **1.18x** | 1.11x – 1.24x | 9m |
| AMD Ryzen 9 7945HX3D | Zen 4 | 1.85x | 2.68x | 1.56x | **1.18x** | 1.11x – 1.24x | 9m |
| Intel Core i7-13700 | Core 13th gen | 1.78x | 2.68x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| Intel Core i7-13700F | Core 13th gen | 1.78x | 2.68x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| AMD Ryzen 7 PRO 9745 | Zen 5 | 2.19x | 2.67x | 1.61x | **1.19x** | 1.12x – 1.26x | 9m |
| AMD EPYC 7763 | Zen 3 | 1.07x | 2.67x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core i9-12900KF | Core 12th gen | 1.78x | 2.66x | 1.55x | **1.18x** | 1.11x – 1.23x | 8m |
| Intel Core Ultra 5 230F | Core Series 2 | 1.97x | 2.65x | 1.58x | **1.18x** | 1.12x – 1.24x | 9m |
| AMD EPYC 7713 | Zen 3 | 1.15x | 2.65x | 1.41x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD EPYC 7443 | Zen 3 | 1.16x | 2.64x | 1.41x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core i9-13900E | Core 13th gen | 1.74x | 2.64x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| Intel Core Ultra 9 386H | Core Series 3 | 1.87x | 2.64x | 1.56x | **1.18x** | 1.11x – 1.24x | 9m |
| AMD Ryzen Threadripper 3990X | Zen 2 | 1.09x | 2.64x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD Ryzen 9 7940HX | Zen 4 | 1.79x | 2.63x | 1.55x | **1.18x** | 1.11x – 1.23x | 8m |
| Intel Core i9-13900HX | Core 13th gen | 1.81x | 2.62x | 1.55x | **1.18x** | 1.11x – 1.23x | 8m |
| AMD EPYC 7642 | Zen 2 | 0.89x | 2.61x | 1.32x | **1.11x** | 1.07x – 1.15x | 6m |
| Apple M3 Pro (12-CPU 18-GPU) | M3 | 2.10x | 2.60x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| MacBook Pro (14-inch, Nov 2023) — Apple M3 Pro @ 4.1 GHz (12 CPU cores, 18 GPU cores) | M3 | 2.10x | 2.60x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| MacBook Pro (16-inch, Nov 2023) — Apple M3 Pro @ 4.1 GHz (12 CPU cores, 18 GPU cores) | M3 | 2.10x | 2.60x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core Ultra 7 366H | Core Series 3 | 1.83x | 2.58x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| Intel Core Ultra 7 251HX | Core Series 2 | 1.94x | 2.56x | 1.56x | **1.18x** | 1.11x – 1.24x | 9m |
| Intel Core i9-12900 | Core 12th gen | 1.76x | 2.56x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| Intel Core i9-12900F | Core 12th gen | 1.76x | 2.56x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| Intel Core i5-14600T | Core 14th gen | 1.75x | 2.56x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| Intel Core Ultra 5 225 | Core Series 2 | 1.93x | 2.56x | 1.56x | **1.18x** | 1.11x – 1.24x | 8m |
| AMD Ryzen Threadripper PRO 3975WX | Zen 2 | 1.08x | 2.55x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD EPYC 7313 | Zen 3 | 1.16x | 2.54x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD Ryzen 7 7700X | Zen 4 | 1.93x | 2.52x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| AMD Ryzen AI 9 HX 370 | Zen 5 | 1.94x | 2.51x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| AMD Ryzen AI 9 HX 375 | Zen 5 | 1.94x | 2.51x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| AMD Ryzen AI 9 PRO HX 370 | Zen 5 | 1.94x | 2.51x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| AMD Ryzen AI 9 PRO HX 375 | Zen 5 | 1.94x | 2.51x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| Intel Core Ultra 7 356H | Core Series 3 | 1.81x | 2.50x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| Intel Core i7-13700T | Core 13th gen | 1.69x | 2.50x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| AMD EPYC 7643 | Zen 3 | 1.11x | 2.50x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen AI 9 HX 470 | Zen 5 | 1.94x | 2.50x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| Intel Core i5-14500 | Core 14th gen | 1.78x | 2.49x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| Intel Core i5-13600 | Core 13th gen | 1.66x | 2.49x | 1.50x | **1.17x** | 1.10x – 1.22x | 8m |
| Intel Core Ultra 7 265H | Core Series 2 | 1.94x | 2.49x | 1.55x | **1.18x** | 1.11x – 1.24x | 8m |
| Apple M4 (10-CPU) | M4 | 2.54x | 2.49x | 1.64x | **1.20x** | 1.12x – 1.26x | 9m |
| Mac mini (2024) — Apple M4 @ 4.4 GHz (10 CPU cores, 10 GPU cores) | M4 | 2.54x | 2.49x | 1.64x | **1.20x** | 1.12x – 1.26x | 9m |
| MacBook Air (13-inch, 2025) — Apple M4 @ 4.4 GHz (10 CPU cores, 10 GPU cores) | M4 | 2.54x | 2.49x | 1.64x | **1.20x** | 1.12x – 1.26x | 9m |
| MacBook Air (13-inch, 2025) — Apple M4 @ 4.4 GHz (10 CPU cores, 8 GPU cores) | M4 | 2.54x | 2.49x | 1.64x | **1.20x** | 1.12x – 1.26x | 9m |
| MacBook Air (15-inch, 2025) — Apple M4 @ 4.4 GHz (10 CPU cores, 10 GPU cores) | M4 | 2.54x | 2.49x | 1.64x | **1.20x** | 1.12x – 1.26x | 9m |
| MacBook Pro (14-inch, 2024) — Apple M4 @ 4.4 GHz (10 CPU cores, 10 GPU cores) | M4 | 2.54x | 2.49x | 1.64x | **1.20x** | 1.12x – 1.26x | 9m |
| iMac (24-inch, 2024) — Apple M4 @ 4.4 GHz (10 CPU cores, 10 GPU cores) | M4 | 2.54x | 2.49x | 1.64x | **1.20x** | 1.12x – 1.26x | 9m |
| AMD EPYC 7413 | Zen 3 | 1.14x | 2.49x | 1.38x | **1.13x** | 1.08x – 1.17x | 7m |
| AMD EPYC 7313P | Zen 3 | 1.15x | 2.48x | 1.38x | **1.13x** | 1.09x – 1.17x | 7m |
| Intel Core Ultra 5 245T | Core Series 2 | 1.92x | 2.47x | 1.55x | **1.18x** | 1.11x – 1.23x | 8m |
| Intel Core i7-13700E | Core 13th gen | 1.69x | 2.45x | 1.50x | **1.17x** | 1.10x – 1.22x | 8m |
| AMD Ryzen 7 7700 | Zen 4 | 1.85x | 2.45x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| AMD Ryzen 7 PRO 7745 | Zen 4 | 1.85x | 2.45x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| AMD Ryzen AI Max+ 388 | Zen 5 | 1.92x | 2.45x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| AMD Ryzen Threadripper 3970X | Zen 2 | 1.15x | 2.44x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core i9-13900T | Core 13th gen | 1.75x | 2.44x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| Intel Core i9-12900HX | Core 12th gen | 1.62x | 2.44x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen AI 9 HX 475 | Zen 5 | 1.91x | 2.43x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| Intel Core i7-13850HX | Core 13th gen | 1.80x | 2.43x | 1.52x | **1.17x** | 1.11x – 1.23x | 8m |
| AMD Ryzen AI Max 385 | Zen 5 | 1.92x | 2.40x | 1.54x | **1.17x** | 1.11x – 1.23x | 8m |
| AMD Ryzen AI Max PRO 385 | Zen 5 | 1.92x | 2.40x | 1.54x | **1.17x** | 1.11x – 1.23x | 8m |
| Intel Core i7-14650HX | Core 14th gen | 1.80x | 2.40x | 1.52x | **1.17x** | 1.11x – 1.22x | 8m |
| AMD Ryzen 5 9600X | Zen 5 | 2.19x | 2.40x | 1.58x | **1.18x** | 1.12x – 1.25x | 9m |
| AMD EPYC 7542 | Zen 2 | 0.91x | 2.40x | 1.30x | **1.11x** | 1.07x – 1.14x | 5m |
| AMD Ryzen 5 9500F | Zen 5 | 2.08x | 2.40x | 1.56x | **1.18x** | 1.11x – 1.24x | 8m |
| Intel Core Ultra 7 255H | Core Series 2 | 1.84x | 2.39x | 1.52x | **1.17x** | 1.11x – 1.23x | 8m |
| AMD Ryzen 7 8700F | Zen 4 | 1.81x | 2.39x | 1.52x | **1.17x** | 1.11x – 1.22x | 8m |
| AMD Ryzen 7 8700G | Zen 4 | 1.81x | 2.39x | 1.52x | **1.17x** | 1.11x – 1.22x | 8m |
| AMD Ryzen 7 PRO 8700G | Source-listed (see product page) | 1.81x | 2.39x | 1.52x | **1.17x** | 1.11x – 1.22x | 8m |
| Intel Core Ultra 5 225F | Core Series 2 | 1.90x | 2.38x | 1.53x | **1.17x** | 1.11x – 1.23x | 8m |
| AMD Ryzen 5 9600 | Zen 5 | 2.11x | 2.38x | 1.56x | **1.18x** | 1.11x – 1.24x | 9m |
| AMD Ryzen 7 7800X3D | Zen 4 | 1.82x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| Apple M2 Max (12-CPU 30-GPU) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| Apple M2 Max (12-CPU 38-GPU) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| Apple M2 Pro (12-CPU 19-GPU) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| Mac Studio (2023) — Apple M2 Max @ 3.7 GHz (12 CPU cores, 38 GPU cores) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| Mac mini (2023) — Apple M2 Pro @ 3.5 GHz (12 CPU cores, 19 GPU cores) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| MacBook Pro (14-inch, 2023) — Apple M2 Pro @ 3.5 GHz (12 CPU cores, 19 GPU cores) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| MacBook Pro (16-inch, 2023) — Apple M2 Max @ 3.7 GHz (12 CPU cores, 30 GPU cores) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| MacBook Pro (16-inch, 2023) — Apple M2 Max @ 3.7 GHz (12 CPU cores, 38 GPU cores) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| MacBook Pro (16-inch, 2023) — Apple M2 Pro @ 3.5 GHz (12 CPU cores, 19 GPU cores) | M2 | 1.79x | 2.37x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| Intel Core i5-13500 | Core 13th gen | 1.58x | 2.36x | 1.47x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen 7 7700X3D | Zen 4 | 1.70x | 2.36x | 1.49x | **1.16x** | 1.10x – 1.22x | 8m |
| Intel Core i7-12700K | Core 12th gen | 1.69x | 2.35x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i7-12700KF | Core 12th gen | 1.69x | 2.35x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen 5 PRO 9645 | Source-listed (see product page) | 2.19x | 2.35x | 1.57x | **1.18x** | 1.11x – 1.24x | 9m |
| Intel Core i7-13650HX | Core 13th gen | 1.68x | 2.35x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i7-12800HX | Core 12th gen | 1.49x | 2.32x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Intel Core i7-12850HX | Core 12th gen | 1.49x | 2.32x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen Threadripper 3960X | Zen 2 | 1.12x | 2.31x | 1.35x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i7-13700HX | Core 13th gen | 1.69x | 2.30x | 1.48x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen Threadripper PRO 5945WX | Zen 3 | 1.37x | 2.30x | 1.41x | **1.14x** | 1.09x – 1.19x | 7m |
| Apple M3 Pro (11-CPU 14-GPU) | M3 | 2.08x | 2.29x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| MacBook Pro (14-inch, Nov 2023) — Apple M3 Pro @ 4.1 GHz (11 CPU cores, 14 GPU cores) | M3 | 2.08x | 2.29x | 1.54x | **1.18x** | 1.11x – 1.23x | 8m |
| AMD Ryzen Threadripper PRO 3955WX | Zen 2 | 1.10x | 2.29x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| AMD EPYC 9174F | Zen 4 | 1.52x | 2.28x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Intel Core i5-14400 | Core 14th gen | 1.71x | 2.28x | 1.48x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i5-14400F | Core 14th gen | 1.71x | 2.28x | 1.48x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD EPYC 7F72 | Zen 2 | 0.97x | 2.28x | 1.30x | **1.11x** | 1.07x – 1.14x | 5m |
| AMD Ryzen 9 7845HX | Zen 4 | 1.76x | 2.28x | 1.49x | **1.16x** | 1.10x – 1.22x | 8m |
| Intel Core i9-12950HX | Core 12th gen | 1.57x | 2.27x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Intel Core i9-13905H | Core 13th gen | 1.69x | 2.27x | 1.48x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i9-13900H | Core 13th gen | 1.75x | 2.27x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i9-13900HK | Core 13th gen | 1.75x | 2.27x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i7-13800H | Core 13th gen | 1.74x | 2.27x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen AI 9 465 | Zen 5 | 1.88x | 2.26x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| AMD Ryzen 7 7745HX | Zen 4 | 1.78x | 2.24x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen AI 7 350 | Zen 5 | 1.90x | 2.23x | 1.51x | **1.17x** | 1.11x – 1.22x | 8m |
| Intel Core i7-13800HE | Core 13th gen | 1.69x | 2.23x | 1.47x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i7-13800HRE | Core 13th gen | 1.69x | 2.23x | 1.47x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i7-13700H | Core 13th gen | 1.69x | 2.23x | 1.47x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i7-13705H | Core 13th gen | 1.69x | 2.23x | 1.47x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD EPYC 7402P | Zen 2 | 0.88x | 2.23x | 1.26x | **1.10x** | 1.06x – 1.12x | 5m |
| AMD Ryzen 9 5950X | Zen 3 | 1.48x | 2.22x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Apple M4 (9-CPU) | M4 | 2.51x | 2.22x | 1.59x | **1.19x** | 1.12x – 1.25x | 9m |
| Intel Core Ultra 5 235H | Core Series 2 | 1.81x | 2.21x | 1.49x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i9-12900T | Core 12th gen | 1.67x | 2.21x | 1.46x | **1.16x** | 1.10x – 1.21x | 7m |
| Intel Core i5-13600HX | Core 13th gen | 1.60x | 2.19x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Intel Core i5-14500HX | Core 14th gen | 1.64x | 2.19x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Intel Core i9-12900E | Core 12th gen | 1.74x | 2.18x | 1.47x | **1.16x** | 1.10x – 1.21x | 8m |
| AMD Ryzen 9 5900XT | Zen 3 | 1.47x | 2.18x | 1.42x | **1.14x** | 1.09x – 1.19x | 7m |
| AMD Ryzen AI 7 450 | Zen 5 | 1.91x | 2.18x | 1.50x | **1.17x** | 1.10x – 1.22x | 8m |
| AMD Ryzen AI 9 365 | Zen 5 | 1.81x | 2.18x | 1.48x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core Ultra 5 235T | Core Series 2 | 1.84x | 2.14x | 1.48x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core Ultra 5 338H | Core Series 3 | 1.78x | 2.13x | 1.47x | **1.16x** | 1.10x – 1.21x | 8m |
| Intel Core i5-14500T | Core 14th gen | 1.71x | 2.13x | 1.46x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 5 7600X | Zen 4 | 1.90x | 2.12x | 1.49x | **1.16x** | 1.10x – 1.22x | 8m |
| Intel Core i9-11900K | Core 11th gen | 1.66x | 2.11x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Intel Core i5-13500HX | Core 13th gen | 1.57x | 2.11x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Intel Core Ultra 7 165H | Core Series 1 | 1.67x | 2.09x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| Intel Core i7-12700 | Core 12th gen | 1.67x | 2.08x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| Intel Core i7-12700F | Core 12th gen | 1.67x | 2.08x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| AMD Ryzen 9 7940H | Zen 4 | 1.75x | 2.08x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 9 7940HS | Zen 4 | 1.75x | 2.08x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 9 8945H | Source-listed (see product page) | 1.75x | 2.08x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 9 8945HS | Zen 4 | 1.75x | 2.08x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 9 PRO 7940HS | Zen 4 | 1.75x | 2.08x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 9 PRO 8945HS | Source-listed (see product page) | 1.75x | 2.08x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Apple M1 Max (10-CPU 24-GPU) | M1 | 1.60x | 2.07x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Apple M1 Max (10-CPU 32-GPU) | M1 | 1.60x | 2.07x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| MacBook Pro (14-inch, 2021) — Apple M1 Max @ 3.2 GHz (10 cores) | M1 | 1.60x | 2.07x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| MacBook Pro (16-inch, 2021) — Apple M1 Max @ 3.2 GHz (10 cores) | M1 | 1.60x | 2.07x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 9 5900X | Zen 3 | 1.47x | 2.07x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core i9-12900TE | Core 12th gen | 1.65x | 2.07x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| Intel Core Ultra 7 155H | Core Series 1 | 1.60x | 2.07x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Apple M1 Pro (10-CPU 14-GPU) | M1 | 1.60x | 2.07x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Apple M1 Pro (10-CPU 16-GPU) | M1 | 1.60x | 2.07x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| MacBook Pro (14-inch, 2021) — Apple M1 Pro @ 3.2 GHz (10 cores) | M1 | 1.60x | 2.07x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Intel Core i9-13900TE | Core 13th gen | 1.54x | 2.06x | 1.41x | **1.14x** | 1.09x – 1.19x | 7m |
| Intel Core 7 250H | Core Series 2 | 1.80x | 2.06x | 1.46x | **1.16x** | 1.10x – 1.21x | 7m |
| Intel Core Ultra 5 225H | Core Series 2 | 1.66x | 2.06x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| Intel Core i7-13620H | Core 13th gen | 1.69x | 2.05x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| Intel Core i5-14450HX | Core 14th gen | 1.62x | 2.03x | 1.42x | **1.15x** | 1.09x – 1.19x | 7m |
| Intel Core i9-9980XE | Core 9th gen | 0.97x | 2.03x | 1.26x | **1.10x** | 1.06x – 1.12x | 5m |
| Intel Core i7-12800H | Core 12th gen | 1.49x | 2.03x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core i7-12800HE | Core 12th gen | 1.46x | 2.03x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core i7-12800HL | Core 12th gen | 1.49x | 2.03x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD Ryzen 7 7840H | Zen 4 | 1.64x | 2.02x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 7 7840HS | Zen 4 | 1.64x | 2.02x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 7 8840HS | Zen 4 | 1.64x | 2.02x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 7 8845HS | Zen 4 | 1.64x | 2.02x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 7 PRO 7840HS | Zen 4 | 1.64x | 2.02x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 7 PRO 8840HS | Source-listed (see product page) | 1.64x | 2.02x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 7 PRO 8845HS | Source-listed (see product page) | 1.64x | 2.02x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Apple M2 Pro (10-CPU 16-GPU) | M2 | 1.79x | 2.01x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Mac mini (2023) — Apple M2 Pro @ 3.5 GHz (10 CPU cores, 16 GPU cores) | M2 | 1.79x | 2.01x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| MacBook Pro (14-inch, 2023) — Apple M2 Pro @ 3.5 GHz (10 CPU cores, 16 GPU cores) | M2 | 1.79x | 2.01x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| Intel Core i5-12600K | Core 12th gen | 1.65x | 2.00x | 1.42x | **1.15x** | 1.09x – 1.19x | 7m |
| Intel Core i5-12600KF | Core 12th gen | 1.65x | 2.00x | 1.42x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 7 PRO 8700GE | Zen 4 | 1.78x | 2.00x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 5 7600 | Zen 4 | 1.79x | 1.99x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 5 PRO 7645 | Zen 4 | 1.79x | 1.99x | 1.45x | **1.15x** | 1.10x – 1.20x | 7m |
| AMD Ryzen 5 8400F | Zen 4 | 1.74x | 1.99x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| Intel Core i9-12900H | Core 12th gen | 1.62x | 1.98x | 1.41x | **1.14x** | 1.09x – 1.19x | 7m |
| Intel Core i9-12900HK | Core 12th gen | 1.62x | 1.98x | 1.41x | **1.14x** | 1.09x – 1.19x | 7m |
| Intel Core i5-13450HX | Core 13th gen | 1.56x | 1.98x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| Apple M3 (8-CPU 8-GPU) | M3 | 2.08x | 1.98x | 1.49x | **1.16x** | 1.10x – 1.22x | 8m |
| Apple M3 (8-CPU) | M3 | 2.08x | 1.98x | 1.49x | **1.16x** | 1.10x – 1.22x | 8m |
| MacBook Pro (14-inch, Nov 2023) — Apple M3 @ 4.1 GHz (8 CPU cores, 10 GPU cores) | M3 | 2.08x | 1.98x | 1.49x | **1.16x** | 1.10x – 1.22x | 8m |
| iMac (24-inch, 2023) — Apple M3 @ 4.1 GHz (8 CPU cores, 10 GPU cores) | M3 | 2.08x | 1.98x | 1.49x | **1.16x** | 1.10x – 1.22x | 8m |
| iMac (24-inch, 2023) — Apple M3 @ 4.1 GHz (8 CPU cores, 8 GPU cores) | M3 | 2.08x | 1.98x | 1.49x | **1.16x** | 1.10x – 1.22x | 8m |
| Intel Core i9-10980XE | Core 10th gen | 1.05x | 1.97x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 9 3950X | Zen 2 | 1.13x | 1.97x | 1.30x | **1.11x** | 1.07x – 1.14x | 5m |
| Intel Core i9-10940X | Core 10th gen | 1.04x | 1.96x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i7-1370PE | Core 13th gen | 1.62x | 1.96x | 1.41x | **1.14x** | 1.09x – 1.19x | 7m |
| AMD Ryzen AI Max PRO 380 | Zen 5 | 1.73x | 1.95x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 5 7500F | Zen 4 | 1.75x | 1.94x | 1.43x | **1.15x** | 1.09x – 1.20x | 7m |
| AMD Ryzen 7 5800X3D | Zen 3 | 1.40x | 1.94x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 7 8745HS | Zen 4 | 1.61x | 1.92x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD Ryzen AI 7 PRO 360 | Zen 5 | 1.81x | 1.92x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| AMD Ryzen Z2 Extreme | Zen (varies by model) | 1.81x | 1.92x | 1.44x | **1.15x** | 1.09x – 1.20x | 7m |
| AMD Ryzen 5 7500X3D | Zen 4 | 1.70x | 1.92x | 1.42x | **1.14x** | 1.09x – 1.19x | 7m |
| AMD Ryzen Threadripper PRO 3945WX | Zen 2 | 1.10x | 1.92x | 1.28x | **1.10x** | 1.07x – 1.13x | 5m |
| AMD Ryzen 5 8600G | Zen 4 | 1.78x | 1.91x | 1.43x | **1.15x** | 1.09x – 1.20x | 7m |
| AMD Ryzen 5 PRO 8600G | Source-listed (see product page) | 1.78x | 1.91x | 1.43x | **1.15x** | 1.09x – 1.20x | 7m |
| Intel Core i7-12700H | Core 12th gen | 1.52x | 1.90x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| Intel Core i7-12700HL | Core 12th gen | 1.52x | 1.90x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| Intel Core i7-12700E | Core 12th gen | 1.64x | 1.89x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core i7-12700T | Core 12th gen | 1.59x | 1.88x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core Ultra 9 185H | Core Series 1 | 1.68x | 1.88x | 1.41x | **1.14x** | 1.09x – 1.19x | 7m |
| AMD Ryzen 7 260 | Zen 4 | 1.63x | 1.87x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core Ultra 7 365 | Core Series 3 | 1.79x | 1.87x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Intel Core i9-11900KF | Core 11th gen | 1.57x | 1.86x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| Intel Core i7-12700TE | Core 12th gen | 1.57x | 1.85x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| AMD Ryzen 5 8500G | Zen 4 | 1.79x | 1.84x | 1.42x | **1.14x** | 1.09x – 1.19x | 7m |
| Intel Core Ultra 9 288V | Core Series 2 | 1.85x | 1.84x | 1.43x | **1.15x** | 1.09x – 1.19x | 7m |
| Intel Core i5-13500H | Core 13th gen | 1.57x | 1.84x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core i5-13505H | Core 13th gen | 1.57x | 1.84x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core Ultra 7 355 | Core Series 3 | 1.76x | 1.84x | 1.42x | **1.14x** | 1.09x – 1.19x | 7m |
| Intel Core i9-9960X | Core 9th gen | 0.97x | 1.84x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core i9-10920X | Core 10th gen | 1.04x | 1.83x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| AMD Ryzen 5 7400F | Zen 4 | 1.65x | 1.83x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD Ryzen 7 5800XT | Zen 3 | 1.45x | 1.82x | 1.35x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i5-13600T | Core 13th gen | 1.58x | 1.82x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core i5-12600H | Core 12th gen | 1.48x | 1.81x | 1.35x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i9-9940X | Core 9th gen | 0.97x | 1.80x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core i7-12650HX | Core 12th gen | 1.44x | 1.80x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i5-13490F | Core 13th gen | 1.61x | 1.79x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 7 5700X | Zen 3 | 1.41x | 1.79x | 1.33x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i7-11700K | Core 11th gen | 1.48x | 1.79x | 1.35x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i7-11700KF | Core 11th gen | 1.48x | 1.79x | 1.35x | **1.12x** | 1.08x – 1.16x | 6m |
| AMD Ryzen 7 7840U | Zen 4 | 1.63x | 1.79x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| AMD Ryzen 7 8840U | Zen 4 | 1.63x | 1.79x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| AMD Ryzen 7 PRO 7840U | Zen 4 | 1.63x | 1.79x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| AMD Ryzen 7 PRO 8840U | Source-listed (see product page) | 1.63x | 1.79x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| AMD Ryzen Z1 Extreme | Zen 4 | 1.63x | 1.79x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| AMD Ryzen Z2 | Zen (varies by model) | 1.63x | 1.79x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| AMD Ryzen 9 3900X | Zen 2 | 1.14x | 1.78x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 9 3900XT | Zen 2 | 1.15x | 1.78x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 7 5800X | Zen 3 | 1.43x | 1.77x | 1.33x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i9-11900KB | Core 11th gen | 1.49x | 1.77x | 1.35x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i9-10900KF | Core 10th gen | 1.24x | 1.77x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| Intel Core i5-1340P | Core 13th gen | 1.58x | 1.77x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core 7 240H | Core Series 2 | 1.57x | 1.76x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core i5-1350PE | Core 13th gen | 1.59x | 1.76x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 7 5700X3D | Zen 3 | 1.33x | 1.76x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| AMD Ryzen 5 7600X3D | Zen 4 | 1.71x | 1.76x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD Ryzen 9 PRO 3900 | Source-listed (see product page) | 1.12x | 1.75x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core Ultra 7 256V | Core Series 2 | 1.77x | 1.75x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core Ultra 7 258V | Core Series 2 | 1.77x | 1.75x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core i5-1340PE | Core 13th gen | 1.58x | 1.74x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen AI 5 PRO 440 | Zen 5 | 1.81x | 1.74x | 1.40x | **1.14x** | 1.09x – 1.19x | 7m |
| Apple M1 Pro (8-CPU) | M1 | 1.60x | 1.74x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| MacBook Pro (14-inch, 2021) — Apple M1 Pro @ 3.2 GHz (8 cores) | M1 | 1.60x | 1.74x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core i7-12650H | Core 12th gen | 1.44x | 1.74x | 1.33x | **1.12x** | 1.07x – 1.16x | 6m |
| Intel Core i5-12500 | Core 12th gen | 1.58x | 1.73x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 7 5800 | Zen 3 | 1.39x | 1.73x | 1.32x | **1.11x** | 1.07x – 1.15x | 6m |
| Intel Core i5-12600 | Core 12th gen | 1.59x | 1.73x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 5 7640HS | Zen 4 | 1.65x | 1.73x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 5 8645HS | Zen 4 | 1.65x | 1.73x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 5 PRO 7640HS | Zen 4 | 1.65x | 1.73x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 5 PRO 8645HS | Source-listed (see product page) | 1.65x | 1.73x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen AI 5 340 | Zen 5 | 1.82x | 1.72x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD Ryzen AI 5 PRO 340 | Zen 5 | 1.82x | 1.72x | 1.40x | **1.14x** | 1.09x – 1.18x | 7m |
| AMD Ryzen Threadripper 2990WX | Zen+ | 0.80x | 1.71x | 1.14x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core Ultra 5 236V | Core Series 2 | 1.76x | 1.71x | 1.39x | **1.14x** | 1.08x – 1.18x | 7m |
| Intel Core Ultra 5 238V | Core Series 2 | 1.76x | 1.71x | 1.39x | **1.14x** | 1.08x – 1.18x | 7m |
| AMD Ryzen 9 3900 | Zen 2 | 1.12x | 1.71x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core Ultra 5 125H | Core Series 1 | 1.50x | 1.71x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core Ultra 5 135H | Core Series 1 | 1.50x | 1.71x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| AMD Ryzen 7 5700 | Zen 3 | 1.39x | 1.70x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| Intel Core i9-9920X | Core 9th gen | 0.97x | 1.70x | 1.20x | **1.07x** | 1.05x – 1.10x | 4m |
| Intel Core 5 220H | Core Series 2 | 1.50x | 1.69x | 1.33x | **1.12x** | 1.07x – 1.16x | 6m |
| Intel Core i7-1360P | Core 13th gen | 1.64x | 1.69x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 7 6800H | Zen 3+ | 1.29x | 1.69x | 1.28x | **1.10x** | 1.07x – 1.14x | 5m |
| Intel Core i7-1370P | Core 13th gen | 1.69x | 1.68x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| Apple M2 (8-CPU 8-GPU) | M2 | 1.73x | 1.68x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Apple M2 (8-CPU) | M2 | 1.73x | 1.68x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Mac mini (2023) — Apple M2 @ 3.5 GHz (8 CPU cores, 10 GPU cores) | M2 | 1.73x | 1.68x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| MacBook Air (15-inch, 2023) — Apple M2 @ 3.5 GHz (8 CPU cores, 10 GPU cores) | M2 | 1.73x | 1.68x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| MacBook Air (2022) — Apple M2 @ 3.5 GHz (8 cores) | M2 | 1.73x | 1.68x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| MacBook Pro (13-inch, 2022) — Apple M2 @ 3.5 GHz (8 cores) | M2 | 1.73x | 1.68x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core Ultra 5 226V | Core Series 2 | 1.72x | 1.68x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core Ultra 5 228V | Core Series 2 | 1.72x | 1.68x | 1.38x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core i7-11700B | Core 11th gen | 1.51x | 1.68x | 1.33x | **1.12x** | 1.07x – 1.16x | 6m |
| Intel Core i9-11900 | Core 11th gen | 1.43x | 1.67x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| Intel Core i9-11900F | Core 11th gen | 1.43x | 1.67x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| Intel Core Ultra 7 266V | Core Series 2 | 1.82x | 1.67x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core Ultra 7 268V | Core Series 2 | 1.82x | 1.67x | 1.39x | **1.14x** | 1.09x – 1.18x | 7m |
| Intel Core 5 120F | Source-listed (see product page) | 1.57x | 1.66x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| AMD Ryzen 5 PRO 8500G | Source-listed (see product page) | 1.78x | 1.66x | 1.38x | **1.13x** | 1.08x – 1.18x | 7m |
| Intel Core i5-12500H | Core 12th gen | 1.49x | 1.66x | 1.33x | **1.12x** | 1.07x – 1.15x | 6m |
| AMD Ryzen 9 6900HX | Zen 3+ | 1.40x | 1.66x | 1.30x | **1.11x** | 1.07x – 1.15x | 6m |
| AMD Ryzen 5 PRO 8640HS | Source-listed (see product page) | 1.59x | 1.65x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i9-10850K | Core 10th gen | 1.15x | 1.65x | 1.24x | **1.09x** | 1.06x – 1.12x | 5m |
| AMD Ryzen 7 7735HS | Zen 3+ | 1.35x | 1.64x | 1.29x | **1.10x** | 1.07x – 1.14x | 5m |
| Intel Core i7-1280P | Core 12th gen | 1.45x | 1.64x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| Intel Core Ultra 5 335 | Core Series 3 | 1.66x | 1.64x | 1.35x | **1.12x** | 1.08x – 1.17x | 6m |
| AMD Ryzen AI 7 445 | Zen 5 | 1.72x | 1.63x | 1.36x | **1.13x** | 1.08x – 1.17x | 6m |
| AMD Ryzen 9 6900HS | Zen 3+ | 1.36x | 1.63x | 1.29x | **1.10x** | 1.07x – 1.14x | 5m |
| Intel Core i9-11980HK | Core 11th gen | 1.42x | 1.63x | 1.30x | **1.11x** | 1.07x – 1.15x | 5m |
| Intel Core i5-13420H | Core 13th gen | 1.55x | 1.63x | 1.33x | **1.12x** | 1.07x – 1.16x | 6m |
| AMD Ryzen 9 5900 | Zen 3 | 1.42x | 1.62x | 1.30x | **1.11x** | 1.07x – 1.15x | 5m |
| AMD Ryzen 5 PRO 8500GE | Source-listed (see product page) | 1.77x | 1.62x | 1.37x | **1.13x** | 1.08x – 1.17x | 6m |
| Intel Core i5-13400 | Core 13th gen | 1.58x | 1.62x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i5-13400F | Core 13th gen | 1.58x | 1.62x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| AMD Ryzen 7 7435HS | Zen 3+ | 1.31x | 1.61x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 7 PRO 6850H | Source-listed (see product page) | 1.11x | 1.61x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core Ultra 7 155U | Core Series 1 | 1.57x | 1.60x | 1.33x | **1.12x** | 1.07x – 1.16x | 6m |
| Intel Core i9-11950H | Core 11th gen | 1.42x | 1.59x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| Intel Core Ultra 5 325 | Core Series 3 | 1.69x | 1.58x | 1.35x | **1.12x** | 1.08x – 1.16x | 6m |
| AMD Ryzen 7 6800HS | Zen 3+ | 1.31x | 1.58x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i9-9900X | Core 9th gen | 0.97x | 1.58x | 1.17x | **1.07x** | 1.04x – 1.09x | 3m |
| AMD Ryzen 7 PRO 6850HS | Source-listed (see product page) | 1.31x | 1.57x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core 5 120 | Source-listed (see product page) | 1.59x | 1.57x | 1.33x | **1.12x** | 1.07x – 1.16x | 6m |
| Intel Core i7-11700 | Core 11th gen | 1.46x | 1.56x | 1.30x | **1.11x** | 1.07x – 1.14x | 5m |
| Intel Core i7-11700F | Core 11th gen | 1.46x | 1.56x | 1.30x | **1.11x** | 1.07x – 1.14x | 5m |
| Intel Core i9-9820X | Core 9th gen | 0.93x | 1.56x | 1.15x | **1.06x** | 1.04x – 1.08x | 3m |
| AMD Ryzen 5 5600GT | Zen 3 | 1.48x | 1.56x | 1.30x | **1.11x** | 1.07x – 1.14x | 5m |
| AMD Ryzen 5 5600X | Zen 3 | 1.41x | 1.55x | 1.28x | **1.10x** | 1.06x – 1.14x | 5m |
| AMD Ryzen Threadripper 2970WX | Zen+ | 0.80x | 1.54x | 1.10x | **1.04x** | 1.03x – 1.05x | 2m |
| Intel Core i5-12450HX | Core 12th gen | 1.47x | 1.54x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| Intel Core i7-11800H | Core 11th gen | 1.32x | 1.54x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 5 7640U | Zen 4 | 1.56x | 1.53x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| AMD Ryzen 5 8640U | Zen 4 | 1.56x | 1.53x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| AMD Ryzen 5 PRO 7640U | Zen 4 | 1.56x | 1.53x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| AMD Ryzen 5 PRO 8640U | Source-listed (see product page) | 1.56x | 1.53x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| AMD Ryzen 5 5600T | Zen 3 | 1.42x | 1.53x | 1.28x | **1.10x** | 1.06x – 1.14x | 5m |
| AMD Ryzen 5 PRO 8600GE | Zen 4 | 1.75x | 1.52x | 1.35x | **1.12x** | 1.08x – 1.16x | 6m |
| AMD Ryzen 5 5600X3D | Zen 3 | 1.39x | 1.52x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i9-10900K | Core 10th gen | 1.16x | 1.50x | 1.21x | **1.08x** | 1.05x – 1.10x | 4m |
| Intel Core i9-11900T | Core 11th gen | 1.37x | 1.50x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core Ultra 5 125U | Core Series 1 | 1.43x | 1.50x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i9-10900 | Core 10th gen | 1.11x | 1.50x | 1.19x | **1.07x** | 1.05x – 1.10x | 4m |
| Intel Core i9-10900F | Core 10th gen | 1.11x | 1.50x | 1.19x | **1.07x** | 1.05x – 1.10x | 4m |
| Intel Core i5-11600K | Core 11th gen | 1.43x | 1.49x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i5-11600KF | Core 11th gen | 1.43x | 1.49x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 7 5700G | Zen 3 | 1.32x | 1.49x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core Ultra 5 225T | Core Series 2 | 1.78x | 1.49x | 1.34x | **1.12x** | 1.08x – 1.16x | 6m |
| Intel Core i5-12500T | Core 12th gen | 1.55x | 1.49x | 1.30x | **1.11x** | 1.07x – 1.14x | 5m |
| AMD Ryzen AI 5 435 | Zen 5 | 1.69x | 1.48x | 1.32x | **1.12x** | 1.07x – 1.16x | 6m |
| Intel Core i5-12450H | Core 12th gen | 1.48x | 1.48x | 1.28x | **1.10x** | 1.06x – 1.14x | 5m |
| AMD Ryzen 9 5980HX | Zen 3 | 1.40x | 1.48x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i5-12400 | Core 12th gen | 1.45x | 1.47x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 5 5600 | Zen 3 | 1.39x | 1.47x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 7 PRO 5750G | Source-listed (see product page) | 1.29x | 1.47x | 1.24x | **1.09x** | 1.06x – 1.12x | 5m |
| AMD Ryzen Threadripper 2950X | Zen+ | 0.84x | 1.47x | 1.10x | **1.04x** | 1.02x – 1.05x | 2m |
| Intel Core i9-10900X | Core 10th gen | 0.96x | 1.45x | 1.14x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i3-14100 | Core 14th gen | 1.67x | 1.45x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| Intel Core i3-14100F | Core 14th gen | 1.67x | 1.45x | 1.31x | **1.11x** | 1.07x – 1.15x | 6m |
| AMD Ryzen Threadripper 1950X | Zen 1 | 0.80x | 1.45x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| AMD Ryzen 7 3700X | Zen 2 | 1.09x | 1.45x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| AMD Ryzen 9 PRO 6950H | Source-listed (see product page) | 1.17x | 1.45x | 1.20x | **1.08x** | 1.05x – 1.10x | 4m |
| Intel Core i5-12400F | Core 12th gen | 1.47x | 1.45x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core Ultra 7 164U | Core Series 1 | 1.44x | 1.44x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i7-10700K | Core 10th gen | 1.09x | 1.44x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| Intel Core i7-10700KF | Core 10th gen | 1.09x | 1.44x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| iMac (27-inch Retina Mid 2020) — Intel Core i7-10700K @ 3.8 GHz (8 cores) | Intel Mac | 1.09x | 1.44x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| Intel Core Ultra 5 134U | Core Series 1 | 1.40x | 1.44x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| Apple M1 (8-CPU 7-GPU) | M1 | 1.58x | 1.43x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| Apple M1 (8-CPU) | M1 | 1.58x | 1.43x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| Mac mini (Late 2020) — Apple M1 @ 3.2 GHz (8 cores) | M1 | 1.58x | 1.43x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| MacBook Air (Late 2020) — Apple M1 @ 3.2 GHz (8 CPU cores, 7 GPU cores) | M1 | 1.58x | 1.43x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| MacBook Air (Late 2020) — Apple M1 @ 3.2 GHz (8 CPU cores, 8 GPU cores) | M1 | 1.58x | 1.43x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| MacBook Pro (13-inch Late 2020) — Apple M1 @ 3.2 GHz (8 cores) | M1 | 1.58x | 1.43x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| iMac (24-inch Mid 2021) — Apple M1 @ 3.2 GHz (8 cores) | M1 | 1.58x | 1.43x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| Intel Core i7-11850H | Core 11th gen | 1.28x | 1.43x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| AMD Ryzen 5 5600F | Zen 3 | 1.21x | 1.43x | 1.21x | **1.08x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 5 5500GT | Zen 3 | 1.35x | 1.42x | 1.24x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core i9-9900KS | Core 9th gen | 1.10x | 1.42x | 1.17x | **1.07x** | 1.04x – 1.09x | 3m |
| Intel Core i9-11900H | Core 11th gen | 1.36x | 1.41x | 1.24x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core i9-10910 | Core 10th gen | 1.08x | 1.41x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| iMac (27-inch Retina Mid 2020) — Intel Core i9-10910 @ 3.6 GHz (10 cores) | Intel Mac | 1.08x | 1.41x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| Intel Core i5-1250P | Core 12th gen | 1.40x | 1.40x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| AMD Ryzen 5 5600XT | Zen 3 | 1.43x | 1.40x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core i5-11500B | Core 11th gen | 1.36x | 1.39x | 1.23x | **1.09x** | 1.05x – 1.12x | 4m |
| AMD Ryzen 9 PRO 5945 | Zen 3 | 1.41x | 1.39x | 1.24x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core Ultra 7 265U | Core Series 2 | 1.64x | 1.38x | 1.29x | **1.11x** | 1.07x – 1.14x | 5m |
| Intel Core i3-12300 | Core 12th gen | 1.49x | 1.38x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i5-1345U | Core 13th gen | 1.49x | 1.38x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 7 3800XT | Zen 2 | 1.18x | 1.37x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| AMD Ryzen 7 PRO 6850U | Source-listed (see product page) | 1.27x | 1.37x | 1.21x | **1.08x** | 1.05x – 1.10x | 4m |
| Intel Core i5-11500 | Core 11th gen | 1.36x | 1.37x | 1.23x | **1.09x** | 1.05x – 1.11x | 4m |
| AMD Ryzen 7 250 | Zen 4 | 1.63x | 1.37x | 1.28x | **1.10x** | 1.06x – 1.14x | 5m |
| AMD Ryzen 7 PRO 250 | Zen 4 | 1.63x | 1.37x | 1.28x | **1.10x** | 1.06x – 1.14x | 5m |
| Intel Core 5 210H | Core Series 2 | 1.56x | 1.37x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i9-9900K | Core 9th gen | 1.10x | 1.36x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core i9-9900KF | Core 9th gen | 1.10x | 1.36x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| iMac (27-inch Retina Early 2019) — Intel Core i9-9900K @ 3.6 GHz (8 cores) | Intel Mac | 1.10x | 1.36x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core Ultra 7 255U | Core Series 2 | 1.60x | 1.36x | 1.28x | **1.10x** | 1.06x – 1.14x | 5m |
| AMD Ryzen 5 PRO 6650H | Source-listed (see product page) | 1.26x | 1.36x | 1.20x | **1.08x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 5 PRO 6650HS | Source-listed (see product page) | 1.26x | 1.36x | 1.20x | **1.08x** | 1.05x – 1.10x | 4m |
| AMD Ryzen Threadripper 2920X | Zen+ | 0.82x | 1.36x | 1.07x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 88s |
| Intel Core i7-7820X | Core 7th gen | 1.01x | 1.35x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i5-1335U | Core 13th gen | 1.46x | 1.35x | 1.24x | **1.09x** | 1.06x – 1.12x | 5m |
| AMD Ryzen 5 6600H | Zen 3+ | 1.26x | 1.34x | 1.20x | **1.07x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 5 6600HS | Zen 3+ | 1.26x | 1.34x | 1.20x | **1.07x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 5 7535HS | Zen 3+ | 1.26x | 1.34x | 1.20x | **1.07x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 5 5500 | Zen 3 | 1.28x | 1.34x | 1.20x | **1.08x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 7 7735U | Zen 3+ | 1.25x | 1.34x | 1.19x | **1.07x** | 1.05x – 1.10x | 4m |
| Intel Core i5-11600 | Core 11th gen | 1.42x | 1.33x | 1.23x | **1.09x** | 1.05x – 1.12x | 4m |
| AMD Ryzen 7 7736U | Zen 3+ | 1.24x | 1.33x | 1.19x | **1.07x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 5 5600G | Zen 3 | 1.26x | 1.33x | 1.19x | **1.07x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 7 3800X | Zen 2 | 1.16x | 1.33x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| Intel Core i3-13100 | Core 13th gen | 1.51x | 1.32x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core i3-13100F | Core 13th gen | 1.51x | 1.32x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| Intel Core i7-10700 | Core 10th gen | 1.06x | 1.32x | 1.14x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i7-10700F | Core 10th gen | 1.06x | 1.32x | 1.14x | **1.05x** | 1.03x – 1.07x | 3m |
| AMD Ryzen 7 6800U | Zen 3+ | 1.24x | 1.32x | 1.19x | **1.07x** | 1.04x – 1.09x | 4m |
| Intel Core i5-11400 | Core 11th gen | 1.32x | 1.32x | 1.20x | **1.08x** | 1.05x – 1.10x | 4m |
| Intel Core i5-11400F | Core 11th gen | 1.32x | 1.32x | 1.20x | **1.08x** | 1.05x – 1.10x | 4m |
| Intel Core i7-8086K | Core 8th gen | 1.18x | 1.31x | 1.17x | **1.07x** | 1.04x – 1.09x | 3m |
| Intel Core Ultra 5 235U | Core Series 2 | 1.42x | 1.31x | 1.23x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core Ultra 5 225U | Core Series 2 | 1.32x | 1.31x | 1.20x | **1.08x** | 1.05x – 1.10x | 4m |
| AMD Ryzen 5 7540U | Zen 4 | 1.60x | 1.31x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 5 7545U | Zen 4 | 1.60x | 1.31x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 5 8540U | Zen 4 | 1.60x | 1.31x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 5 PRO 8540U | Source-listed (see product page) | 1.60x | 1.31x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 5 240 | Zen 4 | 1.59x | 1.30x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 7 5800H | Zen 3 | 1.18x | 1.30x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| Intel Core i7-1270P | Core 12th gen | 1.44x | 1.30x | 1.23x | **1.09x** | 1.05x – 1.11x | 4m |
| Intel Core 7 350 | Core Series 3 | 1.71x | 1.29x | 1.28x | **1.10x** | 1.06x – 1.14x | 5m |
| AMD Ryzen 5 PRO 5650G | Source-listed (see product page) | 1.25x | 1.29x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| Intel Core Ultra 5 332 | Core Series 3 | 1.66x | 1.29x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core i7-1260P | Core 12th gen | 1.43x | 1.28x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core i7-9800X | Core 9th gen | 0.92x | 1.28x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| Intel Core i7-5960X | Core 5th gen | 0.77x | 1.27x | 1.03x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 36s |
| Intel Core i9-9900 | Core 9th gen | 1.09x | 1.27x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i3-14100T | Core 14th gen | 1.61x | 1.27x | 1.25x | **1.09x** | 1.06x – 1.13x | 5m |
| Intel Core i5-1334U | Core 13th gen | 1.46x | 1.27x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core i7-1365U | Core 13th gen | 1.44x | 1.26x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core i5-1240P | Core 12th gen | 1.40x | 1.26x | 1.21x | **1.08x** | 1.05x – 1.11x | 4m |
| AMD Ryzen 3 PRO 8300G | Source-listed (see product page) | 1.68x | 1.26x | 1.27x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core 5 320 | Core Series 3 | 1.67x | 1.26x | 1.26x | **1.10x** | 1.06x – 1.13x | 5m |
| Intel Core 5 315 | Core Series 3 | 1.61x | 1.26x | 1.25x | **1.09x** | 1.06x – 1.12x | 5m |
| AMD Ryzen 9 5980HS | Zen 3 | 1.38x | 1.26x | 1.20x | **1.08x** | 1.05x – 1.10x | 4m |
| Intel Core i9-10980HK | Core 10th gen | 1.12x | 1.26x | 1.14x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i9-10900T | Core 10th gen | 1.14x | 1.25x | 1.14x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i7-6900K | Core 6th gen | 0.84x | 1.25x | 1.04x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 59s |
| Intel Core i3-12100 | Core 12th gen | 1.44x | 1.24x | 1.21x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core i3-12100F | Core 12th gen | 1.44x | 1.24x | 1.21x | **1.08x** | 1.05x – 1.11x | 4m |
| AMD Ryzen 5 6600U | Zen 3+ | 1.25x | 1.24x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| AMD Ryzen 5 7535U | Zen 3+ | 1.26x | 1.24x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| AMD Ryzen 5 PRO 6650U | Source-listed (see product page) | 1.25x | 1.24x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| Intel Core i7-6950X | Core 6th gen | 0.82x | 1.24x | 1.04x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 51s |
| Intel Core i5-13500T | Core 13th gen | 1.58x | 1.24x | 1.24x | **1.09x** | 1.06x – 1.12x | 5m |
| AMD Ryzen AI 5 430 | Zen 5 | 1.66x | 1.24x | 1.25x | **1.09x** | 1.06x – 1.13x | 5m |
| AMD Ryzen AI 5 330 | Zen 5 | 1.61x | 1.24x | 1.24x | **1.09x** | 1.06x – 1.12x | 5m |
| AMD Ryzen 9 4900H | Zen 2 | 1.11x | 1.23x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core 5 330 | Core Series 3 | 1.66x | 1.23x | 1.25x | **1.09x** | 1.06x – 1.13x | 5m |
| AMD Ryzen 9 5900H | Source-listed (see product page) | 1.36x | 1.23x | 1.19x | **1.07x** | 1.04x – 1.10x | 4m |
| Intel Core i7-9700K | Core 9th gen | 1.06x | 1.23x | 1.11x | **1.04x** | 1.03x – 1.06x | 2m |
| Intel Core i7-9700KF | Core 9th gen | 1.06x | 1.23x | 1.11x | **1.04x** | 1.03x – 1.06x | 2m |
| Intel Core i9-10885H | Core 10th gen | 1.12x | 1.22x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| AMD Ryzen 9 4900HS | Zen 2 | 1.06x | 1.21x | 1.11x | **1.04x** | 1.03x – 1.06x | 2m |
| AMD 4700S | Zen 2 | 0.84x | 1.21x | 1.03x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 47s |
| AMD Ryzen 7 PRO 5875U | Source-listed (see product page) | 1.25x | 1.21x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| AMD Ryzen 9 5900HX | Zen 3 | 1.33x | 1.21x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| AMD Ryzen 5 3600XT | Zen 2 | 1.17x | 1.21x | 1.14x | **1.05x** | 1.03x – 1.07x | 3m |
| AMD Ryzen 7 5800HS Creator Edition | Source-listed (see product page) | 1.19x | 1.21x | 1.14x | **1.06x** | 1.03x – 1.08x | 3m |
| AMD Ryzen 7 4800HS | Zen 2 | 1.04x | 1.21x | 1.10x | **1.04x** | 1.02x – 1.06x | 2m |
| AMD Ryzen 7 4800H | Zen 2 | 1.04x | 1.20x | 1.10x | **1.04x** | 1.02x – 1.05x | 2m |
| AMD Ryzen 5 220 | Zen 4 | 1.55x | 1.20x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| AMD Ryzen 5 230 | Zen 4 | 1.55x | 1.20x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| AMD Ryzen 5 PRO 220 | Zen 4 | 1.55x | 1.20x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| AMD Ryzen 5 PRO 230 | Zen 4 | 1.55x | 1.20x | 1.22x | **1.08x** | 1.05x – 1.11x | 4m |
| Intel Core i7-9700 | Core 9th gen | 1.05x | 1.20x | 1.10x | **1.04x** | 1.02x – 1.06x | 2m |
| Intel Core i7-9700F | Core 9th gen | 1.05x | 1.20x | 1.10x | **1.04x** | 1.02x – 1.06x | 2m |
| Intel Core i5-10600K | Core 10th gen | 1.05x | 1.20x | 1.10x | **1.04x** | 1.02x – 1.06x | 2m |
| Intel Core i5-10600KF | Core 10th gen | 1.05x | 1.20x | 1.10x | **1.04x** | 1.02x – 1.06x | 2m |
| AMD Ryzen 7 PRO 5850U | Source-listed (see product page) | 1.24x | 1.19x | 1.15x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core i7-1355U | Core 13th gen | 1.64x | 1.19x | 1.24x | **1.09x** | 1.05x – 1.12x | 5m |
| Intel Core i5-11260H | Core 11th gen | 1.28x | 1.19x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core i3-12300T | Core 12th gen | 1.41x | 1.18x | 1.19x | **1.07x** | 1.04x – 1.10x | 4m |
| AMD Ryzen 9 5900HS Creator Edition | Source-listed (see product page) | 1.33x | 1.17x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| Intel Core i3-12100E | Core 12th gen | 1.41x | 1.16x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| AMD Ryzen 7 5800U | Zen 3 | 1.23x | 1.16x | 1.14x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i7-10875H | Core 10th gen | 1.05x | 1.16x | 1.09x | **1.04x** | 1.02x – 1.05x | 2m |
| AMD Ryzen Threadripper 1920X | Zen 1 | 0.77x | 1.16x | 0.99x | **1.00x** (no meaningful gain) | 1.00x – 1.00x | -8s |
| Intel Core i9-9980HK | Core 9th gen | 0.99x | 1.16x | 1.07x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| MacBook Pro (15-inch Mid 2019) — Intel Core i9-9980HK @ 2.4 GHz (8 cores) | Intel Mac | 0.99x | 1.16x | 1.07x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| MacBook Pro (16-inch Late 2019) — Intel Core i9-9980HK @ 2.4 GHz (8 cores) | Intel Mac | 0.99x | 1.16x | 1.07x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| Intel Core i7-1255U | Core 12th gen | 1.42x | 1.15x | 1.18x | **1.07x** | 1.04x – 1.09x | 4m |
| Intel Core i7-7800X | Core 7th gen | 0.94x | 1.15x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 70s |
| AMD Ryzen 9 5900HS | Zen 3 | 1.34x | 1.15x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core i9-10880H | Core 10th gen | 1.08x | 1.15x | 1.09x | **1.04x** | 1.02x – 1.05x | 2m |
| AMD Ryzen 5 3600X | Zen 2 | 1.07x | 1.14x | 1.09x | **1.04x** | 1.02x – 1.05x | 2m |
| Intel Core i7-10870H | Core 10th gen | 1.04x | 1.14x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.05x | 2m |
| Intel Core i7-10700T | Core 10th gen | 1.02x | 1.14x | 1.07x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| Intel Core i7-9700E | Core 9th gen | 0.95x | 1.13x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 70s |
| AMD Ryzen 7 2700X | Zen+ | 0.86x | 1.13x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 29s |
| AMD Ryzen 5 3600 | Zen 2 | 1.03x | 1.13x | 1.07x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| Intel Core i3-1315U | Core 13th gen | 1.42x | 1.13x | 1.17x | **1.07x** | 1.04x – 1.09x | 3m |
| AMD Ryzen 7 5825U | Zen 3 | 1.24x | 1.13x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i5-10600 | Core 10th gen | 1.04x | 1.13x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| iMac (27-inch Retina Mid 2020) — Intel Core i5-10600 @ 3.3 GHz (6 cores) | Intel Mac | 1.04x | 1.13x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| AMD Ryzen 7 5800HS | Zen 3 | 1.18x | 1.12x | 1.11x | **1.05x** | 1.03x – 1.06x | 2m |
| Intel Core i7-8700K | Core 8th gen | 0.99x | 1.12x | 1.06x | **1.02x** (no meaningful gain) | 1.01x – 1.04x | 82s |
| Intel Core i7-10700TE | Core 10th gen | 1.01x | 1.12x | 1.07x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 89s |
| AMD Ryzen 7 PRO 4750GE | Source-listed (see product page) | 1.09x | 1.12x | 1.09x | **1.04x** | 1.02x – 1.05x | 2m |
| AMD Ryzen 5 PRO 5650GE | Source-listed (see product page) | 1.24x | 1.12x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| AMD Ryzen 7 7730U | Zen 3 | 1.24x | 1.12x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| AMD Ryzen 7 PRO 7730U | Zen 3 | 1.24x | 1.12x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i3-1220P | Core 12th gen | 1.40x | 1.11x | 1.16x | **1.06x** | 1.04x – 1.09x | 3m |
| AMD Ryzen 5 5600U | Zen 3 | 1.18x | 1.11x | 1.11x | **1.04x** | 1.03x – 1.06x | 2m |
| Intel Core i5-10505 | Core 10th gen | 1.03x | 1.10x | 1.07x | **1.03x** (no meaningful gain) | 1.01x – 1.04x | 88s |
| Intel Core i3-13100T | Core 13th gen | 1.42x | 1.10x | 1.17x | **1.06x** | 1.04x – 1.09x | 3m |
| AMD Ryzen 3 7440U | Zen 4 | 1.55x | 1.09x | 1.19x | **1.07x** | 1.04x – 1.10x | 4m |
| Intel Core i7-11700T | Core 11th gen | 1.42x | 1.09x | 1.16x | **1.06x** | 1.04x – 1.09x | 3m |
| AMD Ryzen 7 PRO 5750GE | Source-listed (see product page) | 1.27x | 1.09x | 1.13x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i3-12100T | Core 12th gen | 1.40x | 1.09x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core i5-10500 | Core 10th gen | 1.01x | 1.08x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 71s |
| iMac (27-inch Retina Mid 2020) — Intel Core i5-10500 @ 3.1 GHz (6 cores) | Intel Mac | 1.01x | 1.08x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 71s |
| Intel Core i7-11600H | Core 11th gen | 1.27x | 1.08x | 1.12x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i9-9880H | Core 9th gen | 0.95x | 1.08x | 1.03x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 46s |
| MacBook Pro (15-inch Mid 2019) — Intel Core i9-9880H @ 2.3 GHz (8 cores) | Intel Mac | 0.95x | 1.08x | 1.03x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 46s |
| MacBook Pro (16-inch Late 2019) — Intel Core i9-9880H @ 2.3 GHz (8 cores) | Intel Mac | 0.95x | 1.08x | 1.03x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 46s |
| Intel Core i5-11600T | Core 11th gen | 1.24x | 1.08x | 1.11x | **1.04x** | 1.03x – 1.06x | 2m |
| Intel Core i5-1235U | Core 12th gen | 1.39x | 1.08x | 1.15x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core i7-10850H | Core 10th gen | 1.05x | 1.07x | 1.06x | **1.03x** (no meaningful gain) | 1.01x – 1.04x | 83s |
| Intel Core i7-10750H | Core 10th gen | 1.04x | 1.07x | 1.06x | **1.02x** (no meaningful gain) | 1.01x – 1.04x | 81s |
| AMD Ryzen 5 3500X | Zen 2 | 1.10x | 1.07x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| AMD Ryzen 5 5600H | Zen 3 | 1.18x | 1.07x | 1.10x | **1.04x** | 1.02x – 1.05x | 2m |
| AMD Ryzen 3 PRO 8300GE | Source-listed (see product page) | 1.61x | 1.07x | 1.19x | **1.07x** | 1.04x – 1.10x | 4m |
| AMD Ryzen 7 4700GE | Zen 2 | 1.01x | 1.06x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 65s |
| Intel Core 5 220U | Core Series 2 | 1.24x | 1.06x | 1.11x | **1.04x** | 1.03x – 1.06x | 2m |
| Intel Core i5-11500H | Core 11th gen | 1.29x | 1.05x | 1.12x | **1.05x** | 1.03x – 1.07x | 3m |
| Intel Core i5-10400F | Core 10th gen | 0.95x | 1.05x | 1.03x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 39s |
| Intel Core i9-9900T | Core 9th gen | 0.96x | 1.05x | 1.03x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 42s |
| Intel Core i5-11500T | Core 11th gen | 1.21x | 1.05x | 1.10x | **1.04x** | 1.02x – 1.06x | 2m |
| Intel Core i7-1250U | Core 12th gen | 1.41x | 1.05x | 1.15x | **1.06x** | 1.03x – 1.08x | 3m |
| Intel Core i7-1260U | Core 12th gen | 1.41x | 1.05x | 1.15x | **1.06x** | 1.03x – 1.08x | 3m |
| Intel Core i5-10400 | Core 10th gen | 0.95x | 1.04x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 34s |
| AMD Ryzen 7 4800U | Zen 2 | 0.99x | 1.04x | 1.03x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 48s |
| Intel Core i5-9600K | Core 9th gen | 1.04x | 1.04x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 67s |
| Intel Core i5-9600KF | Core 9th gen | 1.04x | 1.04x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 67s |
| iMac (27-inch Retina Early 2019) — Intel Core i5-9600K @ 3.7 GHz (6 cores) | Intel Mac | 1.04x | 1.04x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 67s |
| Intel Core i5-11400H | Core 11th gen | 1.28x | 1.04x | 1.11x | **1.04x** | 1.03x – 1.06x | 2m |
| AMD Ryzen 7 5825C | Source-listed (see product page) | 1.23x | 1.04x | 1.10x | **1.04x** | 1.02x – 1.06x | 2m |
| Intel Core i7-1265UL | Core 12th gen | 1.44x | 1.04x | 1.15x | **1.06x** | 1.03x – 1.08x | 3m |
| Intel Core i7-6850K | Core 6th gen | 0.87x | 1.04x | 0.99x | **1.00x** (no meaningful gain) | 0.99x – 1.00x | -9s |
| AMD Ryzen 5 5600HS | Zen 3 | 1.18x | 1.03x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.05x | 2m |
| AMD Ryzen 7 4700 | Source-listed (see product page) | 0.99x | 1.03x | 1.03x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 42s |
| AMD Ryzen 7 4700G | Zen 2 | 0.99x | 1.03x | 1.03x | **1.01x** (no meaningful gain) | 1.01x – 1.02x | 42s |
| Intel Core i5-11400T | Core 11th gen | 1.18x | 1.03x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.05x | 2m |
| AMD Ryzen 3 210 | Zen 4 | 1.51x | 1.03x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| AMD Ryzen 3 PRO 210 | Zen 4 | 1.51x | 1.03x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core i5-10500E | Core 10th gen | 0.98x | 1.02x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 33s |
| Intel Core i5-10500H | Core 10th gen | 0.98x | 1.02x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 32s |
| AMD Ryzen 3 7335U | Zen 3+ | 1.23x | 1.01x | 1.09x | **1.04x** | 1.02x – 1.05x | 2m |
| AMD Ryzen Z2 Go | Zen (varies by model) | 1.23x | 1.01x | 1.09x | **1.04x** | 1.02x – 1.05x | 2m |
| Intel Core i7-5930K | Core 5th gen | 0.76x | 1.00x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -86s |
| Intel Core i7-8700 | Core 8th gen | 0.97x | 1.00x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.01x | 24s |
| Intel Core i7-8700B | Core 8th gen | 0.97x | 1.00x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.01x | 24s |
| Mac mini (Late 2018) — Intel Core i7-8700B @ 3.2 GHz (6 cores) | Intel Mac | 0.97x | 1.00x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.01x | 24s |
| iMac (21.5-inch Retina Early 2019) — Intel Core i7-8700 @ 3.2 GHz (6 cores) | Intel Mac | 0.97x | 1.00x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.01x | 24s |
| Intel Core i7-9850HE | Core 9th gen | 0.89x | 1.00x | 0.99x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -18s |
| Intel Core 3 304 | Core Series 3 | 1.56x | 0.99x | 1.16x | **1.06x** | 1.04x – 1.08x | 3m |
| Intel Core Ultra 5 115U | Core Series 1 | 1.07x | 0.99x | 1.04x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 60s |
| AMD Ryzen 7 5700U | Zen 2 | 1.08x | 0.99x | 1.04x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 61s |
| Intel Core i7-6800K | Core 6th gen | 0.84x | 0.99x | 0.97x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -41s |
| AMD Ryzen 3 3300X | Zen 2 | 1.10x | 0.99x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 68s |
| AMD Ryzen 7 1800X | Zen 1 | 0.78x | 0.99x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -81s |
| AMD Ryzen 7 2700 | Zen+ | 0.81x | 0.98x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -66s |
| AMD Ryzen 5 5625U | Zen 3 | 1.19x | 0.98x | 1.07x | **1.03x** (no meaningful gain) | 1.02x – 1.04x | 2m |
| Intel Core i5-8600K | Core 8th gen | 1.02x | 0.97x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 29s |
| Intel Core i7-9850H | Core 9th gen | 0.91x | 0.96x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -22s |
| AMD Ryzen 7 1700X | Zen 1 | 0.76x | 0.96x | 0.93x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -105s |
| Intel Core i7-9700T | Core 9th gen | 0.97x | 0.96x | 1.00x | **1.00x** (no meaningful gain) | 1.00x – 1.01x | 6s |
| AMD Ryzen 5 4600H | Zen 2 | 0.97x | 0.96x | 1.00x | **1.00x** (no meaningful gain) | 1.00x – 1.01x | 5s |
| Intel Core i7-5820K | Core 5th gen | 0.72x | 0.96x | 0.92x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -130s |
| AMD Ryzen Threadripper 1900X | Zen 1 | 0.76x | 0.95x | 0.93x | **0.97x** (no meaningful gain) | 0.96x – 0.97x | -114s |
| AMD Ryzen 5 5560U | Zen 3 | 1.13x | 0.95x | 1.04x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 57s |
| Intel Core i7-9750H | Core 9th gen | 0.90x | 0.95x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -36s |
| Intel Core i7-9750HF | Core 9th gen | 0.90x | 0.95x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -36s |
| MacBook Pro (15-inch Mid 2019) — Intel Core i7-9750H @ 2.6 GHz (6 cores) | Intel Mac | 0.90x | 0.95x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -36s |
| MacBook Pro (16-inch Late 2019) — Intel Core i7-9750H @ 2.6 GHz (6 cores) | Intel Mac | 0.90x | 0.95x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -36s |
| Intel Core i7-1195G7 | Core 11th gen | 1.38x | 0.95x | 1.10x | **1.04x** | 1.02x – 1.06x | 2m |
| AMD Ryzen 5 4600HS | Zen 2 | 0.97x | 0.95x | 1.00x | **1.00x** (no meaningful gain) | 1.00x – 1.00x | -5s |
| Intel Core i5-1155G7 | Core 11th gen | 1.17x | 0.94x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 70s |
| Intel Core i5-11320H | Core 11th gen | 1.27x | 0.94x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.05x | 2m |
| Intel Core i7-11390H | Core 11th gen | 1.30x | 0.94x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.05x | 2m |
| Intel Core i7-11375H | Core 11th gen | 1.30x | 0.94x | 1.08x | **1.03x** (no meaningful gain) | 1.02x – 1.05x | 2m |
| Intel Core i5-9600 | Core 9th gen | 0.99x | 0.93x | 1.00x | **1.00x** (no meaningful gain) | 1.00x – 1.00x | -2s |
| AMD Ryzen 5 2600X | Zen+ | 0.86x | 0.93x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -65s |
| Intel Core i7-8700T | Core 8th gen | 0.89x | 0.93x | 0.97x | **0.98x** (no meaningful gain) | 0.98x – 0.99x | -50s |
| Intel Core i9-8950HK | Core 8th gen | 0.96x | 0.93x | 0.99x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -17s |
| MacBook Pro (15-inch Mid 2018) — Intel Core i9-8950HK @ 2.9 GHz (6 cores) | Intel Mac | 0.96x | 0.93x | 0.99x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -17s |
| AMD Ryzen 5 7530U | Zen 3 | 1.26x | 0.92x | 1.07x | **1.03x** (no meaningful gain) | 1.01x – 1.04x | 88s |
| Intel Core i7-10710U | Core 10th gen | 1.00x | 0.92x | 1.00x | **1.00x** (no meaningful gain) | 1.00x – 1.00x | -4s |
| AMD Ryzen 5 3500 | Zen 2 | 1.08x | 0.92x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 27s |
| Intel Core i5-11300H | Core 11th gen | 1.26x | 0.92x | 1.06x | **1.03x** (no meaningful gain) | 1.01x – 1.04x | 87s |
| AMD Ryzen 7 1700 | Zen 1 | 0.74x | 0.91x | 0.91x | **0.96x** (no meaningful gain) | 0.95x – 0.97x | -144s |
| Intel Core i5-1145G7 | Core 11th gen | 1.17x | 0.91x | 1.04x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 54s |
| Intel Core i7-11370H | Core 11th gen | 1.28x | 0.91x | 1.07x | **1.03x** (no meaningful gain) | 1.01x – 1.04x | 89s |
| Intel Core i7-8850H | Core 8th gen | 0.95x | 0.91x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -34s |
| MacBook Pro (15-inch Mid 2018) — Intel Core i7-8850H @ 2.6 GHz (6 cores) | Intel Mac | 0.95x | 0.91x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -34s |
| Intel Core i7-1165G7 | Core 11th gen | 1.21x | 0.91x | 1.05x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 64s |
| Intel Core i5-9500 | Core 9th gen | 0.95x | 0.90x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -35s |
| Intel Core i5-9500F | Core 9th gen | 0.95x | 0.90x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -35s |
| Intel Core i5-8600 | Core 8th gen | 0.94x | 0.90x | 0.97x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -46s |
| iMac (27-inch Retina Early 2019) — Intel Core i5-8600 @ 3.1 GHz (6 cores) | Intel Mac | 0.94x | 0.90x | 0.97x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -46s |
| AMD Ryzen 5 2600 | Zen+ | 0.82x | 0.90x | 0.93x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -105s |
| Intel Core i5-1135G7 | Core 11th gen | 1.13x | 0.90x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 32s |
| AMD Ryzen 3 3100 | Zen 2 | 0.98x | 0.90x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -25s |
| Intel Core i7-1185G7 | Core 11th gen | 1.29x | 0.89x | 1.06x | **1.03x** (no meaningful gain) | 1.01x – 1.04x | 85s |
| Intel Core i7-8750H | Core 8th gen | 0.92x | 0.89x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -58s |
| MacBook Pro (15-inch Mid 2018) — Intel Core i7-8750H @ 2.2 GHz (6 cores) | Intel Mac | 0.92x | 0.89x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -58s |
| AMD Ryzen 3 PRO 4200G | Source-listed (see product page) | 1.02x | 0.89x | 0.99x | **1.00x** (no meaningful gain) | 0.99x – 1.00x | -13s |
| AMD Ryzen 3 PRO 4350G | Source-listed (see product page) | 1.01x | 0.88x | 0.99x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -20s |
| Intel Core i5-8500 | Core 8th gen | 0.91x | 0.88x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -67s |
| iMac (21.5-inch Retina Early 2019) — Intel Core i5-8500 @ 3.0 GHz (6 cores) | Intel Mac | 0.91x | 0.88x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -67s |
| iMac (27-inch Retina Early 2019) — Intel Core i5-8500 @ 3.0 GHz (6 cores) | Intel Mac | 0.91x | 0.88x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -67s |
| AMD Ryzen 3 4100 | Zen 2 | 1.01x | 0.88x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -22s |
| AMD Ryzen 3 4300G | Zen 2 | 1.01x | 0.88x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -23s |
| AMD Ryzen 3 4300GE | Zen 2 | 1.02x | 0.88x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -23s |
| Intel Core i3-10325 | Core 10th gen | 1.05x | 0.87x | 0.99x | **1.00x** (no meaningful gain) | 0.99x – 1.00x | -7s |
| AMD Ryzen 5 5500U | Zen 2 | 0.96x | 0.87x | 0.97x | **0.98x** (no meaningful gain) | 0.98x – 0.99x | -49s |
| AMD Ryzen 3 PRO 4350GE | Source-listed (see product page) | 1.01x | 0.87x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -28s |
| Intel Core i5-8500B | Core 8th gen | 0.91x | 0.87x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -74s |
| Intel Core i7-7740X | Core 7th gen | 1.00x | 0.87x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -33s |
| Mac mini (Late 2018) — Intel Core i5-8500B @ 3.0 GHz (6 cores) | Intel Mac | 0.91x | 0.87x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -74s |
| Intel Core i5-1140G7 | Core 11th gen | 1.13x | 0.87x | 1.01x | **1.00x** (no meaningful gain) | 1.00x – 1.01x | 18s |
| Intel Core i5-9400 | Core 9th gen | 0.90x | 0.86x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -86s |
| Intel Core i5-9400F | Core 9th gen | 0.90x | 0.86x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -86s |
| Intel Core i7-7700K | Core 7th gen | 0.97x | 0.86x | 0.97x | **0.98x** (no meaningful gain) | 0.98x – 0.99x | -50s |
| iMac (27-inch Retina Mid 2017) — Intel Core i7-7700K @ 4.2 GHz (4 cores) | Intel Mac | 0.97x | 0.86x | 0.97x | **0.98x** (no meaningful gain) | 0.98x – 0.99x | -50s |
| AMD Ryzen 5 1600 | Zen 1 | 0.73x | 0.85x | 0.88x | **0.95x** (no meaningful gain) | 0.94x – 0.96x | -190s |
| Intel Core i7-1068G7 | Core 10th gen | 1.05x | 0.85x | 0.99x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -19s |
| Intel Core i7-1068NG7 | Core 10th gen | 1.05x | 0.85x | 0.99x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -19s |
| MacBook Pro (13-inch Mid 2020) — Intel Core i7-1068NG7 @ 2.3 GHz (4 cores) | Intel Mac | 1.05x | 0.85x | 0.99x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -19s |
| Intel Core i3-10320 | Core 10th gen | 1.03x | 0.85x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -29s |
| Intel Core i5-10600T | Core 10th gen | 0.90x | 0.85x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -88s |
| AMD Ryzen 5 1600X | Zen 1 | 0.78x | 0.85x | 0.90x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -163s |
| AMD Ryzen 5 5625C | Source-listed (see product page) | 1.19x | 0.85x | 1.02x | **1.01x** (no meaningful gain) | 1.00x – 1.02x | 29s |
| AMD Ryzen 5 5500H | Zen 3 | 1.09x | 0.85x | 0.99x | **1.00x** (no meaningful gain) | 0.99x – 1.00x | -9s |
| AMD Ryzen 5 4600U | Zen 2 | 0.94x | 0.84x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -76s |
| Intel Core i5-1130G7 | Core 11th gen | 1.10x | 0.84x | 0.99x | **1.00x** (no meaningful gain) | 0.99x – 1.00x | -8s |
| Intel Core i3-10300 | Core 10th gen | 0.98x | 0.84x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -59s |
| Intel Core i5-1145GRE | Core 11th gen | 1.10x | 0.83x | 0.99x | **1.00x** (no meaningful gain) | 0.99x – 1.00x | -14s |
| AMD Ryzen 3 5300G | Zen 3 | 1.16x | 0.83x | 1.00x | **1.00x** (no meaningful gain) | 1.00x – 1.01x | 6s |
| AMD Ryzen 3 PRO 5350G | Source-listed (see product page) | 1.16x | 0.83x | 1.00x | **1.00x** (no meaningful gain) | 1.00x – 1.01x | 6s |
| Intel Core i7-1160G7 | Core 11th gen | 1.17x | 0.82x | 1.01x | **1.00x** (no meaningful gain) | 1.00x – 1.01x | 10s |
| Intel Core i3-10105 | Core 10th gen | 0.98x | 0.82x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -73s |
| Intel Core i3-10105F | Core 10th gen | 0.98x | 0.82x | 0.95x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -73s |
| AMD Ryzen 5 4500 | Zen 2 | 1.02x | 0.81x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.99x | -56s |
| Intel Core i7-9700TE | Core 9th gen | 0.85x | 0.81x | 0.91x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -138s |
| AMD Ryzen 5 4600G | Zen 2 | 1.04x | 0.81x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.99x | -51s |
| Intel Core i7-8569U | Core 8th gen | 0.95x | 0.80x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -93s |
| MacBook Pro (13-inch Mid 2019) — Intel Core i7-8569U @ 2.8 GHz (4 cores) | Intel Mac | 0.95x | 0.80x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -93s |
| Intel Core i5-8400 | Core 8th gen | 0.88x | 0.80x | 0.92x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -132s |
| AMD Ryzen 3 5425U | Zen 3 | 1.11x | 0.80x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -29s |
| Intel Core i5-10500T | Core 10th gen | 0.87x | 0.80x | 0.91x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -139s |
| Intel Core i3-1125G4 | Core 11th gen | 1.04x | 0.80x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.98x | -60s |
| Intel Core i3-10100 | Core 10th gen | 0.96x | 0.80x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -94s |
| Intel Core i3-10100F | Core 10th gen | 0.96x | 0.80x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -94s |
| Intel Core i7-8809G | Core 8th gen | 0.94x | 0.79x | 0.93x | **0.97x** (no meaningful gain) | 0.97x – 0.97x | -110s |
| Intel Core i5-10400H | Core 10th gen | 0.99x | 0.79x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -86s |
| Intel Core i5-1145G7E | Core 11th gen | 1.10x | 0.79x | 0.97x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -39s |
| AMD Ryzen 3 5300GE | Zen 3 | 1.13x | 0.78x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -29s |
| AMD Ryzen 3 PRO 5350GE | Source-listed (see product page) | 1.13x | 0.78x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 1.00x | -29s |
| Intel Core i5-10400T | Core 10th gen | 0.85x | 0.78x | 0.90x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -166s |
| Intel Core i7-8559U | Core 8th gen | 0.93x | 0.78x | 0.92x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -123s |
| MacBook Pro (13-inch Mid 2018) — Intel Core i7-8559U @ 2.7 GHz (4 cores) | Intel Mac | 0.93x | 0.78x | 0.92x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -123s |
| Intel Core i7-4790K | Core 4th gen | 0.93x | 0.78x | 0.92x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -125s |
| Intel Core i7-6700K | Core 6th gen | 0.90x | 0.78x | 0.91x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -140s |
| iMac (27-inch Retina Late 2015) — Intel Core i7-6700K @ 4.0 GHz (4 cores) | Intel Mac | 0.90x | 0.78x | 0.91x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -140s |
| AMD Ryzen 7 4700U | Zen 2 | 0.96x | 0.77x | 0.93x | **0.97x** (no meaningful gain) | 0.97x – 0.97x | -110s |
| Intel Core i5-10300H | Core 10th gen | 0.98x | 0.77x | 0.93x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -102s |
| Intel Core i7-1265U | Core 12th gen | 1.44x | 0.77x | 1.04x | **1.02x** (no meaningful gain) | 1.01x – 1.03x | 61s |
| AMD Ryzen 5 4500U | Zen 2 | 0.94x | 0.77x | 0.92x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -124s |
| Intel Core i7-1180G7 | Core 11th gen | 1.23x | 0.77x | 1.00x | **1.00x** (no meaningful gain) | 0.99x – 1.01x | -4s |
| AMD Ryzen 5 7520U | Zen 2 | 0.93x | 0.76x | 0.91x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -133s |
| Intel Core i5-9600T | Core 9th gen | 0.84x | 0.76x | 0.89x | **0.95x** (no meaningful gain) | 0.94x – 0.96x | -184s |
| Intel Core i3-10305T | Core 10th gen | 0.93x | 0.76x | 0.91x | **0.96x** (no meaningful gain) | 0.96x – 0.97x | -140s |
| Intel Core i3-10105T | Core 10th gen | 0.91x | 0.75x | 0.90x | **0.96x** (no meaningful gain) | 0.95x – 0.97x | -153s |
| Intel Core i3-10300T | Core 10th gen | 0.91x | 0.75x | 0.90x | **0.96x** (no meaningful gain) | 0.95x – 0.97x | -153s |
| Intel Core i5-8600T | Core 8th gen | 0.82x | 0.74x | 0.87x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -212s |
| Intel Core i5-1038NG7 | Core 10th gen | 0.89x | 0.74x | 0.89x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -174s |
| MacBook Pro (13-inch Mid 2020) — Intel Core i5-1038NG7 @ 2.0 GHz (4 cores) | Intel Mac | 0.89x | 0.74x | 0.89x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -174s |
| Intel Core i5-9500T | Core 9th gen | 0.79x | 0.74x | 0.86x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -233s |
| Intel Core i7-8709G | Core 8th gen | 0.91x | 0.74x | 0.90x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -161s |
| Intel Core i7-1065G7 | Core 10th gen | 1.04x | 0.73x | 0.94x | **0.97x** (no meaningful gain) | 0.97x – 0.98x | -99s |
| Intel Core i5-8269U | Core 8th gen | 0.85x | 0.73x | 0.88x | **0.94x** (no meaningful gain) | 0.94x – 0.96x | -197s |
| Intel Core 3 N355 | Core Series 2 | 0.82x | 0.73x | 0.86x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -221s |
| Intel Core i7-5775R | Core 5th gen | 0.84x | 0.73x | 0.87x | **0.94x** (no meaningful gain) | 0.94x – 0.96x | -206s |
| Intel Core i5-9500TE | Core 9th gen | 0.78x | 0.73x | 0.85x | **0.93x** (no meaningful gain) | 0.92x – 0.95x | -245s |
| Intel Core i5-8279U | Core 8th gen | 0.84x | 0.73x | 0.87x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -211s |
| Intel Core i7-8557U | Core 8th gen | 0.91x | 0.73x | 0.89x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -170s |
| MacBook Pro (13-inch Mid 2019) — Intel Core i5-8279U @ 2.4 GHz (4 cores) | Intel Mac | 0.84x | 0.73x | 0.87x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -211s |
| MacBook Pro (13-inch Mid 2019) — Intel Core i7-8557U @ 1.7 GHz (4 cores) | Intel Mac | 0.91x | 0.73x | 0.89x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -170s |
| Intel Core i5-10200H | Core 10th gen | 0.93x | 0.73x | 0.90x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -162s |
| Intel Core i7-8705G | Core 8th gen | 0.91x | 0.73x | 0.89x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -174s |
| Intel Core i7-8706G | Core 8th gen | 0.91x | 0.73x | 0.89x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -174s |
| Intel Core i3-8350K | Core 8th gen | 0.95x | 0.72x | 0.90x | **0.96x** (no meaningful gain) | 0.95x – 0.97x | -154s |
| Intel Core i5-8259U | Core 8th gen | 0.78x | 0.72x | 0.85x | **0.93x** (no meaningful gain) | 0.92x – 0.95x | -258s |
| MacBook Pro (13-inch Mid 2018) — Intel Core i5-8259U @ 2.3 GHz (4 cores) | Intel Mac | 0.78x | 0.72x | 0.85x | **0.93x** (no meaningful gain) | 0.92x – 0.95x | -258s |
| Intel Core i7-5775C | Core 5th gen | 0.82x | 0.72x | 0.86x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -231s |
| Intel Core i7-4940MX | Core 4th gen | 0.73x | 0.72x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -298s |
| Intel Core i7-7700 | Core 7th gen | 0.85x | 0.71x | 0.87x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -217s |
| iMac (21.5-inch Retina Mid 2017) — Intel Core i7-7700 @ 3.6 GHz (4 cores) | Intel Mac | 0.85x | 0.71x | 0.87x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -217s |
| Intel Core i5-7600K | Core 7th gen | 0.95x | 0.71x | 0.90x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -162s |
| iMac (27-inch Retina Mid 2017) — Intel Core i5-7600K @ 3.8 GHz (4 cores) | Intel Mac | 0.95x | 0.71x | 0.90x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -162s |
| Intel Core i7-1185G7E | Core 11th gen | 1.25x | 0.71x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -36s |
| Intel Core i7-1185GRE | Core 11th gen | 1.25x | 0.71x | 0.98x | **0.99x** (no meaningful gain) | 0.99x – 0.99x | -36s |
| Intel Core i3-10100T | Core 10th gen | 0.89x | 0.71x | 0.88x | **0.94x** (no meaningful gain) | 0.94x – 0.96x | -198s |
| Intel Core i5-9400T | Core 9th gen | 0.76x | 0.71x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -283s |
| Intel Core i5-8257U | Core 8th gen | 0.81x | 0.71x | 0.85x | **0.93x** (no meaningful gain) | 0.92x – 0.95x | -249s |
| MacBook Pro (13-inch Mid 2019) — Intel Core i5-8257U @ 1.4 GHz (4 cores) | Intel Mac | 0.81x | 0.71x | 0.85x | **0.93x** (no meaningful gain) | 0.92x – 0.95x | -249s |
| MacBook Pro (13-inch Mid 2020) — Intel Core i5-8257U @ 1.4 GHz (4 cores) | Intel Mac | 0.81x | 0.71x | 0.85x | **0.93x** (no meaningful gain) | 0.92x – 0.95x | -249s |
| Intel Core i5-9400H | Core 9th gen | 0.89x | 0.70x | 0.88x | **0.94x** (no meaningful gain) | 0.94x – 0.96x | -198s |
| Intel Core i7-4930MX | Core 4th gen | 0.72x | 0.70x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -317s |
| AMD Ryzen 3 PRO 4450U | Source-listed (see product page) | 0.90x | 0.70x | 0.88x | **0.94x** (no meaningful gain) | 0.94x – 0.96x | -203s |
| Intel Core i7-10810U | Core 10th gen | 1.01x | 0.69x | 0.91x | **0.96x** (no meaningful gain) | 0.95x – 0.97x | -148s |
| Intel Core i3-1215U | Core 12th gen | 1.39x | 0.69x | 1.00x | **1.00x** (no meaningful gain) | 0.99x – 1.01x | -6s |
| Intel Core i7-7920HQ | Core 7th gen | 0.85x | 0.69x | 0.85x | **0.93x** (no meaningful gain) | 0.93x – 0.95x | -240s |
| MacBook Pro (15-inch Mid 2017) — Intel Core i7-7920HQ @ 3.1 GHz (4 cores) | Intel Mac | 0.85x | 0.69x | 0.85x | **0.93x** (no meaningful gain) | 0.93x – 0.95x | -240s |
| Intel Core i7-4790 | Core 4th gen | 0.81x | 0.68x | 0.84x | **0.93x** (no meaningful gain) | 0.92x – 0.94x | -270s |
| AMD Ryzen 3 7320U | Zen 2 | 0.88x | 0.68x | 0.86x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -225s |
| Intel Core i3-9300T | Core 9th gen | 0.92x | 0.68x | 0.88x | **0.94x** (no meaningful gain) | 0.94x – 0.96x | -202s |
| AMD Ryzen 5 1500X | Zen 1 | 0.81x | 0.68x | 0.84x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -277s |
| Intel Core i3-1305U | Core 13th gen | 1.42x | 0.67x | 0.99x | **1.00x** (no meaningful gain) | 0.99x – 1.00x | -10s |
| Intel Core i7-4930K | Core 4th gen | 0.50x | 0.67x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -584s |
| Intel Core i7-6700 | Core 6th gen | 0.86x | 0.67x | 0.85x | **0.93x** (no meaningful gain) | 0.92x – 0.95x | -249s |
| Intel Core i5-6600K | Core 6th gen | 0.91x | 0.66x | 0.86x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -225s |
| Intel Core i5-7640X | Core 7th gen | 0.94x | 0.66x | 0.87x | **0.94x** (no meaningful gain) | 0.94x – 0.95x | -206s |
| Intel Core i5-8500T | Core 8th gen | 0.78x | 0.66x | 0.82x | **0.92x** (no meaningful gain) | 0.90x – 0.94x | -310s |
| Intel Core i7-4910MQ | Core 4th gen | 0.72x | 0.66x | 0.80x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -355s |
| Intel Core 3 N350 | Core Series 2 | 0.82x | 0.66x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -286s |
| Intel Core i7-7820HK | Core 7th gen | 0.84x | 0.66x | 0.84x | **0.93x** (no meaningful gain) | 0.92x – 0.94x | -268s |
| Intel Core i7-4770K | Core 4th gen | 0.78x | 0.66x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -315s |
| Intel Core i3-9300 | Core 9th gen | 0.94x | 0.66x | 0.87x | **0.94x** (no meaningful gain) | 0.94x – 0.95x | -209s |
| Intel Core i7-4771 | Core 4th gen | 0.76x | 0.65x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -334s |
| iMac (27-inch Late 2013) — Intel Core i7-4771 @ 3.5 GHz (4 cores) | Intel Mac | 0.76x | 0.65x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -334s |
| Intel Core i7-6700HQ | Core 6th gen | 0.75x | 0.65x | 0.81x | **0.91x** (no meaningful gain) | 0.89x – 0.93x | -343s |
| MacBook Pro (15-inch Late 2016) — Intel Core i7-6700HQ @ 2.6 GHz (4 cores) | Intel Mac | 0.75x | 0.65x | 0.81x | **0.91x** (no meaningful gain) | 0.89x – 0.93x | -343s |
| Intel Core i7-6920HQ | Core 6th gen | 0.78x | 0.65x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -323s |
| MacBook Pro (15-inch Late 2016) — Intel Core i7-6920HQ @ 2.9 GHz (4 cores) | Intel Mac | 0.78x | 0.65x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -323s |
| Intel Core i7-10510U | Core 10th gen | 0.87x | 0.65x | 0.84x | **0.93x** (no meaningful gain) | 0.92x – 0.94x | -264s |
| Intel Core i3-8300 | Core 8th gen | 0.86x | 0.65x | 0.84x | **0.93x** (no meaningful gain) | 0.92x – 0.94x | -269s |
| Intel Core i5-9300H | Core 9th gen | 0.86x | 0.64x | 0.84x | **0.93x** (no meaningful gain) | 0.92x – 0.94x | -272s |
| Intel Core i5-9300HF | Core 9th gen | 0.86x | 0.64x | 0.84x | **0.93x** (no meaningful gain) | 0.92x – 0.94x | -272s |
| Intel Core i5-4690K | Core 4th gen | 0.92x | 0.64x | 0.86x | **0.93x** (no meaningful gain) | 0.93x – 0.95x | -234s |
| Intel Core i5-8305G | Core 8th gen | 0.83x | 0.64x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -292s |
| Intel Core i7-4980HQ | Core 4th gen | 0.74x | 0.64x | 0.80x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -362s |
| MacBook Pro (15-inch Retina Mid 2014) — Intel Core i7-4980HQ @ 2.8 GHz (4 cores) | Intel Mac | 0.74x | 0.64x | 0.80x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -362s |
| MacBook Pro (15-inch Retina Mid 2015) — Intel Core i7-4980HQ @ 2.8 GHz (4 cores) | Intel Mac | 0.74x | 0.64x | 0.80x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -362s |
| Intel Core i5-1035G7 | Core 10th gen | 0.85x | 0.64x | 0.84x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -278s |
| Intel Core i7-4900MQ | Core 4th gen | 0.71x | 0.64x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -387s |
| Intel Core i7-4960HQ | Core 4th gen | 0.72x | 0.64x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.93x | -378s |
| MacBook Pro (15-inch Retina Late 2013) — Intel Core i7-4960HQ @ 2.6 GHz (4 cores) | Intel Mac | 0.72x | 0.64x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.93x | -378s |
| Intel Core i5-8400H | Core 8th gen | 0.86x | 0.64x | 0.84x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -275s |
| Intel Core i3-9100 | Core 9th gen | 0.93x | 0.64x | 0.86x | **0.93x** (no meaningful gain) | 0.93x – 0.95x | -236s |
| Intel Core i3-9100F | Core 9th gen | 0.93x | 0.64x | 0.86x | **0.93x** (no meaningful gain) | 0.93x – 0.95x | -236s |
| Intel Core i5-8400T | Core 8th gen | 0.73x | 0.64x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.93x | -375s |
| Intel Core i5-5675C | Core 5th gen | 0.78x | 0.63x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -334s |
| Intel Core i7-4870HQ | Core 4th gen | 0.70x | 0.63x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -404s |
| MacBook Pro (15-inch Retina Mid 2014) — Intel Core i7-4870HQ @ 2.5 GHz (4 cores) | Intel Mac | 0.70x | 0.63x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -404s |
| MacBook Pro (15-inch Retina Mid 2015) — Intel Core i7-4870HQ @ 2.5 GHz (4 cores) | Intel Mac | 0.70x | 0.63x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -404s |
| AMD Ryzen 5 3400G | Zen+ | 0.78x | 0.63x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -339s |
| Intel Core i3-8100B | Core 8th gen | 0.84x | 0.63x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -296s |
| Mac mini (Late 2018) — Intel Core i3-8100B @ 3.6 GHz (4 cores) | Intel Mac | 0.84x | 0.63x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -296s |
| Intel Core i7-7820HQ | Core 7th gen | 0.81x | 0.63x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -320s |
| MacBook Pro (15-inch Mid 2017) — Intel Core i7-7820HQ @ 2.9 GHz (4 cores) | Intel Mac | 0.81x | 0.63x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -320s |
| Intel Core i5-8300H | Core 8th gen | 0.84x | 0.63x | 0.82x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -302s |
| Intel Core i3-1210U | Core 12th gen | 1.36x | 0.63x | 0.96x | **0.98x** (no meaningful gain) | 0.98x – 0.99x | -61s |
| Intel Core i7-10610U | Core 10th gen | 0.96x | 0.63x | 0.86x | **0.94x** (no meaningful gain) | 0.93x – 0.95x | -228s |
| Intel Core i5-8350U | Core 8th gen | 0.80x | 0.63x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -330s |
| Intel Core i5-1035G4 | Core 10th gen | 0.85x | 0.63x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -292s |
| AMD Ryzen Embedded V1807B | Zen 1 | 0.72x | 0.62x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -394s |
| Intel Core i7-7820EQ | Core 7th gen | 0.77x | 0.62x | 0.80x | **0.91x** (no meaningful gain) | 0.89x – 0.93x | -352s |
| Intel Core i7-4770 | Core 4th gen | 0.73x | 0.62x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -383s |
| Intel Core i7-8665U | Core 8th gen | 0.96x | 0.62x | 0.86x | **0.93x** (no meaningful gain) | 0.93x – 0.95x | -235s |
| Intel Core i5-10310U | Core 10th gen | 0.82x | 0.62x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -322s |
| Intel Core i5-7600 | Core 7th gen | 0.87x | 0.62x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -288s |
| iMac (27-inch Retina Mid 2017) — Intel Core i5-7600 @ 3.5 GHz (4 cores) | Intel Mac | 0.87x | 0.62x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -288s |
| AMD Ryzen 3 PRO 5475U | Source-listed (see product page) | 1.10x | 0.62x | 0.90x | **0.95x** (no meaningful gain) | 0.95x – 0.96x | -167s |
| Intel Core i3-10100TE | Core 10th gen | 0.86x | 0.62x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -299s |
| Intel Core i7-4790S | Core 4th gen | 0.80x | 0.62x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -335s |
| Intel Core i7-4860HQ | Core 4th gen | 0.68x | 0.62x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -436s |
| Intel Core i7-4770S | Core 4th gen | 0.73x | 0.62x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -390s |
| Intel Core i7-7700HQ | Core 7th gen | 0.79x | 0.61x | 0.80x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -353s |
| MacBook Pro (15-inch Mid 2017) — Intel Core i7-7700HQ @ 2.8 GHz (4 cores) | Intel Mac | 0.79x | 0.61x | 0.80x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -353s |
| Intel Core i5-7500 | Core 7th gen | 0.84x | 0.61x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -315s |
| Intel Core i7-5950HQ | Core 5th gen | 0.79x | 0.61x | 0.80x | **0.91x** (no meaningful gain) | 0.89x – 0.93x | -353s |
| iMac (21.5-inch Retina Mid 2017) — Intel Core i5-7500 @ 3.4 GHz (4 cores) | Intel Mac | 0.84x | 0.61x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -315s |
| iMac (27-inch Retina Mid 2017) — Intel Core i5-7500 @ 3.4 GHz (4 cores) | Intel Mac | 0.84x | 0.61x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -315s |
| Intel Core i7-6820HQ | Core 6th gen | 0.73x | 0.61x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -398s |
| Intel Core i7-6870HQ | Core 6th gen | 0.73x | 0.61x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -398s |
| MacBook Pro (15-inch Late 2016) — Intel Core i7-6820HQ @ 2.7 GHz (4 cores) | Intel Mac | 0.73x | 0.61x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -398s |
| Intel Core i7-4770HQ | Core 4th gen | 0.68x | 0.61x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -448s |
| MacBook Pro (15-inch Retina Mid 2014) — Intel Core i7-4770HQ @ 2.2 GHz (4 cores) | Intel Mac | 0.68x | 0.61x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -448s |
| MacBook Pro (15-inch Retina Mid 2015) — Intel Core i7-4770HQ @ 2.2 GHz (4 cores) | Intel Mac | 0.68x | 0.61x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -448s |
| Intel Core i7-8565U | Core 8th gen | 0.92x | 0.61x | 0.84x | **0.93x** (no meaningful gain) | 0.92x – 0.94x | -270s |
| Intel Core i5-8260U | Core 8th gen | 0.86x | 0.61x | 0.82x | **0.92x** (no meaningful gain) | 0.90x – 0.94x | -308s |
| Intel Core i5-6600 | Core 6th gen | 0.85x | 0.61x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -313s |
| Intel Core i7-4850HQ | Core 4th gen | 0.67x | 0.61x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -456s |
| MacBook Pro (15-inch Retina Late 2013) — Intel Core i7-4850HQ @ 2.3 GHz (4 cores) | Intel Mac | 0.67x | 0.61x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -456s |
| iMac (27-inch Retina Late 2015) — Intel Core i5-6600 @ 3.3 GHz (4 cores) | Intel Mac | 0.85x | 0.61x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -313s |
| Intel Core i7-4950HQ | Core 4th gen | 0.68x | 0.61x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -449s |
| Intel Core i7-4722HQ | Core 4th gen | 0.67x | 0.61x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -458s |
| Intel Core i5-5675R | Core 5th gen | 0.77x | 0.60x | 0.79x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -374s |
| iMac (21.5-inch Retina Late 2015) — Intel Core i5-5675R @ 3.1 GHz (4 cores) | Intel Mac | 0.77x | 0.60x | 0.79x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -374s |
| Intel Core i3-8100 | Core 8th gen | 0.84x | 0.60x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -323s |
| iMac (21.5-inch Retina Early 2019) — Intel Core i3-8100 @ 3.6 GHz (4 cores) | Intel Mac | 0.84x | 0.60x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -323s |
| Intel Core i7-4720HQ | Core 4th gen | 0.70x | 0.60x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -441s |
| AMD Ryzen 3 5400U | Zen 3 | 1.09x | 0.60x | 0.88x | **0.95x** (no meaningful gain) | 0.94x – 0.96x | -191s |
| AMD Ryzen 3 PRO 5450U | Source-listed (see product page) | 1.09x | 0.60x | 0.88x | **0.95x** (no meaningful gain) | 0.94x – 0.96x | -191s |
| Intel Core i7-6820EQ | Core 6th gen | 0.77x | 0.60x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -385s |
| Intel Core i5-7600T | Core 7th gen | 0.83x | 0.60x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -341s |
| Intel Core i7-8650U | Core 8th gen | 0.92x | 0.59x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -288s |
| Intel Core i7-6820HK | Core 6th gen | 0.78x | 0.59x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -380s |
| Intel Core i5-6585R | Core 6th gen | 0.80x | 0.59x | 0.79x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -371s |
| Intel Core i7-4770R | Core 4th gen | 0.72x | 0.59x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -429s |
| Intel Core i5-4670K | Core 4th gen | 0.65x | 0.59x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -498s |
| Intel Core i5-7440HQ | Core 7th gen | 0.85x | 0.59x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -333s |
| Intel Core i5-10210U | Core 10th gen | 0.78x | 0.59x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -384s |
| Intel Core i7-7700T | Core 7th gen | 0.80x | 0.59x | 0.79x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -368s |
| Intel Core i7-4710MQ | Core 4th gen | 0.68x | 0.59x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -471s |
| Intel Core i7-4710HQ | Core 4th gen | 0.68x | 0.58x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -472s |
| Intel Core i7-4770T | Core 4th gen | 0.70x | 0.58x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -457s |
| Intel Core i3-9100T | Core 9th gen | 0.90x | 0.58x | 0.82x | **0.91x** (no meaningful gain) | 0.90x – 0.94x | -317s |
| Intel Core i7-4700HQ | Core 4th gen | 0.67x | 0.57x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -499s |
| Intel Core i7-8550U | Core 8th gen | 0.86x | 0.57x | 0.80x | **0.91x** (no meaningful gain) | 0.89x – 0.93x | -347s |
| Intel Core i7-4700MQ | Core 4th gen | 0.67x | 0.57x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -507s |
| Intel Core i7-4701EQ | Core 4th gen | 0.67x | 0.57x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -507s |
| Intel Core i7-4790T | Core 4th gen | 0.79x | 0.57x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -404s |
| Intel Core i5-4690 | Core 4th gen | 0.80x | 0.56x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -405s |
| AMD Ryzen 3 5300U | Zen 2 | 0.97x | 0.56x | 0.83x | **0.92x** (no meaningful gain) | 0.91x – 0.94x | -290s |
| AMD Ryzen 5 2400G | Zen 1 | 0.73x | 0.56x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -458s |
| AMD Ryzen 3 2200G | Zen 1 | 0.73x | 0.56x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -464s |
| AMD Ryzen 3 PRO 2200G | Source-listed (see product page) | 0.73x | 0.56x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -464s |
| Intel Core i7-1060G7 | Core 10th gen | 0.91x | 0.56x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -328s |
| Intel Core i7-1060NG7 | Intel Mac CPU | 0.91x | 0.56x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -328s |
| MacBook Air (Early 2020) — Intel Core i7-1060NG7 @ 1.2 GHz (4 cores) | Intel Mac | 0.91x | 0.56x | 0.81x | **0.91x** (no meaningful gain) | 0.90x – 0.93x | -328s |
| Intel Core i5-4670 | Core 4th gen | 0.79x | 0.56x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -418s |
| iMac (27-inch Late 2013) — Intel Core i5-4670 @ 3.4 GHz (4 cores) | Intel Mac | 0.79x | 0.56x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -418s |
| Intel Core i5-7400 | Core 7th gen | 0.78x | 0.56x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -421s |
| iMac (21.5-inch Retina Mid 2017) — Intel Core i5-7400 @ 3.0 GHz (4 cores) | Intel Mac | 0.78x | 0.56x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -421s |
| Intel Core i7-5700HQ | Core 5th gen | 0.74x | 0.56x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -457s |
| Intel Core i7-4810MQ | Core 4th gen | 0.73x | 0.56x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -469s |
| Intel Core i5-8365U | Core 8th gen | 0.87x | 0.56x | 0.80x | **0.90x** (no meaningful gain) | 0.89x – 0.93x | -358s |
| Intel Core i5-7500T | Core 7th gen | 0.76x | 0.56x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -447s |
| AMD Ryzen 7 3750H | Zen+ | 0.69x | 0.55x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -507s |
| Intel Core i5-8250U | Core 8th gen | 0.75x | 0.55x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -454s |
| Intel Core i5-6500 | Core 6th gen | 0.79x | 0.55x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -424s |
| iMac (27-inch Retina Late 2015) — Intel Core i5-6500 @ 3.2 GHz (4 cores) | Intel Mac | 0.79x | 0.55x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -424s |
| AMD Ryzen 3 2300X | Zen+ | 0.79x | 0.55x | 0.77x | **0.89x** (no meaningful gain) | 0.87x – 0.92x | -432s |
| AMD Ryzen 3 3200G | Zen+ | 0.72x | 0.55x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.91x | -487s |
| Intel Core i5-4590 | Core 4th gen | 0.76x | 0.55x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -456s |
| Intel Core i7-5750HQ | Core 5th gen | 0.72x | 0.55x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.91x | -487s |
| Intel Core i7-4800MQ | Core 4th gen | 0.71x | 0.55x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -497s |
| Intel Core i5-8265U | Core 8th gen | 0.86x | 0.54x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -382s |
| Intel Core i5-4570 | Core 4th gen | 0.74x | 0.54x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -476s |
| iMac (27-inch Late 2013) — Intel Core i5-4570 @ 3.2 GHz (4 cores) | Intel Mac | 0.74x | 0.54x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -476s |
| Intel Core i5-1035G1 | Core 10th gen | 0.84x | 0.54x | 0.78x | **0.89x** (no meaningful gain) | 0.88x – 0.92x | -404s |
| Intel Core i5-7300HQ | Core 7th gen | 0.72x | 0.54x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -501s |
| AMD Ryzen 3 PRO 3200G | Zen+ | 0.72x | 0.54x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -506s |
| AMD Ryzen 3 1300X | Zen 1 | 0.75x | 0.53x | 0.75x | **0.87x** (no meaningful gain) | 0.85x – 0.91x | -482s |
| Intel Core i5-5575R | Core 5th gen | 0.71x | 0.53x | 0.73x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -514s |
| Intel Core i5-6600T | Core 6th gen | 0.76x | 0.53x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -471s |
| Intel Core i3-8100T | Core 8th gen | 0.70x | 0.53x | 0.73x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -525s |
| AMD Ryzen Embedded R2544 | Source-listed (see product page) | 0.73x | 0.53x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -497s |
| Intel Core i5-4590S | Core 4th gen | 0.74x | 0.53x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -492s |
| AMD Ryzen 3 1200 (AF) | Zen+ | 0.73x | 0.53x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -507s |
| AMD Ryzen 3 PRO 1300 | Zen 1 | 0.73x | 0.53x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -502s |
| Intel Core i5-4460 | Core 4th gen | 0.69x | 0.53x | 0.72x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -549s |
| AMD Ryzen 3 4300U | Zen 2 | 0.89x | 0.52x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -385s |
| Intel Core i5-6440EQ | Core 6th gen | 0.72x | 0.52x | 0.73x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -519s |
| AMD Ryzen 5 3550H | Zen+ | 0.68x | 0.52x | 0.72x | **0.86x** (no meaningful gain) | 0.83x – 0.89x | -562s |
| AMD Ryzen 7 3700C | Zen+ | 0.68x | 0.52x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -565s |
| AMD Ryzen 7 3700U | Zen+ | 0.68x | 0.52x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -565s |
| AMD Ryzen 7 3780U | Zen+ | 0.68x | 0.52x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -565s |
| Intel Core i5-4440 | Core 4th gen | 0.67x | 0.52x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -578s |
| Intel Core i5-4570S | Core 4th gen | 0.71x | 0.52x | 0.72x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -538s |
| iMac (21.5-inch Late 2013) — Intel Core i5-4570S @ 2.9 GHz (4 cores) | Intel Mac | 0.71x | 0.52x | 0.72x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -538s |
| Intel Core i5-4690S | Core 4th gen | 0.79x | 0.52x | 0.75x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -474s |
| Intel Core i5-6400 | Core 6th gen | 0.76x | 0.51x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -502s |
| Intel Core i5-6440HQ | Core 6th gen | 0.74x | 0.51x | 0.73x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -520s |
| Intel Core i3-1115G4 | Core 11th gen | 1.15x | 0.51x | 0.85x | **0.93x** (no meaningful gain) | 0.92x – 0.94x | -257s |
| Intel Core i5-6500T | Core 6th gen | 0.70x | 0.51x | 0.72x | **0.86x** (no meaningful gain) | 0.84x – 0.89x | -553s |
| AMD Ryzen 3 1200 | Zen 1 | 0.71x | 0.51x | 0.72x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -544s |
| AMD Ryzen 3 PRO 1200 | Zen 1 | 0.71x | 0.51x | 0.72x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -544s |
| Intel Core i7-4960X | Core 4th gen | 0.51x | 0.51x | 0.64x | **0.81x** (no meaningful gain) | 0.78x – 0.86x | -800s |
| Intel Core i5-4430 | Core 4th gen | 0.65x | 0.50x | 0.70x | **0.84x** (no meaningful gain) | 0.82x – 0.88x | -621s |
| Intel Core i5-8365UE | Core 8th gen | 0.86x | 0.49x | 0.76x | **0.88x** (no meaningful gain) | 0.87x – 0.91x | -447s |
| Intel Core i7-10510Y | Core 10th gen | 0.85x | 0.49x | 0.76x | **0.88x** (no meaningful gain) | 0.86x – 0.91x | -458s |
| AMD Ryzen Embedded R2514 | Source-listed (see product page) | 0.71x | 0.49x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -577s |
| AMD Ryzen 7 2700U | Zen 1 | 0.69x | 0.49x | 0.70x | **0.85x** (no meaningful gain) | 0.82x – 0.89x | -600s |
| Intel Core i5-7400T | Core 7th gen | 0.71x | 0.49x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -581s |
| Intel Core i5-4460S | Core 4th gen | 0.68x | 0.48x | 0.70x | **0.84x** (no meaningful gain) | 0.82x – 0.88x | -615s |
| Intel Core i5-4570R | Core 4th gen | 0.64x | 0.48x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.88x | -668s |
| iMac (21.5-inch Late 2013) — Intel Core i5-4570R @ 2.7 GHz (4 cores) | Intel Mac | 0.64x | 0.48x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.88x | -668s |
| AMD Ryzen 5 3500U | Zen+ | 0.65x | 0.48x | 0.69x | **0.84x** (no meaningful gain) | 0.81x – 0.88x | -651s |
| Intel Core i5-4690T | Core 4th gen | 0.69x | 0.48x | 0.70x | **0.84x** (no meaningful gain) | 0.82x – 0.88x | -618s |
| Intel Core i5-1030NG7 | Core 10th gen | 0.83x | 0.48x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -499s |
| MacBook Air (Early 2020) — Intel Core i5-1030NG7 @ 1.1 GHz (4 cores) | Intel Mac | 0.83x | 0.48x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -499s |
| Intel Core i3-1110G4 | Core 11th gen | 1.01x | 0.47x | 0.79x | **0.90x** (no meaningful gain) | 0.88x – 0.92x | -383s |
| Intel Core i5-4440S | Core 4th gen | 0.66x | 0.47x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -676s |
| Intel Core i7-4820K | Core 4th gen | 0.49x | 0.47x | 0.61x | **0.79x** (no meaningful gain) | 0.76x – 0.84x | -900s |
| Intel Core i5-6300HQ | Core 6th gen | 0.70x | 0.47x | 0.69x | **0.84x** (no meaningful gain) | 0.82x – 0.88x | -636s |
| Intel Core i5-6350HQ | Core 6th gen | 0.70x | 0.47x | 0.69x | **0.84x** (no meaningful gain) | 0.82x – 0.88x | -636s |
| Intel Core i5-4590T | Core 4th gen | 0.61x | 0.46x | 0.66x | **0.82x** (no meaningful gain) | 0.79x – 0.86x | -737s |
| Intel Core i5-4430S | Core 4th gen | 0.65x | 0.46x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -697s |
| Intel Core i5-4670T | Core 4th gen | 0.66x | 0.46x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -688s |
| Intel Core i3-7350K | Core 7th gen | 0.86x | 0.46x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -502s |
| Intel Core i5-6400T | Core 6th gen | 0.65x | 0.46x | 0.67x | **0.82x** (no meaningful gain) | 0.80x – 0.87x | -710s |
| Intel Core i3-6320 | Core 6th gen | 0.87x | 0.46x | 0.74x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -498s |
| AMD Ryzen 3 3350U | Zen+ | 0.65x | 0.45x | 0.66x | **0.82x** (no meaningful gain) | 0.80x – 0.87x | -721s |
| Intel Core i3-7320 | Core 7th gen | 0.85x | 0.45x | 0.73x | **0.86x** (no meaningful gain) | 0.84x – 0.90x | -534s |
| Intel Core i7-5700EQ | Core 5th gen | 0.51x | 0.44x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.84x | -930s |
| Intel Core i7-7660U | Core 7th gen | 0.84x | 0.44x | 0.72x | **0.86x** (no meaningful gain) | 0.84x – 0.89x | -552s |
| AMD Athlon Gold 7220U | Zen 2 | 0.79x | 0.44x | 0.70x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -598s |
| Intel Core i7-7567U | Core 7th gen | 0.85x | 0.44x | 0.72x | **0.86x** (no meaningful gain) | 0.84x – 0.89x | -551s |
| Intel Core i5-1030G7 | Core 10th gen | 0.82x | 0.43x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -576s |
| AMD Ryzen 3 PRO 2300U | Source-listed (see product page) | 0.61x | 0.43x | 0.64x | **0.81x** (no meaningful gain) | 0.78x – 0.86x | -794s |
| Intel Core i3-1005G1 | Core 10th gen | 0.90x | 0.43x | 0.73x | **0.87x** (no meaningful gain) | 0.85x – 0.90x | -512s |
| AMD Ryzen 3 2300U | Zen 1 | 0.61x | 0.43x | 0.64x | **0.81x** (no meaningful gain) | 0.78x – 0.85x | -802s |
| AMD Ryzen 3 PRO 3300U | Source-listed (see product page) | 0.65x | 0.43x | 0.65x | **0.81x** (no meaningful gain) | 0.79x – 0.86x | -758s |
| Intel Core i3-6300 | Core 6th gen | 0.83x | 0.43x | 0.71x | **0.85x** (no meaningful gain) | 0.83x – 0.89x | -578s |
| AMD Ryzen 3 3300U | Zen+ | 0.65x | 0.43x | 0.65x | **0.81x** (no meaningful gain) | 0.79x – 0.86x | -764s |
| Intel Core i5-7287U | Core 7th gen | 0.77x | 0.42x | 0.69x | **0.84x** (no meaningful gain) | 0.81x – 0.88x | -642s |
| Intel Core i3-8109U | Core 8th gen | 0.79x | 0.42x | 0.69x | **0.84x** (no meaningful gain) | 0.82x – 0.88x | -628s |
| Intel Core i5-7260U | Core 7th gen | 0.80x | 0.42x | 0.69x | **0.84x** (no meaningful gain) | 0.82x – 0.88x | -630s |
| Intel Core i3-7300 | Core 7th gen | 0.83x | 0.41x | 0.70x | **0.85x** (no meaningful gain) | 0.82x – 0.89x | -605s |
| Intel Core i5-7360U | Core 7th gen | 0.74x | 0.41x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -684s |
| MacBook Pro (13-inch Mid 2017) — Intel Core i5-7360U @ 2.3 GHz (2 cores) | Intel Mac | 0.74x | 0.41x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -684s |
| iMac (21.5-inch Mid 2017) — Intel Core i5-7360U @ 2.3 GHz (2 cores) | Intel Mac | 0.74x | 0.41x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -684s |
| Intel Core i3-4370 | Core 4th gen | 0.79x | 0.41x | 0.69x | **0.84x** (no meaningful gain) | 0.81x – 0.88x | -649s |
| Intel Core i5-4460T | Core 4th gen | 0.55x | 0.41x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -940s |
| Intel Core i3-7100 | Core 7th gen | 0.82x | 0.41x | 0.69x | **0.84x** (no meaningful gain) | 0.82x – 0.88x | -633s |
| Intel Core i5-7267U | Core 7th gen | 0.75x | 0.41x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -697s |
| MacBook Pro (13-inch Mid 2017) — Intel Core i5-7267U @ 3.1 GHz (2 cores) | Intel Mac | 0.75x | 0.41x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -697s |
| Intel Core i3-8121U | Core 8th gen | 0.74x | 0.40x | 0.67x | **0.82x** (no meaningful gain) | 0.80x – 0.87x | -710s |
| Intel Core i3-8140U | Core 8th gen | 0.82x | 0.40x | 0.69x | **0.84x** (no meaningful gain) | 0.81x – 0.88x | -644s |
| Intel Core i3-4360 | Core 4th gen | 0.77x | 0.40x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -692s |
| Intel Core i3-7300T | Core 7th gen | 0.78x | 0.40x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -680s |
| Intel Core i3-4170 | Core 4th gen | 0.76x | 0.40x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -700s |
| Intel Core i3-7101TE | Core 7th gen | 0.77x | 0.39x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -701s |
| Intel Core i3-8145UE | Core 8th gen | 0.81x | 0.39x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.88x | -665s |
| Intel Core i3-6100 | Core 6th gen | 0.81x | 0.39x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -671s |
| Intel Core i7-7600U | Core 7th gen | 0.83x | 0.39x | 0.69x | **0.84x** (no meaningful gain) | 0.81x – 0.88x | -645s |
| Intel Core i3-6300T | Core 6th gen | 0.77x | 0.39x | 0.67x | **0.82x** (no meaningful gain) | 0.80x – 0.87x | -708s |
| Intel Core i3-6098P | Core 6th gen | 0.78x | 0.39x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -696s |
| Intel Core i3-8145U | Core 8th gen | 0.81x | 0.39x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -671s |
| Intel Core i3-7100T | Core 7th gen | 0.77x | 0.39x | 0.67x | **0.82x** (no meaningful gain) | 0.80x – 0.87x | -710s |
| Intel Core i3-4160 | Core 4th gen | 0.74x | 0.39x | 0.65x | **0.82x** (no meaningful gain) | 0.79x – 0.86x | -753s |
| Intel Core i7-7560U | Core 7th gen | 0.82x | 0.38x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -673s |
| Intel Core i3-10110U | Core 10th gen | 0.80x | 0.38x | 0.67x | **0.83x** (no meaningful gain) | 0.80x – 0.87x | -698s |
| Intel Core i7-7500U | Core 7th gen | 0.79x | 0.38x | 0.66x | **0.82x** (no meaningful gain) | 0.80x – 0.87x | -720s |
| Intel Core i5-7300U | Core 7th gen | 0.72x | 0.38x | 0.64x | **0.81x** (no meaningful gain) | 0.78x – 0.86x | -786s |
| Intel Core i7-6567U | Core 6th gen | 0.74x | 0.38x | 0.65x | **0.81x** (no meaningful gain) | 0.79x – 0.86x | -768s |
| MacBook Pro (13-inch Late 2016) — Intel Core i7-6567U @ 3.3 GHz (2 cores) | Intel Mac | 0.74x | 0.38x | 0.65x | **0.81x** (no meaningful gain) | 0.79x – 0.86x | -768s |
| Intel Core i3-1000G4 | Core 10th gen | 0.85x | 0.37x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -672s |
| Intel Core i3-1000NG4 | Core 10th gen | 0.85x | 0.37x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -672s |
| MacBook Air (Early 2020) — Intel Core i3-1000NG4 @ 1.1 GHz (2 cores) | Intel Mac | 0.85x | 0.37x | 0.68x | **0.83x** (no meaningful gain) | 0.81x – 0.87x | -672s |
| Intel Core i5-4340M | Core 4th gen | 0.69x | 0.37x | 0.63x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -845s |
| Intel Core i3-4150 | Core 4th gen | 0.71x | 0.37x | 0.64x | **0.80x** (no meaningful gain) | 0.78x – 0.85x | -814s |
| Intel Core i5-6287U | Core 6th gen | 0.74x | 0.37x | 0.64x | **0.81x** (no meaningful gain) | 0.78x – 0.85x | -791s |
| Intel Core i7-6660U | Core 6th gen | 0.73x | 0.37x | 0.64x | **0.81x** (no meaningful gain) | 0.78x – 0.85x | -808s |
| MacBook Pro (13-inch Late 2016) — Intel Core i7-6660U @ 2.4 GHz (2 cores) | Intel Mac | 0.73x | 0.37x | 0.64x | **0.81x** (no meaningful gain) | 0.78x – 0.85x | -808s |
| Intel Core i7-5557U | Core 5th gen | 0.70x | 0.36x | 0.63x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -846s |
| MacBook Pro (13-inch Retina Early 2015) — Intel Core i7-5557U @ 3.1 GHz (2 cores) | Intel Mac | 0.70x | 0.36x | 0.63x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -846s |
| Intel Core i3-4330 | Core 4th gen | 0.72x | 0.36x | 0.63x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -828s |
| Intel Core i3-6100T | Core 6th gen | 0.72x | 0.36x | 0.63x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -822s |
| AMD Athlon 3000G | Zen 1 / Zen+ | 0.69x | 0.36x | 0.62x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -857s |
| Intel Core i3-8130U | Core 8th gen | 0.76x | 0.36x | 0.64x | **0.81x** (no meaningful gain) | 0.78x – 0.86x | -786s |
| Intel Core i7-6498DU | Core 6th gen | 0.71x | 0.36x | 0.63x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -840s |
| Intel Core i7-6650U | Core 6th gen | 0.73x | 0.36x | 0.63x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -830s |
| Intel Core i7-4600M | Core 4th gen | 0.68x | 0.35x | 0.61x | **0.79x** (no meaningful gain) | 0.76x – 0.84x | -888s |
| Intel Core i7-6500U | Core 6th gen | 0.71x | 0.35x | 0.62x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -852s |
| Intel Core i7-6560U | Core 6th gen | 0.72x | 0.35x | 0.63x | **0.80x** (no meaningful gain) | 0.77x – 0.85x | -846s |
| Intel Core i5-4330M | Core 4th gen | 0.69x | 0.35x | 0.61x | **0.79x** (no meaningful gain) | 0.76x – 0.84x | -895s |
| Intel Core i5-6267U | Core 6th gen | 0.70x | 0.35x | 0.62x | **0.79x** (no meaningful gain) | 0.76x – 0.84x | -877s |
| MacBook Pro (13-inch Late 2016) — Intel Core i5-6267U @ 2.9 GHz (2 cores) | Intel Mac | 0.70x | 0.35x | 0.62x | **0.79x** (no meaningful gain) | 0.76x – 0.84x | -877s |
| Intel Core i3-4130 | Core 4th gen | 0.70x | 0.35x | 0.62x | **0.79x** (no meaningful gain) | 0.76x – 0.84x | -885s |
| AMD Ryzen 5 3500C | Zen+ | 0.62x | 0.34x | 0.59x | **0.77x** (no meaningful gain) | 0.74x – 0.82x | -1001s |
| Intel Core i5-6360U | Core 6th gen | 0.66x | 0.34x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -950s |
| MacBook Pro (13-inch Late 2016) — Intel Core i5-6360U @ 2.0 GHz (2 cores) | Intel Mac | 0.66x | 0.34x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -950s |
| AMD Ryzen 3 5125C | Zen 3 | 0.64x | 0.34x | 0.59x | **0.78x** (no meaningful gain) | 0.74x – 0.83x | -971s |
| Intel Core i5-4210H | Core 4th gen | 0.69x | 0.34x | 0.61x | **0.79x** (no meaningful gain) | 0.76x – 0.84x | -914s |
| Intel Core i5-5287U | Core 5th gen | 0.67x | 0.34x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -935s |
| MacBook Pro (13-inch Retina Early 2015) — Intel Core i5-5287U @ 2.9 GHz (2 cores) | Intel Mac | 0.67x | 0.34x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -935s |
| Intel Core i7-4610M | Core 4th gen | 0.68x | 0.34x | 0.61x | **0.78x** (no meaningful gain) | 0.75x – 0.84x | -921s |
| Intel Core i5-4310M | Core 4th gen | 0.66x | 0.34x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -951s |
| Intel Core i5-4308U | Core 4th gen | 0.65x | 0.34x | 0.59x | **0.77x** (no meaningful gain) | 0.74x – 0.83x | -974s |
| MacBook Pro (13-inch Retina Mid 2014) — Intel Core i5-4308U @ 2.8 GHz (2 cores) | Intel Mac | 0.65x | 0.34x | 0.59x | **0.77x** (no meaningful gain) | 0.74x – 0.83x | -974s |
| Intel Core i5-6260U | Core 6th gen | 0.65x | 0.34x | 0.59x | **0.78x** (no meaningful gain) | 0.74x – 0.83x | -971s |
| Intel Core i5-4300M | Core 4th gen | 0.66x | 0.34x | 0.59x | **0.78x** (no meaningful gain) | 0.74x – 0.83x | -965s |
| Intel Core i5-6300U | Core 6th gen | 0.65x | 0.34x | 0.59x | **0.77x** (no meaningful gain) | 0.74x – 0.83x | -990s |
| Intel Core i7-5600U | Core 5th gen | 0.67x | 0.33x | 0.60x | **0.78x** (no meaningful gain) | 0.74x – 0.83x | -961s |
| Intel Core i7-4578U | Core 4th gen | 0.67x | 0.33x | 0.59x | **0.78x** (no meaningful gain) | 0.74x – 0.83x | -969s |
| Mac mini (Late 2014) — Intel Core i7-4578U @ 3.0 GHz (2 cores) | Intel Mac | 0.67x | 0.33x | 0.59x | **0.78x** (no meaningful gain) | 0.74x – 0.83x | -969s |
| MacBook Pro (13-inch Retina Mid 2014) — Intel Core i7-4578U @ 3.0 GHz (2 cores) | Intel Mac | 0.67x | 0.33x | 0.59x | **0.78x** (no meaningful gain) | 0.74x – 0.83x | -969s |
| AMD Athlon 200GE | Zen 1 / Zen+ | 0.65x | 0.33x | 0.59x | **0.77x** (no meaningful gain) | 0.74x – 0.82x | -995s |
| AMD Athlon Gold 3150C | Zen 1 / Zen+ | 0.61x | 0.33x | 0.57x | **0.76x** (no meaningful gain) | 0.72x – 0.81x | -1068s |
| AMD Athlon Gold 3150U | Zen 1 / Zen+ | 0.61x | 0.33x | 0.57x | **0.76x** (no meaningful gain) | 0.72x – 0.81x | -1068s |
| AMD Athlon 300U | Zen 1 / Zen+ | 0.64x | 0.33x | 0.58x | **0.77x** (no meaningful gain) | 0.73x – 0.82x | -1022s |
| Intel Core i7-4558U | Core 4th gen | 0.64x | 0.33x | 0.58x | **0.77x** (no meaningful gain) | 0.73x – 0.82x | -1024s |
| Intel Core i5-5257U | Core 5th gen | 0.65x | 0.33x | 0.58x | **0.77x** (no meaningful gain) | 0.73x – 0.82x | -1015s |
| MacBook Pro (13-inch Retina Early 2015) — Intel Core i5-5257U @ 2.7 GHz (2 cores) | Intel Mac | 0.65x | 0.33x | 0.58x | **0.77x** (no meaningful gain) | 0.73x – 0.82x | -1015s |
| Intel Core i5-4210M | Core 4th gen | 0.64x | 0.33x | 0.58x | **0.76x** (no meaningful gain) | 0.73x – 0.82x | -1035s |
| Intel Core i5-6198DU | Core 6th gen | 0.63x | 0.32x | 0.57x | **0.76x** (no meaningful gain) | 0.73x – 0.82x | -1048s |
| Intel Core i5-4200H | Core 4th gen | 0.66x | 0.32x | 0.58x | **0.77x** (no meaningful gain) | 0.73x – 0.82x | -1010s |
| Intel Core i7-5550U | Core 5th gen | 0.64x | 0.32x | 0.58x | **0.76x** (no meaningful gain) | 0.73x – 0.82x | -1041s |
| Intel Core i5-7200U | Core 7th gen | 0.66x | 0.32x | 0.58x | **0.77x** (no meaningful gain) | 0.73x – 0.82x | -1016s |
| Intel Core i7-6600U | Core 6th gen | 0.73x | 0.32x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -927s |
| Intel Core i7-5500U | Core 5th gen | 0.64x | 0.32x | 0.58x | **0.76x** (no meaningful gain) | 0.73x – 0.82x | -1045s |
| Intel Core m7-6Y75 | Core 6th gen | 0.73x | 0.32x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -928s |
| Intel Core i3-4160T | Core 4th gen | 0.64x | 0.32x | 0.57x | **0.76x** (no meaningful gain) | 0.73x – 0.82x | -1052s |
| AMD Athlon Silver 7120U | Zen 2 | 0.73x | 0.32x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -940s |
| Intel Core i7-5650U | Core 5th gen | 0.67x | 0.32x | 0.58x | **0.76x** (no meaningful gain) | 0.73x – 0.82x | -1032s |
| MacBook Air (13-inch Early 2015) — Intel Core i7-5650U @ 2.2 GHz (2 cores) | Intel Mac | 0.67x | 0.32x | 0.58x | **0.76x** (no meaningful gain) | 0.73x – 0.82x | -1032s |
| Intel Core i3-6100H | Core 6th gen | 0.61x | 0.31x | 0.56x | **0.75x** (no meaningful gain) | 0.72x – 0.81x | -1107s |
| Intel Core i5-4200M | Core 4th gen | 0.61x | 0.31x | 0.56x | **0.75x** (no meaningful gain) | 0.71x – 0.81x | -1116s |
| Intel Core i5-4278U | Core 4th gen | 0.59x | 0.31x | 0.55x | **0.74x** (no meaningful gain) | 0.71x – 0.80x | -1148s |
| Mac mini (Late 2014) — Intel Core i5-4278U @ 2.6 GHz (2 cores) | Intel Mac | 0.59x | 0.31x | 0.55x | **0.74x** (no meaningful gain) | 0.71x – 0.80x | -1148s |
| MacBook Pro (13-inch Retina Mid 2014) — Intel Core i5-4278U @ 2.6 GHz (2 cores) | Intel Mac | 0.59x | 0.31x | 0.55x | **0.74x** (no meaningful gain) | 0.71x – 0.80x | -1148s |
| Intel Core i5-6200U | Core 6th gen | 0.63x | 0.31x | 0.56x | **0.75x** (no meaningful gain) | 0.72x – 0.81x | -1092s |
| Intel Core i3-4130T | Core 4th gen | 0.61x | 0.31x | 0.56x | **0.75x** (no meaningful gain) | 0.71x – 0.81x | -1126s |
| Intel Core i3-4150T | Core 4th gen | 0.63x | 0.31x | 0.56x | **0.75x** (no meaningful gain) | 0.72x – 0.81x | -1105s |
| Intel Core i5-4288U | Core 4th gen | 0.59x | 0.31x | 0.55x | **0.74x** (no meaningful gain) | 0.70x – 0.80x | -1168s |
| Intel Core i5-5300U | Core 5th gen | 0.61x | 0.31x | 0.56x | **0.75x** (no meaningful gain) | 0.71x – 0.81x | -1136s |
| Intel Core i3-10100Y | Core 10th gen | 0.75x | 0.30x | 0.59x | **0.77x** (no meaningful gain) | 0.74x – 0.83x | -980s |
| AMD Ryzen Embedded V1500B | Zen 1 | 0.37x | 0.30x | 0.45x | **0.66x** (no meaningful gain) | 0.62x – 0.74x | -1714s |
| Intel Core i3-7130U | Core 7th gen | 0.62x | 0.30x | 0.55x | **0.74x** (no meaningful gain) | 0.71x – 0.80x | -1166s |
| Intel Core i7-7Y75 | Core 7th gen | 0.69x | 0.30x | 0.57x | **0.76x** (no meaningful gain) | 0.72x – 0.81x | -1068s |
| MacBook (Mid 2017) — Intel Core i7-7Y75 @ 1.4 GHz (2 cores) | Intel Mac | 0.69x | 0.30x | 0.57x | **0.76x** (no meaningful gain) | 0.72x – 0.81x | -1068s |
| Intel Core m3-7Y32 | Core 7th gen | 0.63x | 0.30x | 0.56x | **0.74x** (no meaningful gain) | 0.71x – 0.81x | -1140s |
| MacBook (Mid 2017) — Intel Core m3-7Y32 @ 1.2 GHz (2 cores) | Intel Mac | 0.63x | 0.30x | 0.56x | **0.74x** (no meaningful gain) | 0.71x – 0.81x | -1140s |
| Intel Core i5-5200U | Core 5th gen | 0.56x | 0.29x | 0.53x | **0.73x** (no meaningful gain) | 0.69x – 0.79x | -1259s |
| AMD Ryzen 3 2200U | Zen 1 | 0.57x | 0.29x | 0.53x | **0.73x** (no meaningful gain) | 0.69x – 0.79x | -1245s |
| Intel Core i5-4310U | Core 4th gen | 0.57x | 0.29x | 0.53x | **0.73x** (no meaningful gain) | 0.69x – 0.79x | -1246s |
| Intel Core i7-4650U | Core 4th gen | 0.63x | 0.29x | 0.55x | **0.74x** (no meaningful gain) | 0.71x – 0.80x | -1154s |
| Intel Core i7-8500Y | Core 8th gen | 0.80x | 0.29x | 0.60x | **0.78x** (no meaningful gain) | 0.75x – 0.83x | -947s |
| Intel Core i7-4510U | Core 4th gen | 0.62x | 0.29x | 0.55x | **0.74x** (no meaningful gain) | 0.70x – 0.80x | -1183s |
| Intel Core m3-8100Y | Core 8th gen | 0.69x | 0.29x | 0.57x | **0.75x** (no meaningful gain) | 0.72x – 0.81x | -1090s |
| Intel Core i5-5350U | Core 5th gen | 0.60x | 0.29x | 0.54x | **0.73x** (no meaningful gain) | 0.70x – 0.80x | -1217s |
| MacBook Air (Mid 2017) — Intel Core i5-5350U @ 1.8 GHz (2 cores) | Intel Mac | 0.60x | 0.29x | 0.54x | **0.73x** (no meaningful gain) | 0.70x – 0.80x | -1217s |
| Intel Core i3-4110M | Core 4th gen | 0.53x | 0.29x | 0.51x | **0.71x** (no meaningful gain) | 0.67x – 0.78x | -1346s |
| Intel Core i7-4600U | Core 4th gen | 0.63x | 0.29x | 0.55x | **0.74x** (no meaningful gain) | 0.71x – 0.80x | -1167s |
| Intel Core i5-4300U | Core 4th gen | 0.55x | 0.29x | 0.52x | **0.72x** (no meaningful gain) | 0.68x – 0.78x | -1323s |
| Intel Core i5-8210Y | Core 8th gen | 0.53x | 0.29x | 0.51x | **0.71x** (no meaningful gain) | 0.67x – 0.78x | -1352s |
| Intel Core i5-8310Y | Core 8th gen | 0.57x | 0.29x | 0.53x | **0.72x** (no meaningful gain) | 0.69x – 0.79x | -1276s |
| Intel Core i3-6157U | Core 6th gen | 0.50x | 0.29x | 0.50x | **0.70x** (no meaningful gain) | 0.66x – 0.77x | -1429s |
| Intel Core i3-7100U | Core 7th gen | 0.56x | 0.28x | 0.52x | **0.72x** (no meaningful gain) | 0.68x – 0.78x | -1312s |
| Intel Core i5-7Y54 | Core 7th gen | 0.60x | 0.28x | 0.53x | **0.73x** (no meaningful gain) | 0.69x – 0.79x | -1256s |
| Intel Core i5-7Y57 | Core 7th gen | 0.61x | 0.28x | 0.54x | **0.73x** (no meaningful gain) | 0.69x – 0.79x | -1232s |
| MacBook (Mid 2017) — Intel Core i5-7Y54 @ 1.3 GHz (2 cores) | Intel Mac | 0.60x | 0.28x | 0.53x | **0.73x** (no meaningful gain) | 0.69x – 0.79x | -1256s |
| Intel Core i3-7020U | Core 7th gen | 0.55x | 0.28x | 0.51x | **0.71x** (no meaningful gain) | 0.67x – 0.78x | -1348s |
| Intel Core i5-4258U | Core 4th gen | 0.56x | 0.28x | 0.52x | **0.71x** (no meaningful gain) | 0.68x – 0.78x | -1336s |
| MacBook Pro (13-inch Retina Late 2013) — Intel Core i5-4258U @ 2.4 GHz (2 cores) | Intel Mac | 0.56x | 0.28x | 0.52x | **0.71x** (no meaningful gain) | 0.68x – 0.78x | -1336s |
| Intel Core m5-6Y54 | Core 6th gen | 0.58x | 0.28x | 0.52x | **0.72x** (no meaningful gain) | 0.68x – 0.78x | -1307s |
| MacBook (Early 2016) — Intel Core m5-6Y54 @ 1.2 GHz (2 cores) | Intel Mac | 0.58x | 0.28x | 0.52x | **0.72x** (no meaningful gain) | 0.68x – 0.78x | -1307s |
| Intel Core i3-4100M | Core 4th gen | 0.51x | 0.27x | 0.49x | **0.70x** (no meaningful gain) | 0.66x – 0.77x | -1447s |
| Intel Core i3-6100U | Core 6th gen | 0.48x | 0.27x | 0.48x | **0.69x** (no meaningful gain) | 0.65x – 0.76x | -1520s |
| Intel Core i5-5250U | Core 5th gen | 0.56x | 0.27x | 0.51x | **0.71x** (no meaningful gain) | 0.67x – 0.78x | -1363s |
| MacBook Air (13-inch Early 2015) — Intel Core i5-5250U @ 1.6 GHz (2 cores) | Intel Mac | 0.56x | 0.27x | 0.51x | **0.71x** (no meaningful gain) | 0.67x – 0.78x | -1363s |
| AMD Ryzen 3 3200U | Zen 1 | 0.62x | 0.27x | 0.53x | **0.72x** (no meaningful gain) | 0.69x – 0.79x | -1286s |
| AMD Ryzen 3 3250U | Zen 1 | 0.62x | 0.27x | 0.53x | **0.72x** (no meaningful gain) | 0.69x – 0.79x | -1286s |
| Intel Core i3-5157U | Core 5th gen | 0.53x | 0.26x | 0.49x | **0.70x** (no meaningful gain) | 0.66x – 0.76x | -1460s |
| Intel Core i7-4500U | Core 4th gen | 0.60x | 0.26x | 0.51x | **0.71x** (no meaningful gain) | 0.67x – 0.78x | -1354s |
| Intel Core m3-7Y30 | Core 7th gen | 0.57x | 0.26x | 0.50x | **0.70x** (no meaningful gain) | 0.66x – 0.77x | -1412s |
| Intel Core i3-4000M | Core 4th gen | 0.49x | 0.26x | 0.47x | **0.68x** (no meaningful gain) | 0.64x – 0.75x | -1579s |
| AMD Athlon Silver 3050U | Zen 1 / Zen+ | 0.58x | 0.25x | 0.50x | **0.70x** (no meaningful gain) | 0.67x – 0.77x | -1404s |
| Intel Core i3-5020U | Core 5th gen | 0.49x | 0.25x | 0.47x | **0.68x** (no meaningful gain) | 0.63x – 0.75x | -1610s |
| Intel Core i5-4210U | Core 4th gen | 0.53x | 0.25x | 0.48x | **0.69x** (no meaningful gain) | 0.65x – 0.76x | -1529s |
| AMD Athlon Silver 3050e | Zen 1 / Zen+ | 0.51x | 0.25x | 0.47x | **0.68x** (no meaningful gain) | 0.64x – 0.75x | -1586s |
| Intel Core m3-6Y30 | Core 6th gen | 0.51x | 0.25x | 0.47x | **0.68x** (no meaningful gain) | 0.64x – 0.75x | -1580s |
| MacBook (Early 2016) — Intel Core m3-6Y30 @ 1.1 GHz (2 cores) | Intel Mac | 0.51x | 0.25x | 0.47x | **0.68x** (no meaningful gain) | 0.64x – 0.75x | -1580s |
| Intel Core i5-4260U | Core 4th gen | 0.53x | 0.24x | 0.48x | **0.68x** (no meaningful gain) | 0.64x – 0.75x | -1548s |
| MacBook Air (13-inch Early 2014) — Intel Core i5-4260U @ 1.4 GHz (2 cores) | Intel Mac | 0.53x | 0.24x | 0.48x | **0.68x** (no meaningful gain) | 0.64x – 0.75x | -1548s |
| Intel Core i7-4550U | Core 4th gen | 0.60x | 0.24x | 0.50x | **0.70x** (no meaningful gain) | 0.66x – 0.77x | -1430s |
| Intel Core i5-4250U | Core 4th gen | 0.51x | 0.24x | 0.47x | **0.68x** (no meaningful gain) | 0.63x – 0.75x | -1607s |
| AMD Ryzen 3 3250C | Zen 1 | 0.64x | 0.24x | 0.51x | **0.71x** (no meaningful gain) | 0.67x – 0.78x | -1368s |
| Intel Core i5-4200U | Core 4th gen | 0.51x | 0.24x | 0.47x | **0.67x** (no meaningful gain) | 0.63x – 0.74x | -1619s |
| Intel Core M 5Y51 | Core 5th gen | 0.52x | 0.24x | 0.47x | **0.68x** (no meaningful gain) | 0.63x – 0.75x | -1611s |
| Intel Core M 5Y71 | Core 5th gen | 0.57x | 0.24x | 0.49x | **0.69x** (no meaningful gain) | 0.65x – 0.76x | -1502s |
| Intel Core i3-4330TE | Core 4th gen | 0.47x | 0.23x | 0.45x | **0.65x** (no meaningful gain) | 0.61x – 0.73x | -1770s |
| Intel Core i5-8200Y | Core 8th gen | 0.57x | 0.23x | 0.48x | **0.69x** (no meaningful gain) | 0.65x – 0.75x | -1539s |
| Intel Core i3-5010U | Core 5th gen | 0.44x | 0.23x | 0.43x | **0.64x** (no meaningful gain) | 0.60x – 0.72x | -1856s |
| Intel Core m5-6Y57 | Core 6th gen | 0.55x | 0.23x | 0.47x | **0.67x** (no meaningful gain) | 0.63x – 0.75x | -1612s |
| Intel Core i3-6006U | Core 6th gen | 0.43x | 0.23x | 0.42x | **0.64x** (no meaningful gain) | 0.59x – 0.71x | -1918s |
| AMD Ryzen Embedded R1600 | Source-listed (see product page) | 0.58x | 0.22x | 0.47x | **0.68x** (no meaningful gain) | 0.64x – 0.75x | -1572s |
| Intel Core i3-5015U | Core 5th gen | 0.44x | 0.22x | 0.43x | **0.64x** (no meaningful gain) | 0.59x – 0.71x | -1902s |
| Intel Core M 5Y10c | Core 5th gen | 0.46x | 0.22x | 0.43x | **0.64x** (no meaningful gain) | 0.60x – 0.72x | -1856s |
| Intel Core M 5Y31 | Core 5th gen | 0.48x | 0.21x | 0.43x | **0.64x** (no meaningful gain) | 0.60x – 0.72x | -1861s |
| MacBook (Early 2015) — Intel Core M-5Y31 @ 1.1 GHz (2 cores) | Intel Mac | 0.48x | 0.21x | 0.43x | **0.64x** (no meaningful gain) | 0.60x – 0.72x | -1861s |
| Intel Core i3-4025U | Core 4th gen | 0.38x | 0.21x | 0.39x | **0.60x** (no meaningful gain) | 0.55x – 0.68x | -2230s |
| Intel Core i3-4030U | Core 4th gen | 0.38x | 0.21x | 0.39x | **0.60x** (no meaningful gain) | 0.55x – 0.68x | -2230s |
| Intel Core i3-5005U | Core 5th gen | 0.42x | 0.20x | 0.40x | **0.61x** (no meaningful gain) | 0.56x – 0.69x | -2148s |
| Intel Core i3-4005U | Core 4th gen | 0.35x | 0.18x | 0.36x | **0.56x** (no meaningful gain) | 0.52x – 0.65x | -2572s |
| Intel Core i3-4010U | Core 4th gen | 0.35x | 0.18x | 0.36x | **0.56x** (no meaningful gain) | 0.52x – 0.65x | -2572s |
| Intel Core i5-4302Y | Core 4th gen | 0.45x | 0.18x | 0.39x | **0.60x** (no meaningful gain) | 0.56x – 0.68x | -2208s |
| Intel Core i5-4220Y | Core 4th gen | 0.39x | 0.17x | 0.36x | **0.57x** (no meaningful gain) | 0.53x – 0.66x | -2478s |
| Intel Core i5-4202Y | Core 4th gen | 0.39x | 0.17x | 0.36x | **0.57x** (no meaningful gain) | 0.53x – 0.66x | -2508s |
| Intel Core i5-4210Y | Core 4th gen | 0.38x | 0.17x | 0.35x | **0.56x** (no meaningful gain) | 0.52x – 0.65x | -2595s |
| Intel Core i3-4020Y | Core 4th gen | 0.33x | 0.17x | 0.33x | **0.54x** (no meaningful gain) | 0.49x – 0.62x | -2878s |
| Intel Core i5-4200Y | Core 4th gen | 0.38x | 0.17x | 0.35x | **0.56x** (no meaningful gain) | 0.52x – 0.65x | -2615s |
| Intel Core i3-4012Y | Core 4th gen | 0.32x | 0.17x | 0.33x | **0.53x** (no meaningful gain) | 0.49x – 0.62x | -2913s |
| Intel Core i5-4300Y | Core 4th gen | 0.44x | 0.16x | 0.37x | **0.58x** (no meaningful gain) | 0.53x – 0.66x | -2433s |
| Intel Core i3-4010Y | Core 4th gen | 0.29x | 0.15x | 0.30x | **0.51x** (no meaningful gain) | 0.46x – 0.59x | -3249s |

## CPU and Mac inventory

1847 catalog entries · 1258 with GB6 references · 1258 comparisons · checked 2026-11-01

The cited lists cover many generations and configurations; regional and OEM omissions may remain. A listing does not verify availability. Missing or version-conflicting scores are not used for projections. CPU reference scores are not measurements of each Mac.

[CPU and Mac inventory](cpu-catalog.json) · [HTML](report.html)

## Caveats

- SYNTHETIC EXAMPLE: activity, baseline hardware and baseline scores are fictional. Target CPU references come from the attributed public dataset. These projections are not measured results or a real user's history.
- Model time is treated as fixed: it is spent on remote servers, so a faster computer does not change it.
- End to end = agent working time only (model time plus local tool time). Your own reply time is excluded.
- How much of each command category speeds up with CPU and disk is set from experience, not measured. The conservative, expected and optimistic cases use different shares, so read the range.
- Scores are compared across x86 and Apple Silicon chips. Real build and test times also depend on compiler, OS, memory bandwidth and cooling, so read the range, not the midpoint.
- If you approve commands by hand, the wait for your approval is counted as tool time. The per-command cap limits how much of it can inflate the estimate.
- Only 56m of agent working time was found. Treat the numbers as rough.

_Generated by agent-speedup-estimator 0.2.0. Transcripts are parsed locally; prompts, replies and command text are excluded from reports. Reports include activity dates and hardware details._
