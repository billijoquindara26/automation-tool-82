import json
import os
import shutil
from pathlib import Path
from typing import Any, Optional

def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(data: Any, path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def ensure_directory(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def safe_remove(path: str) -> bool:
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        return True
    except OSError:
        return False

def get_env_var(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default or '')

def list_files_by_extension(directory: str, ext: str) -> list[str]:
    return [str(f) for f in Path(directory).glob(f'*.{ext}')]

def chunk_list(data: list, size: int) -> list[list]:
    return [data[i:i + size] for i in range(0, len(data), size)]