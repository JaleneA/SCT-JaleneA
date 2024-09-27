import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app, parse_students, parse_reviews
from App.controllers import ( create_staff, get_all_staffs_json, get_all_staffs, initialize, add_student, search_student_by_student_id, add_review)
from App.controllers.student import (get_all_students_json, get_all_students)
from App.controllers.reviews import (get_all_reviews, get_all_reviews_json)

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    parse_reviews()
    print('database intialized')

'''
Staff Commands
'''

staff_cli = AppGroup('staff', help='Admin object commands') 
# eg : flask staff <command>

# CREATE STAFF ACCOUNT
@staff_cli.command("create", help="Creates an staff account")
@click.argument("suffix", default="Mr.")
@click.argument("firstname", default="Rob")
@click.argument("lastname", default="Bob")
@click.argument("department", default="DCIT")
@click.argument("email", default="rob@mail.com")
@click.argument("is_admin", default=False)
@click.argument("password", default="robpass")
def create_staff_command(suffix, firstname, lastname, email, department, is_admin, password):
    create_staff(suffix, firstname, lastname, department, email, is_admin, password)
    print(f'Staff Account for {suffix + " " + firstname + " " + lastname} Created!')

# LIST ALL staffS IN DATABASE
@staff_cli.command("list", help="Lists all staffs in the database")
@click.argument("format", default="string")
def list_staff_command(format):
    if format == 'string':
        print(get_all_staffs_json())
    else:
        print(get_all_staffs())

# STAFF ADD STUDENT
@staff_cli.command("add_student", help="Adds a student record")
@click.argument("firstname", default="Bobby")
@click.argument("lastname", default="Butterbeard")
@click.argument("email", default="bobby.butterbeard@mail.com")
def add_student_command(firstname, lastname, email):
    add_student(firstname, lastname, email)
    print(f"Student added!")

# STAFF ADD CSV OF STUDENTS
@staff_cli.command("add_students", help="Adds multiple student records from a CSV")
def add_students_command():
    parse_students() # Call the parse_students function to process the CSV
    print(f"All students added from CSV!")

# STAFF VIEW ALL STUDENTS
@staff_cli.command("view_students", help="Lists all students in the database")
@click.argument("format", default="string")
def list_staff_command(format):
    if format == 'string':
        print(get_all_students_json())
    else:
        print(get_all_students()())

# STAFF SEARCH SPECIFIC STUDENT BY ID
@staff_cli.command("search_student", help="Searches for a specific student")
@click.argument("student_id", default="816034565")
def search_student_command(student_id):
    print(search_student_by_student_id(student_id))

# STAFF REVIEW STUDENT
@staff_cli.command("review", help="Add a review for a student")
@click.argument("student_id")
@click.argument("text", nargs=-1)  # Use nargs=-1 to accept multiple words as a single argument
def review_student_command(student_id, text):
    add_review(student_id, text)

# LIST ALL STUDENT REVIEWS
@staff_cli.command("list_reviews", help="List all student reviews")
@click.argument("format", default="string")
def list_review_command(format):
    if format == 'string':
        print(get_all_reviews_json())
    else:
        print(get_all_reviews())

app.cli.add_command(staff_cli)