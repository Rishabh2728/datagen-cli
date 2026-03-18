from __future__ import annotations

from typing import List

from datagen.generators.base import BaseGenerator, GenerationContext
from datagen.models.column import ColumnSchema


class PersonalGenerator(BaseGenerator):
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        values: List[object] = []

        for _ in range(rows):
            if column.generator == "first_name":
                values.append(context.faker.first_name())
            elif column.generator == "last_name":
                values.append(context.faker.last_name())
            elif column.generator == "phone_number":
                values.append(context.faker.phone_number())
            elif column.generator == "company":
                values.append(context.faker.company())
            elif column.generator == "job_title":
                values.append(context.faker.job())
            else:
                values.append(context.faker.name())

        return values
