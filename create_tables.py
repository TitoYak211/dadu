import os
from flask import Flask, request, render_template
from model import *

app = Flask(__name__)
app.config["SQLACHEMY_DATABASE_URL"] = os.getenv("DATABASE_URL")
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()