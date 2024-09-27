from App.controllers.student import get_student
from App.models import Student, Review
from App.models import staff
from App.database import db

def create_staff(suffix, email, firstname, lastname, department, is_admin, password):
    newstaff = staff(suffix=suffix, email=email, firstname=firstname, lastname=lastname, department=department, is_admin=is_admin, password=password)
    db.session.add(newstaff)
    db.session.commit()
    return newstaff

def get_staff_by_staffname(staffname):
    return staff.query.filter_by(staffname=staffname).first()

def get_staff(id):
    return staff.query.get(id)

def get_all_staffs():
    return staff.query.all()

def get_all_staffs_json():
    staffs = staff.query.all()
    if not staffs:
        return []
    staffs = [staff.get_json() for staff in staffs]
    return staffs

def update_staff(id, staffname):
    staff = get_staff(id)
    if staff:
        staff.staffname = staffname
        db.session.add(staff)
        return db.session.commit()
    return None

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