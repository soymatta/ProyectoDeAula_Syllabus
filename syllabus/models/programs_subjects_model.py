from ..db.db import db, ma, app


class ProgramsSubjects(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    programs_id = db.Column(db.Integer, db.ForeignKey("programs.id"), nullable=False)
    subjects_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)

    def __init__(self, program_id, subjects_id):
        self.program_id = program_id
        self.subjects_id = subjects_id


class ProgramsSubjectsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProgramsSubjects


facultySubject_schema = ProgramsSubjectsSchema()
programSubjects_schema = ProgramsSubjectsSchema(many=True)

with app.app_context():
    db.create_all()
