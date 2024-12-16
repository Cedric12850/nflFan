from django.urls import path
from . import views

urlpatterns = [
    path('playgames/', views.PlaygameIndexVue.as_view(), name='playgames_index'),
    path('playgames/addplaygame', views.PlaygameCreateView.as_view(), name='playgames_add'),
    path('playgames/<int:pk>', views.PlaygameDetailView.as_view(), name='playgame_detail'),
    path('playgames/<int:pk>/edit', views.PlaygameUpdateView.as_view(), name='playgame_detail_edit'),
    path('admin/season/<int:season_id>/weeks/', views.get_weeks_by_season, name='get_weeks_by_season'),
]