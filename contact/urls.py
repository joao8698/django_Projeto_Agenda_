from django.contrib import admin
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.inital_page, name='inital_page'),
]