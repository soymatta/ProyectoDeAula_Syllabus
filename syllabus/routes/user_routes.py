from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.user_model import User, UserSchema

user_routes = Blueprint("user", __name__)

# ------- GET -----------
@user_routes.route('/get', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users)), 200

# ------- POST -----------
@user_routes.route('/post', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return UserSchema().jsonify(user), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el usuario", "details": str(e)}), 400

# ------- PUT -----------
@user_routes.route('/put/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(user, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el usuario", "details": str(e)}), 500

# ------- DELETE -----------
@user_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id)

        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el usuario", "details": str(e)}), 500
