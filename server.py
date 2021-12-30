import os
from flask import Flask
from flask_restx import Api, Resource
from dotenv import load_dotenv
from routes.api import ApiRoute
from middleware.api_authenticate import ApiAuthenticate

load_dotenv()

app = Flask(__name__)

app.wsgi_app = ApiAuthenticate(app.wsgi_app)

app.register_blueprint(ApiRoute, url_prefix='/api')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)