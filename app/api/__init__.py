from flask import Blueprint
from app.api.auth import bp as auth_bp

bp = Blueprint('api',__name__,url_prefix='/api')
bp.register_blueprint(auth_bp)