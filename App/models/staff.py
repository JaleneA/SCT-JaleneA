from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suffix = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=True)
    created_by = db.relationship('Staff', remote_side=[id], backref='staff_added', lazy=True)

    def __init__(self, suffix, email, firstname, lastname, is_admin, created_by_id, password):
        self.suffix = suffix
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.is_admin = is_admin
        self.created_by_id = created_by_id
        self.set_password(password)

    def get_json(self):
        return{
            'staff_id': self.id,
            'suffix': self.suffix,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_by': f"{self.created_by.suffix} {self.created_by.firstname} {self.created_by.lastname} ({self.created_by.email})" if self.created_by else None
        }

    def __repr__(self):
        return f"<Staff: {self.suffix} {self.firstname} {self.lastname} | {self.email} | Admin? {self.is_admin}>"

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)