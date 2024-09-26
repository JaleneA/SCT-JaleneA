from .user import User
from .staff import Staff
from App.database import db

class Admin(User):
    activity_log = db.Column(db.String, nullable=True)

    def __init__(self, email, password):
        super().__init__(email, password)

    def get_json(self):
        user_data = super().get_json()
        user_data.update({'contact': self.contact})
        return user_data

    # def manage_staff_list():

    # def manage_student_list():
