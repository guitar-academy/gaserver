from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////gaserver.db'
db.init_app(app)
db.create_all(app=app)

@app.route("/")
def hello():
    db.create_all()
    return "Hello world!"

if __name__ == "__main__":
    app.run(debug=True)

