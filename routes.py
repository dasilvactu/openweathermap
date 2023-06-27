from flask import Blueprint,jsonify
from controllers.OpenWeatherMapController import OpenWeatherMapController
from controllers.TweetController import TweetController
from controllers.OWMSDK import OWMSDK
routes_app = Blueprint("routes", __name__)

@routes_app.route("/publish_weather/<city>", methods = ['POST'])
def publish_weather(city):
    try:
        weather_api = OpenWeatherMapController()
        text = weather_api.get_description(city = city)
        tweetapi = TweetController()
        tweetapi.publish_tweet(text)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    return 'Weather and forecast publish successfully'

@routes_app.route("/publish_weather_sdk/<city>", methods = ['POST'])
def get_message(city):
    try:
        weather_api = OWMSDK()
        text = weather_api.get_description(city = city)
        tweetapi = TweetController()
        tweetapi.publish_tweet(text)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    return 'Weather and forecast publish successfully'