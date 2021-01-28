from app import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'User'
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    confirmpassword = db.Column(db.String(100))
