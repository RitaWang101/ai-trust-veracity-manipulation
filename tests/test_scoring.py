from pathlib import Path

import pytest

from ai_trust_eval.scoring import combine, heuristic_score, run


def test_veracity_weighting():
    assert combine("veracity", 80, 60) == (70.0, "COMPLETE")


def test_manipulation_weighting():
    assert combine("manipulation", 80, 60) == (65.0, "COMPLETE")


def test_missing_judge_is_not_run():
    assert combine("veracity", 100, None) == (None, "NOT_RUN")


def test_lexical_baseline_records_evidence():
    score, evidence = heuristic_score("The answer is George Washington.", "George Washington", "")
    assert score == 100
    assert "george washington" in evidence


def test_invalid_judge_score():
    with pytest.raises(ValueError):
        combine("veracity", 50, 101)


def test_templates_run_without_fabricating_results():
    root = Path(__file__).parents[1]
    rows = run(root / "data/prompts.csv", root / "data/responses_template.csv")
    assert len(rows) == 25
    assert all(row.status == "NOT_RUN" for row in rows)
    assert all(row.final_score is None for row in rows)

