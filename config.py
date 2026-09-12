import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "host": "127.0.0.1",
    "port": 8080,
    "debug": False,
    "timeout": 30,
    "log_level": "INFO"
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json") -> None:
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self.config.update(file_config)
            except (json.JSONDecodeError, IOError):
                pass
        self._override_from_env()
        return self.config

    def _override_from_env(self) -> None:
        for key in self.config:
            env_key = f"APP_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                current_type = type(self.config[key])
                try:
                    if current_type is bool:
                        self.config[key] = val.lower() in ("true", "1", "yes")
                    else:
                        self.config[key] = current_type(val)
                except ValueError:
                    pass