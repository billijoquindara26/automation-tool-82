import re
from typing import Any, Optional

class DataValidator:
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return bool(DataValidator.EMAIL_REGEX.match(email))

    @staticmethod
    def is_non_empty_string(value: Any) -> bool:
        return isinstance(value, str) and len(value.strip()) > 0

    @staticmethod
    def validate_payload(data: dict, schema: dict) -> bool:
        for key, expected_type in schema.items():
            if key not in data or not isinstance(data[key], expected_type):
                return False
        return True

def validate_config_value(value: Optional[Any], validator_func: callable) -> Any:
    if value is None:
        raise ValueError('Configuration value cannot be None')
    if not validator_func(value):
        raise ValueError(f'Validation failed for value: {value}')
    return value