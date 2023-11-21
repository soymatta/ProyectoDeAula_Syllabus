from ..db.db import db, ma, app

class UsersSubjects(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subjects_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)

    def __init__(self, users_id, subjects_id):
        self.users_id = users_id
        self.subjects_id = subjects_id


class UsersSubjectsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsersSubjects

userSubject_schema = UsersSubjectsSchema()
usersSubjects_schema = UsersSubjectsSchema(many=True)

with app.app_context():
    db.create_all()