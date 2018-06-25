from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from chigre.models import Brewery

class BrewerySerializer(CountryFieldMixin, serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    
    class Meta:
        model = Brewery
        fields = ('id', 'name', 'description', 'country', 'webpage', 'logo', 'creator', 'created')
