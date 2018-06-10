from rest_framework import serializers
from chigre.models import Tap
from chigre.serializers import KegSerializerEx, TapTypeSerializer

class TapSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
  
    class Meta:
        model = Tap
        fields = ('id', 'number', 'photo', 'keg', 'taptype', 'creator')
        
class TapSerializerEx(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    keg = KegSerializerEx(read_only=True)
    taptype = TapTypeSerializer(read_only=True)
  
    class Meta:
        model = Tap
        fields = ('id', 'number', 'photo', 'keg', 'taptype', 'creator')
