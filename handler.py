import json
from typing import Any, Dict, Optional

def load_json_file(path: str) -> Dict[str, Any]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json_file(path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def clean_data(data: Any) -> Any:
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [clean_data(item) for item in data if item is not None]
    return data

def get_nested(data: Dict[str, Any], key_path: str, default: Any = None) -> Any:
    keys = key_path.split('.')
    val = data
    try:
        for key in keys:
            val = val[key]
        return val if val is not None else default
    except (KeyError, TypeError):
        return default