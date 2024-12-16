from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.PlaygameIndexVue.as_view(), name='playgames_index'),
    path('playgames/addplaygame', views.PlaygameCreateView.as_view(), name='playgames_add'),
    path('playgames/<int:pk>', views.PlaygameDetailView.as_view(), name='playgame_detail'),
    path('playgames/<int:pk>/edit', views.PlaygameUpdateView.as_view(), name='playgame_detail_edit'),
    path('ajax/load-weeks/', views.ajax_load_weeks, name='ajax_load_weeks'),
     path('get_weeks_for_season/', get_weeks_for_season, name='get_weeks_for_season'),
]