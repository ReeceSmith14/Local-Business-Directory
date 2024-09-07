from flask import render_template
from directory import app, db
from directory.models import User, Business, Category

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/singIn')
def signIn():
    return render_template('sign-in.html')