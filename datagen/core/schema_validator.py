from __future__ import annotations

from datagen.core.exceptions import SchemaValidationError
from datagen.core.registry import build_default_registry
from datagen.models.schema import DatasetSchema


def validate_schema(schema: DatasetSchema) -> DatasetSchema:
    if schema.rows < 1:
        raise SchemaValidationError("'rows' must be greater than 0.")

    if not schema.columns:
        raise SchemaValidationError("At least one column is required.")

    seen = set()
    registry = build_default_registry()

    for column in schema.columns:
        if not column.name.strip():
            raise SchemaValidationError("Column names cannot be empty.")
        lowered = column.name.lower()
        if lowered in seen:
            raise SchemaValidationError(f"Duplicate column name '{column.name}'.")
        seen.add(lowered)
        registry.get(column.generator)

        if column.generator in {"choice", "category"} and not column.params.get("choices"):
            raise SchemaValidationError(f"Column '{column.name}' requires non-empty 'choices'.")

    return schema
