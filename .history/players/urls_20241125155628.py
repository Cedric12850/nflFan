#players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players_index, name='players_index'),
    path('dynamics-css/', views.dynamics_css, name='player_dynamics_css'),
]