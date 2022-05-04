from flask import Flask
from app.controllers import series_controller


def create_app():

    app = Flask(__name__)

    series_controller.init_app(app)

    return app
