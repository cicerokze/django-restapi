## django-restapi

REST API Application developed with:

- Python3
- Django REST framework
- WSGI (Gunicorn)
- SQLite (Development)
- PostgreSQL (Production)

<a href="https://www.buymeacoffee.com/cicerokze" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="150" />
</a>

## Description
- REST API developed for an experiment of a boilerplate/Scaffold with Django Framework. This application works with the following tech stack: Python3, Django REST Framework, WSGI (Gunicorn) and SQLite Database.

## Installation
1 - Make sure you have Python3 installed in your machine

2 - Create and activate a virtual environment to isolate package dependencies locally
```bash
$ python3 -m venv env
$ source env/bin/activate  # On Windows use `.\env\Scripts\activate`
```

3 - This application uses Pipfile and Pipfile.lock to manage its dependencies. Therefore, run the command below in the same directory as Pipefile to install them:
```bash
$ pip install 
```

4 - After installing dependencies, create a file .env in root of the project and add your variables as presented bellow:
```bash
# Suggestion: move all the sensitive data to .env file, especially the SECRET_KEY
SECRET_KEY="your_secret_key_here"
```

5 - Generate Database
```bash
$ python3 manage.py migrate
```

6 - Create an admin user to make requests
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

**GET** http://localhost:8000/users
```bash
$ curl -u admin -H 'Accept: application/json; indent=4' http://localhost:8000/users/
Enter host password for user 'admin':
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://localhost:8000/users/1/",
            "username": "admin",
            "email": "your_email@example.com",
            "groups": []
        }
    ]
}
```

## Optionally, you might access admin area by your preferred web browser

1 - Navigate to 'http://localhost:8000' and check the screen is like the one bellow. Then, click on 'Log in' button located on top-right of screen.

![Api Root](/assets/images/github/image-1.png)

2 - You might see the 'Log in' area as following. Type your superuser and password to access admin area. The same user created before, with this intructions.

![Log in area](/assets/images/github/image-2.png)

3 - After the step before, check the screen is like bellow, in the root area of API where you might access your endpoints. Click on the endpoint '/users' or '/groups' and make a 'POST'.

![Root area](/assets/images/github/image-3.png)

4 - Now, you might use any method allowed as shown bellow.

![Edit area](/assets/images/github/image-4.png)