from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from chigre.models import Brewery
from chigre.serializers import BrewerySerializer

@csrf_exempt
def brewery_list(request):
    """
    List all breweries, or create a new brewery.
    """
    if request.method == 'GET':
        breweries = Brewery.objects.all()
        serializer = BrewerySerializer(breweries, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BrewerySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def brewery_detail(request, pk):
    """
    Retrieve, update or delete a brewery.
    """
    try:
        brewery = Brewery.objects.get(pk=pk)
    except Brewery.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BrewerySerializer(brewery)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BrewerySerializer(brewery, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        brewery.delete()
        return HttpResponse(status=204)
