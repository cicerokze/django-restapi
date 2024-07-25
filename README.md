## django-restapi

REST API Application developed with:

- Python3
- Django Rest
- WSGI Server
- SQLite Database

<a href="https://www.buymeacoffee.com/cicerokze" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="150" />
</a>

## Description
- REST API developed for an experiment of a boilerplate/Scaffold with Django Framework. This application works with the following tech stacks: Python3, Django Rest, WSGI Server and SQLite Database.

## Installation
1 - Make sure you have Python3 installed in your machine

2 - Create a virtual environment to isolate package dependencies locally
```bash
$ python3 -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3 - Install Django and Django REST framework into the virtual environment
```bash
$ pip install djangorestframework
```

4 - Generate Database
```bash
$ python3 manage.py migrate
```

5 - Create an admin user to make requests
```bash
$ python3 manage.py createsuperuser --username admin --email your_email@example.com
```

## Starting Application
```bash
# development
$ python3 manage.py runserver
```

## Requesting
- Get Users

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