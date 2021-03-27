from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

from messageboard import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10))
    body = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default = datetime.now, index = True)