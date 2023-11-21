from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.contentsAndStrategies_model import ContentsAndStrategies, ContentsAndStrategiesSchema

contentsAndStrategies_routes = Blueprint("contentsAndStrategies", __name__)

# ------- GET -----------
@contentsAndStrategies_routes.route('/get', methods=['GET'])
def get_contentsAndStrategies():
    contentsAndStrategies = ContentsAndStrategies.query.all()
    contentAndStrategy_schema = ContentsAndStrategiesSchema(many=True)
    return jsonify(contentAndStrategy_schema.dump(contentsAndStrategies)), 200

# ------- POST -----------
@contentsAndStrategies_routes.route('/post', methods=['POST'])
def create_contentAndStrategy():
    try:
        data = request.get_json()
        contentAndStrategy = User(**data)
        db.session.add(contentAndStrategy)
        db.session.commit()
        return ContentsAndStrategiesSchema().jsonify(contentAndStrategy), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el usuario", "details": str(e)}), 400

# ------- PUT -----------
@contentsAndStrategies_routes.route('/put/<int:id>', methods=['PUT'])
def update_contentAndStrategy(id):
    try:
        contentAndStrategy = ContentsAndStrategies.query.get(id)
        if not contentAndStrategy:
            return jsonify({"error": "Usuario no encontrado"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(contentAndStrategy, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el usuario", "details": str(e)}), 500

# ------- DELETE -----------
@contentsAndStrategies_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_contentAndStrategy(id):
    try:
        contentAndStrategy = ContentsAndStrategies.query.get(id)

        if not contentAndStrategy:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.session.delete(contentAndStrategy)
        db.session.commit()

        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el usuario", "details": str(e)}), 500
