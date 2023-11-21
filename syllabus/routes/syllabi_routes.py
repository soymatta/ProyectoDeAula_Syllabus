from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.syllabi_model import Syllabi, SyllabiSchema

syllabi_routes = Blueprint("syllabi", __name__)

# ------- GET -----------
@syllabi_routes.route('/get', methods=['GET'])
def get_syllabi():
    syllabi = Syllabi.query.all()
    syllabus_schema = SyllabiSchema(many=True)
    return jsonify(syllabus_schema.dump(syllabi)), 200

# ------- POST -----------
@syllabi_routes.route('/post', methods=['POST'])
def create_syllabus():
    try:
        data = request.get_json()
        syllabus = Syllabus(**data)
        db.session.add(syllabus)
        db.session.commit()
        return SyllabiSchema().jsonify(syllabus), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el syllabus", "details": str(e)}), 400

# ------- PUT -----------
@syllabi_routes.route('/put/<int:id>', methods=['PUT'])
def update_syllabus(id):
    try:
        syllabus = Syllabi.query.get(id)
        if not syllabus:
            return jsonify({"error": "Syllabus no encontrado"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(syllabus, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Syllabus actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el syllabus", "details": str(e)}), 500

# ------- DELETE -----------
@syllabi_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_syllabus(id):
    try:
        syllabus = Syllabi.query.get(id)

        if not syllabus:
            return jsonify({"error": "Syllabus no encontrado"}), 404

        db.session.delete(syllabus)
        db.session.commit()

        return jsonify({"mensaje": "Syllabus eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el syllabus", "details": str(e)}), 500
