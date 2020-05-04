# This class act as ORM with work_log table

from .. import db

class Worklog(db.Model):
    __tablename__ = "work_log"

    id = db.Column(db.Integer, primary_key=True)
    work_perfrom_date = db.Column(db.Date, unique=False, nullable=False)
    hours_worked = db.Column(db.Float, unique=True, nullable=False)
    employee_id = db.Column(db.Integer, unique=True, nullable=False)
    job_group = db.Column(db.String(5), unique=True, nullable=False)