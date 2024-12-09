from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.pla, name='playgame_index'),
]