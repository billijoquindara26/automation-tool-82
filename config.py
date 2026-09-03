import json
import os
from typing import Any, Dict, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "timeout": 30,
    "retry_limit": 3,
    "log_level": "INFO",
    "enable_notifications": False,
    "api_url": "https://api.example.com/v1",
}


class Config:
    def __init__(self, config_path: Union[str, None] = None):
        self._config = DEFAULT_CONFIG.copy()
        if config_path and os.path.exists(config_path):
            self.load_from_file(config_path)
        self._load_from_env()

    def load_from_file(self, config_path: str) -> None:
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self._config.update(data)
        except (json.JSONDecodeError, OSError):
            pass

    def _load_from_env(self) -> None:
        for key in self._config:
            env_key = f"AUTO_TOOL_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                self._config[key] = self._parse_env_val(val, type(self._config[key]))

    @staticmethod
    def _parse_env_val(val: str, expected_type: type) -> Any:
        if expected_type is bool:
            return val.lower() in ("true", "1", "yes")
        if expected_type is int:
            try:
                return int(val)
            except ValueError:
                return val
        return val

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def __getattr__(self, name: str) -> Any:
        if name in self._config:
            return self._config[name]
        raise AttributeError(f"'Config' object has no attribute '{name}'")
