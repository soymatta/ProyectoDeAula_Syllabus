from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.subject_model import Subject, SubjectSchema

subject_routes = Blueprint("subject", __name__)

# ------- GET -----------
@subject_routes.route('/get', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    subject_schema = SubjectSchema(many=True)
    return jsonify(subject_schema.dump(subjects)), 200

# ------- POST -----------
@subject_routes.route('/post', methods=['POST'])
def create_subject():
    try:
        data = request.get_json()
        subject = Subject(**data)
        db.session.add(subject)
        db.session.commit()
        return SubjectSchema().jsonify(subject), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear la asignatura", "details": str(e)}), 400

# ------- PUT -----------
@subject_routes.route('/put/<int:id>', methods=['PUT'])
def update_subject(id):
    try:
        subject = Subject.query.get(id)
        if not subject:
            return jsonify({"error": "Asignatura no encontrada"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(subject, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Asignatura actualizada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar la asignatura", "details": str(e)}), 500

# ------- DELETE -----------
@subject_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_subject(id):
    try:
        subject = Subject.query.get(id)

        if not subject:
            return jsonify({"error": "Asignatura no encontrada"}), 404

        db.session.delete(subject)
        db.session.commit()

        return jsonify({"mensaje": "Asignatura eliminada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar la asignatura", "details": str(e)}), 500
