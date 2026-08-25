import json
import os
from typing import Any, Dict, Optional

class ConfigurationLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load_from_file(self, path: str) -> None:
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, dict):
                self.config.update(data)

    def load_from_env(self, prefix: str = 'APP_') -> None:
        for key, value in list(os.environ.items()):
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                self.config[clean_key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.config.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        return dict(self.config)

    def merge(self, other: Dict[str, Any]) -> None:
        self.config.update(other)

    def reset(self) -> None:
        self.config = self.defaults.copy()