#players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players_index, name='players_index'),
    path('dynamics-style.css', views.dynamics_css, name='players_dynamic_css')
]