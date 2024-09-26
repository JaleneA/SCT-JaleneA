from App.models import Review
from App.database import db

def get_all_reviews():
    return Review.query.all()

def get_all_reviews_json():
    reviews = Review.query.all()
    if not reviews:
        return []
    reviews = [review.get_json() for review in reviews]
    return reviews