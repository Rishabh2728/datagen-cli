from __future__ import annotations

from typing import List

from datagen.generators.base import BaseGenerator, GenerationContext
from datagen.models.column import ColumnSchema


class TextGenerator(BaseGenerator):
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        mode = column.params.get("mode", column.generator)
        max_nb_chars = int(column.params.get("max_nb_chars", 32))
        values = []

        for _ in range(rows):
            if mode == "word":
                values.append(context.faker.word())
            elif mode == "paragraph":
                values.append(context.faker.paragraph())
            elif mode == "sentence":
                values.append(context.faker.sentence(nb_words=6))
            else:
                values.append(context.faker.text(max_nb_chars=max_nb_chars))

        return values
