from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

import pandas as pd

from datagen.core.exceptions import ExportError
from datagen.exporters.csv_exporter import CSVExporter
from datagen.exporters.excel_exporter import ExcelExporter
from datagen.exporters.json_exporter import JSONExporter
from datagen.utils.file_utils import ensure_parent_dir


class ExportManager:
    def __init__(self) -> None:
        self.exporters: Dict[str, object] = {
            "csv": CSVExporter(),
            "json": JSONExporter(),
            "xlsx": ExcelExporter(),
            "excel": ExcelExporter(),
        }

    def export(
        self,
        dataframe: pd.DataFrame,
        output_path: Path,
        file_format: Optional[str] = None,
        sheet_name: Optional[str] = None,
    ) -> Path:
        format_name = (file_format or output_path.suffix.lstrip(".") or "csv").lower()
        exporter = self.exporters.get(format_name)
        if exporter is None:
            raise ExportError(f"Unsupported export format '{format_name}'.")

        if not output_path.suffix:
            extension = ".xlsx" if format_name in {"xlsx", "excel"} else f".{format_name}"
            output_path = output_path.with_suffix(extension)

        ensure_parent_dir(output_path)
        return exporter.export(dataframe, output_path, sheet_name=sheet_name)
