import mysql.connector # importing the module
# creating a connection 
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "vyas2007",
    port = 3306
)
# checking the connection
if connection.is_connected():
    print("Connection successful")
else:
    print("connection failed")
# creating a cursdor object
cursor = connection.cursor()
# creating database
cursor.execute("CREATE DATABASE IF NOT EXISTS college")
connection.commit() # using the database
print("Database created successfully")
cursor.execute("USE college")

# creating a table students 
cursor.execute("CREATE  TABLE IF NOT EXISTS students(ID int auto_increment primary key, Name VARCHAR(50), Subject VARCHAR(50), semester int)")
connection.commit()
print("Table created successfully")

# creating a function to insert into the table
def add_student():
    name = input("Enter your name:")
    subject = input("Enter your subject:")
    semester = int(input("Enter the semester:"))
    query = ("INSERT INTO students(Name,Subject,semester)values(%s,%s,%s)")
    values = (name, subject, semester)
    cursor.execute(query,values)
    connection.commit()
    print("Data entered successfully!")
# creating a function to view data
def view_data():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print("----Student Details----")
    for row in records:
        print(row)
# creating a function to delete data
def Delete_student():
    id = int(input("ENTER THE id of student "))
    query = ("DELETE FROM students WHERE ID = %s")
    values = (id,)
    cursor.execute(query,values)
    connection.commit()
    print("Student data deleted successfully!")
# creating a function for updating the student data
def update_data():
    id = int(input("Enter the id of student:"))
    name = input("enter the name of student:")
    subject = input("Enter the subject of student:")
    semester = int(input("Enter the semester of student:"))
    query = ("UPDATE students SET Name = %s, Subject = %s, semester = %s Where ID = %s")
    values = (name, subject, semester, id)
    cursor.execute(query,values)
    connection.commit()
    print("Student Data updated Successfully!")
# creating a menu for the user
while True:
    print("----Student Management System----")
    print("1 Add Student\n2 View Student\n3 Update Student Data\n4 Delete Student\n5 Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_data()
    elif choice == 3:
        update_data()
    elif choice == 4:
        Delete_student()
    elif choice == 5:
        print("Exiting the programme...")
        break
    else:
        print("Invalid Operation! Please try again.")
# closing the connection
cursor.close()
connection.close()
print("Connection closed successfully!")