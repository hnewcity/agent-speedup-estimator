# Contributing

Small, focused pull requests are welcome. Explain the observed problem and the behavior after your change.

## Run locally

Use Python 3.9 or newer. From the repository root:

```bash
python -m unittest discover -s skills/agent-speedup-estimator/tests -v
python skills/agent-speedup-estimator/scripts/agent_speedup.py --help
```

Python 3.14 exercises standard-library Zstandard support. The analyzer itself has no required third-party dependencies.

## Changes that help

- **Adapters:** return `SessionTiming` objects from a parser under `scripts/aspeed/adapters/`, wire discovery into the CLI, and include synthetic fixtures for the timing schema.
- **Classification:** add a rule and a representative command test. Only allowlisted command families may reach report output.
- **CPU data:** include a verifiable source URL and the exact chip variant. Do not put invented or extrapolated scores in `cpu_scores.json`; documented proxies belong in `proxies.json`.
- **Sensitivity assumptions:** explain the workload evidence. CPU and disk shares must stay in `[0, 1]`, sum to at most 1 in every scenario, and include three scenarios plus a valid `mt` weight.
- **Translations:** keep language navigation and CLI commands consistent across `README.md` and `docs/README.*.md`. README translations do not imply additional report languages.

Keep reports and tests free of real conversations, credentials, command arguments, personal paths and session identifiers. Reproduce issues with synthetic records. Run `python examples/generate_demo.py` after changing report output and inspect the resulting HTML before committing it.
