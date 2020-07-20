from rest_framework import viewsets
from restapi.serializers import CitySerializer
from weather_stats.models import City

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer