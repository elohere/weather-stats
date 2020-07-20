from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
from weather_stats.models import City, Weather
# Create your views here.
def sendRequest(request):
    res = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=Łabiszyn&appid=50e6d49e940dd59765f1a0a6f19e7e4b")
    data = res.json()
    return data

def importdataapi(request):
    data = sendRequest(request)
    cityapi = data['city']
    weatherlist = data['list']
    cityajdi = cityapi['id']
    try:
        city = City.objects.get(cityid=cityajdi)
    except City.DoesNotExist:
        a = City()
        a.cityid = cityapi['id']
        a.name = cityapi['name']
        a.coordlat = cityapi['coord']['lat']
        a.coordlon = cityapi['coord']['lon']
        a.save()
    finally:
        for w in weatherlist:
            b = Weather()
            b.city = City.objects.get(cityid=cityajdi)
            b.date = w['dt_txt']
            b.temp = w['main']['temp']
            b.temp_min = w['main']['temp_min']
            b.temp_max = w['main']['temp_max']
            b.temp_feels = w['main']['feels_like']
            b.pressure = w['main']['pressure']
            b.weather_main = w['weather'][0]['main']
            b.weather_desc = w['weather'][0]['description']
            b.weather_icon =w['weather'][0]['icon']
            b.save()