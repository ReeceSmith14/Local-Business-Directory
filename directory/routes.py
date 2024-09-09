from flask import render_template, request, url_for, redirect, flash
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

@app.route('/signIn')
def signIn():
    return render_template('sign-in.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form.get("email")

        # Check if the email is already in use
        if User.query.filter_by(email=email).first():
            flash('Registration failed, email already used', 'fail')
            return redirect(url_for('register'))
        
        # Create a new user and add to the database
        user = User(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            user_name=request.form.get("user_name"),
            email=email,
            password=request.form.get("password"),  # Remember to hash passwords in production
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful!", "success")
        return redirect(url_for('signIn'))  # Redirect to the sign-in page after successful registration

    # Render the registration template for GET requests
    return render_template('register.html')