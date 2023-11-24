from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.programs_model import Programs, ProgramsSchema

programs_routes = Blueprint("programs", __name__)


# ------- GET -----------
@programs_routes.route("/get", methods=["GET"])
def get_programs():
    programs = Programs.query.all()
    program_schema = ProgramsSchema(many=True)
    return jsonify(program_schema.dump(programs)), 200


# ------- POST -----------
@programs_routes.route("/post", methods=["POST"])
def create_program():
    try:
        data = request.get_json()
        program = Program(**data)
        db.session.add(program)
        db.session.commit()
        return ProgramsSchema().jsonify(program), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el programa", "details": str(e)}), 400


# ------- PUT -----------
@programs_routes.route("/put/<int:id>", methods=["PUT"])
def update_program(id):
    try:
        program = Programs.query.get(id)
        if not program:
            return jsonify({"error": "Programa no encontrado"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(program, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Programa actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"error": "Error al actualizar el programa", "details": str(e)}),
            500,
        )


# ------- DELETE -----------
@programs_routes.route("/delete/<int:id>", methods=["DELETE"])
def delete_program(id):
    try:
        program = Programs.query.get(id)

        if not program:
            return jsonify({"error": "Programa no encontrado"}), 404

        db.session.delete(program)
        db.session.commit()

        return jsonify({"mensaje": "Programa eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"error": "Error al eliminar el programa", "details": str(e)}),
            500,
        )
