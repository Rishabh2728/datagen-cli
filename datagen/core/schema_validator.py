from __future__ import annotations

from datetime import datetime

from datagen.core.defaults import SUPPORTED_DTYPES
from datagen.core.exceptions import SchemaValidationError
from datagen.core.registry import build_default_registry
from datagen.models.schema import DatasetSchema


def _validate_numeric_bounds(generator_name: str, params: dict, column_name: str) -> None:
    if generator_name not in {"int", "float", "age", "latitude", "longitude"}:
        return

    minimum = params.get("min")
    maximum = params.get("max")
    if minimum is not None and maximum is not None and minimum > maximum:
        raise SchemaValidationError(f"Column '{column_name}' has min greater than max.")


def _validate_precision(generator_name: str, params: dict, column_name: str) -> None:
    if generator_name not in {"float", "latitude", "longitude"}:
        return

    if "precision" not in params:
        return

    precision = params["precision"]
    if isinstance(precision, bool) or not isinstance(precision, int) or precision <= 0:
        raise SchemaValidationError(f"Column '{column_name}' must use a positive integer precision.")


def _parse_temporal(generator_name: str, value: str) -> datetime:
    if generator_name == "date":
        if value == "today":
            return datetime.combine(datetime.today().date(), datetime.min.time())
        return datetime.combine(datetime.fromisoformat(value).date(), datetime.min.time())

    if value == "now":
        return datetime.now()
    return datetime.fromisoformat(value)


def _validate_temporal_bounds(generator_name: str, params: dict, column_name: str) -> None:
    if generator_name not in {"date", "datetime"}:
        return

    start = _parse_temporal(generator_name, str(params.get("start", "2020-01-01" if generator_name == "date" else "2020-01-01T00:00:00")))
    end = _parse_temporal(generator_name, str(params.get("end", "today" if generator_name == "date" else "now")))
    if start > end:
        raise SchemaValidationError(f"Column '{column_name}' has start later than end.")


def _validate_choices(generator_name: str, params: dict, column_name: str) -> None:
    if generator_name not in {"choice", "category"}:
        return

    choices = params.get("choices")
    if not isinstance(choices, list) or not choices:
        raise SchemaValidationError(f"Column '{column_name}' requires non-empty list 'choices'.")


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
        if column.dtype not in SUPPORTED_DTYPES:
            raise SchemaValidationError(f"Column '{column.name}' uses unsupported dtype '{column.dtype}'.")

        _validate_numeric_bounds(column.generator, column.params, column.name)
        _validate_precision(column.generator, column.params, column.name)
        _validate_temporal_bounds(column.generator, column.params, column.name)
        _validate_choices(column.generator, column.params, column.name)

    return schema
