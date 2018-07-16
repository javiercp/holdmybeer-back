from rest_framework import serializers
from chigre.models import PubGallery

class PubGallerySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    
    class Meta:
        model = PubGallery
        fields = ('id', 'title', 'description', 'image', 'creator', 'created')
