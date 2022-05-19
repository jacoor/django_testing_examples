# Django testing example
Sample project to show Django tests in practice.

## Prerequisities
PostgreSQL DB configured as in settings_local.py. Warning: this is a sample project and as such,
settings_local.py is added to the repo. In real life do not commit this file, add to .gitignore. Settings_local.py
contains usually private data like your DB password and other keys. 

## Instalation
Mac:
```
$ brew install python@3.10
$ pipenv install --dev --python /usr/local/Cellar/python@3.10/3.10.2/bin/python3
$ pipenv shell
$ ./manage.py migrate
```

## Running
Starting the app:
```
$ ./manage.py runserver
```

Running tests
```
$ pytest
```

