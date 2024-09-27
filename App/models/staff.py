from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suffix = db.Column(db.String, nullable=False, default='')
    department = db.Column(db.String, nullable=False, default='Unassigned')
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean(False), nullable=False)

    def __init__(self, suffix, email, firstname, lastname, department, is_admin, password):
        self.suffix = suffix
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.department = department
        self.is_admin = is_admin
        self.set_password(password)

    def get_json(self):
        return{
            'staff_id': self.id,
            'staffname': self.staffname,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)