import os
import requests

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Goodreads API
#api_key = os.getenv("APP_API_KEY")

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL_P1"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL_P1"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    """Main page"""
    
    return render_template("index.html")