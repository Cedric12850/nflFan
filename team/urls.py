#teams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.teams_index, name='teams_index'),
    path('dynamics-style.css', views.dynamics_css, name='dynamic_css'),
    path('teams/<int:team_id>', views.team_detail_view, name='team_detail')
]