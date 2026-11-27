#!/usr/bin/env python3
"""Pull a sanitised inventory from the CPM scenario runtime and render the map.

This is an explicit local bridge between the private CPM checkout and the
public app-downloads checkout.  It never copies prompts, model output,
credentials or receipts; only the runtime's machine-readable inventory is
passed to the deterministic renderer.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import generate_jarvis_capability_map as renderer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cpm-root", required=True, help="lokální checkout codex-private-memory")
    parser.add_argument("--state", required=True, help="sanitizovaný scenario-state ledger")
    parser.add_argument("--scenario-runtime", help="override cesty k scenario_pyramid_runtime.py")
    parser.add_argument("--check", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cpm_root = Path(args.cpm_root).resolve()
    runtime = Path(args.scenario_runtime) if args.scenario_runtime else cpm_root / "tools/jarvis/tools/scenario_pyramid_runtime.py"
    state = Path(args.state).resolve()
    if not runtime.exists():
        raise SystemExit(f"Scenario runtime neexistuje: {runtime}")
    command = [
        sys.executable,
        str(runtime),
        "--repo-root",
        str(cpm_root),
        "--state",
        str(state),
        "inventory",
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        sys.stderr.write(completed.stderr)
        return completed.returncode
    try:
        inventory = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Scenario runtime vrátil neplatný inventory JSON: {exc}")
    with tempfile.TemporaryDirectory(prefix="jarvis-capability-inventory-") as temporary:
        inventory_path = Path(temporary) / "inventory.json"
        inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, sort_keys=True), encoding="utf-8")
        renderer_args = ["--inventory", str(inventory_path)]
        if args.check:
            renderer_args.append("--check")
        return renderer.main(renderer_args)


if __name__ == "__main__":
    raise SystemExit(main())
