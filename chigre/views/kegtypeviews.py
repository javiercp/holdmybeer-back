from django.shortcuts import render
from rest_framework import permissions

# Create your views here.

from chigre.models import KegType
from chigre.serializers import KegTypeSerializer
from rest_framework import generics

class KegTypeList(generics.ListCreateAPIView):
    """
    List all keg types, or create a new keg type.
    """
    queryset = KegType.objects.all()
    serializer_class = KegTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class KegTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a keg type.
    """
    queryset = KegType.objects.all()
    serializer_class = KegTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
