from rest_framework import serializers
from chigre.models import Pub

class PubSerializer(serializers.ModelSerializer):
    updater = serializers.ReadOnlyField(source='updater.username')

    class Meta:
        model = Pub
        fields = ('name', 'motto', 'description', 'address', 'lat', 'lng', 'telephone', 'logo', 'updater', 'updated')
    