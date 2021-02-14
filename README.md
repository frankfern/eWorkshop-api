# eWorkshop API

This is an electronics workshop managment system REST Api made in Python language using Django, Django Rest Framework and Celery.

## Overview

eWorkshop API allows eworkshops staff to offer services like selling products, tracking the progress of broken equipment fix.

## Software Requirements

- [python 3.8+](https://www.python.org/)
- [Django 3.1+](https://www.djangoproject.com/download/)
- [Django Rest Framework 3.12+](http://www.django-rest-framework.org/#installation)
- [Celery 5.0+](https://docs.celeryproject.org/en/stable/index.html)

### Installing Dependencies

```bash
# Install virtualenv
$ pip install virtualenv
# Move to project directory
$ cd eWorkshop-api
# Create virtual enviroment
$ virtualenv .venv
# Use the environment created
$ source .venv/bin/activate
# Install the requirements
$ pip install -r requirements/local.txt
```

### Running the Project

```bash
$ python manage.py migrate
$ pyhhon manage.py createsuperuser
$ python manage.py runserver
```

## To do

- [ ] Add a Dashboard!
- [ ] Add tests and coverage implementations
- [ ] Implement more async and periodic tasks to improve the tracking of fix service
- [ ] A UI!

## License

[This project is under MIT License](https://opensource.org/licenses/MIT)
