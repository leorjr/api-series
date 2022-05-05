from flask import Flask, jsonify, request
from app.models.series_model import Series


def init_app(app: Flask):

    @app.get("/series")
    def list_all_series():
        data = Series.list_all_series()
        return jsonify(data), 200

    @app.post("/series")
    def create_serie():
        data = request.json
        serie = Series(data)
        new_serie = Series.create_serie(serie)
        return new_serie, 200

    return app
