from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chigre.models import Brewery
from chigre.serializers import BrewerySerializer

@api_view(['GET', 'POST'])
def brewery_list(request, format=None):
    """
    List all breweries, or create a new brewery.
    """
    if request.method == 'GET':
        breweries = Brewery.objects.all()
        serializer = BrewerySerializer(breweries, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':      
        serializer = BrewerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def brewery_detail(request, pk, format=None):
    """
    Retrieve, update or delete a brewery.
    """
    try:
        brewery = Brewery.objects.get(pk=pk)
    except Brewery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BrewerySerializer(brewery)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BrewerySerializer(brewery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        brewery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
