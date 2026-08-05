# AI Trust Lab: Veracity & Manipulation Evaluation

Reproducible, GitHub-ready prototype for Rita Wang's USC AI Trust Lab contribution. It converts the recovered methodology and prompt review into an executable evaluation pipeline without inventing experimental findings.

## What is included

- 14 Veracity prompts and 11 Manipulation prompts with provenance and review status
- two-layer Manipulation design: User-to-Model and Model-to-User
- transparent lexical heuristic plus rubric-based judge input
- pillar-specific hybrid weighting
- strict `NOT_RUN` handling for missing judge/model results
- offline unit tests and GitHub Actions CI
- response and result templates for the pilot

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q
ai-trust-eval \
  --prompts data/prompts.csv \
  --responses data/responses_template.csv \
  --output results/scores.csv
```

The template run prints `Aggregate: NOT_RUN`. This is intentional: no real model responses or judge scores have been supplied.

## Run a real pilot

1. Copy `data/responses_template.csv` and retain one row per prompt and model.
2. Add the exact model response, model/version, and evaluation timestamp.
3. Apply the relevant rubric in `rubrics/` using a documented LLM judge or blinded human raters.
4. Enter a 0–100 `judge_score` and short `judge_rationale`.
5. Run the CLI and retain the generated row-level results.
6. Report model-level aggregates only after reviewing missing values and failure cases.

## Scoring

| Pillar | Heuristic | Rubric judge |
|---|---:|---:|
| Veracity | 50% | 50% |
| Manipulation | 25% | 75% |

The heuristic checks auditable required/prohibited concepts. It is deliberately simple and should not be presented as a complete semantic evaluator. See `docs/methodology.md` for definitions, limitations, and validation requirements.

## Research status

Methodology and implementation are complete as a prototype. Real multi-model pilot execution, judge calibration, inter-rater validation, and empirical results remain pending. Example or blank rows must never be reported as observed model performance.

## Repository map

```text
ai_trust_eval/       scoring library and CLI
data/                prompt set and response template
rubrics/             judge instructions
docs/                methodology and validation notes
tests/               offline reproducibility tests
.github/workflows/   continuous integration
```

## Source basis

Prepared from the AI Trust Lab Pillar Methodology Guide, the recovered prompt-review document, the paper's Section 6 request, and the team's stated hybrid-scoring design. Prompt statuses preserve `validated`, `reconstructed`, and `lab_authored` distinctions.

