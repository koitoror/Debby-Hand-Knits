from unittest import TestCase

import requests


class TestFlaskApiUsingRequests(TestCase):
    def test_home(self):
        response = requests.get('http://localhost')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = requests.get('http://localhost/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = requests.get('http://localhost/register')
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):
        response = requests.get('http://localhost/checkout')
        self.assertEqual(response.status_code, 200)
