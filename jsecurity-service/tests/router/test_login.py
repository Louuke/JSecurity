import unittest

from tests import client


class LoginTest(unittest.TestCase):

    @staticmethod
    def test_successful_login_returns_message():
        request = {'email': 'test@example.org', 'password': 'valid_password'}
        response = client.post('/login', json=request)
        assert response.status_code == 200

    @staticmethod
    def test_login_with_empty_email_raises_http_exception():
        request = {'email': '', 'password': 'valid_password'}
        response = client.post('/login', json=request)
        assert response.status_code == 422

    @staticmethod
    def test_login_with_empty_password_raises_http_exception():
        request = {'email': 'test@example.org', 'password': ''}
        response = client.post('/login', json=request)
        assert response.status_code == 422
