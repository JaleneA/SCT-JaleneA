from .user import User
from App.database import db

class Staff(User):
    department = db.Column(db.String, nullable=False)

    def __init__(self, email, password, department):
        super().__init__(email, password)
        self.department = department

    def get_json(self):
        user_data = super().get_json()
        user_data.update({'department': self.department})
        return user_data