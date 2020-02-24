from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User_model(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_user(self, user):
        self.users.append(p)