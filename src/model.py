"""Model wrapper and interface module for Amazon ML Challenge 2026.

Responsibility:
- Define a unified model interface for training, prediction, and probability estimation.
- Maintain modularity to support evaluating multiple model families (e.g., LightGBM, XGBoost, CatBoost, Neural networks).
- Handle model saving, loading, and artifact persistence.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional


class BaseModelWrapper(ABC):
    """Abstract base class interface for entity resolution matching models."""

    @abstractmethod
    def fit(self, X: Any, y: Any, **kwargs: Any) -> "BaseModelWrapper":
        """Fit model on feature matrix X and targets y.

        Args:
            X: Feature matrix.
            y: Binary match labels.

        Returns:
            Self instance.
        """
        pass

    @abstractmethod
    def predict_proba(self, X: Any) -> Any:
        """Predict match probability scores for candidates.

        Args:
            X: Feature matrix.

        Returns:
            Array-like match probabilities.
        """
        pass

    @abstractmethod
    def save(self, filepath: Path) -> None:
        """Save serialized model artifact to disk.

        Args:
            filepath: Destination file path for saved model.
        """
        pass

    @abstractmethod
    def load(self, filepath: Path) -> "BaseModelWrapper":
        """Load serialized model artifact from disk.

        Args:
            filepath: Source file path.

        Returns:
            Loaded model wrapper instance.
        """
        pass


class MatchClassifierWrapper(BaseModelWrapper):
    """Modular wrapper around underlying classifier implementations."""

    def __init__(self, model_name: str = "lgbm", model_params: Optional[Dict[str, Any]] = None) -> None:
        """Initialize classifier wrapper with specified model type and parameters.

        Args:
            model_name: Name of model algorithm ('lgbm', 'xgboost', 'catboost').
            model_params: Dictionary of hyperparameters.
        """
        self.model_name = model_name
        self.model_params = model_params or {}
        self.model: Any = None

    def fit(self, X: Any, y: Any, **kwargs: Any) -> "MatchClassifierWrapper":
        """Fit underlying model on training data.

        Args:
            X: Training feature matrix.
            y: Binary target labels.

        Returns:
            Self instance.
        """
        # TODO: Instantiate and fit target model algorithm.
        raise NotImplementedError("Model fitting will be implemented after dataset creation.")

    def predict_proba(self, X: Any) -> Any:
        """Estimate pairwise match probabilities.

        Args:
            X: Feature matrix.

        Returns:
            Predicted match probability array.
        """
        # TODO: Implement inference call on underlying model.
        raise NotImplementedError("Probability prediction will be implemented after training.")

    def save(self, filepath: Path) -> None:
        """Persist model state to file.

        Args:
            filepath: Path to output model file.
        """
        # TODO: Implement model serialization.
        pass

    def load(self, filepath: Path) -> "MatchClassifierWrapper":
        """Load persisted model state from file.

        Args:
            filepath: Path to model file.

        Returns:
            Loaded MatchClassifierWrapper instance.
        """
        # TODO: Implement model deserialization.
        return self
