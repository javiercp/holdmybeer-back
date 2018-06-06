from rest_framework import serializers
from chigre.models import Brewery

class BrewerySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    
    class Meta:
        model = Brewery
        fields = ('id', 'name', 'description', 'webpage', 'logo', 'creator')
