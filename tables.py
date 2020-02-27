import os
from flask import Flask, request, render_template
from model import User, db

app = Flask(__name__)
app.config["SQLACHEMY_DATABASE_URL"] = os.getenv("DATABASE_URL")
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def create_tables():
    db.create_all()