from typing import Any, Dict, List

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def unflatten_dict(d: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in d.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current or not isinstance(current.get(part), dict):
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result

def merge_dicts(d1: Dict[str, Any], d2: Dict[str, Any]) -> Dict[str, Any]:
    result = d1.copy()
    for k, v in d2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = merge_dicts(result[k], v)
        else:
            result[k] = v
    return result

def filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    return [item for item in data if isinstance(item, dict) and item.get(key) == value]

def remap_data(data: List[Dict[str, Any]], mapping: Dict[str, str]) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []
    for item in data:
        if isinstance(item, dict):
            new_item: Dict[str, Any] = {}
            for old_key, new_key in mapping.items():
                if old_key in item:
                    new_item[new_key] = item[old_key]
            result.append(new_item)
    return result

def safe_get(data: Dict[str, Any], path: str, default: Any = None, sep: str = '.') -> Any:
    keys = path.split(sep)
    current: Any = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current