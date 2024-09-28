import os, csv
from flask import Flask, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from App.database import init_db
from App.config import load_config
from App.models import db, Student, Review

def create_app(overrides={}):
    app = Flask(__name__)
    load_config(app, overrides)
    CORS(app)
    init_db(app)
    app.app_context().push()
    return app

# uncomment when models are implemented
def parse_students():
  with open('App/students.csv', encoding='unicode_escape') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
      student = Student(student_id=row['student_id'],
                  firstname=row['firstname'],
                  lastname=row['lastname'],
                  email=row['email'])
      db.session.add(student)
  db.session.commit()

def parse_reviews():
  with open('App/reviews.csv', encoding='unicode_escape') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
      review = Review(text=row['text'],
                      student_id=int(row['student_id']),
                      reviewer_id=int(row['reviewer_id']))
      db.session.add(review)
    db.session.commit()