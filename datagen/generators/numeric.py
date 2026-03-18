from __future__ import annotations

from typing import List

from datagen.generators.base import BaseGenerator, GenerationContext
from datagen.models.column import ColumnSchema


class NumericGenerator(BaseGenerator):
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        minimum = column.params.get("min", 0)
        maximum = column.params.get("max", 100)
        precision = int(column.params.get("precision", 2))

        if column.generator in {"int", "age"}:
            return [context.random.randint(int(minimum), int(maximum)) for _ in range(rows)]

        return [round(context.random.uniform(float(minimum), float(maximum)), precision) for _ in range(rows)]
