from ..db.db import db, ma, app

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    subjects = db.Column(db.Text)
    teachers = db.Column(db.Text)

    def __init__(self, name, subjects=None, teachers=None):
        self.name = name
        self.subjects = subjects
        self.teachers = teachers

class FacultySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Faculty

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)

with app.app_context():
    db.create_all()