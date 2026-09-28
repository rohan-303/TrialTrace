from __future__ import annotations

import argparse
import json
from pathlib import Path

from trialtrace.prototype import generate_prototype, heuristic_sanity, source_manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the bounded TrialTrace EI feasibility prototype")
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=64)
    parser.add_argument("--seed", type=int, default=17)
    args = parser.parse_args()
    summary = generate_prototype(args.data_root, args.output, args.limit, args.seed)
    summary["heuristic"] = heuristic_sanity(args.output)
    source_manifest([args.data_root / "annotations_merged.csv", args.data_root / "prompts_merged.csv"], args.manifest)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
