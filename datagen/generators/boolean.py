from __future__ import annotations

from typing import List

from datagen.generators.base import BaseGenerator, GenerationContext
from datagen.models.column import ColumnSchema


class BooleanGenerator(BaseGenerator):
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        true_probability = float(column.params.get("true_probability", 0.5))
        return [context.random.random() < true_probability for _ in range(rows)]
