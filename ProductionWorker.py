import Employee


class ProductionWorker:

    def __init__(self):
        self.first_name = Employee.usrFName
        self.last_name = Employee.usrLName
        self.shift = Employee.usrShift
        self.wage = Employee.usrWage


print("Your First name is " + Employee.usrFName + "\n Your Last Name is " + Employee.usrFName + "\n Your Shift is " + Employee.usrShift   + "\n Your hourly pay rate is " + Employee.usrWage)


prd_worker = ProductionWorker()
