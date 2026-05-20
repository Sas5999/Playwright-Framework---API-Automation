import os

from dotenv import load_dotenv  

load_dotenv()  # Load environment variables from .env file

class EnvLoader:

    @staticmethod
    def get_env_variable(key):
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Environment variable '{key}' not found.")
        return value
    