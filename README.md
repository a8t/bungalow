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

## Tests

Run the tests with:

```
python manage.py test
```

# API docs

Once this API is running, you can expect the following interface from the `/properties/` and `/zillow_properties/` endpoints:

## GET

`GET /properties/`: get all Properties

`GET /properties/{id}`: get Property with this id

`GET /zillow_properties/`: get all Zillow properties

`GET /zillow_properties/{id}`: get Zillow property with this id

## DELETE

`DELETE /properties/{id}`: delete Property with this id

`DELETE /zillow_properties/{id}`: delete Zillow property with this id

## POST

`POST /properties/`: Creates a Property with a POST body adhering to the following shape, attached as JSON:

```
area_unit : "SqFt" (the only value available right now)
home_size : int
bathrooms : float
bedrooms : int
property_size : int
home_type : "SingleFamily"
          | "Apartment"
          | "Condominium"
          | "Duplex"
          | "Miscellaneous"
          | "MultiFamily2To4"
          | "VacantResidentialLand"
last_sold_date : string as YYYY-MM-DD
last_sold_price : int
price : int
rent_price : int
tax_value : float
tax_year : int
year_built : int
address : string
city : string
state : string
zipcode : string
```

`POST /zillow_properties/`: Creates a Zillow Property with a POST body adhering to the following shape, attached as JSON:

```
area_unit : "SqFt" (the only value available right now)
home_size : int
bathrooms : float
bedrooms : int
property_size : int
home_type : "SingleFamily"
          | "Apartment"
          | "Condominium"
          | "Duplex"
          | "Miscellaneous"
          | "MultiFamily2To4"
          | "VacantResidentialLand"
last_sold_date : string as YYYY-MM-DD
last_sold_price : int
price : int
rent_price : int
tax_value : float
tax_year : int
year_built : int
address : string
city : string
state : string
zipcode : string
link : string
zillow_id : string
rentzestimate_amount : int
rentzestimate_last_updated : string as YYYY-MM-DD
zestimate_amount : int
zestimate_last_updated : string as YYYY-MM-DD
```
