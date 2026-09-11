import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-82",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30,
    "max_retries": 3,
    "output_dir": "./output",
}


class ConfigLoader:
    def __init__(self, config_path: str | Path | None = None):
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        if self.config_path and self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                self._config.update(file_config)

        self._apply_env_overrides()
        return self._config

    def _apply_env_overrides(self) -> None:
        for key in self._config:
            env_key = f"APP_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                if isinstance(self._config[key], bool):
                    self._config[key] = val.lower() in ("true", "1", "yes")
                elif isinstance(self._config[key], int):
                    self._config[key] = int(val)
                else:
                    self._config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)
