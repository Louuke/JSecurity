from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import jsecurity_api.config.factories as factories


class Settings(BaseSettings):
    SECRET_KEY: str = Field(default_factory=factories.secret_key, min_length=8)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default_factory=factories.access_token_expire_minutes, gt=0)

    model_config = SettingsConfigDict(env_file='settings.env')


