from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    github = db.Column(db.String(30))
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


def add_user_to_database(user):
    db.session.add(user)
    db.session.commit()
