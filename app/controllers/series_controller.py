from flask import Flask, jsonify
from app.models.series_model import Series


def init_app(app: Flask):

    @app.get("/series")
    def list_all_series():
        data = Series.list_all_series()
        return jsonify(data), 200

    return app
