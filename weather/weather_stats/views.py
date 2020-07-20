from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import City, Weather
import requests
# Create your views here.

def index(request):
    miasta = City.objects.all()
    data = {
        'City' : miasta
    }
    return render(request, 'weather_stats/index.html', data)

def miasto(request, cityid):
    try:
        city = City.objects.get(pk=cityid)
        weather = Weather.objects.filter(city__in=City.objects.filter(name=city.name)).distinct()
    except City.DoesNotExist:
        raise Http404("Brak miasta w bazie")
    data = {
        "city": city,
        "weather": weather
    }
    return render(request, "weather_stats/miasto.html", data)