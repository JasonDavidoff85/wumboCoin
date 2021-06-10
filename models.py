from db import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    passHash = db.Column(db.String(64), nullable=False)
    pubKey = db.Column(db.String(64))
    balance = db.Column(db.Integer, nullable=False)
