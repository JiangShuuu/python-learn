from pydantic_settings import BaseSettings, SettingsConfigDict

class _Environment(BaseSettings):
    # database settings
    db_host: str
    db_port: str
    db_name: str
    db_username: str
    db_password: str


    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


env = _Environment()
