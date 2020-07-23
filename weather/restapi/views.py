from rest_framework import viewsets, filters
from restapi.serializers import CitySerializer, WeatherSerializer
from weather_stats.models import City, Weather

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    search_fields = ['city__name']
    filter_backends = (filters.SearchFilter,)
