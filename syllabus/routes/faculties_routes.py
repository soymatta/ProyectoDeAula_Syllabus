from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.faculties_model import Faculties, FacultiesSchema

faculties_routes = Blueprint("faculties", __name__)


# ------- GET -----------
@faculties_routes.route("/get", methods=["GET"])
def get_faculty():
    faculty = Faculties.query.all()
    faculty_schema = FacultiesSchema(many=True)
    return jsonify(faculty_schema.dump(faculty)), 200


# ------- POST -----------
@faculties_routes.route("/post", methods=["POST"])
def create_faculty():
    try:
        data = request.get_json()
        faculty = Faculty(**data)
        db.session.add(faculty)
        db.session.commit()
        return FacultiesSchema().jsonify(faculty), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear la facultad", "details": str(e)}), 400


# ------- PUT -----------
@faculties_routes.route("/put/<int:id>", methods=["PUT"])
def update_faculty(id):
    try:
        faculty = Faculties.query.get(id)
        if not faculty:
            return jsonify({"error": "Facultad no encontrada"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(faculty, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Facultad actualizada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"error": "Error al actualizar la facultad", "details": str(e)}),
            500,
        )


# ------- DELETE -----------
@faculties_routes.route("/delete/<int:id>", methods=["DELETE"])
def delete_faculty(id):
    try:
        faculty = Faculties.query.get(id)

        if not faculty:
            return jsonify({"error": "Facultad no encontrada"}), 404

        db.session.delete(faculty)
        db.session.commit()

        return jsonify({"mensaje": "Facultad eliminada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"error": "Error al eliminar la facultad", "details": str(e)}),
            500,
        )
