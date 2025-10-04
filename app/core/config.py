from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # Configuration to load environment variables from a .env file
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    # Application settings
    APP_NAME: str = 'My FastAPI Application'
    DEBUG: bool = False

    # Database settings
    DATABASE_USER: str = 'user'
    DATABASE_PASSWORD: str = 'password'
    DATABASE_NAME: str = 'test'
    DATABASE_URL: str = f'sqlite:///./{DATABASE_NAME}.db'


config = Config()
