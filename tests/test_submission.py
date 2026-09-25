"""Unit tests for submission generation module."""

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


from src.submission import SubmissionGenerator


def test_submission_generator_init() -> None:
    """Test SubmissionGenerator initialization."""
    generator = SubmissionGenerator()
    assert generator.output_dir.name == "predictions"


@skip_pending(reason="Pending official submission schema validation criteria")
def test_validate_submission_format() -> None:
    """Test submission schema validation logic."""
    generator = SubmissionGenerator()
    assert generator.validate_submission_format(None) is True
