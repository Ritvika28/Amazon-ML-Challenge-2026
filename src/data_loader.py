"""Data loader module for Amazon ML Challenge 2026.

Responsibility:
- Load Source 1, Source 2, Source 3, and Ground Truth datasets.
- Detect actual file schemas and types after EDA.
"""

from pathlib import Path
from typing import Any, Dict, Optional


class DataLoader:
    """Loads competition datasets safely without modifying raw files."""

    def __init__(self, raw_data_dir: Optional[Path] = None) -> None:
        """Initialize DataLoader with path to raw data directory.

        Args:
            raw_data_dir: Path to directory containing raw dataset files.
        """
        self.raw_data_dir = raw_data_dir or Path("data/raw")

    def load_source_1(self) -> Any:
        """Load Source 1 business entity set.

        Returns:
            DataFrame containing Source 1 records.
        """
        # TODO: Implement dataset loading after actual file format and schema are discovered in EDA.
        raise NotImplementedError("Source 1 loading will be implemented after EDA.")

    def load_source_2(self) -> Any:
        """Load Source 2 potential corresponding records.

        Returns:
            DataFrame containing Source 2 records.
        """
        # TODO: Implement dataset loading after actual file format and schema are discovered in EDA.
        raise NotImplementedError("Source 2 loading will be implemented after EDA.")

    def load_source_3(self) -> Any:
        """Load Source 3 potential corresponding records.

        Returns:
            DataFrame containing Source 3 records.
        """
        # TODO: Implement dataset loading after actual file format and schema are discovered in EDA.
        raise NotImplementedError("Source 3 loading will be implemented after EDA.")

    def load_ground_truth(self) -> Any:
        """Load training ground truth matches.

        Returns:
            DataFrame containing ground truth entity mappings.
        """
        # TODO: Implement ground truth loading after dataset structure is verified.
        raise NotImplementedError("Ground truth loading will be implemented after EDA.")

    def inspect_schemas(self) -> Dict[str, Any]:
        """Detect and return schemas of available raw data files.

        Returns:
            Dictionary containing detected column schemas per source.
        """
        # TODO: Automatically inspect columns and datatypes of files in data/raw/.
        return {}
