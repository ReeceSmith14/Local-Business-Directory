from flask import render_template, request, url_for, redirect, session
from directory import app, db
from directory.models import User, Business

@app.route('/', methods=['GET'])
def home():
    """Render the home page with a list of all businesses.

    Handles GET requests to the root URL. Retrieves all businesses from 
    the database and renders the 'home.html' template with the list.
    
    Returns:
        Response: Rendered 'home.html' template with businesses.
    """
    businesses = Business.query.all()  # Retrieve all businesses from the database
    return render_template('home.html', businesses=businesses)

@app.route('/businesses/add', methods=['GET', 'POST'])
def add():
    """Handle the addition of a new business.

    Handles both GET and POST requests to the '/businesses/add' URL. 
    For GET requests, it renders the form to add a new business. For POST 
    requests, it processes the form submission, checks for duplicates, and 
    saves the new business to the database if no duplicates are found.
    
    Returns:
        Response: Redirects to the profile page after successful addition 
        or re-renders the form with an error message if validation fails.
    """
    if 'username' not in session:
        return redirect(url_for('sign_in'))  # Redirect to sign-in if not logged in

    user = User.query.filter_by(username=session['username']).first()
    if not user:
        return redirect(url_for('sign_in'))  # Redirect to sign-in if user not found

    if request.method == 'POST':
        business_name = request.form.get('business_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        website = request.form.get('website')

        existing_business = Business.query.filter(
            (Business.business_name == business_name) |
            (Business.phone == phone) |
            (Business.email == email)
        ).first()

        if existing_business:
            error_message = "A business with the same "
            if existing_business.business_name == business_name:
                error_message += "name already exists."
            elif existing_business.phone == phone:
                error_message += "phone number already exists."
            elif existing_business.email == email:
                error_message += "email already exists."
            
            return render_template('add.html', error=error_message)

        business = Business(
            business_name=business_name,
            business_description=request.form.get('business_description'),
            category_name=request.form.get('category_name'),
            user_id=user.id,
            email=email,
            phone=phone,
            website=website,
            image_url=request.form.get('image_url')
        )

        db.session.add(business)
        db.session.commit()
        return redirect(url_for('profile'))

    return render_template('add.html')

@app.route('/businesses/<int:business_id>/edit', methods=['GET', 'POST'])
def edit(business_id):
    """Handle the editing of an existing business.

    Handles both GET and POST requests to the '/businesses/<business_id>/edit' URL. 
    For GET requests, it renders the form to edit the specified business. For POST 
    requests, it processes the form submission, checks for duplicates (excluding 
    the current business), and updates the business details if no duplicates are found.
    
    Args:
        business_id (int): The ID of the business to edit.
    
    Returns:
        Response: Redirects to the profile page after successful update or 
        re-renders the form with an error message if validation fails.
    """
    business = Business.query.get_or_404(business_id)

    if request.method == 'POST':
        business_name = request.form.get('business_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        website = request.form.get('website')

        existing_business = Business.query.filter(
            (Business.id != business_id) & (
                (Business.business_name == business_name) |
                (Business.phone == phone) |
                (Business.email == email)
            )
        ).first()

        if existing_business:
            error_message = "A business with the same "
            if existing_business.business_name == business_name:
                error_message += "name already exists."
            elif existing_business.phone == phone:
                error_message += "phone number already exists."
            elif existing_business.email == email:
                error_message += "email already exists."
            
            return render_template('edit.html', business=business, error=error_message)

        business.business_name = business_name
        business.business_description = request.form.get('business_description')
        business.category_name = request.form.get('category_name')
        business.phone = phone
        business.email = email
        business.website = website
        business.image_url = request.form.get('image_url')

        db.session.commit()
        return redirect(url_for('profile'))

    return render_template('edit.html', business=business)

@app.route('/profile', methods=['GET'])
def profile():
    """Render the profile page for the logged-in user.

    Handles GET requests to the '/profile' URL. Checks if the user is logged in, 
    retrieves the user's associated businesses, and renders the 'profile.html' 
    template with the user's businesses.

    Returns:
        Response: Rendered 'profile.html' template with user's businesses.
    """
    if 'username' not in session:
        return redirect(url_for('sign_in'))  # Redirect to sign-in if not logged in

    user = User.query.filter_by(username=session['username']).first()
    if not user:
        session.pop('username', None)  # Clear invalid session data
        return redirect(url_for('sign_in'))

    businesses = user.businesses
    return render_template('profile.html', businesses=businesses, user=user)

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    """Handle user sign-in.

    Handles both GET and POST requests to the '/sign-in' URL. For GET requests, 
    it renders the sign-in form. For POST requests, it processes the form submission 
    to authenticate the user, and redirects to the profile page upon successful sign-in.

    Returns:
        Response: Redirects to the profile page if sign-in is successful or 
        renders the sign-in page with an error message for invalid credentials.
    """
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        if user:
            return redirect(url_for('profile'))

        session.pop('username', None)  # Clear invalid session data

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
    """Handle user registration.

    Handles both GET and POST requests to the '/register' URL. For GET requests, 
    it renders the registration form. For POST requests, it processes the form 
    submission to create a new user and redirects to the profile page upon successful 
    registration.

    Returns:
        Response: Redirects to the profile page after successful registration or 
        renders the registration page with an error message if the user already exists.
    """
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

    return render_template('register.html')

@app.route('/sign-out')
def sign_out():
    """Handle user sign-out.

    Clears the username from the session to log out the user and redirects 
    to the sign-in page.

    Returns:
        Response: Redirects to the sign-in page after signing out.
    """
    session.pop('username', None)
    return redirect(url_for('sign_in'))

@app.route('/delete_business/<int:business_id>')
def delete_business(business_id):
    """Delete a business from the database.

    Retrieves the specified business by ID, deletes it from the database, 
    and redirects to the profile page.

    Args:
        business_id (int): The ID of the business to delete.

    Returns:
        Response: Redirects to the profile page after deletion.
    """
    business = Business.query.get_or_404(business_id)
    db.session.delete(business)
    db.session.commit()
    return redirect(url_for('profile'))

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    """Delete a user from the database.

    Retrieves the specified user by ID, deletes the user from the database, 
    and redirects to the sign-in page.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        Response: Redirects to the sign-in page after deletion.
    """
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('sign_in'))
