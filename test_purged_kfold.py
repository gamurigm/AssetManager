"""
test_purged_kfold.py
=====================
Unit tests for PurgedKFoldSplitter — fully offline, no data fetch required.

Run with:
    python c:\\AssetManager\\test_purged_kfold.py
"""

import sys
import os
from datetime import date, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from app.agents.strategies.engine.purged_kfold import PurgedKFoldSplitter, _to_date

# ------------------------------------------------------------------ #
#  Helpers
# ------------------------------------------------------------------ #

def make_sessions(start: date, n_days: int):
    """Generate n_days trading sessions (Mon-Fri only, skipping weekends)."""
    sessions = []
    current = start
    added = 0
    while added < n_days:
        if current.weekday() < 5:  # Mon–Fri
            sessions.append({"date": current, "m5": [], "m1": []})
            added += 1
        current += timedelta(days=1)
    return sessions


def assert_no_leakage(splitter: PurgedKFoldSplitter, sessions):
    """Assert no train session falls within the embargo window of any test fold."""
    for train, test in splitter.split(sessions):
        if not test:
            continue
        t_start = _to_date(test[0]["date"])
        t_end   = _to_date(test[-1]["date"])
        embargo_lo = t_start - timedelta(days=splitter.embargo_days)
        embargo_hi = t_end   + timedelta(days=splitter.embargo_days)
        for s in train:
            d = _to_date(s["date"])
            assert not (embargo_lo <= d <= embargo_hi), (
                f"LEAKAGE: train session {d} is inside embargo [{embargo_lo}, {embargo_hi}]"
            )


def assert_test_folds_cover_all(splitter: PurgedKFoldSplitter, sessions):
    """Assert the union of all test folds covers every session exactly once."""
    all_test_dates = set()
    for _, test in splitter.split(sessions):
        for s in test:
            d = _to_date(s["date"])
            assert d not in all_test_dates, f"OVERLAP: date {d} appears in multiple test folds"
            all_test_dates.add(d)

    all_dates = {_to_date(s["date"]) for s in sessions}
    assert all_test_dates == all_dates, (
        f"INCOMPLETE COVERAGE: {len(all_dates) - len(all_test_dates)} sessions not in any test fold"
    )


def assert_test_folds_chronological(splitter: PurgedKFoldSplitter, sessions):
    """Assert test folds are in ascending chronological order and non-overlapping."""
    prev_end = None
    for _, test in splitter.split(sessions):
        if not test:
            continue
        t_start = _to_date(test[0]["date"])
        t_end   = _to_date(test[-1]["date"])
        assert t_start <= t_end, f"Test fold is not sorted: {t_start} > {t_end}"
        if prev_end is not None:
            assert t_start > prev_end, (
                f"Test folds overlap or are not ordered: {t_start} <= {prev_end}"
            )
        prev_end = t_end


# ------------------------------------------------------------------ #
#  Tests
# ------------------------------------------------------------------ #

def test_basic_5fold():
    """Standard 5-fold with 100 trading days and 5-day embargo."""
    sessions = make_sessions(date(2024, 1, 2), 100)
    splitter = PurgedKFoldSplitter(n_splits=5, embargo_days=5)
    folds = list(splitter.split(sessions))
    assert len(folds) == 5, f"Expected 5 folds, got {len(folds)}"
    print(f"  [OK] 5 folds generated")


def test_no_leakage_embargo_5():
    """No training session falls inside the 5-day embargo window."""
    sessions = make_sessions(date(2024, 1, 2), 100)
    splitter = PurgedKFoldSplitter(n_splits=5, embargo_days=5)
    assert_no_leakage(splitter, sessions)
    print(f"  [OK] No leakage (embargo=5)")


def test_no_leakage_embargo_0():
    """With embargo=0 there is still no leakage (test sessions excluded from train)."""
    sessions = make_sessions(date(2024, 1, 2), 60)
    splitter = PurgedKFoldSplitter(n_splits=4, embargo_days=0)
    assert_no_leakage(splitter, sessions)
    print(f"  [OK] No leakage (embargo=0)")


