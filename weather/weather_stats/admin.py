from django.contrib import admin

# Register your models her
from .models import City, Weather

class WeatherAdmin(admin.ModelAdmin):
    list_display = ('city', 'date', 'temp', 'weather_desc')
    list_filter = ('city',)
admin.site.register(City)
admin.site.register(Weather, WeatherAdmin)
