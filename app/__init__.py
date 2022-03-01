from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
CORS(app)

def create_app():
    from app.models import User
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
