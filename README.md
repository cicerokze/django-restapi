## django-restapi

# REST API Application developed with:
- Python3
- Django Rest
- WSGI Server
- SQLite Database

## Description

# REST API developed for an experiment of a boilerplate/Scaffold with Django Framework. This application works with the following tech stacks: Python3, Django Rest, WSGI Server and SQLite Database.

## Installation
# Make sure you have Python3 installed in your machine

# Create a virtual environment to isolate package dependencies locally
```bash
$ python3 -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`
```

# Install Django and Django REST framework into the virtual environment
```bash
$ pip install djangorestframework
```

# Generating Database
```bash
$ python3 manage.py migrate
```

# Create an admin user to make requests
```bash
$ python3 manage.py createsuperuser --username admin --email your_email@example.com
```

## Starting Application
```bash
# development
$ python3 manage.py runserver
```

## Requesting

# Get Users

**GET** http://127.0.0.1:8000/users
```bash
$ curl -u admin -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
Enter host password for user 'admin':
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/users/1/",
            "username": "admin",
            "email": "your_email@example.com",
            "groups": []
        }
    ]
}
```