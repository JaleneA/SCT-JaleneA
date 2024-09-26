from .user import User
from App.database import db

class Staff(User):
    suffix = db.Column(db.String, nullable=False, default='')
    department = db.Column(db.String, nullable=False, default='Unassigned')

    def __init__(self, suffix, email, firstname, lastname, password, department):
        super().__init__(email, firstname, lastname, password)
        self.suffix = suffix
        self.department = department

    def get_json(self):
        user_data = super().get_json()
        user_data.update({'department': self.department})
        user_data.update({'suffix': self.suffix})
        return user_data

    @classmethod
    def login(cls, email, password):
        staff_member = cls.query.filter_by(email=email).first()
        if staff_member and staff_member.check_password(password):
            return staff_member
        return None