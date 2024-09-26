from App.models import Staff
from App.database import db

def create_staff(suffix, email, firstname, lastname, department, password):
    new_staff = Staff(suffix=suffix, email=email, firstname=firstname, lastname=lastname, department=department, password=password)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff