import os

from flask import Flask, session, render_template, request, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from helpers import *
from model import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    """Main page"""
    
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password and confirmation match
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # create new user
        new_user = User(username = request.form.get("username"), password = request.form.get("password"))

        session = db()

        session.add(new_user)
        # today = date.today()
        # print(today)
        session.commit()
        # db.commit()

        # unique username constraint violated?
        # if not new_user:
        #     return apology("username taken", 400)

        # Remember which user has logged in
        # session["user_id"] = new_user.id

        # Display a flash message
        flash("Registered!")

        # Redirect user to home page
        return redirect("/")

    # else if user reached route via GET
    else:
        return render_template("register.html")