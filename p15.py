'''
Create a class Employee with attributes emp_id, name, basic_pay. Add a method calculate_salary() that calculates gross salary as:
Gross = Basic Pay + HRA (20%) + DA (10%).
Then display the salary details.
'''

class Employee:
    def __init__(self,emp_id, name, basic_pay):
        self.emp_id = emp_id
        self.name = name
        self.basic_pay = basic_pay

    def details(self):
        print("Employee ID: ", self.emp_id)
        print("Employee name:", self.name)
        
    def calculate_salary(self):
        basic_pay = self.basic_pay
        HRA = (20/100)*basic_pay
        DA = (10/100)*basic_pay
        salary = basic_pay + HRA + DA
        return salary

emp_id = int(input("Enter employee id:"))
name = input("Enter name:")
basic_pay = int(input("Enter basic pay:"))
emp = Employee(emp_id, name, basic_pay)
emp.details()
print("Salary: ", emp.calculate_salary())

