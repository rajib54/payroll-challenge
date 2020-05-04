# This class handles DB queries that keep tracks of reports processed

from ..model import ReportProcessed
from .. import db

class ReportProcessedHandler:
    def get_processed_report_ids(self):
        return ReportProcessed.query.all()

    def add_processed_report_id(self, id):
        try:
            report = ReportProcessed(report_id=id)
            db.session.add(report)
            db.session.commit()
        except:
            db.session.rollback()
