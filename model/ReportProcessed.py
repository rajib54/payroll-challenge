# This class act as ORM with # This class act as ORM with work_log table table

from .. import db

class ReportProcessed(db.Model):
    __tablename__ = "# This class act as ORM with work_log table"

    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, unique=True, nullable=False)
