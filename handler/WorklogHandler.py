# This class handles DB queries for archiving employee work log

from ..model import Worklog, ReportProcessed
from .. import db

class WorklogHandler:
    def get_work_logs(self):
        return Worklog.query.order_by(Worklog.employee_id).order_by(Worklog.work_perfrom_date).all()

    def insert_work_log(self, workperformdate, hoursworked, employeeid, jobgroup):
        try:
            work = Worklog(work_perfrom_date=workperformdate, hours_worked=hoursworked, employee_id=employeeid, job_group=jobgroup)
            db.session.add(work)
            db.session.commit()
        except:
            db.session.rollback()
