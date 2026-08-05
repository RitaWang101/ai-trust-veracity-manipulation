from __future__ import annotations

import argparse
from pathlib import Path

from .scoring import run, write_scores


def main() -> None:
    parser = argparse.ArgumentParser(description="Score AI Trust Lab model responses")
    parser.add_argument("--prompts", type=Path, required=True)
    parser.add_argument("--responses", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("results/scores.csv"))
    args = parser.parse_args()
    scores = run(args.prompts, args.responses)
    write_scores(scores, args.output)
    complete = [score.final_score for score in scores if score.final_score is not None]
    print(f"Wrote {len(scores)} rows to {args.output}")
    print("Aggregate: NOT_RUN" if not complete else f"Aggregate: {sum(complete) / len(complete):.2f}")


if __name__ == "__main__":
    main()

