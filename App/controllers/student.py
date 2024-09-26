from App.models import Student
from App.database import db

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    students = Student.query.all()
    if not students:
        return []
    students = [student.get_json() for student in students]
    return students

def get_student(student_id):
    student = Student.query.get(student_id)
    if student:
        return student.get_json()
    else:
        return {"error": "Student not found."}
