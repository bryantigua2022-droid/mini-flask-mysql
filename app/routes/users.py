# en app/routes/users.py
from flask import Blueprint, jsonify
from app import mysql

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def get_users():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT 'Conexión MySQL exitosa!'")
    result = cursor.fetchone()
    cursor.close()
    return jsonify({"message": result[0]})
