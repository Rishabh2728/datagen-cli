from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Union

from datagen.core.exceptions import SchemaLoadError

SchemaInput = Union[Dict[str, Any], str, Path]


def load_schema(schema_input: SchemaInput) -> Dict[str, Any]:
    if isinstance(schema_input, dict):
        return schema_input

    path = Path(schema_input)
    if not path.exists():
        raise SchemaLoadError(f"Schema file not found: {path}")

    if path.suffix.lower() != ".json":
        raise SchemaLoadError("Phase 1 supports JSON schema files only.")

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SchemaLoadError(f"Invalid JSON schema: {exc}") from exc
