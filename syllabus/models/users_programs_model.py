from ..db.db import db, ma, app


class UsersPrograms(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    programs_id = db.Column(db.Integer, db.ForeignKey("programs.id"), nullable=False)

    def __init__(self, users_id, programs_id):
        self.users_id = users_id
        self.programs_id = programs_id


class UsersProgramsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsersPrograms


userProgram_schema = UsersProgramsSchema()
usersPrograms_schema = UsersProgramsSchema(many=True)

with app.app_context():
    db.create_all()
