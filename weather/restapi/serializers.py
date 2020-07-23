from rest_framework import serializers
from weather_stats.models import City, Weather

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['url', 'name']

class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = ['city', 'temp', 'date']