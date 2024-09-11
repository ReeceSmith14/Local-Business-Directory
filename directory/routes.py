from flask import render_template, request, url_for, redirect, session
from directory import app, db
from directory.models import User, Business
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/', methods=["GET"])
def home():

    businesses = Business.query.all()

    return render_template('home.html', businesses=businesses)
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'username' not in session:
        return redirect(url_for('signIn'))  # Redirect to sign-in if the user is not logged in

    user = User.query.filter_by(username=session['username']).first()  # Retrieve the user from the database

    if not user:
        return redirect(url_for('signIn'))  # Redirect if user not found (shouldn't happen normally)

    if request.method == 'POST':
        business = Business(
            business_name=request.form.get('business_name'),
            business_description=request.form.get('business_description'),
            category_name=request.form.get('category_name'),
            user_id=user.id,  # Assign the user's ID to the new business
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            website=request.form.get('website'),
            image_url=request.form.get('image_url')
        )
        db.session.add(business)
        db.session.commit()
        return redirect(url_for('profile'))  # Redirect to a profile or business list after adding

    return render_template('add.html')


@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if "username" not in session:
        return redirect(url_for('signIn'))  # Redirect to sign-in if the user is not logged in

    # Retrieve the user and their associated businesses
    user = User.query.filter_by(username=session['username']).first()

    if not user:
        session.pop('username', None)  # Clear invalid session data
        return redirect(url_for('signIn'))  # Redirect to sign-in if the user is not found

    # Get the user's businesses
    businesses = user.businesses  # Access the user's businesses via the relationship
    
    return render_template('profile.html', businesses=businesses)




@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()  # Ensure the user exists
        if user:
            return redirect(url_for('profile'))  # Redirect if user is valid in the session
        else:
            # Clear the session if the user in session doesn't exist
            session.pop('username', None)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return render_template('sign-in.html', error='Invalid username or password')

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


