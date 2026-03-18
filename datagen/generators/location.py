from __future__ import annotations

from typing import List

from datagen.generators.base import BaseGenerator, GenerationContext
from datagen.models.column import ColumnSchema


class LocationGenerator(BaseGenerator):
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        values: List[object] = []

        for _ in range(rows):
            if column.generator == "country":
                values.append(context.faker.country())
            elif column.generator == "state":
                values.append(context.faker.state())
            elif column.generator == "postal_code":
                values.append(context.faker.postcode())
            else:
                values.append(context.faker.city())

        return values
