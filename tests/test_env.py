from src.core.auth.env_loader import EnvLoader

def test_env_loader():

    api_token = EnvLoader.get_env_variable("API_TOKEN")

    print(api_token)

    assert api_token is not None

    
