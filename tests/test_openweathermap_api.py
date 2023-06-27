# -*- coding: utf-8 -*-
import unittest, os
from dotenv import load_dotenv
import requests

class ApiOpenWeatherMap((unittest.TestCase)):
    
    def setUp(self):
        load_dotenv()
        
    def test_valid_credentials_fail(self):
        api_key = os.getenv('OPEN_WEATHER_API_KEY') + 'error'
        daily_url = "https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&lang=pt&appid={api_key}".format(city= 'Rio de Janeiro', api_key = api_key)
        response = requests.get(daily_url)
        self.assertFalse(response.status_code == 200)
    def test_valid_credentials_pass(self):
        api_key = os.getenv('OPEN_WEATHER_API_KEY')
        daily_url = "https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&lang=pt&appid={api_key}".format(city= 'Rio de Janeiro', api_key = api_key)
        response = requests.get(daily_url)
        self.assertTrue(response.status_code == 200)
if __name__ == '__main__':
    unittest.main()