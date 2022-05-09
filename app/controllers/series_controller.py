from flask import jsonify, request
from app.exc.series_exceptions import SeriesExceptions
from app.models.series_model import Series
from psycopg2.errors import UniqueViolation


def list_all_series():
    data = Series.list_all_series()
    return jsonify(data), 200


def list_by_id(id: int):
    try:
        data = Series.list_serie_by_id(id)
        return jsonify(data), 200
    except SeriesExceptions as e:
        return {"error": str(e)}, 404


def create_serie():
    try:
        data = request.json
        serie = Series(data)
        new_serie = Series.create_serie(serie)
        return new_serie, 200
    except UniqueViolation as e:
        return {"error": "série já existe"}, 404


def delete(id: int):
    try:
        data = Series.delete(id)
        return jsonify(data), 200
    except SeriesExceptions as e:
        return {"error": str(e)}, 404


def update(id: int):
    try:
        data_to_update = request.json
        data = Series.update(id, data_to_update)
        return jsonify(data), 200
    except SeriesExceptions as e:
        return {"error": str(e)}, 404
