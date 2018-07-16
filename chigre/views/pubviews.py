from django.shortcuts import get_object_or_404
from rest_framework import permissions

# Create your views here.

from chigre.models import Pub
from chigre.serializers import PubSerializer
from rest_framework import generics
from rest_framework.response import Response


class PubDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete the pub info.
    """
    queryset = Pub.objects.all()
    serializer_class = PubSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )

    def get_object(self):
        savedpub = Pub.load()
        return savedpub

    def retrieve(self, request, pk=None):
        queryset = self.get_object()
        serializer = PubSerializer(queryset)
        return Response(serializer.data) 

