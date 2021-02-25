first=0
last=0
pay=0
prog_lang=0

def emp_info_input(first,last,pay,prog_lang):
    first=input("Enter employee's first name:")
    last=input("Enter employee's last name:")
    pay=input("Enter employee's pay/salary:")
    prog_lang=input("Enter employee's preferred programming language:")
    print( "{} {}".format(first,last))
    print("Pay:{}              Programming Language:{}".format(pay,prog_lang))


emp_info_input(first,last,pay,prog_lang)