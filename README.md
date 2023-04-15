# Guide for Surfers
**Currently, this version of the project in this repository is no longer up to date and supported, but the project is still being developed and rebuilt**

The project was a summary and final work during a Python programming course. The project is a kind of service for people who surf or plan to start practicing this sport.

## The main assumptions of the project:
* Connecting  surfers or people interested in surfing
* Sharing your experiences
* Finding and sharing new surf spots
* Help in planning your next surfing trips


The main functionality was the ability for logged users to add surfing sports by creating a database of places

## Installation

1. Clone this repository.
2. Install Python 3.x on your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt` in the project root directory.


## Setup

1. Create a virtual environment by running `python3 -m venv venv` in the project root directory.
2. Activate the virtual environment by running `source venv/bin/activate`.
3. Install PostgreSQL on your local machine (but you can skip this step, you can install pgAdmin to make your work with database easier).
    **Only if you installed PostgreSQL**
    * Create a new database by running `create database 'name_of_db';`.
    * Create a `local_settings.py` file in the project root directory with the following contents:
```
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#Replace PORT, NAME, USER, and PASSWORD with your own values.

DATABASES = {
    'default': {
        'PORT': 'YOUR_PORT',
        'HOST': '127.0.0.1',
        'NAME': 'NAME_OF_YOUR_DATABASE',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'YOUR_PASWORD',
    }
}
#Replace mysecretkey, myuser, mypassword, and mydatabase with your own values.
```

## Running the project

1. Apply the database migrations by running `python manage.py migrate`.
2. You can create superuser to acces admin panel by running `python manage.py createsuperuser` (but you can skip this step).
3. Start the development server by running `python manage.py runserver`. The web application will be available at http://localhost:8000.


