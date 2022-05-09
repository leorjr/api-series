from flask import Blueprint

from app.routes import series_blueprint

bp = Blueprint("api_bp", __name__, url_prefix="/api")

bp.register_blueprint(series_blueprint.bp)
