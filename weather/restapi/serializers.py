from rest_framework import serializers
from weather_stats.models import City

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['url', 'name']