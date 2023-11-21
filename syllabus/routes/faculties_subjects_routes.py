from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.faculties_subjects_model import FacultiesSubjects, FacultiesSubjectsSchema

faculties_subjects_routes = Blueprint("faculties_subjects", __name__)

# ------- GET -----------
@faculties_subjects_routes.route('/get', methods=['GET'])
def get_faculty_subject():
    faculty_subject = FacultiesSubjects.query.all()
    faculty_subject_schema = FacultiesSubjectsSchema(many=True)
    return jsonify(faculty_subject_schema.dump(faculty_subject)), 200

# ------- POST -----------
@faculties_subjects_routes.route('/post', methods=['POST'])
def create_faculty_subject():
    try:
        data = request.get_json()
        faculty_subject = Faculty(**data)
        db.session.add(faculty_subject)
        db.session.commit()
        return FacultiesSubjectsSchema().jsonify(faculty_subject), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear la asignatura", "details": str(e)}), 400

# ------- PUT -----------
@faculties_subjects_routes.route('/put/<int:id>', methods=['PUT'])
def update_faculty_subject(id):
    try:
        faculty_subject = FacultiesSubjects.query.get(id)
        if not faculty_subject:
            return jsonify({"error": "Asignatura no encontrada"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(faculty_subject, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Asignatura actualizada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar la asignatura", "details": str(e)}), 500

# ------- DELETE -----------
@faculties_subjects_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_faculty_subject(id):
    try:
        faculty_subject = FacultiesSubjects.query.get(id)

        if not faculty_subject:
            return jsonify({"error": "Asignatura no encontrada"}), 404

        db.session.delete(faculty_subject)
        db.session.commit()

        return jsonify({"mensaje": "Asignatura eliminada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar la asignatura", "details": str(e)}), 500
