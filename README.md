# Flask Example: Login, Signup and Forgot password

[DEMO](http://flask-login-example.programadorwebvalencia.com)

![login](https://github.com/tanrax/flask-login-example/raw/master/screenshots/login.jpg)

## Description

* Login system.
* Signup.
* Forgot password.
* Validations.
* Private page only for registered users.
* System emails.

## Use

* Flask (Obvious!)
* Flask-SQLAlchemy (ORM for database)
* Flask-WTF (Generation of forms and validations)
* Flask-Migrate(Migratios)
* Flask-Mail(Send emails)

## Install

```bash
cp envExample .env
```

Configure variables. Next.

```bash
source .env
pip install -r requirements.txt
```

Create database.

```bash
python3 models.py db upgrade
```

## Run

```bash
python3 app.py
```

## Screenshots

![signup](https://github.com/tanrax/flask-login-example/raw/master/screenshots/signup.jpg)
![message](https://github.com/tanrax/flask-login-example/raw/master/screenshots/message.jpg)
![forgot](https://github.com/tanrax/flask-login-example/raw/master/screenshots/forgot.jpg)
![email](https://github.com/tanrax/flask-login-example/raw/master/screenshots/email.jpg)
![dashboard](https://github.com/tanrax/flask-login-example/raw/master/screenshots/dashboard.jpg)
