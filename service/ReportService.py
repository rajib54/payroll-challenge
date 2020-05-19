# This class handles business logic and utility functions for payroll report end point

from ..model import Payroll
import calendar

class ReportService:
    def __init__(self, dbhandler):
        self.dbhandler = dbhandler

    def get_payroll_report(self):
        dict = {}
        works = self.dbhandler.get_work_logs()
        for work in works:
            day = '16' if work.work_perfrom_date.day > 15 else '01'
            month = '0' + str(work.work_perfrom_date.month) if work.work_perfrom_date.month < 10 else str(work.work_perfrom_date.month)
            key = str(work.employee_id) + "_" + str(work.work_perfrom_date.year) + "-" + month + "-" + day

            if key in dict:
                dict[key]['hoursWorked'] += work.hours_worked
                amountpaid = self.get_amount_paid(dict[key]['hoursWorked'], work.job_group)
                dict[key]['amountPaid'] = amountpaid
            else:
                if day == '01':
                    enddate = str(work.work_perfrom_date.year) + "-" + month + "-15"
                else:
                    enddate = str(work.work_perfrom_date.year) + "-" + month + "-" + str(self.get_last_day_of_month(work.work_perfrom_date.year, work.work_perfrom_date.month))
                amountpaid = self.get_amount_paid(work.hours_worked, work.job_group)
                dict[key] = {'amountPaid': amountpaid, 'endDate': enddate, 'hoursWorked': work.hours_worked}

        reports = []
        for key, value in dict.items():
            arr = key.split("_")
            payperiod = {'startDate': arr[1], 'endDate': value.get('endDate')}

            report = Payroll()
            report.employeeId = int(arr[0])
            report.payPeriod = payperiod
            report.amountPaid = "$" + str(round(value.get('amountPaid'), 2))
            reports.append(report.toarray())

        payload = {
            "payrollReport": {
                "employeeReports": reports
            }
        }
        return payload

    def get_last_day_of_month(self, year, month):
        return calendar.monthrange(year, month)[1]

    def get_amount_paid(self, hoursWorked, jobGroup):
        if jobGroup == 'A':
            if hoursWorked > 60:
                return (60 * 20) + ((hoursWorked - 60) * 20 * 1.5)
            return hoursWorked * 20
        elif jobGroup == 'B':
            return hoursWorked * 30
        else:
            return 0
