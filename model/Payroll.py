# This class is the payroll object that is returned for reporting

from . import Base

class Payroll(Base):
    employeeId = None
    payPeriod = None
    amountPaid = None