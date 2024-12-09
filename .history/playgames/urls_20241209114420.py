from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.PlaygameIndexVue.as_view(), name='playgame_index'),
]