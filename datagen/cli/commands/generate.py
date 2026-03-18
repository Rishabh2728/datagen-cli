from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from datagen.core.engine import DataGenerationEngine
from datagen.core.exceptions import DataGenError
from datagen.core.schema_loader import load_schema

console = Console()


def generate_command(
    schema: Path = typer.Argument(..., exists=True, readable=True, help="Path to a JSON schema file."),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file path."),
    file_format: Optional[str] = typer.Option(
        None,
        "--format",
        "-f",
        help="Export format override: csv, json, xlsx.",
    ),
    rows: Optional[int] = typer.Option(None, "--rows", "-r", min=1, help="Override row count."),
    preview_rows: int = typer.Option(5, "--preview-rows", min=1, help="Rows to print after generation."),
) -> None:
    """Generate a dataset from a schema."""
    try:
        schema_payload = load_schema(schema)
        engine = DataGenerationEngine()
        dataframe = engine.generate(schema_payload, rows=rows)

        if output:
            exported_path = engine.export(dataframe, output, file_format=file_format)
            console.print(f"[green]Saved[/green] {exported_path}")

        console.print(dataframe.head(preview_rows).to_string(index=False))
        console.print(f"[cyan]Rows:[/cyan] {len(dataframe)}  [cyan]Columns:[/cyan] {len(dataframe.columns)}")
    except DataGenError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1) from exc
