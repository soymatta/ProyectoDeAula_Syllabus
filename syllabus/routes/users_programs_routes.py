from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.users_programs_model import UsersPrograms, UsersProgramsSchema

users_programs_routes = Blueprint("users_programs", __name__)


# ------- GET -----------
@users_programs_routes.route("/get", methods=["GET"])
def get_users_programs():
    users_programs = UsersPrograms.query.all()
    user_schema = UsersProgramsSchema(many=True)
    return jsonify(user_schema.dump(users_programs)), 200


# ------- PUT -----------
@users_programs_routes.route("/put/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        user = UsersPrograms.query.get(id)
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(user, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"error": "Error al actualizar el usuario", "details": str(e)}),
            500,
        )


# ------- DELETE -----------
@users_programs_routes.route("/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = UsersPrograms.query.get(id)

        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"error": "Error al eliminar el usuario", "details": str(e)}),
            500,
        )
