import json
import os

DEFAULT_CONFIG = {
    'setting1': 'value1',
    'setting2': 2,
    'setting3': True
}

class ConfigLoader:
    def __init__(self, config_file=None):
        self.config = DEFAULT_CONFIG.copy()
        if config_file and os.path.isfile(config_file):
            self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            user_config = json.load(f)
            self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self, config_file):
        with open(config_file, 'w') as f:
            json.dump(self.config, f, indent=4)