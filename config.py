import os
import json
from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class AppConfig:
    """Configuration schema for the automation tool."""
    env: str = "development"
    debug: bool = False
    timeout: int = 30
    api_keys: Dict[str, str] = field(default_factory=dict)

    def load_from_env(self) -> None:
        """Override configuration values using environment variables."""
        self.env = os.getenv("APP_ENV", self.env)
        self.debug = os.getenv("APP_DEBUG", str(self.debug)).lower() in ("true", "1", "t")
        self.timeout = int(os.getenv("APP_TIMEOUT", str(self.timeout)))
        
        api_keys_raw = os.getenv("APP_API_KEYS")
        if api_keys_raw:
            try:
                self.api_keys = json.loads(api_keys_raw)
            except json.JSONDecodeError:
                pass

    def to_dict(self) -> Dict[str, Any]:
        """Convert the configuration state to a dictionary.

        Returns:
            Dict[str, Any]: The configuration dictionary.
        """
        return {
            "env": self.env,
            "debug": self.debug,
            "timeout": self.timeout,
            "api_keys": self.api_keys,
        }