from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    reviewer = db.relationship('Staff', backref='reviewed', lazy=True)

    def __init__(self, text, student_id, reviewer_id):
      self.text = text
      self.student_id = student_id
      self.reviewer_id = reviewer_id

    def get_json(self):
        return{
            'student_id': self.student_id,
            'text': self.text,
             'reviewer': f"{self.reviewer.suffix} {self.reviewer.firstname} {self.reviewer.lastname}"
        }

    def __repr__(self):
       return f"\n<Review: {self.text} \n Written By: {self.reviewer.suffix} {self.reviewer.firstname} {self.reviewer.lastname}>\n"