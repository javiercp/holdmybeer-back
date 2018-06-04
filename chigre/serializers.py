from rest_framework import serializers
from chigre.models import Brewery

class BrewerySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    webpage = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        """
        Create and return a new `Brewery` instance, given the validated data.
        """
        return Brewery.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Brewery` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.webpage = validated_data.get('webpage', instance.webpage)
        instance.save()
        return instance
