from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from datagen.core.engine import DataGenerationEngine
from datagen.core.exceptions import DataGenError
from datagen.core.schema_loader import load_schema

console = Console()


def preview_command(
    schema: Path = typer.Argument(..., exists=True, readable=True, help="Path to a JSON schema file."),
    rows: Optional[int] = typer.Option(None, "--rows", "-r", min=1, help="Override row count."),
    limit: int = typer.Option(10, "--limit", "-n", min=1, help="Rows to show."),
) -> None:
    """Preview generated rows without exporting."""
    try:
        schema_payload = load_schema(schema)
        engine = DataGenerationEngine()
        dataframe = engine.generate(schema_payload, rows=rows)
        console.print(dataframe.head(limit).to_string(index=False))
    except DataGenError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1) from exc
