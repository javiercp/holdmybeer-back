from django.shortcuts import render, get_object_or_404
from rest_framework import permissions

# Create your views here.

from chigre.models import Tap
from chigre.serializers import TapSerializer, TapSerializerEx
from rest_framework import generics
from rest_framework.response import Response

class TapList(generics.ListCreateAPIView):
    """
    List all taps, or create a new tap.
    """
    queryset = Tap.objects.all()
    serializer_class = TapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class TapListEx(generics.ListCreateAPIView):
    """
    List all taps, or create a new tap.
    """
    serializer_class = TapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def get_queryset(self):
        queryset = Tap.objects.all()
        queryset = TapSerializerEx.setup_eager_loading(queryset=queryset)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TapSerializerEx(queryset, many=True)
        return Response(serializer.data) 
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class TapDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a tap.
    """
    queryset = Tap.objects.all()
    serializer_class = TapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

class TapDetailEx(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a tap.
    """
    serializer_class = TapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

    def get_queryset(self):
        queryset = Tap.objects.all()
        queryset = TapSerializerEx.setup_eager_loading(queryset=queryset)
        return queryset

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        tap = get_object_or_404(queryset, pk=pk)
        serializer = TapSerializerEx(tap)
        return Response(serializer.data) 
