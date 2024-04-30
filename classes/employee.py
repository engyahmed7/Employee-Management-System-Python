
from db.db import connection

connection.execute('''create table if not exists employee(
    id int primary key auto_increment not null,
    first_name text not null,
    last_name text not null,
    age int not null,
    department char(50),
    salary int
    );''')


class Employee:
    employees = []
    def __init__(self, id, first_name, last_name, age, department, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employees.append(self)

        connection.execute(f"SELECT * FROM employee WHERE first_name = '{self.first_name}' AND last_name = '{self.last_name}'")
        result = connection.fetchone()
        if result:
            print(f"Employee with first name '{self.first_name}' and last name '{self.last_name}' already exists.")
        else:
            connection.execute(f"INSERT INTO employee(first_name, last_name, age, department, salary) VALUES ('{self.first_name}', '{self.last_name}', {self.age}, '{self.department}', {self.salary})")
            connection.execute('commit')
            print('Record inserted successfully')


    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}"
    
    @classmethod
    def get_employee_by_id(cls, emp_id):
        connection.execute(f"SELECT * FROM employee WHERE id = {emp_id}")
        result = connection.fetchone()
        if result:
            emp_id, first_name, last_name, age, department, salary = result
            return cls(emp_id, first_name, last_name, age, department, salary)
        else:
            return None

        
    @property
    def department(self):
        return self.__department


    @department.setter
    def department(self, value):
        self.__department = value
    
    def transfer(self, new_dept):
        self.department = new_dept
        connection.execute(f"UPDATE employee SET department = '{self.department}' WHERE id ='{self.id}'")
        connection.execute('commit')
        print('Record updated successfully')


    def fire(self):
        Employee.employees.remove(self)
        connection.execute(f"DELETE FROM employee WHERE id={self.id}")
        connection.execute('commit')
        print('Record deleted successfully')
        
    @classmethod    
    def show(cls):
        print('Data From Database')
        connection.execute('SELECT * FROM employee')
        all_employees = connection.fetchall()
        for employee in all_employees:
            print(employee)
            
    @staticmethod
    def list_employee():
        print('List of Employees:')
        for employee in Employee.employees:
            print(employee)
        


