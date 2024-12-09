from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.playgames_index, name='playgame_index'),
    path('navbar/divisions/', views.division_team, name='division_team'),
]