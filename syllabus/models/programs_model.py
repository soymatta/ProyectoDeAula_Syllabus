from ..db.db import ma, db, app


class Programs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey("faculties.id"))

    def __init__(self, name, faculty_id):
        self.name = name
        self.faculty_id = faculty_id


class ProgramsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Programs


Program_schema = ProgramsSchema()
Programs_schema = ProgramsSchema(many=True)

with app.app_context():
    db.create_all()
