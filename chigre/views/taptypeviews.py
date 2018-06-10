from django.shortcuts import render
from rest_framework import permissions

# Create your views here.

from chigre.models import TapType
from chigre.serializers import TapTypeSerializer
from rest_framework import generics

class TapTypeList(generics.ListCreateAPIView):
    """
    List all keg types, or create a new tap type.
    """
    queryset = TapType.objects.all()
    serializer_class = TapTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

class TapTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a tap type.
    """
    queryset = TapType.objects.all()
    serializer_class = TapTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
