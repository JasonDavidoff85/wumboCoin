from db import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default="true")
    privKey = db.Column(db.String(64))
    passHash = db.Column(db.String(64), nullable=False)

    @property
    def identity(self):
        return self.id

    @property
    def rolenames(self):
        try:
            return self.roles.split(",")
        except Exception:
            return []

    @property
    def password(self):
        return self.passHash

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)
    
    def is_valid(self):
        return self.is_active
    
class Blockchain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wub_file = db.Column(db.String(80), unique=True, nullable=False)
    current = db.Column(db.Boolean, default=True, server_default="true")
    prevBlockHash = db.Column(db.String(256))
    blockHash = db.Column(db.String(256))

    @property
    def identity(self):
        return self.id

    @classmethod
    def lookup(cls, id):
        return cls.query.filter_by(id=id).one_or_none()
    
    @classmethod
    def get_current(cls):
        return cls.query.filter_by(current=True).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)
    
    def is_current(self):
        return self.current

