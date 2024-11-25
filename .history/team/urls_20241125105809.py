#teams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.team_index, name='team_index')
]