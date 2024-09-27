from .staff import create_staff
from App.database import db

def initialize():
    db.drop_all()
    db.create_all()
    create_staff('Mr.','staff1@mail.com', 'Bob', 'Bobberson', 'DCIT', True, 'bobpass')
