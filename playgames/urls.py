from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.PlaygameIndexVue.as_view(), name='playgames_index'),
    path('playgames/addplaygame', views.PlaygameCreateView.as_view(), name='playgames_add'),
]