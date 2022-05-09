from flask import Flask
from app.controllers import series_controller
from app.routes import series_blueprint


def create_app():

    app = Flask(__name__)

    # series_controller.init_app(app)
    app.register_blueprint(series_blueprint.bp)

    return app
