from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'breweries': reverse('brewery-list', request=request, format=format),
        'kegtypes': reverse('kegtype-list', request=request, format=format),
        'beertypes': reverse('beertype-list', request=request, format=format),
        'beers': reverse('beer-list', request=request, format=format),
        'kegs': reverse('keg-list', request=request, format=format),
        'taps': reverse('tap-list', request=request, format=format),
        'beers-expanded': reverse('beer-list-ex', request=request, format=format),
        'kegs-expanded': reverse('keg-list-ex', request=request, format=format),
        'taps-expanded': reverse('tap-list-ex', request=request, format=format),
    })