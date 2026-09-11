import re
from typing import Any, Dict, Type


def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def is_valid_ip(ip: str) -> bool:
    if not isinstance(ip, str):
        return False
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False


def safe_cast_int(val: Any, default: int = 0) -> int:
    try:
        return int(val)
    except (ValueError, TypeError):
        return default


def validate_dict_schema(data: Dict[str, Any], schema: Dict[str, Type]) -> bool:
    if not isinstance(data, dict) or not isinstance(schema, dict):
        return False
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True
