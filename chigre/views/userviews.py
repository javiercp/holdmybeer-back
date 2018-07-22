from django.shortcuts import render
from rest_framework import permissions

# Create your views here.
from chigre.serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response

class UserAuthDetail(generics.ListCreateAPIView):
    """
    List authenticated user info.
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        queryset = self.request.user
        serializer = UserSerializer(queryset)
        return Response(serializer.data) 