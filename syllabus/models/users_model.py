from ..db.db import ma, db, app
from sqlalchemy import Enum, DateTime
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    role = db.Column(Enum("admin", "teacher"), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey("faculties.id"), nullable=False)

    def __init__(self, name, email, password, role, status, faculty_id):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status
        self.faculty_id = faculty_id


class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

with app.app_context():
    db.create_all()
