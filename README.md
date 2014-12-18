Guitar Academy Server
=====================

Server for Guitar Academy written in Python.

## How to start

**Note**: If you have both Python 2 and 3 on your environment, you may have to use 'pip3' and 'python3' instead of 'pip' and 'python' on the instructions below.

- Step 0 (Optional) Install virtualenv and activate it.

- Step 1. Install requirements
   pip install -r requirements.txt

- Step 2. Initiate database
   python manage.py migrate

- Step 3. Run server
   python manage.py runserver

