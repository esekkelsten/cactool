from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
 
db = SQLAlchemy()

class User(db.Model):
    ID = db.Column(db.String(512), unique=True, primary_key=True)
    admin = db.Column(db.Boolean)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(1024))
    firstname = db.Column(db.String(50))
    surname = db.Column(db.String(50))