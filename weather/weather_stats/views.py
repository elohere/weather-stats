from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import City, Weather
from django.db.models import Avg, Count, Max
import json 
from django.core.serializers.json import DjangoJSONEncoder
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
        args = Weather.objects.filter(city__in=City.objects.filter(name=city.name))
        weather = args.distinct()
        srednia = args.aggregate(Avg('temp'), Max('temp'))
        arg = args.order_by('-temp').first()
        popularnosc = args.values_list('weather_desc').annotate(truck_count=Count('weather_desc')).order_by('-truck_count').first()

    except City.DoesNotExist:
        raise Http404("Brak miasta w bazie")
    data = {
        "city": city,
        "weather": weather,
        "srednia": srednia,
        "popularnosc": popularnosc,
        "najcieplejszy" : arg
    }
    return render(request, "weather_stats/miasto.html", data)

def delmiasto(request, cityid):
    City.objects.filter(pk=cityid).delete()
    return redirect('/', foo='bar')