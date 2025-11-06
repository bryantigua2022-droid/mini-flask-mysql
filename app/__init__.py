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

    # Crear tablas si no existen (solo para ejemplo/dev)
    with app.app_context():
        from . import models  # importa modelos para que SQLAlchemy los registre
        db.create_all()

    # Registrar rutas
    from .routes import bp
    app.register_blueprint(bp)

    return app
