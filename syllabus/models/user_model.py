from ..db.db import ma, db, app
from sqlalchemy import Enum, DateTime
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    role = db.Column(Enum('admin', 'teacher'), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    subjects = db.Column(db.String(1500))
    faculties = db.Column(db.String(1000))
    last_update = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, password, role, status, subjects=None, faculties=None):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status
        self.subjects = subjects
        self.faculties = faculties

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)

with app.app_context():
    db.create_all()
