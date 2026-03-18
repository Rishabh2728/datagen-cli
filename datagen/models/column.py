from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class ColumnSchema:
    name: str
    generator: str = "text"
    dtype: str = "string"
    nullable: bool = False
    unique: bool = False
    description: Optional[str] = None
    params: Dict[str, Any] = field(default_factory=dict)
