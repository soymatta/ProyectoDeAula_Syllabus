from ..db.db import db, ma, app

class UsersSyllabi(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    syllabi_id = db.Column(db.Integer, db.ForeignKey('syllabi.id'), nullable=False)

    def __init__(self, user_id, syllabi_id):
        self.user_id = user_id
        self.syllabi_id = syllabi_id

class UsersSyllabiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsersSyllabi

user_syllabus_schema = UsersSyllabiSchema()
users_syllabi_schema = UsersSyllabiSchema(many=True)

with app.app_context():
    db.create_all()
