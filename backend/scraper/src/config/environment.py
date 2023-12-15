from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='scraper.env', env_prefix='DB_', case_sensitive=False)

    host: str
    port: int
    user: str
    password: str
    name: str

class SIACSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='scraper.env', env_prefix='SIAC_', case_sensitive=False)

    user: str
    password: str

class Settings(BaseSettings):

    postgres: Optional[PostgresSettings] = PostgresSettings()
    siac: Optional[SIACSettings] = SIACSettings()

settings = Settings()