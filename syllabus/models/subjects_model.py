from ..db.db import db, ma, app
from sqlalchemy import Enum

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(Enum('practica', 'teorica', 'teorico-practica'), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.String(2), nullable=False)
    bibliography = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, name, type, credits, semester, bibliography, content):
        self.name = name
        self.type = type
        self.credits = credits
        self.semester = semester
        self.bibliography = bibliography
        self.content = content

class SubjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subjects

subject_schema = SubjectSchema()
subjects_schema = SubjectSchema(many=True)

with app.app_context():
    db.create_all()