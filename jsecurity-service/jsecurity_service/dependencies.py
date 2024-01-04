from functools import lru_cache
from jsecurity_api.config.settings import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()
