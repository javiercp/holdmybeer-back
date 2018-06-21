from django.shortcuts import get_object_or_404
from rest_framework import permissions

# Create your views here.

from chigre.models import Keg
from chigre.serializers import KegSerializer, KegSerializerEx
from rest_framework import generics
from rest_framework.response import Response

class KegList(generics.ListCreateAPIView):
    """
    List all kegs, or create a new keg.
    """
    queryset = Keg.objects.all()
    serializer_class = KegSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class KegListEx(generics.ListCreateAPIView):
    """
    List all kegs, or create a new keg.
    """
    serializer_class = KegSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def get_queryset(self):
        queryset = Keg.objects.all()
        queryset = KegSerializerEx.setup_eager_loading(queryset=queryset) 
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = KegSerializerEx(queryset, many=True)
        return Response(serializer.data) 
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class KegDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer.
    """
    queryset = Keg.objects.all()
    serializer_class = KegSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

class KegDetailEx(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer.
    """
    serializer_class = KegSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

    def get_queryset(self):
        queryset = Keg.objects.all()
        queryset = KegSerializerEx.setup_eager_loading(queryset=queryset) 
        return queryset

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        keg = get_object_or_404(queryset, pk=pk)
        serializer = KegSerializerEx(keg)
        return Response(serializer.data) 
