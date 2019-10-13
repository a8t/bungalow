from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_text
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from .models import Property


# model test
class PropertyTestCase(TestCase):

    def create_property(self,
                        area_unit="SqFt",
                        bathrooms=2.0,
                        bedrooms=4,
                        home_size=1372,
                        property_size=10611,
                        home_type="SingleFamily",
                        last_sold_date=datetime.now(),
                        last_sold_price=None,
                        price=739000,
                        rent_price=0,
                        tax_value=215083.0,
                        tax_year=2019,
                        year_built=2019,
                        address="7417 Quimby Ave",
                        city="West Hills",
                        state="CA",
                        zipcode="91307",
                        ):
        return Property.objects.create(area_unit=area_unit,
                                       bathrooms=bathrooms,
                                       bedrooms=bedrooms,
                                       home_size=home_size,
                                       property_size=property_size,
                                       home_type=home_type,
                                       last_sold_date=last_sold_date,
                                       last_sold_price=last_sold_price,
                                       price=price,
                                       rent_price=rent_price,
                                       tax_value=tax_value,
                                       tax_year=tax_year,
                                       year_built=year_built,
                                       address=address,
                                       city=city,
                                       state=state,
                                       zipcode=zipcode,)

    def test_property_creation(self):
        p = self.create_property()
        self.assertTrue(isinstance(p, Property))
        self.assertEqual(p.__str__(), f'{p.address}, {p.city}, {p.state}')

# api tests


class PropertyResourceTest(APITestCase):

    def test_get_property(self):
        '''
        test that getting a Property works
        '''
        # test that there's no Properties and get()ing properties results in none
        self.assertEqual(Property.objects.count(), 0)
        response = self.client.get('/properties/', format='json')
        self.assertEqual(response.data, [])

        # create a property
        test_property = PropertyTestCase().create_property()

        # test that we actually get the new property back
        self.assertEqual(Property.objects.count(), 1)
        response = self.client.get('/properties/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_property.address)

    def test_post_property_fails_on_invalid_input(self):
        '''
        test that it fails with invalid input
        '''
        response = self.client.post('/properties/', {'name': 'blah'})
        self.assertEqual(Property.objects.count(), 0)
        self.assertEqual(response.status_code, 400)

    def test_post_property_fails_on_invalid_input(self):
        '''
        test that it succeessfully posts
        '''
        self.assertEqual(Property.objects.count(), 0)
        test_data = {
            "area_unit": "SqFt",
            "bathrooms": 2.0,
            "bedrooms": 4,
            "home_size": 1372,
            "property_size": 10611,
            "home_type": "SingleFamily",
            "last_sold_date": "1995-04-07",
            "last_sold_price": '',
            "price": 739000,
            "rent_price": 0,
            "tax_value": 215083.0,
            "tax_year": 2019,
            "year_built": 2019,
            "address": "7417 Quimby Ave",
            "city": "West Hills",
            "state": "CA",
            "zipcode": "91307",
        }
        response = self.client.post('/properties/', test_data)
        # 201 is successfully created
        self.assertEqual(response.status_code, 201)
        # we now have 1 Property
        self.assertEqual(Property.objects.count(), 1)

        # test that the 1 property is the same as if we
        # directly created an object with the same data
        result_property = Property.objects.get()
        test_property = PropertyTestCase().create_property(test_data)
        self.assertEqual(test_property.__str__(), result_property.__str__())
