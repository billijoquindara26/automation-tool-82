import os
import shutil
from typing import List, Optional
from pathlib import Path

def clean_directory(target: str, extensions: Optional[List[str]] = None) -> None:
    path = Path(target)
    if not path.is_dir():
        raise ValueError(f'Invalid directory: {target}')

    for item in path.iterdir():
        if extensions and item.suffix not in extensions:
            continue
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

def ensure_paths(paths: List[str]) -> None:
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)

def get_file_stats(target: str) -> dict:
    path = Path(target)
    if not path.exists():
        return {}
    return {
        'size': path.stat().st_size,
        'modified': path.stat().st_mtime
    }

def archive_data(source: str, destination: str) -> None:
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.make_archive(str(Path(destination) / 'backup'), 'zip', source)