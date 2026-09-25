"""Unit tests for evaluation metrics module."""

import sys
from pathlib import Path

# Add project root to sys.path for IDE and test runner import resolution
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    import pytest  # type: ignore
except ImportError:
    pytest = None  # type: ignore

def skip_pending(reason: str):
    """Decorator helper that safely handles missing pytest before package installation."""
    if pytest is not None:
        return pytest.mark.skip(reason=reason)
    return lambda func: func


from src.evaluation import Evaluator, calculate_f_beta


def test_calculate_f_beta() -> None:
    """Test F0.5 score calculation with precision=1.0, recall=0.5."""
    score = calculate_f_beta(precision=1.0, recall=0.5, beta=0.5)
    # F0.5 = (1 + 0.25) * (1.0 * 0.5) / (0.25 * 1.0 + 0.5) = 1.25 * 0.5 / 0.75 = 0.8333...
    assert round(score, 4) == 0.8333


def test_calculate_f_beta_zero() -> None:
    """Test F-beta calculation when precision and recall are zero."""
    score = calculate_f_beta(precision=0.0, recall=0.0, beta=0.5)
    assert score == 0.0


def test_evaluator_init() -> None:
    """Test Evaluator initialization."""
    evaluator = Evaluator(beta=0.5)
    assert evaluator.beta == 0.5
