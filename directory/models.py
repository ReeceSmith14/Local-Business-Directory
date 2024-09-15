from directory import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """Define the User model with fields for user data and relationships.

    Attributes:
        id (int): Primary key for the User model.
        username (str): Unique username for the user; cannot be null.
        password_hash (str): Hashed password for the user; cannot be null.
        businesses (relationship): One-to-many relationship with the Business model.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    businesses = db.relationship("Business", backref="user", cascade="all, delete", lazy=True)
    # 'backref' creates a reverse relationship to the User model; 
    # 'cascade="all, delete"' ensures that related Business entries are deleted 
    # when the User is deleted.

    def set_password(self, password):
        """Hash and store the password in the password_hash field.

        Args:
            password (str): The plaintext password to hash and store.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hashed password.

        Args:
            password (str): The plaintext password to check.

        Returns:
            bool: True if the password matches the stored hash, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Define a string representation of the User object for easier debugging.

        Returns:
            str: A string containing the user's id and username.
        """
        return f"{self.id} - Username: {self.username}"

class Business(db.Model):
    """Define the Business model with fields for business data.

    Attributes:
        id (int): Primary key for the Business model.
        business_name (str): Unique name of the business; cannot be null.
        business_description (str): Description of the business; cannot be null.
        category_name (str): Category of the business; cannot be null.
        user_id (int): Foreign key linking to the User model; ensures businesses are 
                       deleted when the associated user is deleted.
        phone (str): Unique phone number for the business; cannot be null.
        email (str): Unique email address for the business; cannot be null.
        website (str): Optional URL for the business's website.
        image_url (str): URL for the business image; cannot be null.
    """

    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(50), unique=True, nullable=False)
    business_description = db.Column(db.String(255), nullable=False)
    category_name = db.Column(db.String(25), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    website = db.Column(db.String(255), unique=False, nullable=True)
    image_url = db.Column(db.String(), nullable=False)

    def __repr__(self):
        """Define a string representation of the Business object for easier debugging.

        Returns:
            str: A string containing the business's id and name.
        """
        return f"{self.id} - Business Name: {self.business_name}"
