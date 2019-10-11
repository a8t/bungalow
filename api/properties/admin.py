from django.contrib import admin
from .models import ZillowProperty, Property

admin.site.register(Property)
admin.site.register(ZillowProperty)
