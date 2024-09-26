from .user import User
from .staff import Staff
from App.database import db

class Admin(User):
    contact = db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        super().__init__(email, password)

    def get_json(self):
        user_data = super().get_json()
        user_data.update({'contact': self.contact})
        return user_data

    # def manage_staff_list():

    # def manage_student_list():

    def create_staff_account(self, email, password, department):
        new_staff = Staff(email=email, password=password, department=department)
        db.session.add(new_staff)
        db.session.commit()
        return new_staff