from db.db import connection
from classes.employee import Employee

class Manager(Employee):

    def __init__(self, id, first_name, last_name, age, department, salary, managed_department):
        super().__init__(id, first_name, last_name, age, department, salary)
        self.managed_department = managed_department
        # update empolyee daata
        connection.execute(f"UPDATE employee SET department = '{self.department}' WHERE first_name = '{self.first_name}'")
        connection.execute('commit')
        
    def __str__(self):
        return f"{super().__str__()}, Managed Department: {self.managed_department}"
    
    @classmethod
    def show(cls):
        connection.execute('SELECT * FROM employee')
        result = connection.fetchall()
        for employee in result:
            print(f"First Name: {employee[1]}, Last Name: {employee[2]}, Age: {employee[3]}, Department: {employee[4]}, Salary: Confidential")
            
            
    