def test_test_folds_cover_all_sessions():
    """Union of test folds must be exactly the full session set."""
    sessions = make_sessions(date(2024, 1, 2), 80)
    splitter = PurgedKFoldSplitter(n_splits=4, embargo_days=3)
    assert_test_folds_cover_all(splitter, sessions)
    print(f"  [OK] Test folds cover 100% of sessions with no overlap")


def test_folds_chronological():
    """Test folds must be ordered chronologically and non-overlapping."""
    sessions = make_sessions(date(2024, 1, 2), 100)
    splitter = PurgedKFoldSplitter(n_splits=5, embargo_days=5)
    assert_test_folds_chronological(splitter, sessions)
    print(f"  [OK] Folds are chronologically ordered")


def test_train_smaller_than_full_set():
    """Training set should be smaller than the full session list (embargo removes some)."""
    sessions = make_sessions(date(2024, 1, 2), 60)
    splitter = PurgedKFoldSplitter(n_splits=3, embargo_days=10)
    for i, (train, test) in enumerate(splitter.split(sessions)):
        assert len(train) < len(sessions), (
            f"Fold {i}: train set == full set, embargo has no effect"
        )
        assert len(train) + len(test) <= len(sessions)
    print(f"  [OK] Embargo correctly reduces train set size")


def test_string_dates():
    """Dates can be ISO strings, not just datetime.date objects."""
    sessions = [
        {"date": "2024-01-02", "m5": [], "m1": []},
        {"date": "2024-01-03", "m5": [], "m1": []},
        {"date": "2024-01-04", "m5": [], "m1": []},
        {"date": "2024-01-05", "m5": [], "m1": []},
        {"date": "2024-01-08", "m5": [], "m1": []},
        {"date": "2024-01-09", "m5": [], "m1": []},
        {"date": "2024-01-10", "m5": [], "m1": []},
        {"date": "2024-01-11", "m5": [], "m1": []},
    ]
    splitter = PurgedKFoldSplitter(n_splits=2, embargo_days=1)
    folds = list(splitter.split(sessions))
    assert len(folds) == 2
    assert_no_leakage(splitter, sessions)
    print(f"  [OK] ISO string dates handled correctly")


def test_validate_no_leakage_helper():
    """The built-in validate_no_leakage() method returns True on valid splits."""
    sessions = make_sessions(date(2024, 1, 2), 50)
    splitter = PurgedKFoldSplitter(n_splits=5, embargo_days=3)
    result = splitter.validate_no_leakage(sessions)
    assert result is True
    print(f"  [OK] validate_no_leakage() returned True")


def test_fold_sizes_approximately_equal():
    """Folds should be as equal in size as possible."""
    sessions = make_sessions(date(2024, 1, 2), 100)
    splitter = PurgedKFoldSplitter(n_splits=5, embargo_days=0)
    test_sizes = [len(test) for _, test in splitter.split(sessions)]
    assert max(test_sizes) - min(test_sizes) <= 1, (
        f"Fold sizes too unequal: {test_sizes}"
    )
    print(f"  [OK] Fold sizes balanced: {test_sizes}")


# ------------------------------------------------------------------ #
#  Runner
# ------------------------------------------------------------------ #

TESTS = [
    test_basic_5fold,
    test_no_leakage_embargo_5,
    test_no_leakage_embargo_0,
    test_test_folds_cover_all_sessions,
    test_folds_chronological,
    test_train_smaller_than_full_set,
    test_string_dates,
    test_validate_no_leakage_helper,
    test_fold_sizes_approximately_equal,
]

if __name__ == "__main__":
    passed = 0
    failed = 0
    print("=" * 60)
    print("PurgedKFoldSplitter — Unit Tests")
    print("=" * 60)
    for test_fn in TESTS:
        name = test_fn.__name__
        try:
            print(f"\n→ {name}")
            test_fn()
            passed += 1
        except AssertionError as e:
            print(f"  [FAIL] {e}")
            failed += 1
        except Exception as e:
            print(f"  [ERROR] {type(e).__name__}: {e}")
            failed += 1

    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    sys.exit(0 if failed == 0 else 1)
