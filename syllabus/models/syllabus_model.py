from ..db.db import db, ma, app

class Syllabus(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    cycle = db.Column(db.String(500))
    identification = db.Column(db.Text)
    justification = db.Column(db.Text)
    competences = db.Column(db.Text)
    learning_results = db.Column(db.Text)
    methodology = db.Column(db.Text)
    program_content = db.Column(db.Text)
    strategies = db.Column(db.Text)
    evaluation = db.Column(db.String(2500))
    bibliography = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __init__(self, date, cycle, identification, justification, competences, learning_results,
                 methodology, program_content, strategies, evaluation, bibliography, subject_id, faculty_id):
        self.date = date
        self.cycle = cycle
        self.identification = identification
        self.justification = justification
        self.competences = competences
        self.learning_results = learning_results
        self.methodology = methodology
        self.program_content = program_content
        self.strategies = strategies
        self.evaluation = evaluation
        self.bibliography = bibliography
        self.subject_id = subject_id
        self.faculty_id = faculty_id

class SyllabusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Syllabus

syllabus_schema = SyllabusSchema()
syllabi_schema = SyllabusSchema(many=True)

