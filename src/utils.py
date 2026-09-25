"""Shared utility functions module for Amazon ML Challenge 2026.

Responsibility:
- Set global random seeds for deterministic reproducibility.
- Configure logging handlers and formatters.
- Provide general path and environment helpers.
"""

import logging
import random
from pathlib import Path
from typing import Optional

try:
    import numpy as np  # type: ignore
except ImportError:
    np = None


def set_seed(seed: int = 42) -> None:
    """Set random seeds across standard library and scientific computing libraries.

    Args:
        seed: Integer random seed value.
    """
    random.seed(seed)
    if np is not None:
        np.random.seed(seed)
    # TODO: Add torch/framework seed settings if neural models are adopted.


def setup_logger(name: str = "amazon_ml_2026", log_file: Optional[Path] = None, level: int = logging.INFO) -> logging.Logger:
    """Configure and return a standardized logger instance.

    Args:
        name: Logger name identifier.
        log_file: Optional path to log file.
        level: Logging verbosity level.

    Returns:
        Configured Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
