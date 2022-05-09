from app.controllers.series_controller import delete, list_all_series, list_by_id, create_serie, delete, update

from flask import Blueprint

bp = Blueprint("series_bp", __name__, url_prefix="/series")


bp.get("/")(list_all_series)
bp.get("/<int:id>")(list_by_id)
bp.get("/")(create_serie)
bp.get("/<int:id>")(delete)
bp.get("/<int:id>")(update)
