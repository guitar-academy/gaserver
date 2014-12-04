from flask import Flask
from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////gaserver.db'

# attach app to gaserver.database.db
db.init_app(app)
# create tables in database
db.create_all(app=app)

@app.route("/")
def hello():
    db.create_all()
    return "Hello world!"

@app.route("/user")


if __name__ == "__main__":
    app.run(debug=True)

