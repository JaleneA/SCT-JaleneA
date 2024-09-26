from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)

    def __init__(self, text, student_id):
      self.text = text
      self.student_id = student_id

    def get_json(self):
        return{
            'student_id': self.student_id,
            'text': self.text
        }