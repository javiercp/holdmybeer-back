from django.shortcuts import render
from rest_framework import permissions

# Create your views here.

from chigre.models import PubGallery
from chigre.serializers import PubGallerySerializer
from rest_framework import generics

class PubGalleryList(generics.ListCreateAPIView):
    """
    List all photos, or create a new photo.
    """
    queryset = PubGallery.objects.all()
    serializer_class = PubGallerySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class PubGalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a photo.
    """
    queryset = PubGallery.objects.all()
    serializer_class = PubGallerySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

