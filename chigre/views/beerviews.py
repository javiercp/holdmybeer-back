from django.shortcuts import render
from rest_framework import permissions

# Create your views here.

from chigre.models import Beer
from chigre.serializers import BeerSerializer, BeerSerializerEx
from rest_framework import generics

class BeerList(generics.ListCreateAPIView):
    """
    List all beers, or create a new beer.
    """
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer.
    """
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
        
class BeerListEx(generics.ListAPIView):
    """
    List all beers.
    """
    queryset = Beer.objects.all()
    serializer_class = BeerSerializerEx

class BeerDetailEx(generics.RetrieveAPIView):
    """
    Retrieve a beer.
    """
    queryset = Beer.objects.all()
    serializer_class = BeerSerializerEx
