from pathlib import Path
from typing import Optional

import typer

app = typer.Typer(
    help="Schema-driven synthetic dataset generator with Python and CLI interfaces.",
    no_args_is_help=True,
)


@app.command("generate")
def generate(
    schema: Path = typer.Argument(..., exists=True, readable=True, help="Path to a JSON schema file."),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file path."),
    file_format: Optional[str] = typer.Option(None, "--format", "-f", help="Export format override: csv, json, xlsx."),
    rows: Optional[int] = typer.Option(None, "--rows", "-r", min=1, help="Override row count."),
    preview_rows: int = typer.Option(5, "--preview-rows", min=1, help="Rows to print after generation."),
) -> None:
    from datagen.cli.commands.generate import generate_command

    generate_command(
        schema=schema,
        output=output,
        file_format=file_format,
        rows=rows,
        preview_rows=preview_rows,
    )


@app.command("preview")
def preview(
    schema: Path = typer.Argument(..., exists=True, readable=True, help="Path to a JSON schema file."),
    rows: Optional[int] = typer.Option(None, "--rows", "-r", min=1, help="Override row count."),
    limit: int = typer.Option(10, "--limit", "-n", min=1, help="Rows to show."),
) -> None:
    from datagen.cli.commands.preview import preview_command

    preview_command(schema=schema, rows=rows, limit=limit)


@app.command("validate")
def validate(
    schema: Path = typer.Argument(..., exists=True, readable=True, help="Path to a JSON schema file."),
) -> None:
    from datagen.cli.commands.validate import validate_command

    validate_command(schema=schema)
