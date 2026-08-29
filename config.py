import json
import os
from typing import Any, Dict, Optional

class AutomationConfig:
    """Holds configuration settings for automation-tool-82."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        """Initialize with default or provided settings."""
        self._settings: Dict[str, Any] = {
            "max_retries": 3,
            "timeout": 60,
            "log_level": "INFO",
            "output_dir": "./output",
        }
        if settings:
            self._settings.update(settings)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve config value for key."""
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Update config value for key."""
        self._settings[key] = value

    def load_from_file(self, filepath: str) -> None:
        """Load settings from JSON file at filepath."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Config file not found: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            data: Dict[str, Any] = json.load(f)
        self._settings.update(data)

    def save_to_file(self, filepath: str) -> None:
        """Save settings to JSON file at filepath."""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self._settings, f, indent=4)

    def get_all(self) -> Dict[str, Any]:
        """Return copy of all settings."""
        return self._settings.copy()

    def validate(self) -> bool:
        """Validate key settings are positive."""
        if self.get("max_retries") < 0 or self.get("timeout") <= 0:
            return False
        return True

def create_default_config() -> AutomationConfig:
    """Return default AutomationConfig instance."""
    return AutomationConfig()

def merge_configs(base: AutomationConfig, override: Dict[str, Any]) -> AutomationConfig:
    """Return new config merging override into base."""
    new_settings = base.get_all()
    new_settings.update(override)
    return AutomationConfig(new_settings)