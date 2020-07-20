from django.contrib import admin

# Register your models her
from .models import City, Weather

admin.site.register(City)
admin.site.register(Weather)
