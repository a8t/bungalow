from django.shortcuts import render
from rest_framework import viewsets
from .models import Property, ZillowProperty
from .serializers import PropertySerializer, ZillowPropertySerializer


class PropertyView(viewsets.ModelViewSet):
    """
    DRF view for base Properties
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class ZillowPropertyView(viewsets.ModelViewSet):

    """
    DRF view for Zillow Properties
    """
    queryset = ZillowProperty.objects.all()
    serializer_class = ZillowPropertySerializer
