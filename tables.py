import os
from flask import Flask, request, render_template
from model import User, User

app = Flask(__name__)
app.config["SQLACHEMY_DATABASE_URL"] = os.getenv("DATABASE_URL")
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()