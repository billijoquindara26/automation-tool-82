import json
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-82",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30.0,
    "output_dir": "./output",
}


class ConfigManager:
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        if self.config_path:
            self.load()

    def load(self) -> Dict[str, Any]:
        if self.config_path and self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                self._config.update(user_config)
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value

    def save(self, target_path: Optional[str] = None) -> None:
        path = Path(target_path) if target_path else self.config_path
        if not path:
            raise ValueError("No file path specified for saving configuration")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._config, f, indent=4)

    @property
    def data(self) -> Dict[str, Any]:
        return self._config.copy()
