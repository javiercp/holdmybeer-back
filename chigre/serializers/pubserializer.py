from rest_framework import serializers
from chigre.models import Pub

class PubSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pub
        fields = ('name', 'description', 'address', 'webpage', 'logo')
    