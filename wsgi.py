import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize)
from App.controllers.student import (get_all_students_json, get_all_students)
from App.controllers.staff import (add_student, login_staff, search_student_by_name)
from App.controllers.admin import create_staff

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

user_cli = AppGroup('user', help='Admin object commands') 
# eg : flask user <command>

# CREATE ADMIN ACCOUNT
@user_cli.command("create", help="Creates an admin account")
@click.argument("email", default="rob@mail.com")
@click.argument("firstname", default="rob")
@click.argument("lastname", default="bob")
@click.argument("password", default="robpass")
def create_user_command(email, firstname, lastname, password):
    create_user(email, firstname, lastname, password)
    print(f'{firstname + " " + lastname} created!')

# LIST ALL USERS IN DATABASE
@user_cli.command("list", help="Lists all users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users_json())
    else:
        print(get_all_users())

app.cli.add_command(user_cli)

'''
Admin Commands
'''

admin_cli = AppGroup('admin', help='Admin object commands') 
# eg : flask admin <command>

@admin_cli.command("create_staff", help="Creates a staff account")
@click.argument("suffix", default="Mr.")
@click.argument("email", default="rob@mail.com")
@click.argument("firstname", default="Rock")
@click.argument("lastname", default="Hobber")
@click.argument("department", default="Department of Computing and Information Technology")
@click.argument("password", default="robpass")
def create_staff_command(suffix, email, firstname, lastname, department, password):
    create_staff(suffix, email, firstname, lastname, department, password)
    print(f"Staff account created for {suffix} {lastname}!")

# @admin_cli.command("create_staffs", help="Creates a staff account")
# @click.argument("suffix", default="Mr.")
# @click.argument("email", default="rob@mail.com")
# @click.argument("firstname", default="Rock")
# @click.argument("lastname", default="Hobber")
# @click.argument("department", default="Department of Computing and Information Technology")
# @click.argument("password", default="robpass")
# def create_staff_command(suffix, email, firstname, lastname, department, password):
#     create_staff(suffix, email, firstname, lastname, department, password)
#     print(f"Staff accounts created!")

app.cli.add_command(admin_cli)

'''
Staff Commands
'''

staff_cli = AppGroup('staff', help='Staff object commands') 
# eg : flask staff <command>

# STAFF LOGIN
@staff_cli.command("login", help="Logs into a staff account")
@click.argument("email", default="rob@mail.com")
@click.argument("password", default="robpass")
def login_staff_command(email, password):
    login_staff(email, password)

# STAFF ADD STUDENT
@staff_cli.command("add_student", help="Adds a student account")
@click.argument("firstname", default="Bobby")
@click.argument("lastname", default="Butterbeard")
@click.argument("email", default="bobby.butterbeard@mail.com")
def add_student_command(firstname, lastname, email):
    add_student(firstname, lastname, email)
    print(f"Student added!")

# STAFF VIEW STUDENTS
@staff_cli.command("view_students", help="Lists all students in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_students_json())
    else:
        print(get_all_students()())

# STAFF SEARCH STUDENT
@staff_cli.command("search_students", help="Searches for a specific student")
@click.argument("firstname", default="bobby")
def search_student_command(firstname):
    search_student_by_name(firstname)
    
app.cli.add_command(staff_cli)