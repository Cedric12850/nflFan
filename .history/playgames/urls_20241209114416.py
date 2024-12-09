from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.PlaygameIndexVue, name='playgame_index'),
]