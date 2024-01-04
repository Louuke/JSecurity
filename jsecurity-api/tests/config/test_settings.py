import unittest
import pytest
from pydantic import ValidationError
from jsecurity_api.config.settings import Settings


class SettingsTest(unittest.TestCase):

    @staticmethod
    def test_settings_with_valid_data_creates_instance():
        settings = Settings(SECRET_KEY='my_secret', ACCESS_TOKEN_EXPIRE_MINUTES=60)
        assert settings.SECRET_KEY == 'my_secret'
        assert settings.ACCESS_TOKEN_EXPIRE_MINUTES == 60

    @staticmethod
    def test_settings_with_empty_secret_key_raises_validation_error():
        with pytest.raises(ValidationError):
            Settings(SECRET_KEY='', ACCESS_TOKEN_EXPIRE_MINUTES=60)

    @staticmethod
    def test_settings_with_negative_token_expire_time_raises_validation_error():
        with pytest.raises(ValidationError):
            Settings(SECRET_KEY='my_secret', ACCESS_TOKEN_EXPIRE_MINUTES=-1)

    @staticmethod
    def test_settings_with_zero_token_expire_time_raises_validation_error():
        with pytest.raises(ValidationError):
            Settings(SECRET_KEY='my_secret', ACCESS_TOKEN_EXPIRE_MINUTES=0)
