from flask import render_template, request, url_for, redirect, session
from directory import app, db
from directory.models import User, Business
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if "username" in session:
        return render_template('profile.html')
    else:
        return redirect(url_for('signIn'))
    

    return render_template('profile.html')


@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
   
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return render_template('sign-in.html', error='Invalid username or password')

 
    
    # Render the sign-in page for GET requests
    return render_template('sign-in.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            return render_template('register.html', error='User already exists')
        else:
            new_user = User(username=username)
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()

            session['username'] = username

            return redirect(url_for('profile'))

    # Render the registration form for GET requests
    return render_template('register.html')

@app.route('/signOut')
def signOut():
    session.pop('username',None)
    return redirect(url_for('signIn'))
