from ..db.db import db, ma, app

class Faculties(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)

    def __init__(self, name, subjects=None, teachers=None):
        self.name = name

class FacultySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Faculties

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)

with app.app_context():
    db.create_all()