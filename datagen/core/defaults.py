from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

DEFAULT_ROWS = 100
DEFAULT_DATASET_NAME = "generated_dataset"
DEFAULT_LOCALE = "en_US"
DEFAULT_EXPORT_FORMAT = "csv"

DEFAULT_SCHEMA: Dict[str, Any] = {
    "name": DEFAULT_DATASET_NAME,
    "rows": DEFAULT_ROWS,
    "config": {
        "seed": None,
        "locale": DEFAULT_LOCALE,
        "output_format": DEFAULT_EXPORT_FORMAT,
        "sheet_name": "Sheet1",
    },
    "columns": [
        {"name": "id", "generator": "uuid"},
        {"name": "name", "generator": "full_name"},
        {"name": "email", "generator": "email"},
    ],
}

DEFAULT_GENERATOR_PARAMS: Dict[str, Dict[str, Any]] = {
    "text": {"mode": "sentence", "max_nb_chars": 32},
    "word": {"mode": "word"},
    "sentence": {"mode": "sentence", "max_nb_chars": 48},
    "paragraph": {"mode": "paragraph"},
    "int": {"min": 0, "max": 100},
    "float": {"min": 0.0, "max": 1000.0, "precision": 2},
    "age": {"min": 18, "max": 80},
    "boolean": {"true_probability": 0.5},
    "date": {"start": "2020-01-01", "end": "today"},
    "datetime": {"start": "2020-01-01T00:00:00", "end": "now"},
    "full_name": {},
    "first_name": {},
    "last_name": {},
    "phone_number": {},
    "company": {},
    "job_title": {},
    "email": {},
    "domain": {},
    "url": {},
    "username": {},
    "ipv4": {},
    "city": {},
    "country": {},
    "state": {},
    "postal_code": {},
    "latitude": {"min": -90.0, "max": 90.0, "precision": 6},
    "longitude": {"min": -180.0, "max": 180.0, "precision": 6},
    "uuid": {},
    "order_id": {"prefix": "ORD", "min": 10000, "max": 99999},
    "transaction_id": {"prefix": "TXN", "min": 100000, "max": 999999},
    "choice": {"choices": ["A", "B", "C"]},
    "category": {"choices": ["Retail", "Finance", "Healthcare", "Technology"]},
}

NAME_HINTS: Dict[str, Dict[str, Any]] = {
    "id": {"generator": "uuid", "dtype": "string"},
    "uuid": {"generator": "uuid", "dtype": "string"},
    "order_id": {"generator": "order_id", "dtype": "string"},
    "transaction_id": {"generator": "transaction_id", "dtype": "string"},
    "name": {"generator": "full_name", "dtype": "string"},
    "first_name": {"generator": "first_name", "dtype": "string"},
    "last_name": {"generator": "last_name", "dtype": "string"},
    "email": {"generator": "email", "dtype": "string"},
    "username": {"generator": "username", "dtype": "string"},
    "domain": {"generator": "domain", "dtype": "string"},
    "url": {"generator": "url", "dtype": "string"},
    "phone": {"generator": "phone_number", "dtype": "string"},
    "city": {"generator": "city", "dtype": "string"},
    "country": {"generator": "country", "dtype": "string"},
    "state": {"generator": "state", "dtype": "string"},
    "postal_code": {"generator": "postal_code", "dtype": "string"},
    "zip": {"generator": "postal_code", "dtype": "string"},
    "age": {"generator": "age", "dtype": "int"},
    "score": {"generator": "float", "dtype": "float"},
    "amount": {"generator": "float", "dtype": "float"},
    "price": {"generator": "float", "dtype": "float"},
    "quantity": {"generator": "int", "dtype": "int"},
    "count": {"generator": "int", "dtype": "int"},
    "is_active": {"generator": "boolean", "dtype": "bool"},
    "active": {"generator": "boolean", "dtype": "bool"},
    "enabled": {"generator": "boolean", "dtype": "bool"},
    "created_at": {"generator": "datetime", "dtype": "datetime"},
    "updated_at": {"generator": "datetime", "dtype": "datetime"},
    "date": {"generator": "date", "dtype": "date"},
    "company": {"generator": "company", "dtype": "string"},
    "job_title": {"generator": "job_title", "dtype": "string"},
    "category": {"generator": "category", "dtype": "string"},
    "description": {"generator": "sentence", "dtype": "string"},
}


def get_default_generator_params(generator_name: str) -> Dict[str, Any]:
    return deepcopy(DEFAULT_GENERATOR_PARAMS.get(generator_name, {}))
