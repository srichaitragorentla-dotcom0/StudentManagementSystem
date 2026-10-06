import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

connection= mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
)

cursor =connection.cursor()



# ---------------- ADD STUDENT ----------------

def add_student():

    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    query = """
        INSERT INTO students (id, name, age, course, marks)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (student_id, name, age, course, marks)

    cursor.execute(query, values)
    connection.commit()

    print("Student added successfully!")


# ---------------- VIEW STUDENTS ----------------

def view_students():

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found.")
        return

    print("\n----------- STUDENT RECORDS -----------")

    for student in students:

        print(
            "ID:", student[0],
            "| Name:", student[1],
            "| Age:", student[2],
            "| Course:", student[3],
            "| Marks:", student[4]
        )


# ---------------- SEARCH STUDENT ----------------

def search_student():

    student_id = int(input("Enter student ID to search: "))

    query = "SELECT * FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if student:

        print("\nStudent Found!")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("Marks:", student[4])

    else:

        print("Student not found.")


# ---------------- UPDATE STUDENT ----------------

def update_student():

    student_id = int(input("Enter student ID to update: "))

    # First check whether student exists
    query = "SELECT * FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if not student:

        print("Student not found.")
        return

    print("\nCurrent student details:")

    print("Name:", student[1])
    print("Age:", student[2])
    print("Course:", student[3])
    print("Marks:", student[4])

    print("\nEnter new details:")

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    marks = float(input("Enter new marks: "))

    query = """
        UPDATE students
        SET name = %s,
            age = %s,
            course = %s,
            marks = %s
        WHERE id = %s
    """

    values = (name, age, course, marks, student_id)

    cursor.execute(query, values)
    connection.commit()

    print("Student updated successfully!")


# ---------------- DELETE STUDENT ----------------

def delete_student():

    student_id = int(input("Enter student ID to delete: "))

    # Check whether student exists
    query = "SELECT * FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if not student:

        print("Student not found.")
        return

    print("\nStudent found:")
    print("Name:", student[1])
    print("Course:", student[3])

    confirm = input("Are you sure you want to delete this student? (yes/no): ")

    if confirm.lower() == "yes":

        query = "DELETE FROM students WHERE id = %s"

        cursor.execute(query, (student_id,))
        connection.commit()

        print("Student deleted successfully!")

    else:

        print("Delete operation cancelled.")


# ---------------- MAIN MENU ----------------

while True:

    print("\n===================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        update_student()

    elif choice == "5":

        delete_student()

    elif choice == "6":

        print("Program ended.")
        break

    else:

        print("Invalid choice. Please try again.")


# ---------------- CLOSE CONNECTION ----------------

cursor.close()
connection.close()