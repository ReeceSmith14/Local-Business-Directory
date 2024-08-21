from flask import render_template
from directory import app, db
from directory.models import User, Business, Category

@app.route("/")
def home():
    return render_template("base.html")