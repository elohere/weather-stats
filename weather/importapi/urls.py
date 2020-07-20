from django.urls import path

from . import views

app_name='importapi'
urlpatterns = [
    path('', views.importdataapi, name='importdataapi')
]