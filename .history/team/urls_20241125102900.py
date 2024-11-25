#players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.players_index, name='players_index')
]