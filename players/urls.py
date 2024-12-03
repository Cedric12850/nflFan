#players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players_index, name='players_index'),
    path('players/addplayer/', views.addplayer, name="addplayer"),
    path('players/<int:id>/', views.player_detail, name='player_detail'),
    path('dynamics-style.css', views.dynamics_css, name='dynamic_css')
]