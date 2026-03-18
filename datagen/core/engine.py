from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd

from datagen.core.registry import build_default_registry
from datagen.core.schema_loader import SchemaInput, load_schema
from datagen.core.schema_normalizer import normalize_schema
from datagen.core.schema_validator import validate_schema
from datagen.exporters.manager import ExportManager
from datagen.generators.base import GenerationContext
from datagen.models.schema import DatasetSchema


class DataGenerationEngine:
    def __init__(self) -> None:
        self.registry = build_default_registry()
        self.export_manager = ExportManager()

    def prepare_schema(self, schema_input: SchemaInput, rows: Optional[int] = None) -> DatasetSchema:
        loaded = load_schema(schema_input)
        if rows is not None:
            loaded = dict(loaded)
            loaded["rows"] = rows
        normalized = normalize_schema(loaded)
        return validate_schema(normalized)

    def generate(self, schema_input: SchemaInput, rows: Optional[int] = None) -> pd.DataFrame:
        schema = self.prepare_schema(schema_input, rows=rows)
        context = GenerationContext.from_schema(schema)
        frame_data: Dict[str, Any] = {}

        for column in schema.columns:
            generator = self.registry.get(column.generator)
            frame_data[column.name] = generator.generate(column=column, rows=schema.rows, context=context)

        return pd.DataFrame(frame_data)

    def export(
        self,
        dataframe: pd.DataFrame,
        output_path: Path | str,
        file_format: Optional[str] = None,
        schema: Optional[DatasetSchema] = None,
    ) -> Path:
        return self.export_manager.export(
            dataframe=dataframe,
            output_path=Path(output_path),
            file_format=file_format or (schema.config.output_format if schema else None),
            sheet_name=schema.config.sheet_name if schema else None,
        )


def generate_dataset(schema_input: SchemaInput, rows: Optional[int] = None) -> pd.DataFrame:
    engine = DataGenerationEngine()
    return engine.generate(schema_input, rows=rows)
