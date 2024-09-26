from App.models import Staff, Student
from App.database import db

def login_staff(email, password):
    staff_member = Staff.login(email, password)
    if staff_member:
        print(f"Welcome, {staff_member.suffix} {staff_member.lastname}!")
    else:
        print("Login failed. Please check your email and password.")

def add_student (firstname, lastname, email):
    new_student = Student(firstname=firstname, lastname=lastname, email=email)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def search_student_by_name(firstname):
    return Student.query.filter_by(firstname=firstname).first()