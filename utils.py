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

def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v is not None}

def format_data(data: Any, indent: int = 2) -> str:
    return json.dumps(data, indent=indent)

def get_nested_key(data: Dict[str, Any], keys: list) -> Optional[Any]:
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data