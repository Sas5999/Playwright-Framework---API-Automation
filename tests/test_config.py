from src.core.config_manager.config_manager import ConfigManager

def test_environment(env):

    config = ConfigManager(env=env)

    print(config.get("base_url"))
    print(config.get("timeout"))
    # print(config.get("retries"))

    assert config.get("base_url") is not None
    assert config.get("timeout") is not None
    # assert config.get("retries") is None

