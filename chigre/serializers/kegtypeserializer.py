from rest_framework import serializers
from chigre.models import KegType

class KegTypeSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    
    class Meta:
        model = KegType
        fields = ('id', 'name', 'size', 'pints', 'canyas', 'creator')
