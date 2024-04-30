import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='pythonLabs'
)

connection = mydb.cursor()
# print(connection)