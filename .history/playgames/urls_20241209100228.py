from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.TeamIndexView.as_view(), name='teams_index'),
    path('navbar/divisions/', views.division_team, name='division_team'),
]