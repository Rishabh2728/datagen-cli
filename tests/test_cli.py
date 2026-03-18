from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from typer.testing import CliRunner

from datagen.cli.app import app


class CLITests(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = CliRunner()

    def _write_schema(self, payload: dict) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp_dir = tempfile.TemporaryDirectory()
        path = Path(temp_dir.name) / "schema.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return temp_dir, path

    def test_generate_command_runs_successfully(self) -> None:
        temp_dir, schema_path = self._write_schema({"rows": 3, "columns": ["name", "email"]})
        self.addCleanup(temp_dir.cleanup)
        output_path = Path(temp_dir.name) / "generated.csv"

        result = self.runner.invoke(app, ["generate", str(schema_path), "--output", str(output_path), "--format", "csv"])

        self.assertEqual(result.exit_code, 0, msg=result.stdout)
        self.assertTrue(output_path.exists())

    def test_preview_command_runs_successfully(self) -> None:
        temp_dir, schema_path = self._write_schema({"rows": 3, "columns": ["name", "email"]})
        self.addCleanup(temp_dir.cleanup)

        result = self.runner.invoke(app, ["preview", str(schema_path), "--limit", "2"])

        self.assertEqual(result.exit_code, 0, msg=result.stdout)
        self.assertIn("name", result.stdout)

    def test_validate_command_runs_successfully(self) -> None:
        temp_dir, schema_path = self._write_schema({"rows": 3, "columns": ["name", "email"]})
        self.addCleanup(temp_dir.cleanup)

        result = self.runner.invoke(app, ["validate", str(schema_path)])

        self.assertEqual(result.exit_code, 0, msg=result.stdout)
        self.assertIn("Schema is valid.", result.stdout)

    def test_invalid_schema_exits_with_code_1(self) -> None:
        temp_dir, schema_path = self._write_schema(
            {"rows": 3, "columns": [{"name": "value", "generator": "float", "params": {"min": 5, "max": 1}}]}
        )
        self.addCleanup(temp_dir.cleanup)

        result = self.runner.invoke(app, ["validate", str(schema_path)])

        self.assertEqual(result.exit_code, 1, msg=result.stdout)
        self.assertIn("Error:", result.stdout)


if __name__ == "__main__":
    unittest.main()
