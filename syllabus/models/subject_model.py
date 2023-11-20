from ..db.db import db, ma, app
from sqlalchemy import Enum

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    faculties = db.Column(db.Text)
    teachers = db.Column(db.Text)
    type = db.Column(Enum('practica', 'teorica', 'teorico-practica'), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    bibliography = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __init__(self, name, faculties, teachers, type, credits, bibliography, content, faculty_id):
        self.name = name
        self.faculties = faculties
        self.teachers = teachers
        self.type = type
        self.credits = credits
        self.bibliography = bibliography
        self.content = content
        self.faculty_id = faculty_id

class SubjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subject

subject_schema = SubjectSchema()
subjects_schema = SubjectSchema(many=True)

with app.app_context():
    db.create_all()