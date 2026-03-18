class DataGenError(Exception):
    """Base package exception."""


class SchemaLoadError(DataGenError):
    """Raised when a schema cannot be loaded."""


class SchemaValidationError(DataGenError):
    """Raised when a schema is invalid."""


class GeneratorNotFoundError(DataGenError):
    """Raised when a column references an unknown generator."""


class ExportError(DataGenError):
    """Raised when exporting fails."""
