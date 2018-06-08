from django.shortcuts import render
from rest_framework import permissions

# Create your views here.

from chigre.models import BeerType
from chigre.serializers import BeerTypeSerializer
from rest_framework import generics

class BeerTypeList(generics.ListCreateAPIView):
    """
    List all beer types, or create a new beer type.
    """
    queryset = BeerType.objects.all()
    serializer_class = BeerTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

class BeerTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer type.
    """
    queryset = BeerType.objects.all()
    serializer_class = BeerTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
