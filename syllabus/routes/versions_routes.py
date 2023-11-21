from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.versions_model import Versions, VersionsSchema

versions_routes = Blueprint("versions", __name__)

# ------- GET -----------
@versions_routes.route('/get', methods=['GET'])
def get_versions():
    versions = Versions.query.all()
    version_schema = VersionsSchema(many=True)
    return jsonify(version_schema.dump(versions)), 200

# ------- POST -----------
@versions_routes.route('/post', methods=['POST'])
def create_version():
    try:
        data = request.get_json()
        version = Version(**data)
        db.session.add(version)
        db.session.commit()
        return VersionsSchema().jsonify(version), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear la versión", "details": str(e)}), 400

# ------- PUT -----------
@versions_routes.route('/put/<int:id>', methods=['PUT'])
def update_version(id):
    try:
        version = Versions.query.get(id)
        if not version:
            return jsonify({"error": "Versión no encontrada"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(version, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Versión actualizada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar la versión", "details": str(e)}), 500

# ------- DELETE -----------
@versions_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_version(id):
    try:
        version = Versions.query.get(id)

        if not version:
            return jsonify({"error": "Versión no encontrada"}), 404

        db.session.delete(version)
        db.session.commit()

        return jsonify({"mensaje": "Versión eliminada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar la versión", "details": str(e)}), 500
