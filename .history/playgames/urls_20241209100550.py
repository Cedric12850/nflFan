from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.playgames_index, name='playgame_index'),
]