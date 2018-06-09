from rest_framework import serializers
from chigre.models import Beer,Brewery,BeerType

from chigre.serializers import BrewerySerializer, BeerTypeSerializer

class BeerSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
  
    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'abv', 'webpage', 'logo', 'brewery', 'beertype', 'creator')
        
class BeerSerializerEx(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    brewery = BrewerySerializer(read_only=True)
    beertype = BeerTypeSerializer(read_only=True)
  
    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'abv', 'webpage', 'logo', 'brewery', 'beertype', 'creator')
