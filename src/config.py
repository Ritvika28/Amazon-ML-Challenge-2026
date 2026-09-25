"""Configuration management module for Amazon ML Challenge 2026.

This module provides path definitions and project settings loaded from configuration files.
"""

from pathlib import Path
from typing import Any, Dict, Optional


class Config:
    """Project configuration and path manager."""

    # Project root directory
    ROOT_DIR: Path = Path(__file__).resolve().parent.parent

    # Standard data directories
    DATA_DIR: Path = ROOT_DIR / "data"
    RAW_DATA_DIR: Path = DATA_DIR / "raw"
    PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"

    # Models and outputs directories
    MODELS_DIR: Path = ROOT_DIR / "models"
    OUTPUTS_DIR: Path = ROOT_DIR / "outputs"
    PREDICTIONS_DIR: Path = OUTPUTS_DIR / "predictions"
    CANDIDATES_DIR: Path = OUTPUTS_DIR / "candidates"
    VALIDATION_DIR: Path = OUTPUTS_DIR / "validation"

    # Config directory
    CONFIGS_DIR: Path = ROOT_DIR / "configs"
    DEFAULT_CONFIG_PATH: Path = CONFIGS_DIR / "config.yaml"

    def __init__(self, config_path: Optional[Path] = None) -> None:
        """Initialize configuration with an optional YAML config path.

        Args:
            config_path: Optional custom path to a YAML configuration file.
        """
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        self._config_data: Dict[str, Any] = {}

    def load_config(self) -> Dict[str, Any]:
        """Load YAML configuration settings into memory.

        Returns:
            Dict containing configuration options.
        """
        # TODO: Implement PyYAML config file parsing once config.yaml schema is finalized after EDA.
        return self._config_data
