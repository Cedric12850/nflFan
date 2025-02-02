#user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.sign_up.as_view(), name='users_sign_up'),
    path('dynamics-style.css', views.dynamics_css, name='dynamic_css'),
    path('teams/<int:pk>', views.teamDetailView.as_view(), name='team_detail'),
    path('teams/<int:pk>/edit', views.UpdateTeamView.as_view(), name='team_detail_edit'),
    path('navbar/divisions/', views.division_team, name='division_team'),
]