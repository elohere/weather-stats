from django.urls import path

from . import views

app_name='weather_stats'
urlpatterns = [
    path('', views.index, name='index'),
    path("<int:cityid>", views.miasto, name="miasto")
]