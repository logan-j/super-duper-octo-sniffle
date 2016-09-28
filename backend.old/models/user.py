import bcrypt

from database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.Text)

    firstname = db.Column(db.String(30))
    middlename = db.Column(db.String(30))
    lastname = db.Column(db.String(30))

    location = db.Column(db.String(100)) # Examples: "Des Moines, IA", "Atlanta, Georgia, USA"

    feeds = db.relationship("Feed")

    def __init__(self, json_data):
        pass

    def hashpw(self, password):
        return bcrypt.hashpw(password, self.password)
