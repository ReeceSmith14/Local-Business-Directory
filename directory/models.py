from directory import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # Define the User model with fields for user data and relationships
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)  # Username must be unique and cannot be null
    password_hash = db.Column(db.String(128), nullable=False)  # Store the hashed password (128 characters for the hash)

    # Define a one-to-many relationship with the Business model
    businesses = db.relationship("Business", backref="user", cascade="all, delete", lazy=True)
    # 'backref' creates a reverse relationship; 'cascade="all, delete"' ensures that related businesses are deleted when the user is deleted

    def set_password(self, password):
        # Hash and store the password in the password_hash field
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check if the provided password matches the stored hashed password
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        # Define a string representation of the User object for easier debugging
        return f"{self.id} - Username: {self.username}"

class Business(db.Model):
    # Define the Business model with fields for business data
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each business
    business_name = db.Column(db.String(50), unique=True, nullable=False)  # Business name must be unique and cannot be null
    business_description = db.Column(db.String(255), nullable=False)  # Description of the business (cannot be null)
    category_name = db.Column(db.String(25), nullable=False)  # Category of the business (cannot be null)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    # Foreign key linking to the User model, with cascade delete to remove associated businesses if the user is deleted
    phone = db.Column(db.String(11), unique=True, nullable=False)  # Phone number must be unique and cannot be null
    email = db.Column(db.String(255), unique=True, nullable=False)  # Email address must be unique and cannot be null
    website = db.Column(db.String(255), unique=False, nullable=True)  # Optional field for the business website
    image_url = db.Column(db.String(), nullable=False)  # URL for the business image (cannot be null)

    def __repr__(self):
        # Define a string representation of the Business object for easier debugging
        return f"{self.id} - Business Name: {self.business_name}"
