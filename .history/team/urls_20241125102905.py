#players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.teams_index, name='players_index')
]