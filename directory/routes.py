from flask import render_template, request, url_for, redirect, session
from directory import app, db
from directory.models import User, Business

@app.route('/', methods=['GET'])
def home():
    businesses = Business.query.all()
    return render_template('home.html', businesses=businesses)

@app.route('/businesses/add', methods=['GET', 'POST'])
def add():
    if 'username' not in session:
        return redirect(url_for('sign_in'))  # Redirect to sign-in if the user is not logged in

    user = User.query.filter_by(username=session['username']).first()  # Retrieve the user from the database

    if not user:
        return redirect(url_for('sign_in'))  # Redirect if user not found (shouldn't happen normally)

    if request.method == 'POST':
        business_name = request.form.get('business_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        website = request.form.get('website')

        # Check for existing business with the same name, phone, email, or website
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

        # No duplicates, proceed to add the business
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
    business = Business.query.get_or_404(business_id)

    if request.method == 'POST':
        business_name = request.form.get('business_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        website = request.form.get('website')

        # Check for existing business with the same name, phone, email, or website (excluding the current one)
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

        # No duplicates, proceed to update the business
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
    if 'username' not in session:
        return redirect(url_for('sign_in'))  # Redirect to sign-in if the user is not logged in

    # Retrieve the user and their associated businesses
    user = User.query.filter_by(username=session['username']).first()

    if not user:
        session.pop('username', None)  # Clear invalid session data
        return redirect(url_for('sign_in'))  # Redirect to sign-in if the user is not found

    # Get the user's businesses
    businesses = user.businesses  # Access the user's businesses via the relationship
    
    return render_template('profile.html', businesses=businesses)

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
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

@app.route('/sign-out')
def sign_out():
    session.pop('username', None)
    return redirect(url_for('sign_in'))

@app.route('/delete_business/<int:business_id>')
def delete_business(business_id):
    business = Business.query.get_or_404(business_id)
    db.session.delete(business)
    db.session.commit()
    return redirect(url_for('profile'))