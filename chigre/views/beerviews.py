from django.shortcuts import get_object_or_404
from rest_framework import permissions

# Create your views here.

from chigre.models import Beer
from chigre.serializers import BeerSerializer, BeerSerializerEx
from rest_framework import generics
from rest_framework.response import Response

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

class BeerListEx(generics.ListCreateAPIView):
    """
    List all beers, or create a new beer.
    """
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def get_queryset(self):
        queryset = Beer.objects.all()
        queryset = BeerSerializerEx.setup_eager_loading(queryset=queryset) 
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BeerSerializerEx(queryset, many=True)
        return Response(serializer.data) 
    
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

class BeerDetailEx(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer with details.
    """
    serializer_class = BeerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

    def get_queryset(self):
        queryset = Beer.objects.all()
        queryset = BeerSerializerEx.setup_eager_loading(queryset=queryset) 
        return queryset

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        beer = get_object_or_404(queryset, pk=pk)
        serializer = BeerSerializerEx(beer)
        return Response(serializer.data) 
