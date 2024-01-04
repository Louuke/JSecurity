import logging as log
import secrets


def secret_key():
    key = secrets.token_hex(32)
    log.warning(f'SECRET_KEY not set in settings.env. Using generated key: {key}')
    return key


def access_token_expire_minutes():
    return 30
