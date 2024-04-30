from classes.employee import Employee
from classes.manager import Manager

def add_employee():
    emp_id = input("ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    salary = int(input("Salary: "))
    emp = Employee(emp_id, first_name, last_name, age, department, salary)
    print(emp)
    

def add_manager():
    emp_id = input("ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    salary = int(input("Salary: "))
    managed_department = input("Managed Department: ")
    manager = Manager(emp_id,first_name, last_name, age, department, salary, managed_department)
    print(manager)
    
    
def show_all():
    Employee.show()
    Manager.show()
    
def transfer_employee():
    emp_id = int(input("Enter ID of Employee: "))
    new_dept = input("Enter New Department: ")
    emp = Employee.get_employee_by_id(emp_id)
    print(emp)
    if emp:
        emp.transfer(new_dept)
        print("Employee transferred successfully.")
    else:
        print("Employee not found.")

    

def fire_employee():
    emp_id = int(input("Enter the ID of the employee to fire: "))
    emp = Employee.get_employee_by_id(emp_id)
    if emp:
        emp.fire()
    else:
        print("Employee not found.")

def menu():
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Show All")
    print("4. Transfer Employee")
    print("5. Fire Employee")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        add_employee()
    elif choice == '2':
        add_manager()
    elif choice == '3':
        show_all()
    elif choice == '4':
        transfer_employee()
    elif choice == '5':
        fire_employee()
    elif choice == '6':
        exit()
    else:
        print("Invalid choice. Please try again.")
        

while True:
    menu()
    
    