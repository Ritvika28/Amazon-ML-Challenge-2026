"""Unit tests for text normalization module."""

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


from src.normalization import Normalizer


def test_normalizer_init() -> None:
    """Test Normalizer initialization."""
    normalizer = Normalizer()
    assert normalizer is not None


def test_normalize_name_placeholder() -> None:
    """Test basic whitespace trimming and lowercasing."""
    normalizer = Normalizer()
    result = normalizer.normalize_name("  Test Business Inc. ")
    assert result == "test business inc."


@skip_pending(reason="Pending EDA discovery of domain-specific text patterns")
def test_advanced_name_normalization() -> None:
    """Test advanced normalization rules after EDA."""
    pass
