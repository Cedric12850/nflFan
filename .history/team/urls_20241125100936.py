#teams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_index, name='teams_index')
]