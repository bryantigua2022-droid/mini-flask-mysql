from flask import Blueprint, request, jsonify
from . import db
from .models import User

bp = Blueprint("api", __name__)

@bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Mini Flask + MySQL API running"}), 200

@bp.route("/users", methods=["GET"])
def list_users():
    users = User.query.order_by(User.id).all()
    return jsonify([u.to_dict() for u in users]), 200

@bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "name and email required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "email already exists"}), 400

    u = User(name=name, email=email)
    db.session.add(u)
    db.session.commit()
    return jsonify(u.to_dict()), 201

@bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    u = User.query.get_or_404(user_id)
    return jsonify(u.to_dict()), 200

@bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    u = User.query.get_or_404(user_id)
    db.session.delete(u)
    db.session.commit()
    return jsonify({"message": "deleted"}), 200
