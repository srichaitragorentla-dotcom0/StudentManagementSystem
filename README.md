# 🎓 Student Management System

A simple and user-friendly **Student Management System** developed as a web-based application using **Python, Flask, HTML, CSS, and MySQL**.

The main purpose of this project is to make student record management easier by providing a web interface where users can **add, view, search, update, and delete student information**.

---

## 📌 About the Project

Managing student records manually can be time-consuming and difficult to maintain. This project provides a simple digital solution for managing student information efficiently.

The application connects a **Flask-based Python backend** with a **MySQL database** to store and manage student records.

Users can perform different operations on student data through a simple web interface without directly interacting with the database.

---

## ✨ Features

### ➕ Add Student
Users can add a new student by providing details such as:

- Student ID
- Name
- Age
- Course
- Marks

### 👀 View Students
Displays the student records stored in the database in an organized format.

### 🔍 Search Student
Users can search for a specific student using their **Student ID**.

### ✏️ Update Student
Existing student information can be modified whenever changes are required.

### 🗑️ Delete Student
Student records can be removed from the database when they are no longer required.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Backend programming |
| **Flask** | Web application framework |
| **MySQL** | Database management |
| **HTML** | Web page structure |
| **CSS** | Styling and user interface |
| **Git & GitHub** | Version control and project hosting |

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────┐
                    │     Browser     │
                    │   HTML + CSS    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Flask       │
                    │    Backend      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      MySQL      │
                    │    Database     │
                    └─────────────────┘
🔄 How the System Works
The user opens the Student Management System in a browser.
The user selects an operation such as Add, View, Search, Update, or Delete.
The request is sent to the Flask backend.
Flask processes the request.
The backend communicates with the MySQL database.
The required student information is retrieved or modified.
The result is displayed back to the user through the web interface.

💡 Conclusion

The Student Management System is a beginner-friendly web application that demonstrates how a Python backend, web interface, and relational database can work together.

It provides the basic functionality required to manage student records while also serving as a practical project for learning Python, Flask, MySQL, HTML, CSS, CRUD operations, and Git/GitHub.

👨‍💻 Author

Srichaitra Gorentla

GitHub:
https://github.com/srichaitragorentla-dotcom0
