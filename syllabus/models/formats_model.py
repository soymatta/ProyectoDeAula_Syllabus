from ..db.db import ma, db, app
from sqlalchemy import Enum, DateTime
from datetime import datetime


class Formats(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(30))
    version = db.Column(db.Integer, nullable=False)
    update_date = db.Column(DateTime, nullable=False)

    def __init__(self, code, version, update_date):
        self.code = code
        self.version = version
        self.update_date = update_date


class FormatsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Formats


format_schema = FormatsSchema()
formats_schema = FormatsSchema(many=True)

with app.app_context():
    db.create_all()
