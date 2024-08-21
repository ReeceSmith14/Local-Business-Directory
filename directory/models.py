from directory import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(25), nullable = False)
    last_name = db.Column(db.String(25), nullable = False)
    user_name = db.Column(db.String(25), unique = True, nullable = False)
    email = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.String(25), nullable = False)

    def __repr__(self):
        return f"Name: {first_name} {last_name}, Username: {user_name}, Email: {email}, Password: {password}"



class Business(db.Model):
    id = db.Column(db.Integer, primary_key = True)




class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)

