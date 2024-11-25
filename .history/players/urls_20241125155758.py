#players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players_index, name='players_index'),
    path('dynamics-css/', views.players_dynamics_cssdynamics_css, name='players_dynamics_css'),
]