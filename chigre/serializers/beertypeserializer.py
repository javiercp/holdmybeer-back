from rest_framework import serializers
from chigre.models import BeerType

class BeerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BeerType
        fields = ('id', 'name', 'description')
