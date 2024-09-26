from App.database import db

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False, unique=True)
    reviews = db.relationship('Review', backref='student', lazy=True)

    def __init__(self, student_id, email, firstname, lastname):
        self.student_id = student_id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    def get_json(self):
        return{
            'student_id': self.student_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'reviews': [review.text for review in self.reviews]
        }