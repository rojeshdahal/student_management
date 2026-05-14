# Student Management System

A command-line based Student Management System built with **Python** and **SQLite**.

This project was built to practice Python fundamentals before moving into Django. It covers object-oriented thinking, database operations, SQL queries, and CRUD functionality.

---

## Features

This application supports:

* Add a student
* View all students
* Search student by name
* Update student marks
* Delete student records

---

## Concepts Learned

This project helped me practice:

### Python Fundamentals

* Functions
* Loops
* User input
* Variables
* Data structures

### Database Concepts

* Connecting Python with SQLite
* Creating tables
* Executing SQL queries
* Using placeholders (`?`)
* Committing transactions

### CRUD Operations

* **Create** → Insert new students
* **Read** → View/Search students
* **Update** → Modify student marks
* **Delete** → Remove student records

---

## Project Structure

```bash
student-management/
│
├── main.py
├── students.db
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <https://github.com/rojeshdahal/student_management.git>
cd student-management
```

Run the project:

```bash
python main.py
```

---

## Database Schema

The students table contains:

| Column | Type    |
| ------ | ------- |
| id     | INTEGER |
| name   | TEXT    |
| age    | INTEGER |
| marks  | INTEGER |

---

## Example Menu

```text
1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Delete Student
6. Exit
```

---

## Future Improvements

Possible features to add:

* Input validation
* Prevent duplicate student entries
* Search by ID
* Sort by marks
* Export student data to JSON or CSV

---

## What I Learned

This project helped me understand how Python interacts with databases and gave me hands-on experience with SQL queries, data persistence, and application logic.
