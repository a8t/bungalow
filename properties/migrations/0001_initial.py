# Generated by Django 2.2.6 on 2019-10-11 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(choices=[('SqFt', 'SqFt')], default='SqFt', max_length=255)),
                ('home_size', models.PositiveIntegerField(null=True)),
                ('bathrooms', models.DecimalField(decimal_places=3, max_digits=5)),
                ('bedrooms', models.PositiveIntegerField(null=True)),
                ('property_size', models.PositiveIntegerField(null=True)),
                ('home_type', models.CharField(choices=[('SingleFamily', 'SingleFamily'), ('Apartment', 'Apartment'), ('Condominium', 'Condominium'), ('Duplex', 'Duplex'), ('Miscellaneous', 'Miscellaneous'), ('MultiFamily2To4', 'MultiFamily2To4'), ('VacantResidentialLand', 'VacantResidentialLand')], default='SingleFamily', max_length=255)),
                ('last_sold_date', models.DateField(null=True)),
                ('last_sold_price', models.PositiveIntegerField(null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('rent_price', models.PositiveIntegerField(null=True)),
                ('tax_value', models.DecimalField(decimal_places=1, max_digits=20)),
                ('tax_year', models.PositiveIntegerField(null=True)),
                ('year_built', models.PositiveIntegerField(null=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ZillowProperty',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.Property')),
                ('link', models.URLField(default='')),
                ('zillow_id', models.CharField(max_length=255)),
                ('rentzestimate_amount', models.PositiveIntegerField(null=True)),
                ('rentzestimate_last_updated', models.DateField(null=True)),
                ('zestimate_amount', models.PositiveIntegerField(null=True)),
                ('zestimate_last_updated', models.DateField(null=True)),
            ],
            bases=('properties.property',),
        ),
    ]
