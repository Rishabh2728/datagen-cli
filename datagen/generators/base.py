from __future__ import annotations

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from faker import Faker

from datagen.models.column import ColumnSchema
from datagen.models.schema import DatasetSchema


@dataclass
class GenerationContext:
    random: random.Random
    faker: Faker

    @classmethod
    def from_schema(cls, schema: DatasetSchema) -> "GenerationContext":
        rng = random.Random(schema.config.seed)
        faker = Faker(schema.config.locale)
        if schema.config.seed is not None:
            Faker.seed(schema.config.seed)
            faker.seed_instance(schema.config.seed)
        return cls(random=rng, faker=faker)


class BaseGenerator(ABC):
    @abstractmethod
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        raise NotImplementedError
