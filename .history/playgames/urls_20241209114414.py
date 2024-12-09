from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.PlaygameIndexVueas, name='playgame_index'),
]