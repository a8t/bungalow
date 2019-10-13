import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from properties.models import ZillowProperty


class Command(BaseCommand):
    help = "This script opens a csv, parses it, and adds zillow properties to the db"

    def add_arguments(self, parser):
        parser.add_argument('csv')

    def create_zillow_property(self, **row):
        def mk_int(s):
            s = s.strip()
            return int(s) if s else 0

        def mk_float(s):
            s = s.strip()
            return float(s) if s else 0

        # this is crappy and very specific to the given inputs
        # but not sure what other possible inputs might look like
        def parse_price(price):
            _, *value, multiplier = price
            return float(''.join(value)) * (1000 if multiplier == 'k' else 1000000)

        ZillowProperty.objects.create(
            area_unit=row['area_unit'],
            home_size=mk_int(row['home_size']),
            bathrooms=mk_float(row['bathrooms']),
            bedrooms=mk_int(row['bedrooms']),
            property_size=mk_int(row['property_size']),
            home_type=row['home_type'],
            last_sold_date=parse_datetime(row['last_sold_date']),
            last_sold_price=mk_int(row['last_sold_price']),
            price=parse_price(row['price']),
            rent_price=mk_int(row['rent_price']),
            tax_value=mk_float(row['tax_value']),
            tax_year=mk_int(row['tax_year']),
            year_built=mk_int(row['year_built']),
            address=row['address'],
            city=row['city'],
            state=row['state'],
            zipcode=row['zipcode'],
            link=row['link'],
            zillow_id=row['zillow_id'],
            rentzestimate_amount=mk_int(row['rentzestimate_amount']),
            rentzestimate_last_updated=parse_datetime(
                row['rentzestimate_last_updated']),
            zestimate_amount=mk_int(row['zestimate_amount']),
            zestimate_last_updated=parse_datetime(
                row['zestimate_last_updated']),
        )

    def handle(self, *args, **options):
        csv_file_location = options['csv']
        with open(csv_file_location, newline='\n') as csv_file:
            file_reader = csv.DictReader(csv_file)

            for row in file_reader:
                self.create_zillow_property(**row)
