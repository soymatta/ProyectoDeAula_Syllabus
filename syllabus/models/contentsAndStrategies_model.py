from ..db.db import db, ma, app

class ContentsAndStrategies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_name = db.Column(db.String(50), nullable=False)
    sub_content = db.Column(db.Text)
    strategies = db.Column(db.Text)
    syllabi_id = db.Column(db.Integer, db.ForeignKey('syllabi.id'), nullable=False)

    def __init__(self, content_name, sub_content, strategies, syllabi_id):
        self.content_name = content_name
        self.sub_content = sub_content
        self.strategies = strategies
        self.syllabi_id = syllabi_id

class ContentsAndStrategiesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContentsAndStrategies

content_and_strategy_schema = ContentsAndStrategiesSchema()
contents_and_strategies_schemas = ContentsAndStrategiesSchema(many=True)

with app.app_context():
    db.create_all()