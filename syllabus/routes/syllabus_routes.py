from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.syllabus_model import Syllabus, SyllabusSchema

syllabus_routes = Blueprint("syllabus", __name__)

# ------- GET -----------
@syllabus_routes.route('/get', methods=['GET'])
def get_syllabi():
    syllabi = Syllabus.query.all()
    syllabus_schema = SyllabusSchema(many=True)
    return jsonify(syllabus_schema.dump(syllabi)), 200

# ------- POST -----------
@syllabus_routes.route('/post', methods=['POST'])
def create_syllabus():
    try:
        data = request.get_json()
        syllabus = Syllabus(**data)
        db.session.add(syllabus)
        db.session.commit()
        return SyllabusSchema().jsonify(syllabus), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el syllabus", "details": str(e)}), 400

# ------- PUT -----------
@syllabus_routes.route('/put/<int:id>', methods=['PUT'])
def update_syllabus(id):
    try:
        syllabus = Syllabus.query.get(id)
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
@syllabus_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_syllabus(id):
    try:
        syllabus = Syllabus.query.get(id)

        if not syllabus:
            return jsonify({"error": "Syllabus no encontrado"}), 404

        db.session.delete(syllabus)
        db.session.commit()

        return jsonify({"mensaje": "Syllabus eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el syllabus", "details": str(e)}), 500
