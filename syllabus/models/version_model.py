from ..db.db import ma, db, app
from sqlalchemy import DateTime
from datetime import datetime 

class Version(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    update_date = db.Column(DateTime, nullable=False)
    description = db.Column(db.String(500))
    owner = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, update_date, description, owner, user_id):
        self.update_date = update_date
        self.description = description
        self.owner = owner
        self.user_id = user_id

class VersionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Version

version_schema = VersionSchema()
versions_schema = VersionSchema(many=True)

with app.app_context():
    db.create_all()