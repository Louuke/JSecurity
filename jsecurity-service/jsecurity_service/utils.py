import secrets


def generate_token(length=32) -> str:
    return secrets.token_hex(length)
