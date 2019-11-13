class Company(object):
    def __init__(self,employee_list):
        self.employee=employee_list
company=Company(['Bekzhan','Bayan','Gera'])
employee=company.employee
for item in employee:
    print(item)