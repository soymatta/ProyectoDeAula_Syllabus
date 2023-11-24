from ..db.db import db, ma, app


class FacultiesSubjects(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    faculties_id = db.Column(db.Integer, db.ForeignKey("faculties.id"), nullable=False)
    subjects_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)

    def __init__(self, faculties_id, subjects_id):
        self.faculties_id = faculties_id
        self.subjects_id = subjects_id


class FacultiesSubjectsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FacultiesSubjects


facultySubject_schema = FacultiesSubjectsSchema()
facultiesSubjects_schema = FacultiesSubjectsSchema(many=True)

with app.app_context():
    db.create_all()
