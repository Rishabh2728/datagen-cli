from pathlib import Path

import typer
from rich.console import Console

from datagen.core.exceptions import DataGenError
from datagen.core.schema_loader import load_schema
from datagen.core.schema_normalizer import normalize_schema
from datagen.core.schema_validator import validate_schema

console = Console()


def validate_command(
    schema: Path = typer.Argument(..., exists=True, readable=True, help="Path to a JSON schema file."),
) -> None:
    """Validate and normalize a schema."""
    try:
        schema_payload = load_schema(schema)
        normalized = normalize_schema(schema_payload)
        validate_schema(normalized)
        console.print("[green]Schema is valid.[/green]")
        console.print(f"Columns: {len(normalized.columns)}")
        console.print(f"Rows: {normalized.rows}")
    except DataGenError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1) from exc
