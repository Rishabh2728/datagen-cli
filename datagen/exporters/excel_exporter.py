from __future__ import annotations

from pathlib import Path

import pandas as pd


class ExcelExporter:
    extension = ".xlsx"

    def export(self, dataframe: pd.DataFrame, output_path: Path, **kwargs: object) -> Path:
        sheet_name = str(kwargs.get("sheet_name") or "Sheet1")
        dataframe.to_excel(output_path, index=False, sheet_name=sheet_name)
        return output_path
