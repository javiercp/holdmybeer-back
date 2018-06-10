from rest_framework import serializers
from chigre.models import Keg
from chigre.serializers import BeerSerializerEx, KegTypeSerializer

class KegSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
  
    class Meta:
        model = Keg
        fields = ('id', 'pintprice', 'canyaprice', 'fullweight', 'emptyweight', 'actualweight', 'beer', 'kegtype', 'creator')
        
class KegSerializerEx(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    kegtype = KegTypeSerializer(read_only=True)
    beer = BeerSerializerEx(read_only=True)
  
    class Meta:
        model = Keg
        fields = ('id', 'pintprice', 'canyaprice', 'fullweight', 'emptyweight', 'actualweight', 'beer', 'kegtype', 'creator')
