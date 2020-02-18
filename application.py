import os
import requests
from flask import Flask, request, render_template, url_for, flash, jsonify, redirect, session, json, Response, views, make_response, Markup
from flask_session import Session
from functools import wraps
from werkzeug.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import create_database, database_exists

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine("sqlite:///data.db", encoding='latin1', echo=True)
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=["GET"])
def index():
    """Show stocks of stocks"""
    return render_template("index.html", **locals())