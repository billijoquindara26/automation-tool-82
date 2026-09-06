import os
from pathlib import Path
from typing import List

class DataProcessor:
    def __init__(self, target_dir: str):
        self.target_dir = Path(target_dir)

    def get_files(self) -> List[Path]:
        if not self.target_dir.exists():
            return []
        return [f for f in self.target_dir.iterdir() if f.is_file()]

    def purge_temporary_files(self, extension: str = '.tmp') -> int:
        count = 0
        for file_path in self.get_files():
            if file_path.suffix == extension:
                try:
                    file_path.unlink()
                    count += 1
                except OSError:
                    continue
        return count

    def organize_by_extension(self) -> None:
        for file_path in self.get_files():
            subdir = self.target_dir / file_path.suffix.lstrip('.')
            subdir.mkdir(exist_ok=True)
            file_path.rename(subdir / file_path.name)

def run_cleanup(path: str) -> None:
    processor = DataProcessor(path)
    processor.purge_temporary_files()
    processor.organize_by_extension()