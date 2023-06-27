import unittest, json,os
import datetime
from app import app
from dotenv import load_dotenv

class AppTestCase(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.app = app
        self.app.config['TESTING'] = True
    def test_if_api_returns_success(self):
        client = self.app.test_client()
        response = client.post('/publish_weather/Betim%2CBR')
        self.assertEqual(response.status_code, 200)
    def test_if_api_returns_not_sucess(self):
        client = self.app.test_client()
        response = client.post('/publish_weather/error')
        self.assertNotEqual(response.status_code, 200)