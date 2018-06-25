from rest_framework import serializers
from chigre.models import Tap
from chigre.serializers import KegSerializerEx, TapTypeSerializer

class TapSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
  
    class Meta:
        model = Tap
        fields = ('id', 'number', 'photo', 'keg', 'taptype', 'creator', 'created')
        
class TapSerializerEx(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    keg = KegSerializerEx(read_only=True)
    taptype = TapTypeSerializer(read_only=True)
  
    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('creator')
        queryset = queryset.prefetch_related('taptype', 'keg', 
            'keg__kegtype', 'keg__beer', 'keg__beer__beertype', 'keg__beer__brewery')
        return queryset

    class Meta:
        model = Tap
        fields = ('id', 'number', 'photo', 'keg', 'taptype', 'creator', 'created')
