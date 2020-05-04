# This class handles business logic and utility functions for csv parsing end point

import csv

class ParserService:
    def __init__(self, workloghandler, reportprocessedhandler):
        self.workloghandler = workloghandler
        self.reportprocessedhandler = reportprocessedhandler

    def is_report_uploaded(self, id):
        reportids = self.reportprocessedhandler.get_processed_report_ids()
        for r in reportids:
            if id == r.report_id:
                return True
        return False

    def add_report_id(self, id):
        self.reportprocessedhandler.add_processed_report_id(id)

    def parse_csv(self, file):
        with open(file) as csvfile:
            mycsv = csv.reader(csvfile, delimiter=',')
            line = 0
            for row in mycsv:
                line += 1
                if line == 1:
                    if not self.is_header_valid(row[0], row[1], row[2], row[3]):
                        return False
                else:
                    self.workloghandler.insert_work_log(self.convert_date_form(row[0]), row[1], row[2], row[3])
            if line == 0:
                return False
        return True

    def convert_date_form(self, date):
        arr = date.split("/")
        return arr[2] + "-" + arr[1] + "-" + arr[0]

    def is_header_valid(self, header1, header2, header3, header4):
        if header1 != 'date':
            return False
        if header2 != 'hours worked':
            return False
        if header3 != 'employee id':
            return False
        if header4 != 'job group':
            return False
        return True