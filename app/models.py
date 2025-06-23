# models.py — for SQLAlchemy models if database is used
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    favorite_city = db.Column(db.String(100))
