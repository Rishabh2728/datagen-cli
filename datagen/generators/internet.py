from __future__ import annotations

from typing import List

from datagen.generators.base import BaseGenerator, GenerationContext
from datagen.models.column import ColumnSchema


class InternetGenerator(BaseGenerator):
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        values: List[object] = []

        for _ in range(rows):
            if column.generator == "domain":
                values.append(context.faker.domain_name())
            elif column.generator == "url":
                values.append(context.faker.url())
            elif column.generator == "username":
                values.append(context.faker.user_name())
            elif column.generator == "ipv4":
                values.append(context.faker.ipv4())
            else:
                values.append(context.faker.email())

        return values
