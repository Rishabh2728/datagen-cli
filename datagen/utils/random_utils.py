from __future__ import annotations

import random
from typing import Optional


def build_random(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed)
