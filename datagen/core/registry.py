from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from datagen.core.exceptions import GeneratorNotFoundError
from datagen.generators.base import BaseGenerator
from datagen.generators.boolean import BooleanGenerator
from datagen.generators.choice import ChoiceGenerator
from datagen.generators.datetime import DateTimeGenerator
from datagen.generators.identifiers import IdentifierGenerator
from datagen.generators.internet import InternetGenerator
from datagen.generators.location import LocationGenerator
from datagen.generators.numeric import NumericGenerator
from datagen.generators.personal import PersonalGenerator
from datagen.generators.text import TextGenerator


@dataclass
class GeneratorRegistry:
    generators: Dict[str, BaseGenerator] = field(default_factory=dict)

    def register(self, name: str, generator: BaseGenerator) -> None:
        self.generators[name] = generator

    def get(self, name: str) -> BaseGenerator:
        try:
            return self.generators[name]
        except KeyError as exc:
            raise GeneratorNotFoundError(f"Unknown generator '{name}'.") from exc


def build_default_registry() -> GeneratorRegistry:
    registry = GeneratorRegistry()
    text_generator = TextGenerator()
    numeric_generator = NumericGenerator()
    boolean_generator = BooleanGenerator()
    datetime_generator = DateTimeGenerator()
    personal_generator = PersonalGenerator()
    internet_generator = InternetGenerator()
    location_generator = LocationGenerator()
    identifier_generator = IdentifierGenerator()
    choice_generator = ChoiceGenerator()

    for alias in ("text", "word", "sentence", "paragraph"):
        registry.register(alias, text_generator)
    for alias in ("int", "float", "age", "latitude", "longitude"):
        registry.register(alias, numeric_generator)
    registry.register("boolean", boolean_generator)
    for alias in ("date", "datetime"):
        registry.register(alias, datetime_generator)
    for alias in ("full_name", "first_name", "last_name", "phone_number", "company", "job_title"):
        registry.register(alias, personal_generator)
    for alias in ("email", "domain", "url", "username", "ipv4"):
        registry.register(alias, internet_generator)
    for alias in ("city", "country", "state", "postal_code"):
        registry.register(alias, location_generator)
    for alias in ("uuid", "order_id", "transaction_id"):
        registry.register(alias, identifier_generator)
    for alias in ("choice", "category"):
        registry.register(alias, choice_generator)
    return registry
