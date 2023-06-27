from flask import Blueprint,jsonify
routes_app = Blueprint("routes", __name__)

@routes_app.route("/publish_weather/<city>", methods = ['POST'])
def publish_weather(city):
    return