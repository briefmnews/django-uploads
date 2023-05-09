# django-uploads
[![Python 3](https://img.shields.io/badge/python-3.6|3.7|3.8-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Django 3](https://img.shields.io/badge/django-2.x-blue.svg)](https://docs.djangoproject.com/en/3.2/)
![Python CI](https://github.com/briefmnews/django-uploads/workflows/Python%20CI/badge.svg) 
[![codecov](https://codecov.io/gh/briefmnews/django-uploads/branch/main/graph/badge.svg?token=ETW1Q1HOCY)](https://codecov.io/gh/briefmnews/django-uploads)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)  
Django file uploader app. Admin users can upload and manage files in a dedicated app. 

## Installation
Install with pip:
```
pip install -e git://github.com/briefmnews/django-uploads.git@main#egg=django_uploads
```

## Setup
In order to make `django-uploads` works, you'll need to follow the steps below.

### Settings
First you need to add the following configuration to your settings:
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',

    'uploads',
    ...
)
```

### Migrations
Next, you need to run the migrations in order to update your database schema.
```
python manage.py migrate
```

## Tests
Testing is managed by `pytest`. Required package for testing can be installed with:
```
make install
```

To run testing locally:
```
pytest
```

## Resources
[django-simple-file-handler](https://github.com/jonathanrickard/django-simple-file-handler)
