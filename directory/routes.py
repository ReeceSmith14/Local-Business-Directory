from flask import render_template, request, url_for, redirect, session
from directory import app, db
from directory.models import User, Business

@app.route('/', methods=['GET'])
def home():
    # Retrieve all businesses from the database
    businesses = Business.query.all()
    # Render the home page with the list of businesses
    return render_template('home.html', businesses=businesses)

@app.route('/businesses/add', methods=['GET', 'POST'])
def add():
    # Check if the user is logged in by looking for 'username' in the session
    if 'username' not in session:
        return redirect(url_for('sign_in'))  # Redirect to sign-in if not logged in

    # Retrieve the user object from the database based on the session username
    user = User.query.filter_by(username=session['username']).first()

    # Redirect to sign-in if user is not found in the database
    if not user:
        return redirect(url_for('sign_in'))

    if request.method == 'POST':
        # Get business details from the form submission
        business_name = request.form.get('business_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        website = request.form.get('website')

        # Check for an existing business with the same name, phone, email, or website
        existing_business = Business.query.filter(
            (Business.business_name == business_name) |
            (Business.phone == phone) |
            (Business.email == email)
        ).first()

        # If a duplicate exists, prepare an appropriate error message
        if existing_business:
            error_message = "A business with the same "
            if existing_business.business_name == business_name:
                error_message += "name already exists."
            elif existing_business.phone == phone:
                error_message += "phone number already exists."
            elif existing_business.email == email:
                error_message += "email already exists."
            
            # Re-render the form with the error message
            return render_template('add.html', error=error_message)

        # Create a new business instance with the provided details
        business = Business(
            business_name=business_name,
            business_description=request.form.get('business_description'),
            category_name=request.form.get('category_name'),
            user_id=user.id,  # Associate the business with the current user
            email=email,
            phone=phone,
            website=website,
            image_url=request.form.get('image_url')
        )

        # Add the new business to the database and commit
        db.session.add(business)
        db.session.commit()
        # Redirect to the profile page after successful addition
        return redirect(url_for('profile'))

    # Render the form to add a new business for GET requests
    return render_template('add.html')

@app.route('/businesses/<int:business_id>/edit', methods=['GET', 'POST'])
def edit(business_id):
    # Retrieve the business to edit from the database, or return a 404 error if not found
    business = Business.query.get_or_404(business_id)

    if request.method == 'POST':
        # Get updated business details from the form submission
        business_name = request.form.get('business_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        website = request.form.get('website')

        # Check for existing businesses with the same name, phone, email, or website
        # Exclude the current business being edited
        existing_business = Business.query.filter(
            (Business.id != business_id) & (
                (Business.business_name == business_name) |
                (Business.phone == phone) |
                (Business.email == email)
            )
        ).first()

        # If a duplicate exists, prepare an appropriate error message
        if existing_business:
            error_message = "A business with the same "
            if existing_business.business_name == business_name:
                error_message += "name already exists."
            elif existing_business.phone == phone:
                error_message += "phone number already exists."
            elif existing_business.email == email:
                error_message += "email already exists."
            
            # Re-render the edit form with the error message
            return render_template('edit.html', business=business, error=error_message)

        # Update the business details
        business.business_name = business_name
        business.business_description = request.form.get('business_description')
        business.category_name = request.form.get('category_name')
        business.phone = phone
        business.email = email
        business.website = website
        business.image_url = request.form.get('image_url')

        # Commit the updated business details to the database
        db.session.commit()
        # Redirect to the profile page after successful update
        return redirect(url_for('profile'))

    # Render the edit form for GET requests
    return render_template('edit.html', business=business)

@app.route('/profile', methods=['GET'])
def profile():
    # Check if the user is logged in by looking for 'username' in the session
    if 'username' not in session:
        return redirect(url_for('sign_in'))  # Redirect to sign-in if not logged in

    # Retrieve the user object from the database based on the session username
    user = User.query.filter_by(username=session['username']).first()

    # Redirect to sign-in if the user is not found in the database
    if not user:
        session.pop('username', None)  # Clear invalid session data
        return redirect(url_for('sign_in'))

    # Get the list of businesses associated with the user
    businesses = user.businesses  # Access the user's businesses via the relationship
    
    # Render the profile page with the user's businesses
    return render_template('profile.html', businesses=businesses, user=user)

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    # If a user is already logged in, redirect to the profile page
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        if user:
            return redirect(url_for('profile'))  # Redirect to profile if user is valid in the session
        else:
            # Clear the session if the user in session doesn't exist
            session.pop('username', None)

    if request.method == 'POST':
        # Get the username and password from the form submission
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and if the password is correct
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username  # Set the username in the session
            return redirect(url_for('profile'))  # Redirect to profile after successful sign-in
        else:
            # Render the sign-in page with an error message for invalid credentials
            return render_template('sign-in.html', error='Invalid username or password')

    # Render the sign-in form for GET requests
    return render_template('sign-in.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the username and password from the form submission
        username = request.form['username']
        password = request.form['password']

        # Check if a user with the same username already exists
        user = User.query.filter_by(username=username).first()

        if user:
            # Render the registration page with an error message if the user already exists
            return render_template('register.html', error='User already exists')
        else:
            # Create a new user with the provided username and password
            new_user = User(username=username)
            new_user.set_password(password)

            # Add the new user to the database and commit
            db.session.add(new_user)
            db.session.commit()

            # Set the username in the session and redirect to the profile page
            session['username'] = username
            return redirect(url_for('profile'))

    # Render the registration form for GET requests
    return render_template('register.html')

@app.route('/sign-out')
def sign_out():
    # Clear the username from the session to sign out the user
    session.pop('username', None)
    # Redirect to the sign-in page
    return redirect(url_for('sign_in'))

@app.route('/delete_business/<int:business_id>')
def delete_business(business_id):
    # Retrieve the business to delete from the database or return a 404 error if not found
    business = Business.query.get_or_404(business_id)
    # Delete the business from the database
    db.session.delete(business)
    db.session.commit()
    # Redirect to the profile page after deletion
    return redirect(url_for('profile'))

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    # Retrieve the user to delete from the database or return a 404 error if not found
    user = User.query.get_or_404(user_id)
    # Delete the user from the database
    db.session.delete(user)
    db.session.commit()
    # Redirect to the sign-in page after deletion
    return redirect(url_for('sign_in'))
