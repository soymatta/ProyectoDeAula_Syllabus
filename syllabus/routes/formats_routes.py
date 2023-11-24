from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.formats_model import Formats, FormatsSchema

formats_routes = Blueprint("formats", __name__)


# ------- GET -----------
@formats_routes.route("/get", methods=["GET"])
def get_formats():
    formats = Formats.query.all()
    format_schema = FormatsSchema(many=True)
    return jsonify(format_schema.dump(formats)), 200


# ------- POST -----------
@formats_routes.route("/post", methods=["POST"])
def create_format():
    try:
        data = request.get_json()
        format = Format(**data)
        db.session.add(format)
        db.session.commit()
        return FormatsSchema().jsonify(format), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el formato", "details": str(e)}), 400


# ------- PUT -----------
@formats_routes.route("/put/<int:id>", methods=["PUT"])
def update_format(id):
    try:
        format = Formats.query.get(id)
        if not format:
            return jsonify({"error": "Formato no encontrado"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(format, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Formato actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"error": "Error al actualizar el formato", "details": str(e)}),
            500,
        )


# ------- DELETE -----------
@formats_routes.route("/delete/<int:id>", methods=["DELETE"])
def delete_format(id):
    try:
        format = Formats.query.get(id)

        if not format:
            return jsonify({"error": "Formato no encontrado"}), 404

        db.session.delete(format)
        db.session.commit()

        return jsonify({"mensaje": "Formato eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"error": "Error al eliminar el formato", "details": str(e)}),
            500,
        )
