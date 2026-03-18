from __future__ import annotations

from pathlib import Path

import pandas as pd


class CSVExporter:
    extension = ".csv"

    def export(self, dataframe: pd.DataFrame, output_path: Path, **_: object) -> Path:
        dataframe.to_csv(output_path, index=False)
        return output_path
