from __future__ import annotations

from typing import List

from datagen.generators.base import BaseGenerator, GenerationContext
from datagen.models.column import ColumnSchema


class IdentifierGenerator(BaseGenerator):
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        prefix = str(column.params.get("prefix", "ID"))
        minimum = int(column.params.get("min", 1))
        maximum = int(column.params.get("max", 999999))

        if column.generator == "uuid":
            return [context.faker.uuid4() for _ in range(rows)]

        return [f"{prefix}-{context.random.randint(minimum, maximum)}" for _ in range(rows)]
