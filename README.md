# django-uploads
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