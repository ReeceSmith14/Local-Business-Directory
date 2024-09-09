from directory import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(25), nullable = False)
    last_name = db.Column(db.String(25), nullable = False)
    user_name = db.Column(db.String(25), unique = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(25), nullable = False)

    businesses = db.relationship("Business", backref = "user", cascade = "all, delete", lazy = True)

    def __repr__(self):
        return f"{self.id} - Name: {self.first_name} {self.last_name}, Username: {self.user_name}"



class Business(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    business_name = db.Column(db.String(50), unique = True, nullable = False)
    business_description = db.Column(db.String(255), nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete = "CASCADE"), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete = "CASCADE"), nullable = False)
    phone = db.Column(db.String(11), unique=True, nullable=True)
    email = db.Column(db.String(255), unique = True, nullable = True)
    website = db.Column(db.String(255), unique = True, nullable = True)
    image_url = db.Column(db.String(255), nullable=True) 

    def __repr__(self):
        return f"{self.id} - Business Name: {self.business_name}"

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(25), unique = True, nullable = False)
    
    businesses = db.relationship("Business", backref = "category", cascade = "all, delete", lazy = True)

    def __repr__(self):
        return f"{self.id} - Category Name: {self.category_name}"