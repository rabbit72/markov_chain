from app import db
from sqlalchemy.sql import func


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    created_time = db.Column(db.DateTime, server_default=func.current_timestamp())

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f"<User({self.name},{self.password})>"


class Texts(db.Model):
    __tablename__ = "texts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text(10000))
    markov = db.Column(db.String(255))
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_time = db.Column(db.DateTime, server_default=func.current_timestamp())

    def __init__(self, text, markov, user):
        self.text = text
        self.markov = markov
        self.user = user

    def __repr__(self):
        return f"<Text({self.user}, {self.markov})>"
