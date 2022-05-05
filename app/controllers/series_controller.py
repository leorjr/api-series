from flask import Flask, jsonify, request
from app.exc.series_exceptions import SeriesExceptions
from app.models.series_model import Series
from psycopg2.errors import UniqueViolation


def init_app(app: Flask):

    @app.get("/series")
    def list_all_series():
        data = Series.list_all_series()
        return jsonify(data), 200

    @app.get("/series/<int:id>")
    def list_by_id(id: int):
        try:
            data = Series.list_serie_by_id(id)
            return jsonify(data), 200
        except SeriesExceptions as e:
            return {"error": str(e)}, 404

    @app.post("/series")
    def create_serie():
        try:
            data = request.json
            serie = Series(data)
            new_serie = Series.create_serie(serie)
            return new_serie, 200
        except UniqueViolation as e:
            return {"error": "série já existe"}, 404

    return app
