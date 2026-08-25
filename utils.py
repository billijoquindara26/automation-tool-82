def chunk_data(data, chunk_size):
    if not isinstance(data, list) or not isinstance(chunk_size, int) or chunk_size <= 0:
        return []
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunks.append(data[i:i + chunk_size])
    return chunks
def flatten_data(data):
    if not isinstance(data, list):
        return [data] if data is not None else []
    flattened = []
    for item in data:
        if isinstance(item, list):
            flattened.extend(flatten_data(item))
        else:
            flattened.append(item)
    return flattened
def unique_data(data):
    if not isinstance(data, list):
        return []
    seen = set()
    unique_list = []
    for item in data:
        try:
            if item not in seen:
                seen.add(item)
                unique_list.append(item)
        except TypeError:
            if item not in unique_list:
                unique_list.append(item)
    return unique_list
def merge_dicts(dict1, dict2):
    if not isinstance(dict1, dict):
        return dict2 if isinstance(dict2, dict) else {}
    if not isinstance(dict2, dict):
        return dict1
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result
def get_nested_value(data, path, default=None, separator='.'):
    if not isinstance(data, dict) or not isinstance(path, str):
        return default
    keys = path.split(separator)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
def filter_data(data, include_keys=None, exclude_keys=None):
    if not isinstance(data, dict):
        return {}
    if include_keys is not None:
        return {k: v for k, v in data.items() if k in include_keys}
    if exclude_keys is not None:
        return {k: v for k, v in data.items() if k not in exclude_keys}
    return data.copy()