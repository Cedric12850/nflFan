#teams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.teams_index, name='teams_index')
]