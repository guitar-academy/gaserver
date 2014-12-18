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
mkvirtualenv --no-site-packages {{ project_name }}-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages {{ project_name }}-env
cd {{ project_name }}-env
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

## Running ##
```bash
python manage.py runserver
```

Open browser to http://localhost:8000
