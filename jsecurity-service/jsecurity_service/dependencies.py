import logging as log

from functools import lru_cache
from jsecurity_api.model.settings import Settings
from jsecurity_service.utils import generate_token


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    if not settings.SECRET_KEY:
        settings.SECRET_KEY = generate_token()
        log.warning(f'SECRET_KEY not set in settings.env. Using generated key: {settings.SECRET_KEY}')
    return settings
