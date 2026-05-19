import yaml
from pathlib import Path


class ConfigManager:

    def __init__(self, env="dev"):
        self.env = env
        self.config = self.load_config()

    def load_config(self):

        config_path = Path(f"config/{self.env}.yaml")

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        try:
            with open(config_path, "r") as file:

                config_data = yaml.safe_load(file)

                if config_data is None:
                    raise ValueError(
                        f"Configuration file is empty: {config_path}"
                    )

                return config_data

        except yaml.YAMLError as error:
            raise ValueError(
                f"Invalid YAML format in file: {config_path}"
            ) from error

    def get(self, key):

        value = self.config.get(key)

        if value is None:
            raise KeyError(
                f"Key '{key}' not found in {self.env}.yaml"
            )

        return value