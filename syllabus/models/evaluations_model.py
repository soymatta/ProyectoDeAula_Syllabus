from ..db.db import db, ma, app


class Evaluations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_percentage = db.Column(db.Integer, nullable=False)
    description_first_percentage = db.Column(db.Text, nullable=False)
    second_percentage = db.Column(db.Integer, nullable=True)
    description_second_percentage = db.Column(db.Text, nullable=True)
    third_percentage = db.Column(db.Integer, nullable=True)
    description_third_percentage = db.Column(db.Text, nullable=True)
    syllabus_id = db.Column(db.Integer, db.ForeignKey("syllabi.id"), nullable=False)

    def __init__(
        self,
        first_percentage,
        description_first_percentage,
        second_percentage,
        description_second_percentage,
        third_percentage,
        description_third_percentage,
        syllabus_id,
    ):
        self.first_percentage = first_percentage
        self.description_first_percentage = description_first_percentage
        self.second_percentage = second_percentage
        self.description_second_percentage = description_second_percentage
        self.third_percentage = third_percentage
        self.description_third_percentage = description_third_percentage
        self.syllabus_id = syllabus_id


class EvaluationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Evaluations


evaluation_schema = EvaluationsSchema()
evaluations_schemas = EvaluationsSchema(many=True)

with app.app_context():
    db.create_all()
