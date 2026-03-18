from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from datagen.core.defaults import DEFAULT_EXPORT_FORMAT, DEFAULT_LOCALE


@dataclass
class GenerationConfig:
    seed: Optional[int] = None
    locale: str = DEFAULT_LOCALE
    output_format: str = DEFAULT_EXPORT_FORMAT
    sheet_name: str = "Sheet1"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GenerationConfig":
        return cls(
            seed=data.get("seed"),
            locale=data.get("locale", DEFAULT_LOCALE),
            output_format=data.get("output_format", DEFAULT_EXPORT_FORMAT),
            sheet_name=data.get("sheet_name", "Sheet1"),
        )
