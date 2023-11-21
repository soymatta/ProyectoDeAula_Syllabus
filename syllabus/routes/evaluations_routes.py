from flask import Blueprint, request, jsonify
from ..db.db import db
from ..models.evaluations_model import Evaluations, EvaluationsSchema

evaluations_routes = Blueprint("evaluations", __name__)

# ------- GET -----------
@evaluations_routes.route('/get', methods=['GET'])
def get_evaluations():
    evaluations = Evaluations.query.all()
    evaluation_schema = EvaluationsSchema(many=True)
    return jsonify(evaluation_schema.dump(evaluations)), 200

# ------- POST -----------
@evaluations_routes.route('/post', methods=['POST'])
def create_evaluation():
    try:
        data = request.get_json()
        evaluation = Evaluation(**data)
        db.session.add(evaluation)
        db.session.commit()
        return EvaluationsSchema().jsonify(evaluation), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el usuario", "details": str(e)}), 400

# ------- PUT -----------
@evaluations_routes.route('/put/<int:id>', methods=['PUT'])
def update_evaluation(id):
    try:
        evaluation = Evaluations.query.get(id)
        if not evaluation:
            return jsonify({"error": "Usuario no encontrado"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(evaluation, key, value)

        db.session.commit()

        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el usuario", "details": str(e)}), 500

# ------- DELETE -----------
@evaluations_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_evaluation(id):
    try:
        evaluation = Evaluations.query.get(id)

        if not evaluation:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.session.delete(evaluation)
        db.session.commit()

        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el usuario", "details": str(e)}), 500
