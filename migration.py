from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from application import app, db

# Flask-Migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

# Examples on how to use this file
# Create DB / enable migrations to existing DB
#     python migration.py db init 
# Generate a migration
#     python migration.py db migrate
# Apply migration to database (Caution: review first!)
#     python migration.py db upgrade
# See help
#     python migration.py db --help
