# Andy × Bungalow DRF App

> ### A sample codebase using Django + DRF. To get Andy hired!

## Installation

1. Clone this repository.
2. [Install the `pipenv` tool](https://github.com/pypa/pipenv#installation) if necessary.
3. Install dependencies:

```
pipenv install
```

4. Activate the project's virtualenv:

```
pipenv shell
```

5. Activate the project's virtualenv:

```
pipenv shell
```

You're good to go! That was much easier than last time I tried installing Python.

Also, when you're done with the virtualenv shell, you can kill it with command `exit` or by pressing `Ctrl+D`.

## Usage

First: `cd server`.

### Migrate

Initialize the database with a migration:

```
python manage.py migrate
```

### Ingest the data from CSV

Run the script to add data from the provided csv:

```
python manage.py ingest_zillow_csv ./csv/challenge_data.csv
```

### Start the server

```
python manage.py runserver
```

### Admin

As usual with Django projects, you can create an admin user using `python manage.py createsuperuser` once you've. This lets you log on at `localhost:8000/admin`.
