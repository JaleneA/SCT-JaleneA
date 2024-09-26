from App.controllers.student import get_student
from App.models import Staff, Student, Review
from App.database import db

def login_staff(email, password):
    staff_member = Staff.login(email, password)
    if staff_member:
        print(f"Welcome, {staff_member.suffix} {staff_member.lastname}!")
    else:
        print("Login failed. Please check your email and password.")

def add_student (student_id, firstname, lastname, email):
    new_student = Student(student_id, firstname=firstname, lastname=lastname, email=email)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def search_student_by_student_id(student_id):
    return get_student(student_id)

def add_review(student_id, text):
    review_text = ' '.join(text)
    student = Student.query.filter_by(student_id=student_id).first()
    
    if student:
        student_review = Review(text=review_text, student_id=student_id)
        db.session.add(student_review)
        db.session.commit()
        print(f"Review added for student {student.firstname} {student.lastname}: {review_text}")
    else:
        print(f"Student with ID {student_id} not found.")