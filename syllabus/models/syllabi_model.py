from ..db.db import db, ma, app


class Syllabi(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cycle = db.Column(db.String(50))
    justification = db.Column(db.Text)
    competences = db.Column(db.Text)
    learning_results = db.Column(db.Text)
    methodology = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey("faculties.id"), nullable=False)
    format_id = db.Column(db.Integer, db.ForeignKey("formats.id"), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey("programs.id"), nullable=False)

    def __init__(
        self,
        program_id,
        faculty_id,
        cycle,
        identification,
        justification,
        competences,
        learning_results,
        methodology,
        program_content,
        strategies,
        bibliography,
        five_last_updates,
        subject_id,
        format_id,
    ):
        self.program_id = program_id
        self.faculty_id = faculty_id
        self.cycle = cycle
        self.identification = identification
        self.justification = justification
        self.competences = competences
        self.learning_results = learning_results
        self.methodology = methodology
        self.program_content = program_content
        self.strategies = strategies
        self.bibliography = bibliography
        self.five_last_updates = five_last_updates
        self.subject_id = subject_id
        self.format_id = format_id


class SyllabiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Syllabi


syllabus_schema = SyllabiSchema()
syllabi_schema = SyllabiSchema(many=True)

with app.app_context():
    db.create_all()
