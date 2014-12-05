import flask.ext.testing
import unittest
from flask.ext.testing import TestCase
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from gaserver import app, db

class DatabaseTest(TestCase):
    
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://gaserver_testing.db"
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
