from .staff import create_staff
from App.database import db

def initialize():
    db.drop_all()
    db.create_all()
    create_staff('Mr.', 'Bob', 'Bobberson', 'bob.bobberson@mail.com', True, 'bobpass', 0)
