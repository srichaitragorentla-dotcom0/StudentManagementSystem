from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass123!",
    database="student_management"
)

cursor = connection.cursor()


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ADD STUDENT ----------------

@app.route("/add", methods=["GET", "POST"])
def add_student():

    message = ""

    if request.method == "POST":

        student_id = int(request.form["id"])
        name = request.form["name"].strip().title()
        age = int(request.form["age"])
        course = request.form["course"]
        marks = float(request.form["marks"])

        query = """
            INSERT INTO students
            (id, name, age, course, marks)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            student_id,
            name,
            age,
            course,
            marks
        )

        try:
            cursor.execute(query, values)
            connection.commit()

            message = "Student added successfully!"

        except mysql.connector.IntegrityError:

            connection.rollback()

            message = "Student ID already exists!"

    return render_template(
        "add_student.html",
        message=message
    )


# ---------------- VIEW STUDENTS ----------------

@app.route("/view")
def view_students():

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    return render_template(
        "view_students.html",
        students=students
    )


# ---------------- SEARCH STUDENT ----------------

@app.route("/search", methods=["GET", "POST"])
def search_student():

    student = None
    searched = False

    if request.method == "POST":

        student_id = int(request.form["id"])

        query = """
            SELECT * FROM students
            WHERE id = %s
        """

        cursor.execute(
            query,
            (student_id,)
        )

        student = cursor.fetchone()

        searched = True

    return render_template(
        "search_student.html",
        student=student,
        searched=searched
    )


# ---------------- UPDATE STUDENT ----------------
@app.route("/update", methods=["GET", "POST"])
def update_student():

    message = ""

    if request.method == "POST":

        student_id = int(request.form["id"])
        field = request.form["field"]
        value = request.form["value"].strip()

        # Check whether student exists

        query = """
            SELECT * FROM students
            WHERE id = %s
        """

        cursor.execute(query, (student_id,))

        student = cursor.fetchone()

        if not student:

            message = "Student not found."

        else:

            if field == "name":

                value = value.title()

                query = """
                    UPDATE students
                    SET name = %s
                    WHERE id = %s
                """

                cursor.execute(
                    query,
                    (value, student_id)
                )

            elif field == "age":

                value = int(value)

                query = """
                    UPDATE students
                    SET age = %s
                    WHERE id = %s
                """

                cursor.execute(
                    query,
                    (value, student_id)
                )

            elif field == "course":

                value = value.upper()

                query = """
                    UPDATE students
                    SET course = %s
                    WHERE id = %s
                """

                cursor.execute(
                    query,
                    (value, student_id)
                )

            elif field == "marks":

                value = float(value)

                query = """
                    UPDATE students
                    SET marks = %s
                    WHERE id = %s
                """

                cursor.execute(
                    query,
                    (value, student_id)
                )

            connection.commit()

            message = "Student updated successfully!"

    return render_template(
        "update_student.html",
        message=message
    )


# ---------------- DELETE STUDENT ----------------

@app.route("/delete", methods=["GET", "POST"])
def delete_student():

    message = ""
    search = request.args.get("search", "").strip()

    if request.method == "POST":

        student_ids = request.form.getlist("student_ids")

        if not student_ids:
            message = "Please select at least one student."

        else:
            placeholders = ",".join(["%s"] * len(student_ids))

            query = f"""
                DELETE FROM students
                WHERE id IN ({placeholders})
            """

            cursor.execute(query, tuple(student_ids))
            deleted_count = cursor.rowcount
            connection.commit()

            message = f"{deleted_count} student(s) deleted successfully!"

    if search:
        query = """
            SELECT * FROM students
            WHERE CAST(id AS CHAR) LIKE %s
               OR name LIKE %s
            ORDER BY id
        """
        term = f"%{search}%"
        cursor.execute(query, (term, term))
    else:
        cursor.execute("SELECT * FROM students ORDER BY id")

    students = cursor.fetchall()

    return render_template(
        "delete_student.html",
        students=students,
        message=message,
        search=search
    )

# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(
        port=5001,
        debug=True
    )