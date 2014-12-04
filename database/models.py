from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    fullname = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def __repr__(self):
        return '<User %r>' % self.username

