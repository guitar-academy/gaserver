Guitar Academy Server
=====================

Server for Guitar Academy written in Python.

## Prerequisites
* python 3.4
* pip
* virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv ga-env
```

#### For virtualenv ####
```bash
virtualenv ga-env
cd ga-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone git@github.com:guitar-academy/gaserver.git
```

### Install requirements ###
```bash
cd gaserver
pip install -r requirements.txt
```

### Configure project ###
```bash
cp gaserver/__local_settings.py gaserver/local_settings.py
vi gaserver/local_settings.py
```

### Setup database ###
```bash
python manage.py migrate
```

### Setup Root User (Optional) ###
In order to have the access to the Django admin (/admin/), you need to be a staff or superuser.
```bash
python manage.py createsuperuser
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://localhost:8000
