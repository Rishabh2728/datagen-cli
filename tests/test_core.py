from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from datagen import generate_dataset
from datagen.core.engine import DataGenerationEngine
from datagen.core.exceptions import GeneratorNotFoundError, SchemaLoadError, SchemaValidationError
from datagen.core.schema_loader import load_schema
from datagen.core.schema_normalizer import normalize_schema
from datagen.core.schema_validator import validate_schema
from datagen.models.column import ColumnSchema
from datagen.models.config import GenerationConfig
from datagen.models.schema import DatasetSchema


class SchemaLoaderTests(unittest.TestCase):
    def test_load_schema_from_dict_returns_same_payload(self) -> None:
        payload = {"rows": 2, "columns": ["name"]}
        self.assertEqual(load_schema(payload), payload)

    def test_load_schema_from_valid_json_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "schema.json"
            payload = {"rows": 2, "columns": ["name"]}
            path.write_text(json.dumps(payload), encoding="utf-8")

            self.assertEqual(load_schema(path), payload)

    def test_load_schema_missing_file_raises(self) -> None:
        with self.assertRaises(SchemaLoadError):
            load_schema("missing_schema.json")

    def test_load_schema_invalid_json_raises(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "schema.json"
            path.write_text("{invalid", encoding="utf-8")

            with self.assertRaises(SchemaLoadError):
                load_schema(path)


class SchemaNormalizationTests(unittest.TestCase):
    def test_default_schema_merge_applies_defaults(self) -> None:
        schema = normalize_schema({})

        self.assertEqual(schema.name, "generated_dataset")
        self.assertEqual(schema.rows, 100)
        self.assertEqual([column.name for column in schema.columns], ["id", "name", "email"])

    def test_name_based_generator_inference(self) -> None:
        schema = normalize_schema({"columns": ["customer_email", "signup_date"]})

        self.assertEqual(schema.columns[0].generator, "email")
        self.assertEqual(schema.columns[1].generator, "date")

    def test_fallback_column_naming_is_unique(self) -> None:
        schema = normalize_schema({"columns": [{}, {"name": ""}, {"name": "column_1"}]})

        self.assertEqual([column.name for column in schema.columns], ["column_1", "column_2", "column_1"])

    def test_param_merging_keeps_defaults_and_user_values(self) -> None:
        schema = normalize_schema(
            {
                "columns": [
                    {
                        "name": "price",
                        "generator": "float",
                        "params": {"min": 10.5, "max": 20.5, "precision": 4},
                    }
                ]
            }
        )

        params = schema.columns[0].params
        self.assertEqual(params["min"], 10.5)
        self.assertEqual(params["max"], 20.5)
        self.assertEqual(params["precision"], 4)


class SchemaValidationTests(unittest.TestCase):
    def test_rows_must_be_positive(self) -> None:
        schema = DatasetSchema(name="bad", rows=0, columns=[ColumnSchema(name="name")])
        with self.assertRaises(SchemaValidationError):
            validate_schema(schema)

    def test_empty_column_names_are_rejected(self) -> None:
        schema = DatasetSchema(name="bad", rows=1, columns=[ColumnSchema(name=" ")])
        with self.assertRaises(SchemaValidationError):
            validate_schema(schema)

    def test_duplicate_column_names_are_rejected(self) -> None:
        schema = DatasetSchema(
            name="bad",
            rows=1,
            columns=[ColumnSchema(name="name"), ColumnSchema(name="Name")],
        )
        with self.assertRaises(SchemaValidationError):
            validate_schema(schema)

    def test_unknown_generators_are_rejected(self) -> None:
        schema = DatasetSchema(name="bad", rows=1, columns=[ColumnSchema(name="name", generator="unknown")])
        with self.assertRaises(GeneratorNotFoundError):
            validate_schema(schema)

    def test_invalid_numeric_ranges_are_rejected(self) -> None:
        schema = DatasetSchema(
            name="bad",
            rows=1,
            columns=[ColumnSchema(name="age", generator="int", dtype="int", params={"min": 10, "max": 5})],
        )
        with self.assertRaises(SchemaValidationError):
            validate_schema(schema)

    def test_invalid_precision_is_rejected(self) -> None:
        schema = DatasetSchema(
            name="bad",
            rows=1,
            columns=[ColumnSchema(name="score", generator="float", dtype="float", params={"precision": 0})],
        )
        with self.assertRaises(SchemaValidationError):
            validate_schema(schema)

    def test_invalid_date_ranges_are_rejected(self) -> None:
        schema = DatasetSchema(
            name="bad",
            rows=1,
            columns=[
                ColumnSchema(
                    name="signup_date",
                    generator="date",
                    dtype="date",
                    params={"start": "2025-01-02", "end": "2025-01-01"},
                )
            ],
        )
        with self.assertRaises(SchemaValidationError):
            validate_schema(schema)

    def test_empty_choices_are_rejected(self) -> None:
        schema = DatasetSchema(
            name="bad",
            rows=1,
            columns=[ColumnSchema(name="category", generator="choice", params={"choices": []})],
        )
        with self.assertRaises(SchemaValidationError):
            validate_schema(schema)

    def test_unsupported_dtype_is_rejected(self) -> None:
        schema = DatasetSchema(
            name="bad",
            rows=1,
            columns=[ColumnSchema(name="flag", generator="boolean", dtype="binary")],
        )
        with self.assertRaises(SchemaValidationError):
            validate_schema(schema)


class EngineTests(unittest.TestCase):
    def test_generate_dataset_helper_returns_dataframe(self) -> None:
        dataframe = generate_dataset({"rows": 3, "columns": ["name", "email"]})

        self.assertEqual(dataframe.shape, (3, 2))

    def test_engine_row_override_is_applied(self) -> None:
        engine = DataGenerationEngine()
        dataframe = engine.generate({"rows": 10, "columns": ["name"]}, rows=4)

        self.assertEqual(len(dataframe), 4)

    def test_engine_export_writes_file(self) -> None:
        engine = DataGenerationEngine()
        dataframe = engine.generate({"rows": 2, "columns": ["name", "email"]})

        with tempfile.TemporaryDirectory() as temp_dir:
            export_path = Path(temp_dir) / "output.csv"
            result = engine.export(dataframe, export_path)

            self.assertEqual(result, export_path)
            self.assertTrue(export_path.exists())


if __name__ == "__main__":
    unittest.main()
