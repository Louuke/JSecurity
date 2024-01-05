import unittest
import pytest
from pydantic import ValidationError
from jsecurity_api.model.request import LoginRequest


class RequestTest(unittest.TestCase):

    @staticmethod
    def test_login_request_with_valid_data_creates_instance():
        request = LoginRequest(email='test@example.com', password='password123')
        assert request.email == 'test@example.com'
        assert request.password == 'password123'

    @staticmethod
    def test_login_request_invalid_email():
        with pytest.raises(ValidationError):
            LoginRequest(email="invalid_email", password="password123")

    @staticmethod
    def test_login_request_short_password():
        with pytest.raises(ValidationError):
            LoginRequest(email="test@example.com", password="short")

    @staticmethod
    def test_login_request_long_password():
        with pytest.raises(ValidationError):
            LoginRequest(email="test@example.com", password="a" * 257)
