# -*- coding: utf-8 -*-
import unittest, os
from controllers.OpenWeatherMapController import OpenWeatherMapController
from dotenv import load_dotenv

class OpenWeatherMapControllerApi((unittest.TestCase)):
    def setUp(self):
        load_dotenv()
        
    def test_if_consult_weahter_city_is_success(self):
        client = OpenWeatherMapController()
        response = client.get_weather('Rio de Janeiro,BR')
        dict_structure = {"desc": None, "temp": None, "date": None}
        self.assertEqual(set(response.keys()),set(dict_structure.keys()))
    def test_if_consult_weahter_city_is_not_success(self):
        client = OpenWeatherMapController()
        response = client.get_weather('error')
        dict_structure = {"desc": None, "temp": None, "date": None}
        self.assertNotEqual(set(response.keys()),set(dict_structure.keys()))
    def test_if_consult_daily_forecast_city_is_success(self):
        client = OpenWeatherMapController()
        response = client.get_daily_forecast('Rio de Janeiro,BR')
        self.assertIsInstance(response, list)
    def test_if_consult_daily_forecast_city_is_not_success(self):
        client = OpenWeatherMapController()
        response = client.get_daily_forecast('error')
        self.assertNotIsInstance(response, list)
    def test_if_get_message_is_sucess(self):
        client = OpenWeatherMapController()
        response = client.get_description('Rio de Janeiro,BR')
        self.assertIsNotNone(response)
    def test_if_get_message_is_not_sucess(self):
        client = OpenWeatherMapController()
        response = client.get_description('error')
        self.assertIsNone(response)
if __name__ == '__main__':
    unittest.main()