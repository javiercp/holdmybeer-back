from rest_framework import serializers
from chigre.models import Brewery

class BrewerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Brewery
        fields = ('id', 'name', 'description', 'webpage')
