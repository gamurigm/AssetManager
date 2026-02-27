"""
PurgedKFold (purged_kfold.py)
==============================
Temporal cross-validation splitter for financial time series.

Based on: Marcos López de Prado — *Advances in Financial Machine Learning*, Chapter 7.

Key guarantees:
  1. Folds are ordered chronologically (no shuffle).
  2. A configurable **embargo** gap is removed from *both* edges of every
     train split to prevent leakage from serial autocorrelation between
     sessions that are temporally close to the test set.
  3. No data from the future leaks into any training set.

This implementation is **self-contained** — it does NOT depend on mlfinlab,
scikit-learn, pandas, or numpy at import time.  It operates purely on
the list-of-session-dicts produced by BacktestRunner._split_into_sessions().

Usage
-----
    splitter = PurgedKFoldSplitter(n_splits=5, embargo_days=5)
    for fold_idx, (train_sessions, test_sessions) in enumerate(splitter.split(all_sessions)):
        # train_sessions: sessions used to fit/evaluate parameters (in-sample)
        # test_sessions:  sessions used to score strategy (out-of-sample)
        ...

API compatibility note:
    .split() is modelled after the sklearn cross-validator API so that
    the splitter can be dropped into a GridSearchCV wrapper in the future.
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import List, Dict, Tuple, Iterator


class PurgedKFoldSplitter:
    """
    Time-series K-Fold splitter with purging and embargo.

    Parameters
    ----------
    n_splits : int
        Number of folds (K).  Each fold uses 1/K of sessions as test.
    embargo_days : int
        Number of calendar days to exclude from the *training* set on
        both sides of each test window.  Higher values = safer but less
        training data.

    Notes
    -----
    - All sessions **must** be sorted chronologically before calling split().
    - Purging is done by calendar date, not by index, to handle gaps in
      trading calendars correctly.
    """

    def __init__(self, n_splits: int = 5, embargo_days: int = 5) -> None:
        if n_splits < 2:
            raise ValueError("n_splits must be >= 2")
        if embargo_days < 0:
            raise ValueError("embargo_days must be >= 0")
        self.n_splits = n_splits
        self.embargo_days = embargo_days

    # ------------------------------------------------------------------ #
    #  Public API                                                          #
    # ------------------------------------------------------------------ #

    def split(
        self,
        sessions: List[Dict],
    ) -> Iterator[Tuple[List[Dict], List[Dict]]]:
        """
        Yield (train_sessions, test_sessions) for each fold.

        Parameters
        ----------
        sessions : list of session dicts
            Each dict must have a ``"date"`` key (``datetime.date`` or
            ISO-8601 string ``"YYYY-MM-DD"``).

        Yields
        ------
        train_sessions, test_sessions : List[Dict]
        """
        sessions = _ensure_sorted(sessions)
        n = len(sessions)

        if n < self.n_splits:
            raise ValueError(
                f"Cannot split {n} sessions into {self.n_splits} folds. "
                "Reduce n_splits or extend the date range."
            )

        # Build fold boundaries (start-inclusive, end-exclusive index ranges)
        fold_boundaries = _compute_fold_boundaries(n, self.n_splits)

        for fold_idx, (test_start_i, test_end_i) in enumerate(fold_boundaries):
            test_sessions = sessions[test_start_i:test_end_i]
            if not test_sessions:
                continue

            test_date_start: date = _to_date(test_sessions[0]["date"])
            test_date_end:   date = _to_date(test_sessions[-1]["date"])

            embargo_before = test_date_start - timedelta(days=self.embargo_days)
            embargo_after  = test_date_end   + timedelta(days=self.embargo_days)

            # A session is valid for training if it does NOT fall inside the
            # embargo window around the test period.
            train_sessions = [
                s for s in sessions
                if not (embargo_before <= _to_date(s["date"]) <= embargo_after)
            ]

            yield train_sessions, test_sessions

    def get_test_date_ranges(
        self,
        sessions: List[Dict],
    ) -> List[Tuple[date, date]]:
        """
        Utility: return (test_start, test_end) date tuples for every fold.
        Useful for logging and reporting.
        """
        sessions = _ensure_sorted(sessions)
        n = len(sessions)
        fold_boundaries = _compute_fold_boundaries(n, self.n_splits)
        ranges = []
        for test_start_i, test_end_i in fold_boundaries:
            test = sessions[test_start_i:test_end_i]
            if test:
                ranges.append(
                    (_to_date(test[0]["date"]), _to_date(test[-1]["date"]))
                )
        return ranges

    def validate_no_leakage(self, sessions: List[Dict]) -> bool:
        """
        Sanity check: asserts that no training session falls inside the
        embargo window of any test fold.  Returns True if valid; raises
        AssertionError otherwise.  Useful in tests.
        """
        for train_sessions, test_sessions in self.split(sessions):
            if not test_sessions:
                continue
            test_date_start = _to_date(test_sessions[0]["date"])
            test_date_end   = _to_date(test_sessions[-1]["date"])
            embargo_before  = test_date_start - timedelta(days=self.embargo_days)
            embargo_after   = test_date_end   + timedelta(days=self.embargo_days)
            for s in train_sessions:
                d = _to_date(s["date"])
                assert not (embargo_before <= d <= embargo_after), (
                    f"Leakage detected: training session {d} falls within "
                    f"embargo window [{embargo_before}, {embargo_after}]"
                )
        return True


# ------------------------------------------------------------------ #
#  Helpers (module-private)                                           #
# ------------------------------------------------------------------ #

def _to_date(value) -> date:
    """Coerce date or ISO string to datetime.date."""
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value)[:10])


def _ensure_sorted(sessions: List[Dict]) -> List[Dict]:
    """Return sessions sorted by date (ascending). Does not mutate input."""
    return sorted(sessions, key=lambda s: _to_date(s["date"]))


def _compute_fold_boundaries(n: int, k: int) -> List[Tuple[int, int]]:
    """
    Split n items into k folds as evenly as possible.
    Returns list of (start_inclusive, end_exclusive) index tuples.
    Extra items are distributed to the first folds.
    """
    base_size, remainder = divmod(n, k)
    boundaries = []
    start = 0
    for i in range(k):
        size = base_size + (1 if i < remainder else 0)
        end = start + size
        boundaries.append((start, end))
        start = end
    return boundaries
