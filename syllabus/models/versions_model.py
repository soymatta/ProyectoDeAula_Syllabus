from ..db.db import ma, db, app
from sqlalchemy import DateTime
from datetime import datetime 

class Versions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    update_date = db.Column(DateTime, nullable=False)
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, update_date, description, owner, user_id):
        self.update_date = update_date
        self.description = description
        self.owner = owner
        self.user_id = user_id

class VersionsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Versions

version_schema = VersionsSchema()
versions_schema = VersionsSchema(many=True)

with app.app_context():
    db.create_all()