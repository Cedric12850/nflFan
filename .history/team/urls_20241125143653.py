#teams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.teams_index, name='teams_index'),
    path('dynamics-style.css', views.dynm)
]