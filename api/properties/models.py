from django.db import models


class Property(models.Model):
    verbose_name_plural = "Properties"

    SQUARE_FEET = 'SqFt'
    AREA_UNITS = [
        (SQUARE_FEET, 'SqFt')
    ]
    area_unit = models.CharField(
        choices=AREA_UNITS, default=SQUARE_FEET, max_length=255)

    # PositiveIntegerField includes 0 even though that's mathematically incorrect
    # (and also kinda messed up for a house to not have a bathroom...)
    home_size = models.PositiveIntegerField(null=True)
    bathrooms = models.PositiveIntegerField(null=True)
    bedrooms = models.PositiveIntegerField(null=True)
    property_size = models.PositiveIntegerField(null=True)

    SINGLE_FAMILY = 'SingleFamily'
    APARTMENT = 'Apartment'
    CONDOMINIUM = 'Condominium'
    DUPLEX = 'Duplex'
    MISCELLANEOUS = 'Miscellaneous'
    MULTI_FAMILY2_TO4 = 'MultiFamily2To4'
    VACANT_RESIDENTIAL_LAND = 'VacantResidentialLand'
    HOME_TYPES = [(SINGLE_FAMILY, 'SingleFamily'),
                  (APARTMENT, 'Apartment'),
                  (CONDOMINIUM, 'Condominium'),
                  (DUPLEX, 'Duplex'),
                  (MISCELLANEOUS, 'Miscellaneous'),
                  (MULTI_FAMILY2_TO4, 'MultiFamily2To4'),
                  (VACANT_RESIDENTIAL_LAND, 'VacantResidentialLand')]
    home_type = models.CharField(
        choices=HOME_TYPES, default=SINGLE_FAMILY, max_length=255)

    last_sold_date = models.DateField(null=True)
    last_sold_price = models.DateField(null=True)
    price = models.PositiveIntegerField(null=True)
    rent_price = models.PositiveIntegerField(null=True)
    tax_value = models.DecimalField(decimal_places=1, max_digits=20)
    tax_year = models.PositiveIntegerField(null=True)
    year_built = models.PositiveIntegerField(null=True)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.PositiveIntegerField(null=True)


class ZillowProperty(Property):
    verbose_name_plural = "Zillow properties"

    link = models.URLField(default='')
    zillow_id = models.CharField(max_length=255)
    rentzestimate_amount = models.PositiveIntegerField(null=True)
    rentzestimate_last_updated = models.DateField(null=True)
    zestimate_amount = models.PositiveIntegerField(null=True)
    zestimate_last_updated = models.DateField(null=True)
