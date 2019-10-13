from rest_framework import serializers
from .models import Property, ZillowProperty


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('area_unit',
                  'home_size',
                  'bathrooms',
                  'bedrooms',
                  'property_size',
                  'home_type',
                  'last_sold_date',
                  'last_sold_price',
                  'price',
                  'rent_price',
                  'tax_value',
                  'tax_year',
                  'year_built',
                  'address',
                  'city',
                  'state',
                  'zipcode',)


class ZillowPropertySerializer(PropertySerializer):
    class Meta:
        # DRF docs ecommend not using inheritance on inner Meta classes,
        # but instead declaring all options explicitly.
        # Who am I to question the almighty documentation?
        model = ZillowProperty
        fields = ('area_unit',
                  'home_size',
                  'bathrooms',
                  'bedrooms',
                  'property_size',
                  'home_type',
                  'last_sold_date',
                  'last_sold_price',
                  'price',
                  'rent_price',
                  'tax_value',
                  'tax_year',
                  'year_built',
                  'address',
                  'city',
                  'state',
                  'zipcode',
                  'link',
                  'zillow_id',
                  'rentzestimate_amount',
                  'rentzestimate_last_updated',
                  'zestimate_amount',
                  'zestimate_last_updated',)
