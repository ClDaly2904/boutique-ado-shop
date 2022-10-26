"""boutique_ado URL Configuration for Home"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
