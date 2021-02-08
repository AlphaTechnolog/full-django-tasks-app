# Full django tasks app

Welcome to the django full tasks app. In this file yo learn to run this
app in development mode and install django... etc

## Requirements

- Python3
- Django
- Git
- Linux (If you use windows please use your os commands)

## Installing requirements (optional)

In this tutorial i use Debian, you must use anyone os!

### Python3

If you don't have python3 in your machine, install it with apt (In debian, ubuntu...)

```sh
sudo apt install python3 python3-pip # python3-pip to use pip in python3
```

It command install python and pip in your path as: `python3`, `pip3` or `python3 -m pip`.

### Django

To install django, use pip

```sh
python3 -m pip install Django
```

Wait and now django is installed!

### Git

If you don't have git installed install in debian with:

```sh
sudo apt install git
```

Now you must use git in all projects

## Cloning app

To clone app use git, as this:

```sh
mkdir -p ~/repo
cd ~/repo
git clone https://github.com/AlphaTechnolog/full-django-tasks-app.git tasks-app
cd tasks-app
```

Now the tasks app was cloned successfully!

## Creating database and running migrations

First create migrations to the tasks app:

```sh
cd ~/repo/tasks-app
python3 ./manage.py makemigrations tasks
```

Now migrate:

```sh
python3 ./manage.py migrate
```

Now the database is empty... create the superuser

```sh
python3 ./manage.py createsuperuser
# Ask all questions
```

Now the database contain an admin user

## Running app

To run app use this commands:

```sh
cd ~/repo/tasks-app
python3 ./manage.py runserver
```

Now go to [https://localhost:8000](http://localhost:8000)

## Enjoy

Thanks for read this!
