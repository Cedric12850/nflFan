#players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players_index, name='players_index'),
    path('dynamics-css/', views.playerdynamics_css, name='players_dynamics_css'),
]