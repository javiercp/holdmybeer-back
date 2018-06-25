from rest_framework import serializers
from chigre.models import Beer
from chigre.serializers import BrewerySerializer, BeerTypeSerializer

class BeerSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
  
    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'abv', 'webpage', 'logo', 'brewery', 'beertype', 'creator', 'created')
        
class BeerSerializerEx(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    brewery = BrewerySerializer(read_only=True)
    beertype = BeerTypeSerializer(read_only=True)
  
    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('creator')
        queryset = queryset.prefetch_related('brewery', 'beertype')
        return queryset

    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'abv', 'webpage', 'logo', 'brewery', 'beertype', 'creator', 'created')
