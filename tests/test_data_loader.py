"""Unit tests for data loader module."""

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


from src.data_loader import DataLoader


def test_data_loader_init() -> None:
    """Test DataLoader initialization."""
    loader = DataLoader()
    assert loader.raw_data_dir.name == "raw"


@skip_pending(reason="Pending competition dataset placement in data/raw/")
def test_load_source_1() -> None:
    """Test loading Source 1 dataset."""
    loader = DataLoader()
    df = loader.load_source_1()
    assert df is not None
