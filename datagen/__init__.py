"""DataGen CLI package."""

from typing import Any

__all__ = ["DataGenerationEngine", "DatasetSchema", "generate_dataset"]
__version__ = "0.2.0"


def __getattr__(name: str) -> Any:
    if name in {"DataGenerationEngine", "generate_dataset"}:
        from datagen.core.engine import DataGenerationEngine, generate_dataset

        exports = {
            "DataGenerationEngine": DataGenerationEngine,
            "generate_dataset": generate_dataset,
        }
        return exports[name]

    if name == "DatasetSchema":
        from datagen.models.schema import DatasetSchema

        return DatasetSchema

    raise AttributeError(f"module 'datagen' has no attribute '{name}'")
