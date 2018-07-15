from django.contrib import admin
from django.urls import path
from Converter import views

app_name = 'Converter'

urlpatterns = [
    path('', views.index, name='index'),
    path('convLength', views.convLength, name='convLength'),
    path('convWeight', views.convWeight, name='convWeight'),
    path('convVolume', views.convVolume, name='convVolume'),
    path('convCurrency', views.convCurrency, name='convCurrency')
]
