from src.core.config_manager.config_manager import ConfigManager

config = ConfigManager(env= "dev")

print(config.get("base_url"))
print(config.get("timeout"))
# print(config.get("retries"))

