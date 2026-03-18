from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Iterable, List

from datagen.core.defaults import DEFAULT_SCHEMA, NAME_HINTS, get_default_generator_params
from datagen.models.column import ColumnSchema
from datagen.models.config import GenerationConfig
from datagen.models.schema import DatasetSchema


def _normalize_column_name(raw_name: str) -> str:
    return raw_name.strip()


def _name_key(column_name: str) -> str:
    return column_name.strip().lower().replace(" ", "_")


def _infer_column_defaults(column_name: str) -> Dict[str, Any]:
    key = _name_key(column_name)
    exact_match = NAME_HINTS.get(key)
    if exact_match:
        return deepcopy(exact_match)

    for hint_key in sorted(NAME_HINTS, key=len, reverse=True):
        if key.endswith(hint_key) or f"_{hint_key}_" in f"_{key}_":
            return deepcopy(NAME_HINTS[hint_key])

    return {"generator": "text", "dtype": "string"}


def _normalize_columns(columns: Iterable[Any]) -> List[ColumnSchema]:
    normalized_columns: List[ColumnSchema] = []

    for raw_column in columns:
        if isinstance(raw_column, str):
            raw_column = {"name": raw_column}

        column_name = _normalize_column_name(str(raw_column.get("name", "column")))
        inferred = _infer_column_defaults(column_name)
        generator_name = raw_column.get("generator") or raw_column.get("type") or inferred["generator"]
        params = get_default_generator_params(generator_name)
        params.update(raw_column.get("params", {}))

        normalized_columns.append(
            ColumnSchema(
                name=column_name,
                generator=generator_name,
                dtype=raw_column.get("dtype", inferred.get("dtype", "string")),
                nullable=bool(raw_column.get("nullable", False)),
                unique=bool(raw_column.get("unique", False)),
                description=raw_column.get("description"),
                params=params,
            )
        )

    return normalized_columns


def normalize_schema(schema_dict: Dict[str, Any]) -> DatasetSchema:
    merged = deepcopy(DEFAULT_SCHEMA)
    merged.update({k: v for k, v in schema_dict.items() if k != "config"})
    merged["config"].update(schema_dict.get("config") or {})

    config = GenerationConfig.from_dict(merged["config"])
    columns = _normalize_columns(merged.get("columns") or DEFAULT_SCHEMA["columns"])

    return DatasetSchema(
        name=merged.get("name", DEFAULT_SCHEMA["name"]),
        rows=int(merged.get("rows", DEFAULT_SCHEMA["rows"])),
        columns=columns,
        config=config,
    )
