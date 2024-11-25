#teams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.team_index, name='team_index')
]