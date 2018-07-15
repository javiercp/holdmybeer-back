from rest_framework import serializers
from chigre.models import Secrets

class SecretsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Secrets
        fields = ('maps_key', )
        #fields = '__all__'
    