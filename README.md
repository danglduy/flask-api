### A simple API built on Python Flask

#### Manual for development
- Create a MySQL Database
- Copy .env.example to .env and set your db configs there
- Install Python 3.7 and pipenv, run `pipenv install` for packages install
- Run `pipenv shell` each time to enter the virualenv with packages installed
- Run `source .env; flask db upgrade` to create tables
- Run `python run.py` to start the server
