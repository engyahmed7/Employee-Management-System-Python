# Employee Management System

#### Description:
This repository contains a Python-based Employee Management System that allows users to perform various administrative tasks related to managing employees. The system is designed to simplify the process of adding, updating, and removing employee records, as well as providing functionalities for managing managers.


#### Features:
- **Add Employee:** Add new employee records by providing details such as ID, name, age, department, and salary.
  
- **Add Manager:** Create manager profiles with additional information such as the department they oversee.
  
- **Show All:** Display a comprehensive list of all employees and managers currently registered in the system.
  
- **Transfer Employee:** Transfer employees between departments by specifying their ID and the new department.
  
- **Fire Employee:** Remove employees from the system by specifying their ID.


#### Installation:
1. Clone the repository to your local machine.
2. Ensure you have Python and MySQL installed.
3. Create a MySQL database named `pythonLabs`.
4. Import the database schema using the SQL script provided in the `db` folder.
5. Update the database connection details in the `db.py` file if necessary.


#### Usage:
1. Run the `index.py` file to launch the Employee Management System.
2. Follow the on-screen prompts to perform various operations.
3. Choose options from the menu to add employees, managers, view records, transfer employees, or terminate employees.


#### Repository Structure:
- **classes:** Contains Python class definitions for Employee and Manager.
- **db:** Includes the SQL script for database schema creation.
- **index.py:** Main Python script for running the Employee Management System.
- **db.py:** Database connection configuration file.
- **README.md:** Documentation providing information about the project.


