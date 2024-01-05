import unittest
from jsecurity_api.config.settings import Settings
from jsecurity_service.dependencies import get_settings


class DependenciesTest(unittest.TestCase):

    @staticmethod
    def test_settings_returned_correctly():
        settings = get_settings()
        assert isinstance(settings, Settings)

    @staticmethod
    def test_settings_cached():
        settings1 = get_settings()
        settings2 = get_settings()
        assert settings1 is settings2
