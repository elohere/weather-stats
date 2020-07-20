from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=254)
    cityid = models.IntegerField()
    coordlon = models.FloatField()
    coordlat = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateTimeField()
    temp = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    temp_feels = models.FloatField()
    pressure = models.FloatField()
    weather_main = models.CharField(max_length=32)
    weather_desc = models.CharField(max_length=64)
    weather_icon = models.CharField(max_length=32)