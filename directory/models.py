from directory import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Store a hashed password (increase length)

    businesses = db.relationship("Business", backref="user", cascade="all, delete", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  # Store the hash in the password field

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  # Verify the hash with the stored password

    def __repr__(self):
        return f"{self.id} - Username: {self.username}"



class Business(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    business_name = db.Column(db.String(50), unique = True, nullable = False)
    business_description = db.Column(db.String(255), nullable = False)
    category_name = db.Column(db.String(25), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete = "CASCADE"), nullable = False)
    phone = db.Column(db.String(11), unique=True, nullable=True)
    email = db.Column(db.String(255), unique = True, nullable = True)
    website = db.Column(db.String(255), unique = True, nullable = True)
    image_url = db.Column(db.String(255), nullable=True) 

    def __repr__(self):
        return f"{self.id} - Business Name: {self.business_name}"

