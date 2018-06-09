from rest_framework import serializers
from chigre.models import Beer

class BeerSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    #brewery = serializers.RelatedField(queryset read_only=True)
    #beertype = serializers.RelatedField(read_only=True)
    
    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'abv', 'webpage', 'logo', 'brewery', 'beertype', 'creator')
