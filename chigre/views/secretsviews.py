from django.shortcuts import get_object_or_404
from rest_framework import permissions

# Create your views here.

from chigre.models import Secrets
from chigre.serializers import SecretsSerializer
from rest_framework import generics
from rest_framework.response import Response


class SecretsDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete the pub info.
    """
    queryset = Secrets.objects.all()
    serializer_class = SecretsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissionsOrAnonReadOnly, )
    schema = None

    def get_object(self):
        savedpub = Secrets.load()
        return savedpub

    def retrieve(self, request, pk=None):
        queryset = self.get_object()
        serializer = SecretsSerializer(queryset)
        return Response(serializer.data) 

