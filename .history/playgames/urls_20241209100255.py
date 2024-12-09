from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.PLaygames_index, name='teams_index'),
    path('navbar/divisions/', views.division_team, name='division_team'),
]