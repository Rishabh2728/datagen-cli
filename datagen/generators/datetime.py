from __future__ import annotations

from datetime import date, datetime
from typing import List

from datagen.generators.base import BaseGenerator, GenerationContext
from datagen.models.column import ColumnSchema


def _parse_date(value: str) -> date:
    if value == "today":
        return date.today()
    return datetime.fromisoformat(value).date()


def _parse_datetime(value: str) -> datetime:
    if value == "now":
        return datetime.now()
    return datetime.fromisoformat(value)


class DateTimeGenerator(BaseGenerator):
    def generate(self, column: ColumnSchema, rows: int, context: GenerationContext) -> List[object]:
        if column.generator == "date":
            start = _parse_date(str(column.params.get("start", "2020-01-01")))
            end = _parse_date(str(column.params.get("end", "today")))
            return [context.faker.date_between(start_date=start, end_date=end) for _ in range(rows)]

        start_dt = _parse_datetime(str(column.params.get("start", "2020-01-01T00:00:00")))
        end_dt = _parse_datetime(str(column.params.get("end", "now")))
        return [context.faker.date_time_between(start_date=start_dt, end_date=end_dt) for _ in range(rows)]
