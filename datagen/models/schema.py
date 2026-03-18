from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from datagen.models.column import ColumnSchema
from datagen.models.config import GenerationConfig


@dataclass
class DatasetSchema:
    name: str
    rows: int
    columns: List[ColumnSchema]
    config: GenerationConfig = field(default_factory=GenerationConfig)
