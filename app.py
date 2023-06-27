from flask import Flask
from routes import routes_app
from dotenv import load_dotenv
import os
app = Flask(__name__)
app.register_blueprint(routes_app)

if __name__ == '__main__':
    load_dotenv()
    app.run(host="0.0.0.0", port=5000, debug=True)