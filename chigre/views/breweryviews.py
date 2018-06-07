from django.shortcuts import render
from rest_framework import permissions

# Create your views here.

from chigre.models import Brewery
from chigre.serializers import BrewerySerializer
from rest_framework import generics

class BreweryList(generics.ListCreateAPIView):
    """
    List all breweries, or create a new brewery.
    """
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a brewery.
    """
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

