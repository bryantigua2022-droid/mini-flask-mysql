from flask import Blueprint, jsonify, request
from ..models import db, Product

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@products_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    new_product = Product(name=data["name"], price=data["price"])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201
