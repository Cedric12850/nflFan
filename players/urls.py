#players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.PlayerListView.as_view(), name='players_index'),
    path('players/autocomplete/', views.player_autocomplete, name='player_autocomplete'),
    path('players/addplayer/', views.PlayerCreateView.as_view(), name="addplayer"),
    path('players/<int:pk>/', views.player_detail, name='player_detail'),
    path('players/<int:pk>/edit', views.PlayerUpdateView.as_view(), name='player_detail_edit'),
    path('players/<int:pk>/delete', views.PlayerDeleteView.as_view(), name='player_detail_delete'),
    path('dynamics-style.css', views.dynamics_css, name='dynamic_css')
]