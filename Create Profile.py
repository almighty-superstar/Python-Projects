class Employee():
    def __init__(self,first,last,pay,role):
        self.first=first
        self.last=last
        self.pay=pay
        self.role=role
def CreateProfile():
    print('{} {}    {}'.format(first,last,role))
    print("Salary:{}".format(pay))
    print("{}.{}@Company.com".format(first,last))




first=input("Please enter the employee's first name:")
last=input("Please enter the employee's last name:")
role=input("Please enter the employee's role:")
pay=input("Please enter the employee's salary:")



CreateProfile()