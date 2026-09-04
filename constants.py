import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
TEMP_DIR = BASE_DIR / "temp"

DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

SUPPORTED_EXTENSIONS = {".txt", ".json", ".csv", ".yaml"}

ENV_VARS = {
    "API_KEY": "APP_API_KEY",
    "DB_URL": "APP_DB_URL",
    "LOG_LEVEL": "APP_LOG_LEVEL",
}

HTTP_HEADERS = {
    "User-Agent": "automation-tool-82/1.0",
    "Content-Type": "application/json",
}

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def get_env_variable(key: str, default: str = None) -> str:
    return os.getenv(ENV_VARS.get(key, key), default)