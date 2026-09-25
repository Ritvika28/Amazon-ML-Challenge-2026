"""Unit tests for feature extraction module."""

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


from src.features import FeatureExtractor


def test_feature_extractor_init() -> None:
    """Test FeatureExtractor initialization."""
    extractor = FeatureExtractor()
    assert extractor.feature_configs == []


@skip_pending(reason="Pending feature definition after EDA")
def test_compute_name_similarities() -> None:
    """Test pairwise name similarity feature computation."""
    extractor = FeatureExtractor()
    scores = extractor.compute_name_similarities("Company A", "Company A")
    assert isinstance(scores, dict)
