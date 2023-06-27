from openweathermapsdk.OpenWeatherMap import OpenWeatherMap
import os
class OWMSDK:
    def __init__(self):
        self.client = OpenWeatherMap(os.getenv("OPEN_WEATHER_API_KEY"))
    def get_description(self,city):
        return self.client.get_description(city)
    def get_weather(self,city):
        return self.client.get_weather(city)
    def get_daily_forecast(self,city):
        return self.client.get_daily_forecast(city)