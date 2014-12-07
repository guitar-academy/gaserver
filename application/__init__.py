from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

# create database
db = SQLAlchemy(app)

from application import views
from application.models import core, login
