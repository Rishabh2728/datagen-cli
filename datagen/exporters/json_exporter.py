from __future__ import annotations

from pathlib import Path

import pandas as pd


class JSONExporter:
    extension = ".json"

    def export(self, dataframe: pd.DataFrame, output_path: Path, **_: object) -> Path:
        dataframe.to_json(output_path, orient="records", indent=2, date_format="iso")
        return output_path
