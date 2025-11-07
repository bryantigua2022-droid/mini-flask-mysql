import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST", "db")
    database = os.getenv("MYSQL_DATABASE")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from . import models
    with app.app_context():
        db.create_all()

    # Registrar rutas correctamente
    from .routes.users import users_bp
    from .routes.products import products_bp
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(products_bp, url_prefix="/products")

    # Endpoint de prueba
    @app.route("/")
    def index():
        return {"message": "API funcionando correctamente"}

    return app
