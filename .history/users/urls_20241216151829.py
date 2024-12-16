#user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.sign_up.as_view(), name='users_sign_up'),
]