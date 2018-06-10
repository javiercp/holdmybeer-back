from rest_framework import serializers
from chigre.models import TapType

class TapTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TapType
        fields = ('id', 'name')
